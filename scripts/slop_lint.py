#!/usr/bin/env python3
"""slop_lint.py: static review candidates for a deck; not an AI-authorship detector.

Usage:
  python3 slop_lint.py <file.html|file.css|file.pptx|folder> [--json] [--lang=fi|en] [--ghost]
                       [--forbid="Real Target Oy,Buyer name"] [--mode=read|present] [--strict-style]

  --ghost   also print the ghost deck: the slide titles alone, in order
  --forbid  terms that must not appear anywhere (codename hygiene): slide text,
            notes, file properties. Case-insensitive.

Reads HTML, CSS, JSX/TSX/Vue/Svelte, Markdown and .pptx. Prints one line per
finding with the sign id from references/signs.md, where it lives and the fix.
The scan is a first pass, not a verdict: it finds candidates fast, the eyes on
the rendered slides decide. Exit code 0 always, so it never blocks a pipeline.

Standard library only, plus python-pptx for .pptx files.
"""
from __future__ import annotations

import colorsys
import html as htmllib
import json
import re
import sys
import zipfile
from collections import Counter, defaultdict
from dataclasses import dataclass, asdict
from pathlib import Path

# ---------------------------------------------------------------- findings


@dataclass
class Finding:
    id: str
    severity: str  # high, medium, low
    where: str
    what: str
    fix: str


# Style checks remain visible, but cannot mandate minimalism in the default profile.
STRICT_STYLE = False
WORD_LIMIT = 180
CONTEXT_FIXES = {
    "N1": "Use a supported takeaway, a useful descriptive title or a genuine question according to the page's job",
    "N2": "Inspect grouping and intended reading size; preserve related evidence and necessary caveats",
    "N3": "Keep navigation, synthesis or discussion pages when they serve this audience",
    "K1": "Check tone and purpose; preserve meaningful quotation or deliberate emphasis",
    "K2": "Replace unsupported or vague copy; preserve accurate technical terms and quotations",
    "K4": "Apply the deck's punctuation convention consistently",
    "K5": "Apply the brand's case convention consistently",
    "K8": "Inspect readability in context rather than removing punctuation mechanically",
    "T1": "Bold can be appropriate; check that hierarchy remains clear and emphasis selective",
    "T2": "Short uppercase labels can aid navigation; check readability and role consistency",
    "T3": "Check whether sizes correspond to coherent roles; a rich diagram may need several roles",
    "T4": "Check deliberate font roles, glyph coverage and availability",
    "T5": "Keep meaningful italics, titles of works and deliberate editorial typography",
    "T6": "Check legibility and purpose of the display treatment",
    "C1": "Keep a gradient when it encodes quantity or serves a specific image/brand treatment",
    "C2": "Inspect legibility and purpose; do not infer authorship from a text effect",
    "C3": "Keep depth cues only when they clarify grouping, material or emphasis",
    "C4": "Inspect whether the background supports the content and preserves contrast",
    "C5": "Colour is not an AI tell; verify brand, semantic role and contrast",
    "C6": "Inspect readability and whether transparency helps the intended composition",
    "C7": "Check whether the border defines a meaningful boundary or merely competes with evidence",
    "C8": "Use enough colours for the categorical, sequential and brand roles; keep meanings stable",
    "L1": "Check the reading path; centring can be appropriate for a short statement or symmetric comparison",
    "L2": "Align related objects; diagram coordinates need not share text-column edges",
    "L4": "Compare title positions within layout families, not across unrelated compositions",
    "L5": "Keep repeated layouts when they help comparison or show a sequence",
    "S1": "Use coherent spacing while allowing data geometry and optical adjustments",
    "D1": "Check whether shape communicates grouping or function",
    "D2": "Keep rules and colour boundaries only when they have a clear structural role",
    "D3": "Keep icons that identify actual roles; replace generic icon rows with an explanatory form",
    "D4": "Inspect whether the rule contributes useful hierarchy or is unnecessary decoration",
    "D5": "Keep explanatory perspective only when it does not distort quantitative evidence",
    "D6": "Keep labels or section numbers when they help orientation",
    "G2": "Choose the form for the comparison; direct labels and a readable number of parts matter",
    "G3": "Several hues may encode meaningful categories; keep labels and stable colour roles",
    "G4": "Use a legend only when it improves reading over direct labelling",
    "I1": "Check that symbols communicate meaning and fit the brand and audience",
    "I2": "Keep only if the symbol communicates actual content rather than generic decoration",
    "M1": "Keep motion only when it explains change; provide reduced-motion and static states",
    "M2": "Use targeted transitions that do not interfere with comprehension",
    "M3": "Check whether interaction helps the audience's task",
    "M4": "Check animation performance and whether it explains the content",
    "M5": "Keep a visual effect only when it serves a specific explanation",
    "H2": "Remove accidental scaffolding; preserve truthful required attribution and provenance",
}
FINDINGS: list[Finding] = []
SLIDES: list[dict] = []   # where, title, text, notes, layout — filled by the scanners, read by check_deck()
META: list[tuple[str, str]] = []  # (where, text) of file properties and generator tags


def add(id_, sev, where, what, fix):
    if not STRICT_STYLE and id_ in CONTEXT_FIXES:
        sev, fix = "low", CONTEXT_FIXES[id_]
    FINDINGS.append(Finding(id_, sev, where, what.strip()[:160], fix))


# ---------------------------------------------------------------- word lists

HYPE_EN = [
    "supercharge", "seamless", "seamlessly", "unlock", "unleash", "magic", "magical",
    "revolutionize", "revolutionary", "game-changing", "game changer", "cutting-edge",
    "next-level", "next level", "world-class", "best-in-class", "synergy", "synergies",
    "leverage", "empower", "transformative", "disruptive", "elevate", "turbocharge",
    "unparalleled", "state-of-the-art", "harness the power", "in today's fast-paced",
    "ever-evolving", "delve", "tapestry", "landscape of", "robust", "holistic",
]
HYPE_FI = [
    "mullistava", "vallankumouksellinen", "saumaton", "saumattomasti", "huippuluokan",
    "maailmanluokan", "ainutlaatuinen", "pelinmuuttaja", "seuraavalle tasolle",
    "innovatiivinen", "tehokkaasti ja helposti", "synergia", "valjastaa", "kärkeen",
    "tämän päivän nopeasti muuttuvassa", "ennennäkemätön",
]
FILLER_SLIDES = [
    r"^thank you!?$", r"^thanks!?$", r"^questions\??$", r"^any questions\??$", r"^q ?& ?a$",
    r"^kiitos!?$", r"^kysymyksiä\??$", r"^introduction$", r"^johdanto$",
    r"^key takeaways?$", r"^keskeiset (opit|havainnot)$", r"^conclusion$", r"^yhteenveto$",
    r"^about us$", r"^meistä$", r"^agenda$",
]
UNVERIFIABLE = [
    r"\b\d+x (faster|better|more)\b", r"trusted by", r"loved by", r"\b10,?000\+",
    r"industry[- ]leading", r"market leader", r"#1\b", r"number one", r"markkinajohtaja", r"ykkönen",
]

EMOJI_RE = re.compile(
    "[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U0001F000-\U0001F2FF\U00002B50\U00002B55"
    "\U0001F900-\U0001F9FF✅❌✨⚡⬆↗↘]"
)
SPARKLE_RE = re.compile("[✨❇✴\U0001F31F\U0001F4AB]")

# ---------------------------------------------------------------- colour helpers

NAMED = {
    "purple": "#800080", "violet": "#ee82ee", "indigo": "#4b0082", "magenta": "#ff00ff",
    "fuchsia": "#ff00ff", "cyan": "#00ffff", "aqua": "#00ffff", "blue": "#0000ff",
    "red": "#ff0000", "orange": "#ffa500", "yellow": "#ffff00", "green": "#008000",
    "lime": "#00ff00", "pink": "#ffc0cb", "teal": "#008080", "white": "#ffffff",
    "black": "#000000", "gray": "#808080", "grey": "#808080",
}
COLOR_RE = re.compile(
    r"#[0-9a-fA-F]{3,8}\b|rgba?\([^)]*\)|hsla?\([^)]*\)|\b(" + "|".join(NAMED) + r")\b"
)
AI_HEXES = {"6366f1", "8b5cf6", "a855f7", "7c3aed", "9333ea", "4f46e5", "818cf8", "c084fc",
            "a78bfa", "ec4899", "d946ef", "06b6d4", "22d3ee", "00ffcc", "ff00aa", "00ffff"}


def parse_color(token: str):
    """Return (r, g, b, a) in 0..1 or None."""
    t = token.strip().lower()
    if t in NAMED:
        t = NAMED[t]
    if t.startswith("#"):
        h = t[1:]
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        if len(h) not in (6, 8):
            return None
        try:
            r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
            a = int(h[6:8], 16) / 255 if len(h) == 8 else 1.0
            return r, g, b, a
        except ValueError:
            return None
    m = re.match(r"(rgba?|hsla?)\(([^)]*)\)", t)
    if not m:
        return None
    parts = [p for p in re.split(r"[\s,/]+", m.group(2)) if p]
    try:
        if m.group(1).startswith("rgb"):
            vals = [float(p.rstrip("%")) * (2.55 if p.endswith("%") else 1) for p in parts[:3]]
            a = float(parts[3].rstrip("%")) / (100 if parts[3].endswith("%") else 1) if len(parts) > 3 else 1.0
            return vals[0] / 255, vals[1] / 255, vals[2] / 255, a
        hue = float(re.sub(r"deg$", "", parts[0]))
        s = float(parts[1].rstrip("%")) / 100
        l = float(parts[2].rstrip("%")) / 100
        a = float(parts[3].rstrip("%")) / (100 if parts[3].endswith("%") else 1) if len(parts) > 3 else 1.0
        r, g, b = colorsys.hls_to_rgb((hue % 360) / 360, l, s)
        return r, g, b, a
    except (ValueError, IndexError):
        return None


def hsl(rgb):
    h, l, s = colorsys.rgb_to_hls(*rgb[:3])
    return h * 360, s, l


def saturated(rgb, min_s=0.25):
    h, s, l = hsl(rgb)
    return s >= min_s and 0.12 < l < 0.92


def hue_dist(a, b):
    d = abs(a - b) % 360
    return min(d, 360 - d)


def is_ai_purple(rgb):
    h, s, l = hsl(rgb)
    return s > 0.35 and 245 <= h <= 300 and 0.3 < l < 0.8


# ---------------------------------------------------------------- text helpers


def strip_tags(html: str) -> list[tuple[str, str]]:
    """Return (tag, text) pairs for text-bearing elements, roughly."""
    html = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", html, flags=re.S | re.I)
    out = []
    for m in re.finditer(r"<(h[1-6]|p|li|span|div|button|a|td|th|figcaption|small|strong|label)\b[^>]*>(.*?)</\1>", html, flags=re.S | re.I):
        text = htmllib.unescape(re.sub(r"<[^>]+>", " ", m.group(2)))
        text = re.sub(r"[ \t\r\n]+", " ", text).strip()
        if text:
            out.append((m.group(1).lower(), text))
    return out


def line_of(src: str, pos: int) -> int:
    return src.count("\n", 0, pos) + 1


def title_case_ratio(text: str) -> float:
    words = [w for w in re.findall(r"[A-Za-zÅÄÖåäö][\w'’-]*", text)]
    small = {"a", "an", "the", "and", "or", "of", "in", "on", "to", "for", "vs", "with", "by", "at"}
    words = [w for w in words if w.lower() not in small]
    if len(words) < 3:
        return 0.0
    return sum(1 for w in words if w[0].isupper()) / len(words)


# ---------------------------------------------------------------- copy checks (shared)


def check_copy(texts: list[tuple[str, str]], where_prefix: str, lang: str):
    hype = HYPE_EN + (HYPE_FI if lang in ("fi", "auto") else [])
    excl = 0
    emoji_hits = []
    for tag, text in texts:
        low = text.lower()
        w = f"{where_prefix} <{tag}> “{text[:60]}”"
        if "!" in text and not re.search(r"!=|!\w", text):
            excl += 1
            if excl <= 6:
                add("K1", "medium", w, "Exclamation mark in slide text", "State it plainly, no exclamation marks")
        for word in hype:
            if re.search(r"(?<![\w-])" + re.escape(word) + r"(?![\w-])", low):
                add("K2", "medium", w, f"Hype word: {word}", "Say what it does, with a number or a noun from the deal")
                break
        if tag in ("h1", "h2", "h3", "title"):
            stripped = low.strip(" .!")
            for pat in FILLER_SLIDES:
                if re.match(pat, stripped):
                    add("N3", "medium", w, "Filler slide title", "Replace with the slide's message, or cut the slide")
                    break
            if text.rstrip().endswith(".") and len(text.split()) < 14:
                add("K4", "low", w, "Trailing period on a title", "Titles end without a period")
            if lang != "fi" and title_case_ratio(text) > 0.8:
                add("K5", "low", w, "Title Case Headline", "Sentence case")
            if len(text.split()) <= 3 and tag in ("h2", "title") and not re.search(r"\d", text):
                add("N1", "low", w, "Topic label as title, not a message", "Write an action title: the one thing this slide proves")
        for pat in UNVERIFIABLE:
            if re.search(pat, low):
                add("K6", "medium", w, "Claim needing source and scope", "Verify against the source; qualify or flag if unresolved")
                break
        if re.search(r"[+−-][\s\u00a0]?\d+[\d.,]*[\s\u00a0\u202f]?%(?!.*\b(vs|than|from|yoy|y/y|ed\.|edell|vrt|vs\.)\b)", low) and len(text) < 40:
            add("K7", "low", w, "Change without a reference", "Say what it compares to: +12 % vs FY24")
        if SPARKLE_RE.search(text):
            add("I2", "high", w, "Sparkle emoji", "Remove; a sparkle says nothing about the content")
        elif EMOJI_RE.search(text):
            emoji_hits.append(text[:40])
    if emoji_hits:
        add("I1", "high" if len(emoji_hits) > 2 else "medium", where_prefix,
            f"Emoji in {len(emoji_hits)} text elements, e.g. “{emoji_hits[0]}”", "Line icon from one set, or nothing")


def check_numbers(all_text: str, where: str):
    comma_thousands = re.findall(r"\b\d{1,3}(?:,\d{3})+(?:\.\d+)?\b", all_text)
    comma_decimal = re.findall(r"\b\d+,\d{1,2}\b(?!\d)", all_text)
    space_thousands = re.findall(r"\b\d{1,3}(?:[ \u00a0\u202f]\d{3})+\b", all_text)
    dot_decimal = re.findall(r"\b\d+\.\d{1,2}\b", all_text)
    if (comma_thousands or dot_decimal) and (comma_decimal or space_thousands):
        a = (comma_thousands or dot_decimal)[0]
        b = (comma_decimal or space_thousands)[0]
        add("N4", "medium", where, f"Mixed number conventions: {a} and {b}",
            "One convention per deck. Finnish: 1 234,5. English: 1,234.5")
    cur = Counter()
    for m in re.finditer(r"(€|EUR|\$|USD)\s?\d[\d.,]*\s?(bn|mn|m|M|k|K)?\b|\d[\d.,\u00a0 ]*[ \u00a0\u202f]?(M€|k€|MEUR|meur|milj\. ?€|milj\. euroa|€|EUR)", all_text):
        tok = m.group(0)
        if tok[0] in "€$" or tok.startswith(("EUR", "USD")):
            kind = "symbol first (€12.4M)"
        elif re.search(r"[Mk]€|MEUR|meur", tok):
            kind = "unit after (12,4 M€)"
        elif "milj" in tok:
            kind = "milj. €"
        else:
            kind = "symbol after (12 €)"
        cur[kind] += 1
    if len(cur) > 1:
        add("N4", "medium", where, f"Possible mixed currency formats: {', '.join(cur)}", "One currency format across the deck")
    fake = re.findall(r"\b(123[,.]?456|99[,.]9{2,})\b", all_text, flags=re.I)
    if fake:
        add("N5", "high", where, f"Possible example data: {fake[0]}", "Plausible, real or clearly marked numbers")


# ---------------------------------------------------------------- CSS / markup checks


PROP_RE = re.compile(r"([a-z-]+)\s*:\s*([^;{}]+)")
SPACING_PROPS = re.compile(r"^(margin|padding|gap|row-gap|column-gap|top|left|right|bottom|inset)(-[a-z]+)?$")


def check_css(src: str, where_file: str):
    """Scan CSS text (or HTML with inline CSS / Tailwind classes)."""
    colors_sat = Counter()
    stock = Counter()
    stock_loc = {}
    off_grid = []
    weights = Counter()
    families = set()
    pills = 0
    centered = 0
    lefted = 0

    for m in PROP_RE.finditer(src):
        prop, val = m.group(1).lower(), m.group(2).strip()
        loc = f"{where_file}:{line_of(src, m.start())}"
        low = val.lower()

        # colour inventory
        for cm in COLOR_RE.finditer(val):
            c = parse_color(cm.group(0))
            if c and c[3] > 0.2 and saturated(c):
                colors_sat[cm.group(0).lower()] += 1
            if c and cm.group(0).lower().lstrip("#") in AI_HEXES:
                stock[cm.group(0).lower()] += 1
                stock_loc.setdefault("first", loc)

        if "gradient(" in low and prop in ("background", "background-image", "border-image", "fill", "color"):
            stops = [parse_color(x.group(0)) for x in COLOR_RE.finditer(val)]
            stops = [s for s in stops if s and s[3] > 0.15]
            hues = [hsl(s)[0] for s in stops if saturated(s, 0.2)]
            if "radial-gradient" in low and any(saturated(s, 0.25) for s in stops):
                add("C4", "high", loc, "Radial colour wash or blob", "Remove; quiet surface")
            elif len(hues) >= 2 and max(hue_dist(a, b) for a in hues for b in hues) > 25:
                add("C1", "high", loc, f"Hue-to-hue gradient: {val[:70]}", "One flat surface; tone shift inside one neutral at most")
        if prop in ("-webkit-background-clip", "background-clip") and "text" in low:
            add("C2", "high", loc, "Gradient text", "Solid primary text colour")
        if prop in ("-webkit-text-fill-color",) and "transparent" in low and "background-clip" not in src[max(0, m.start() - 200):m.start()]:
            add("C2", "high", loc, "Transparent text fill (gradient text)", "Solid primary text colour")
        if prop in ("box-shadow", "text-shadow", "filter") and ("shadow" in prop or "drop-shadow" in low):
            for cm in COLOR_RE.finditer(val):
                c = parse_color(cm.group(0))
                if c and saturated(c, 0.3) and c[3] > 0.1:
                    add("C3", "high", loc, f"Coloured glow or shadow: {val[:60]}", "Remove; depth from surface steps and hairlines")
                    break
            else:
                if re.search(r"\b0(px)?\s+0(px)?\s+[1-9]\d+px", low) and prop != "filter":
                    add("C3", "medium", loc, f"Halo glow (0 0 blur): {val[:60]}", "Remove, or a small neutral offset shadow on light themes")
        if prop in ("backdrop-filter", "-webkit-backdrop-filter") and "blur" in low:
            add("C6", "medium", loc, "Glass blur panel", "Plain raised surface with a hairline")
        if prop.startswith("border") and re.search(r"\b[2-9]px\b", low):
            for cm in COLOR_RE.finditer(val):
                c = parse_color(cm.group(0))
                if c and saturated(c, 0.45):
                    side = prop.split("-")[1] if "-" in prop else ""
                    if side in ("left", "top", "right", "bottom"):
                        add("D2", "medium", loc, f"Coloured accent stripe on one side ({prop})", "Remove; set apart with space or a surface step")
                    else:
                        add("C7", "medium", loc, f"Neon or heavy coloured border: {val[:50]}", "Hairline at 6 to 10 % of the text colour")
                    break

        # type
        if prop == "font-weight":
            try:
                weights[int(re.findall(r"\d+", low)[0])] += 1
            except IndexError:
                if "bold" in low:
                    weights[700] += 1
        if prop == "font-family":
            fam = low.split(",")[0].strip(" '\"")
            if fam and not fam.startswith("var("):
                families.add(fam)
        if prop == "letter-spacing":
            num = re.findall(r"(-?[\d.]+)(em|px|rem)", low)
            if num:
                v, unit = float(num[0][0]), num[0][1]
                block = src[max(0, src.rfind("{", 0, m.start())):m.start() + 200]
                if v > 0.04 and unit == "em" or v > 0.8 and unit == "px":
                    if re.search(r"text-transform\s*:\s*uppercase", block, re.I):
                        add("T2", "high", loc, "Uppercase label with wide tracking", "Sentence case, normal tracking")
        if prop == "font-style" and "italic" in low:
            add("T5", "low", loc, "Italic", "Emphasis through colour or weight, italic only for titles of works")

        # spacing grid
        if SPACING_PROPS.match(prop) and "calc" not in low and "clamp" not in low and "var(" not in low:
            for px in re.findall(r"(-?\d+(?:\.\d+)?)px", low):
                n = abs(float(px))
                if n > 2 and n % 4 != 0:
                    off_grid.append((loc, prop, px))

        # details
        if prop == "border-radius" and re.search(r"(999|9999|100)px|50%", low):
            pills += 1
        if prop == "text-align":
            if "center" in low:
                centered += 1
            elif "left" in low or "start" in low:
                lefted += 1

        # motion
        if prop in ("animation", "animation-iteration-count") and "infinite" in low:
            add("M1", "high", loc, f"Looping animation: {val[:50]}", "Static; motion only where something is live")
        if prop == "transition" and re.search(r"\ball\b", low):
            add("M2", "medium", loc, "transition: all", "Name the properties: color, background-color, opacity, transform")
        if prop in ("transition", "transition-property") and re.search(r"\b(width|height|top|left|margin)\b", low):
            add("M4", "medium", loc, f"Animating layout properties: {val[:50]}", "Transform and opacity only")
        if prop == "cursor" and "none" in low:
            add("M5", "medium", loc, "Custom cursor", "Default cursor")

    # Tailwind class tells
    tw = [
        (r"\b(from|via|to)-(purple|violet|indigo|fuchsia|pink)-\d{3}\b", "C1", "high", "Tailwind purple/violet gradient stop"),
        (r"\bbg-clip-text\b", "C2", "high", "Tailwind gradient text"),
        (r"\bshadow-\[[^\]]*rgba?\([^\]]*\]", "C3", "high", "Tailwind arbitrary coloured shadow"),
        (r"\bshadow-(purple|violet|indigo|blue|pink|cyan)-\d{3}", "C3", "high", "Tailwind coloured shadow"),
        (r"\bbackdrop-blur(-\w+)?\b", "C6", "medium", "Tailwind glass blur"),
        (r"\buppercase\b[^\"']*\btracking-(wide|wider|widest)\b|\btracking-(wide|wider|widest)\b[^\"']*\buppercase\b", "T2", "high", "Tailwind uppercase + wide tracking"),
        (r"\bfont-(extrabold|black)\b", "T1", "medium", "Tailwind 800 to 900 weight"),
        (r"\banimate-(pulse|ping|bounce|spin)\b", "M1", "high", "Tailwind looping animation"),
        (r"\btransition-all\b", "M2", "medium", "Tailwind transition-all"),
        (r"\bhover:(scale|-?translate-y|rotate)-[\w\[\]-]+", "M3", "medium", "Hover lift or scale"),
        (r"\b[mp][trblxy]?-\[\d*[13579]px\]|\b(gap|h|w|top|left)-\[\d*[13579]px\]", "S1", "medium", "Arbitrary off-grid value"),
    ]
    for pat, id_, sev, what in tw:
        hits = list(re.finditer(pat, src))
        if hits:
            add(id_, sev, f"{where_file}:{line_of(src, hits[0].start())}", f"{what} ({len(hits)}×)", "See references/signs.md")

    # aggregates
    heavy = sum(v for k, v in weights.items() if k >= 700)
    if heavy:
        add("T1", "medium" if heavy > 2 else "low", where_file, f"Weights 700 to 900 used {heavy}×",
            "400 and 500 for text, 600 at most; hierarchy from size and colour")
    if len(families) > 3:
        add("T4", "medium", where_file, f"{len(families)} font families: {', '.join(sorted(families))}",
            "One family, plus one partner at most")
    if off_grid:
        sample = ", ".join(f"{p} {v}px" for _, p, v in off_grid[:4])
        add("S1", "medium" if len(off_grid) > 3 else "low", off_grid[0][0], f"{len(off_grid)} off-grid spacing values ({sample})",
            "Steps of the 8 px grid, 4 px for nudges inside controls")
    if pills > 4:
        add("D1", "medium", where_file, f"{pills} fully round radii", "Radius by size; nested radius = outer minus padding")
    if centered > 6 and centered > 2 * max(lefted, 1):
        add("L1", "medium", where_file, f"Centred text dominates ({centered} centre vs {lefted} left)",
            "Left-align body and titles; centre only short single lines")
    hues = []
    for tok in colors_sat:
        c = parse_color(tok)
        if c:
            h = hsl(c)[0]
            if all(hue_dist(h, x) > 18 for x in hues):
                hues.append(h)
    if len(hues) > 4:
        add("C8", "medium", where_file, f"{len(hues)} distinct saturated hues in the chrome",
            "One accent; extra hues only where a chart needs to separate series")
    if stock:
        add("C5", "medium", stock_loc["first"], f"Palette review, {sum(stock.values())} uses: {', '.join(k for k, _ in stock.most_common(6))}",
            "Accent from the brand or the deal's world; neutrals for everything else")
    for tok in colors_sat:
        c = parse_color(tok)
        if c and is_ai_purple(c) and tok.lstrip("#") not in AI_HEXES:
            add("C5", "low", where_file, f"Purple/violet in use: {tok}", "Keep only if it is the real brand colour")
            break


def check_markup(src: str, where_file: str, lang: str):
    texts = strip_tags(src)
    check_copy(texts, where_file, lang)
    check_numbers("\n".join(t for _, t in texts), where_file)
    # Particle, parallax, tilt and cursor-trail code
    for pat, what in [(r"particle", "Particle background"), (r"parallax", "Parallax"), (r"\btilt\b|rotateY\(\$\{", "3D tilt on hover"),
                      (r"cursor[-_ ]?trail|custom[-_ ]?cursor", "Custom cursor or trail"), (r"glitch|scramble", "Glitch or scramble text")]:
        m = re.search(pat, src, re.I)
        if m:
            add("M5", "high", f"{where_file}:{line_of(src, m.start())}", what, "Remove; motion only where it explains something")
    # Icon in a circle grids
    circles = len(re.findall(r"class=\"[^\"]*(icon|feature)[^\"]*(circle|round|bubble)", src, re.I))
    circles += len(re.findall(r"rounded-full[^\"]*\b(w|h)-(10|12|14|16)\b", src))
    if circles >= 3:
        add("D3", "medium", where_file, f"Icons in coloured circles ({circles}×)", "Drop the circles; one line icon inline with the label, or no icon")
    # Rainbow bars: sibling bars each in another hue
    bar_cols = [parse_color(c) for c in re.findall(r"class=\"[^\"]*\bbar\b[^\"]*\"[^>]*style=\"[^\"]*background(?:-color)?:\s*([^;\"]+)", src)]
    bar_hues = []
    for c in bar_cols:
        if c and saturated(c):
            h = hsl(c)[0]
            if all(hue_dist(h, x) > 18 for x in bar_hues):
                bar_hues.append(h)
    if len(bar_hues) >= 3:
        add("G3", "high", where_file, f"Bars of one series in {len(bar_hues)} hues", "One neutral for the series, the accent on the bar that matters")
    # Eyebrow labels over titles and numbered section markers
    eb = re.findall(r"<(p|span|div)\b[^>]*class=\"[^\"]*\b(eyebrow|kicker|overline|pretitle|label|tag)\b[^\"]*\"[^>]*>[^<]{1,40}</\1>\s*<h[12]\b", src, re.I)
    if len(eb) >= 2:
        add("D6", "low", where_file, f"Eyebrow label over the title on {len(eb)} slides", "Drop it; the section name goes in the footer if it is needed")
    nums = re.findall(r">\s*0[1-9]\s*(/|·|—)?\s*<", src)
    if len(nums) >= 3:
        add("D6", "low", where_file, f"Numbered section markers 01, 02… ({len(nums)}×)", "Remove; the title carries the section")
    # Accent line under the title
    if re.search(r"(h1|h2|title)[^{]*::?after\s*{[^}]*(width\s*:\s*\d{2,3}px)[^}]*(height\s*:\s*[2-6]px)", src, re.I | re.S):
        add("D4", "medium", where_file, "Short accent bar under the title", "Remove; space and size carry the title")
    for m in re.finditer(r"<meta\s+name=\"generator\"\s+content=\"([^\"]*)\"", src, re.I):
        META.append((where_file, m.group(1)))
    # Slide-level density for HTML decks
    parts = re.split(r"(<section\b[^>]*>)", src)
    slides = [""] + [parts[i] + parts[i + 1] for i in range(1, len(parts) - 1, 2)]
    if len(slides) > 1:
        for i, s in enumerate(slides[1:], 1):
            cls = re.search(r"class=\"([^\"]*)\"", s[:300])
            layout = " ".join(c for c in (cls.group(1).split() if cls else []) if c not in ("slide", "is-active", "active"))
            tm = re.search(r"<(h1|h2)\b[^>]*>(.*?)</\1>", s, re.S | re.I)
            title = htmllib.unescape(re.sub(r"[ \t\r\n]+", " ", re.sub(r"<[^>]+>", " ", tm.group(2)))).strip() if tm else ""
            plain = htmllib.unescape(re.sub(r"[ \t\r\n]+", " ", re.sub(r"<[^>]+>", " ", re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", s, flags=re.S)))).strip()
            items = len(re.findall(r"<li\b", s)) or len(re.findall(r"class=\"[^\"]*\b(card|figure|pillar|item)\b", s))
            SLIDES.append({"where": f"{where_file} slide {i}", "title": title, "text": plain, "notes": "", "layout": layout, "items": items})
            body = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", s, flags=re.S)
            words = len(re.sub(r"<[^>]+>", " ", body).split())
            bullets = len(re.findall(r"<li\b", body))
            if words > WORD_LIMIT:
                add("N2", "medium", f"{where_file} slide {i}", f"{words} words on one slide", "One message per slide; move detail to notes or the appendix")
            if bullets > 6:
                add("N2", "medium", f"{where_file} slide {i}", f"{bullets} bullets on one slide", "Five at most, or a different form: table, chart, split")


# ---------------------------------------------------------------- PPTX checks

EMU_PER_PT = 12700


def check_pptx(path: Path, lang: str):
    try:
        from pptx import Presentation
        from pptx.util import Emu
    except ImportError:
        add("X0", "high", str(path), "python-pptx is not installed", "pip install python-pptx")
        return
    prs = Presentation(str(path))
    sw, sh = prs.slide_width, prs.slide_height
    cp = prs.core_properties
    for field in ("author", "last_modified_by", "title", "subject", "comments", "keywords", "category"):
        v = getattr(cp, field, None)
        if v:
            META.append((f"{path.name} properties.{field}", str(v)))
    fonts = Counter()
    sizes = Counter()
    title_pos = []
    all_text = []
    caps_runs = 0
    bold_runs = runs = 0
    fills = Counter()

    for idx, slide in enumerate(prs.slides, 1):
        where = f"{path.name} slide {idx}"
        words = 0
        bullets = 0
        texts = []
        lefts = Counter()
        min_pt = None
        for shape in slide.shapes:
            lefts[round((shape.left or 0) / 12700 / 4)] += 1
            if shape.left is not None and shape.width is not None:
                if shape.left < 0 or shape.top < 0 or shape.left + shape.width > sw * 1.002 or shape.top + shape.height > sh * 1.002:
                    add("L3", "medium", where, f"Shape '{shape.name}' runs off the slide", "Bring it inside the margins")
            xml = shape._element.xml
            if "<a:gradFill" in xml:
                add("C1", "medium", where, f"Gradient fill on '{shape.name}'", "Flat fill from the ramp")
            if "<a:glow" in xml:
                add("C3", "high", where, f"Glow effect on '{shape.name}'", "Remove")
            if "<a:outerShdw" in xml and "<a:srgbClr" in xml.split("<a:outerShdw")[1][:300]:
                add("C3", "low", where, f"Shadow on '{shape.name}'", "No shadow, or a small neutral one on a floating object")
            if "<a:sp3d" in xml or "<a:scene3d" in xml:
                add("D5", "high", where, f"3D bevel or perspective on '{shape.name}'", "Flat")
            if "prstTxWarp" in xml:
                add("T6", "high", where, f"WordArt warp on '{shape.name}'", "Plain text")
            if "<a:softEdge" in xml or "<a:reflection" in xml:
                add("C3", "medium", where, f"Soft edge or reflection on '{shape.name}'", "Remove")
            for m in re.finditer(r'<a:srgbClr val="([0-9A-Fa-f]{6})"', xml):
                fills[m.group(1).upper()] += 1
            if getattr(shape, "has_chart", False) and shape.has_chart:
                ct = str(shape.chart.chart_type)
                if "THREE_D" in ct:
                    add("G1", "high", where, f"3D chart ({ct})", "2D; 3D distorts the values")
                if "PIE" in ct or "DOUGHNUT" in ct:
                    try:
                        n = len(list(shape.chart.plots[0].categories))
                        if n > 5:
                            add("G2", "medium", where, f"Pie with {n} slices", "Sorted bar chart")
                    except Exception:
                        pass
                cx = shape.chart._chartSpace.xml
                if re.search(r'varyColors(?: val="(?:1|true)")?/>', cx) and "PIE" not in ct and "DOUGHNUT" not in ct:
                    add("G3", "medium", where, "Each bar a different colour in one series", "One colour; accent only on the bar that matters")
                try:
                    if shape.chart.has_legend and len(list(shape.chart.plots[0].series)) == 1:
                        add("G4", "low", where, "Legend on a single-series chart", "Remove the legend; say it in the title")
                except Exception:
                    pass
            if not shape.has_text_frame:
                continue
            is_title = shape.is_placeholder and shape.placeholder_format.type is not None and "TITLE" in str(shape.placeholder_format.type)
            for p in shape.text_frame.paragraphs:
                ptext = "".join(r.text for r in p.runs).strip()
                if not ptext:
                    continue
                words += len(ptext.split())
                if p.level > 0 or (p._p.pPr is not None and p._p.pPr.find("{http://schemas.openxmlformats.org/drawingml/2006/main}buChar") is not None):
                    bullets += 1
                texts.append(("title" if is_title else "p", ptext))
                all_text.append(ptext)
                for r in p.runs:
                    runs += 1
                    f = r.font
                    if f.name:
                        fonts[f.name] += 1
                    if f.size:
                        pt = f.size.pt
                        sizes[round(pt)] += 1
                        min_pt = pt if min_pt is None else min(min_pt, pt)
                    if f.bold:
                        bold_runs += 1
                    if r.text.isupper() and len(r.text) > 6:
                        caps_runs += 1
                    rpr = r._r.find("{http://schemas.openxmlformats.org/drawingml/2006/main}rPr")
                    if rpr is not None and rpr.get("cap") == "all":
                        caps_runs += 1
            if is_title:
                title_pos.append((idx, shape.left, shape.top, shape.width))
        title_text = next((t for k, t in texts if k == "title"), "")
        check_copy([("cover", t) if (k == "title" and idx == 1) else (k, t) for k, t in texts], where, lang)
        notes = ""
        try:
            if slide.has_notes_slide:
                notes = slide.notes_slide.notes_text_frame.text
        except Exception:
            pass
        SLIDES.append({"where": where, "title": title_text,
                       "text": " ".join(t for _, t in texts), "notes": notes,
                       "layout": slide.slide_layout.name if slide.slide_layout is not None else "", "items": bullets})
        if words > WORD_LIMIT:
            add("N2", "medium", where, f"{words} words", "One message per slide; detail to notes or appendix")
        if bullets > 6:
            add("N2", "medium", where, f"{bullets} bullets", "Five at most, or a table, chart or split")
        if min_pt is not None and min_pt < 9:
            add("T7", "high", where, f"Text at {min_pt:.0f} pt", "12 pt floor for read decks, 18 pt for projected text; footnotes 9 to 10 pt only")
        if len(lefts) > 6:
            add("L2", "low", where, f"{len(lefts)} different left edges", "Snap to the column grid; fewer, shared edges")
        if not any(t == "title" for t, _ in texts) and idx > 1:
            add("N1", "low", where, "No title placeholder text", "Every content slide carries an action title")

    # deck-level
    if len(fonts) > 3:
        add("T4", "medium", path.name, f"{len(fonts)} fonts: {', '.join(f for f, _ in fonts.most_common(6))}", "One family, one partner at most")
    if len(sizes) > 8:
        add("T3", "medium", path.name, f"{len(sizes)} different text sizes: {sorted(sizes)}", "A scale of five or six sizes")
    if runs and bold_runs / runs > 0.3:
        add("T1", "medium", path.name, f"{bold_runs} of {runs} text runs bold", "Bold for one phrase per slide at most")
    if caps_runs > 3:
        add("T2", "medium", path.name, f"{caps_runs} all-caps runs", "Sentence case")
    if len(title_pos) > 2:
        xs = {round(l / 12700 / 8) for _, l, t, w in title_pos if l is not None}
        ys = {round(t / 12700 / 8) for _, l, t, w in title_pos if t is not None}
        if len(xs) > 1 or len(ys) > 2:
            add("L4", "medium", path.name, f"Titles drift: {len(xs)} x and {len(ys)} y positions", "One title position on every content slide")
    sat_fills = [c for c in fills if saturated(parse_color("#" + c), 0.3)]
    hues = []
    for c in sat_fills:
        h = hsl(parse_color("#" + c))[0]
        if all(hue_dist(h, x) > 18 for x in hues):
            hues.append(h)
    if len(hues) > 5:
        add("C8", "medium", path.name, f"{len(hues)} distinct saturated hues across the deck", "One accent; series colours inside charts only")
    for c in sat_fills:
        if is_ai_purple(parse_color("#" + c)):
            add("C5", "low", path.name, f"Purple/violet fill #{c}", "Keep only if it is the real brand colour")
            break
    check_numbers("\n".join(all_text), path.name)


# ---------------------------------------------------------------- deck integrity

METRICS = {
    "ARR": r"\bARR\b|toistuva liikevaihto",
    "revenue": r"(?<!recurring )(?<!toistuva )\b(revenue|net sales|turnover|liikevaihto|liikevaihdon)\b",
    "EBITDA": r"\b(EBITDA|käyttökate)\b",
    "NRR": r"\b(NRR|net revenue retention)\b",
    "customers": r"\b(customers|clients|asiakasta|asiakkaat)\b",
    "employees": r"\b(employees|FTEs?|headcount|henkilöstö|työntekijää)\b",
}
NUM_RE = re.compile(r"(€|EUR|\$|USD)?\s?(\d{1,3}(?:[ ,.\u00a0\u202f]\d{3})*(?:[.,]\d+)?|\d+(?:[.,]\d+)?)\s?(bn|mn|m|M€|k€|MEUR|M|k|K|milj\.?|%|€)?(?![\w])")
PLACEHOLDER_RE = re.compile(r"\[(?:company|client|target|name|x+|tbd|insert[^\]]*|year)\]|\bTBD\b|\bXX+\b|\bYYYY\b|lorem ipsum|click to add|lisää otsikko|napsauttamalla", re.I)
GENERATOR_RE = re.compile(r"generated (with|by)|made with (gamma|beautiful\.ai|tome|canva|chatgpt|claude)|as an ai\b|i hope this helps|python-pptx|pptxgenjs", re.I)
COUNT_TITLE_RE = re.compile(r"^(\d+|two|three|four|five|six|seven|kaksi|kolme|neljä|viisi|kuusi)\s+[a-zäöå]+", re.I)
WORD_NUM = {"two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "kaksi": 2, "kolme": 3, "neljä": 4, "viisi": 5, "kuusi": 6}


def to_value(raw: str, unit: str | None) -> float | None:
    t = raw.replace("\u00a0", " ").replace("\u202f", " ")
    if re.fullmatch(r"\d{1,3}(?:[ ]\d{3})+(?:,\d+)?", t):
        t = t.replace(" ", "").replace(",", ".")
    elif re.fullmatch(r"\d{1,3}(?:,\d{3})+(?:\.\d+)?", t):
        t = t.replace(",", "")
    elif re.fullmatch(r"\d{1,3}(?:\.\d{3})+(?:,\d+)?", t):
        t = t.replace(".", "").replace(",", ".")
    else:
        t = t.replace(" ", "").replace(",", ".")
    try:
        v = float(t)
    except ValueError:
        return None
    u = (unit or "").lower()
    if u in ("bn",):
        v *= 1e9
    elif u in ("m", "mn", "m€", "meur", "milj", "milj."):
        v *= 1e6
    elif u in ("k", "k€"):
        v *= 1e3
    return v


def check_deck(forbid: list[str]):
    if not SLIDES and not META:
        return
    # same metric, different values (currency and counts; years must agree)
    seen = defaultdict(list)
    for sl in SLIDES:
        text = sl["text"]
        for name, pat in METRICS.items():
            for m in re.finditer(pat, text, re.I):
                window = text[max(0, m.start() - 24): m.end() + 48]
                year = re.findall(r"\b(?:FY|LTM|NTM)?\s?(20\d\d)\b", window)
                for n in NUM_RE.finditer(text[m.end(): m.end() + 40]):
                    raw, unit, cur = n.group(2), n.group(3), n.group(1)
                    if re.fullmatch(r"20\d\d", raw) or (unit == "%" and name != "NRR"):
                        continue
                    if name in ("ARR", "revenue", "EBITDA") and not (cur or unit in ("bn", "mn", "m", "M€", "k€", "MEUR", "M", "k", "K", "milj", "milj.", "€")):
                        continue
                    v = to_value(raw, unit)
                    if v is not None:
                        seen[(name, year[0] if year else "")].append((v, sl["where"], n.group(0).strip()))
                    break
    for (name, year), vals in seen.items():
        distinct = {}
        for v, where, shown in vals:
            if all(abs(v - d) / max(d, 1e-9) > 0.01 for d in distinct):
                distinct[v] = (where, shown)
        places = {w for _, w, _ in vals}
        if len(distinct) > 1 and len(places) > 1:
            shown = "; ".join(f"{s} ({w.split(' ', 1)[-1]})" for w, s in list(distinct.values())[:3])
            add("N7", "medium", "deck", f"{name}{' ' + year if year else ''} has different values: {shown}",
                "One figure per metric and period across the deck; check the source ledger")
    # fake precision, placeholders, generator text, em dashes, counts, archetype runs, forbidden terms
    dashes = 0
    for sl in SLIDES:
        text = sl["text"]
        for m in re.finditer(r"(€|\$)?\d+[.,]\d{3,}\s?(m|M|mn|M€|MEUR|milj)\b|\b\d+[.,]\d{2,}\s?%", text):
            add("N8", "low", sl["where"], f"Precision review: {m.group(0)}", "Round to what the decision needs: €47.4m, 46 %")
            break
        ph = PLACEHOLDER_RE.search(text + " " + sl["title"])
        if ph:
            add("H1", "high", sl["where"], f"Placeholder left in: {ph.group(0)}", "Fill it or remove it")
        g = GENERATOR_RE.search(text)
        if g:
            add("H2", "medium", sl["where"], f"Tool or AI trace in slide text: {g.group(0)}", "Remove accidental scaffolding; preserve required provenance")
        dashes += text.count("—")
        cm = COUNT_TITLE_RE.match(sl["title"])
        if cm:
            first = cm.group(1).lower()
            n = int(first) if first.isdigit() else WORD_NUM.get(first)
            if n and sl["items"] and sl["items"] != n:
                add("N6", "medium", sl["where"], f"Title promises {n}, the slide shows {sl['items']}", "Make them agree, or title the conclusion instead of the count")
            else:
                add("N6", "low", sl["where"], f"Count title: “{sl['title'][:50]}”", "Title the conclusion, not the count")
    if dashes > max(3, len(SLIDES) // 2):
        add("K8", "low", "deck", f"{dashes} em dashes in slide text", "Commas, colons or two sentences; an en dash only for ranges")
    run, prev = 1, None
    for sl in SLIDES:
        key = sl["layout"]
        run = run + 1 if key and key == prev else 1
        if run == 3:
            add("L5", "low", sl["where"], f"Third slide in a row on the same layout ({key})", "Rotate the form: chart, table, split, statement")
        prev = key
    for where, value in META:
        if GENERATOR_RE.search(value):
            add("H2", "low", where, f"Generator trace in file properties: {value[:40]}", "Set author and title to the adviser and the project codename")
    for term in [t.strip() for t in forbid if t.strip()]:
        pat = re.compile(re.escape(term), re.I)
        hits = [sl["where"] for sl in SLIDES if pat.search(sl["text"] + " " + sl["title"])]
        hits += [sl["where"] + " notes" for sl in SLIDES if sl["notes"] and pat.search(sl["notes"])]
        hits += [w for w, v in META if pat.search(v)]
        if hits:
            add("H3", "high", ", ".join(hits[:4]) + (" …" if len(hits) > 4 else ""), f"Forbidden term appears: {term}",
                "Replace with the codename everywhere, including notes and file properties")


def print_ghost():
    print("\nTitle sequence — check the argument, explanatory progression or reference navigation as appropriate. Titles alone do not verify evidence.\n")
    for i, sl in enumerate(SLIDES, 1):
        print(f"{i:>3}. {sl['title'] or '(no title)'}")


# ---------------------------------------------------------------- driver

TEXT_EXT = {".html", ".htm", ".css", ".scss", ".jsx", ".tsx", ".js", ".ts", ".vue", ".svelte", ".md", ".mdx", ".json"}


def scan(path: Path, lang: str):
    if path.is_dir():
        for p in sorted(path.rglob("*")):
            if p.is_file() and "node_modules" not in p.parts and not any(x.startswith(".") for x in p.parts[len(path.parts):]):
                scan(p, lang)
        return
    ext = path.suffix.lower()
    if ext in (".pptx", ".potx"):
        if not zipfile.is_zipfile(path):
            add("X0", "high", str(path), "Not a valid .pptx", "Check the file")
            return
        check_pptx(path, lang)
    elif ext in TEXT_EXT:
        src = path.read_text(encoding="utf-8", errors="replace")
        if ext in (".md", ".mdx", ".json"):
            texts = [("p", line.strip("#*- ")) for line in src.splitlines() if line.strip()]
            texts = [("h2" if line.startswith("#") else "p", t) for line, (_, t) in zip([l for l in src.splitlines() if l.strip()], texts)]
            check_copy(texts, path.name, lang)
            check_numbers(src, path.name)
            return
        check_css(src, path.name)
        if ext not in (".css", ".scss"):
            check_markup(src, path.name, lang)


def main():
    global STRICT_STYLE, WORD_LIMIT
    STRICT_STYLE = "--strict-style" in sys.argv
    mode = next((a.split("=", 1)[1] for a in sys.argv if a.startswith("--mode=")), "read")
    if mode not in ("read", "present"):
        raise SystemExit("--mode must be read or present")
    WORD_LIMIT = 60 if mode == "present" else 180
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__)
        sys.exit(1)
    as_json = "--json" in sys.argv
    lang = "auto"
    for a in sys.argv:
        if a.startswith("--lang="):
            lang = a.split("=", 1)[1]
    forbid = []
    for a in sys.argv:
        if a.startswith("--forbid="):
            forbid = a.split("=", 1)[1].split(",")
    for a in args:
        scan(Path(a), lang)
    check_deck(forbid)

    # de-duplicate identical findings
    seen, unique = set(), []
    for f in FINDINGS:
        key = (f.id, f.where, f.what)
        if key not in seen:
            seen.add(key)
            unique.append(f)
    order = {"high": 0, "medium": 1, "low": 2}
    unique.sort(key=lambda f: (order[f.severity], f.id))

    if as_json:
        print(json.dumps({"findings": [asdict(f) for f in unique], "ghost": [sl["title"] for sl in SLIDES]}, ensure_ascii=False, indent=1))
        return
    if not unique:
        print("No static signs found. Render the slides and judge them by eye before calling it clean.")
        if "--ghost" in sys.argv:
            print_ghost()
        return
    counts = Counter(f.severity for f in unique)
    print(f"{len(unique)} findings · {counts['high']} high · {counts['medium']} medium · {counts['low']} low\n")
    for f in unique:
        print(f"[{f.severity:<6}] {f.id:<3} {f.where}\n         {f.what}\n         → {f.fix}")
    by_id = Counter(f.id for f in unique)
    print("\nBy sign: " + ", ".join(f"{k}×{v}" for k, v in sorted(by_id.items())))
    print("Static candidates only. Confirm on the rendered page and source data. Style choices may be appropriate; no authorship or factual certification is implied.")
    if "--ghost" in sys.argv:
        print_ghost()


if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:
        pass
