---
name: clear-slides
description: Design, improve, or review presentations, pitch decks, board packs, technical diagrams, and visual one-pagers with purposeful visual explanations, honest data visualization, and editorial hierarchy. Replaces generic AI templates and minimalism dogma with audience- and evidence-tailored representations. Covers visual grammar, chart selection, financial forms, tokens, Finnish/English number conventions, brand fidelity, and multi-scale QA. Works across Antigravity, Claude, and OpenAI environments.
metadata:
  author: Sami Miettinen
  version: 2.0.0
---

# Clear Slides: Visual Explanations & Presentation Design

A comprehensive design skill for turning complex evidence into clear, compelling, and human-crafted visual presentations. It eliminates generic AI aesthetics ("slop"), respects house brand systems, preserves analytical fidelity, and produces editable, durable output across Antigravity, Claude, and OpenAI.

---

## 1. Foundational Philosophy

1. **Explanatory power over decorative minimalism:** Make the audience understand relationships, mechanisms, and patterns they could not see as easily in a plain paragraph. A title and three generic boxes is not a universal solution.
2. **Form follows audience and evidence:** Choose the visual representation from the underlying data and reading conditions (speaker-led talks vs. self-read board packs vs. hybrid memos).
3. **Structured density is a feature:** Do not strip out denominators, uncertainty ranges, counterevidence, definitions, or decision-critical caveats to hit an arbitrary word count. Structure density with clear visual hierarchy.
4. **Richness belongs in the explanation:** Use scale relationships, direct annotations, aligned small multiples, mechanism cutaways, process routes, and authentic screenshots. Remove decorative shapes and filler icons that contribute no meaning.
5. **Zero generic AI aesthetic:** Avoid predictable gradient cards, floating pastel spheres, decorative checkmark icons, buzzword headlines, and sloganized simplifications.
6. **Cross-platform portability:** Designed to work natively inside Antigravity (with executable scripts and progressive disclosure) and directly portable to Claude (Claude Projects / Claude Code) and OpenAI (Custom GPTs / System Instructions).

---

## 2. End-to-End Workflow

Follow this 7-step process for any presentation design, redesign, or review:

```
[1. Diagnose Job & Audience] ──> [2. Storyboard Meaning & Form] ──> [3. Select Visual Form]
                                                                             │
[7. Deliver & Disclose] <── [6. Multi-Scale QA Review] <── [5. Compose Token System] <── [4. Prototype Hard Page]
```

### Step 1: Diagnose the Job & Reading Conditions
Determine the core parameters from the request and source materials:
- **Action:** Create from scratch, improve/redesign existing deck, or review/audit (review produces actionable critique without editing).
- **Audience & Decision:** Who reads or watches? What decision, understanding, or evaluation does the deck drive?
- **Reading Conditions:**
  - *Speaker-led (Talk/Keynote):* High visual impact, large typography (28–44 pt), minimal on-screen text, presenter carries the narrative.
  - *Self-read (Board pack / Slidedoc / M&A IM):* High structured density, standalone explanations, 14–18 pt body, complete definitions, caveats, and sources.
  - *Dual-use:* Clear primary reading path with local annotations and comprehensive footnotes/appendices.
- **Constraints:** Brand identity, confidentiality rules (e.g. M&A codenames), required slide count, aspect ratio (16:9 widescreen default), and editable format (HTML, PPTX, Google Slides).

### Step 2: Storyboard Meaning and Form Together
Do not write titles in isolation. For every slide, define:
1. **Audience Question / Purpose:** What specific question is addressed?
2. **Supported Message:** What is the answer or takeaway?
3. **Evidence & Source:** What data points, quotes, or mechanism verify it?
4. **Visual Form:** Which diagrammatic or chart structure carries the explanation?
5. **Material Caveats:** What constraint, risk, or definition could alter the decision?

*Ghost Deck Check:* Read the proposed slide titles in sequence. The titles alone must tell a coherent narrative without gaps or repeated conclusions.

### Step 3: Choose Representation Before Layout
Select the diagram, chart, or spatial layout that directly visualizes the core relationship (see *Visual Grammar Matrix* below). Never default to a bulleted list or a split 2-column box layout before considering the evidence.

### Step 4: Prototype the Hardest Representative Page Early
Before composing the full deck, build the most complex analytical page, technical mechanism, or dense comparison first. Testing the extreme case (longest labels, densest data, hardest explanation) ensures the design system holds under stress.

### Step 5: Compose with the Token System
Apply consistent typographic roles, semantic color coding, a locked 12-column grid, and uniform spacing rhythm across all pages. Reuse approved structural patterns for identical questions.

### Step 6: Multi-Scale Review & QA
Perform factual verification separately from visual critique. Audit at three distinct visual scales: Contact Sheet (macro narrative), First Glance (visual hierarchy), and Full-Size Inspection (micro precision).

### Step 7: Deliver and Disclose
Deliver the editable presentation (HTML/SVG, native PPTX shapes/charts, or Google Slides). Clearly document:
- Key design decisions and structural improvements made.
- Source reconciliation and data integrity confirmations.
- Any unresolved limitations or assumptions.

---

## 3. Visual Grammar & Form Selection Matrix

Map the audience's underlying question directly to the appropriate visual structure:

| Audience Question | Optimal Visual Form | Construction Principles | Common Pitfalls to Avoid |
| :--- | :--- | :--- | :--- |
| **What changed between two states?** | Dumbbell plot, slope chart, paired panels | Shared zero or common scale; matched categories; direct endpoint labels | Hiding intervening trends; unmatched sample sizes |
| **Where do patterns differ across groups?** | Small multiples | Identical axes across all panels; logical ordering (by value or region) | Panel auto-scaling that exaggerates minor differences |
| **What contributes to the final result?** | Waterfall / Bridge chart | Reconciled start, explicit positive/negative contributions, clear net total | Overlapping contributions; unexplained residuals |
| **What differs between alternatives?** | Aligned comparison matrix / Feature profiles | Same criteria in exact same order; comparable evidence beside each | Arbitrary 1–5 star scores without objective evidence |
| **Who handles what, and when?** | Swimlane / Cross-functional flow | Actors on rows/lanes; chronological left-to-right; labelled hand-offs and returns | Vague arrows implying unverified causality |
| **How does the system work?** | Layered architecture / Mechanism schematic | Named modules, explicit boundaries, interfaces, and directional flows | Floating boxes of nouns with no relationships |
| **How does a physical object work?** | Annotated photo / Cutaway / Exploded view | Authentic photograph or declared schematic; local callouts with leader lines | Decorative stock illustrations disguised as real anatomy |
| **Where does it happen?** | Map with localized insets | Meaningful geography; population-normalized rates; regional detail insets | Mapping country totals when location adds no explanatory value |
| **How uncertain is the estimate?** | Fan chart, range / interval bars, scenarios | Defined statistical bounds (e.g. 80/95%); distinct scenario assumptions | Fake precision; unlabeled confidence bands |
| **How are cases distributed?** | Histogram, dot plot, box plot | Disclosed sample size, sensible bin widths, explicit outliers | Replacing a wide distribution with an average alone |
| **How do entities connect?** | Network graph, hierarchy tree, flow map | Declared node and edge semantics; highlighted primary path | Tangled "hairballs" with no readable takeaway |
| **How does a whole divide?** | Treemap, stacked bar, 100% bar | Common denominator; mutually exclusive parts; direct labels | 3D pie charts; unmeasured slices; non-summing totals |
| **What is the actual user experience?** | Annotated screenshot sequence | Authentic interface crops; numbered step sequence; callout highlights | Fake generic UI mockups; unreadable full-page screenshots |
| **What must the executive decide?** | Structured analytical read page | Prominent decision/finding; grouped evidence panels; visible caveat layer | Walls of unstructured bullet points replacing analysis |

---

## 4. Advanced Composition Patterns

Move beyond the monotonous "title + chart left + bullet text right" layout. Use compositions tailored to the cognitive task:

```
┌──────────────────────────────────────────────┐  ┌──────────────────────────────────────────────┐
│ [Evidence Plate]                             │  │ [Aligned Comparison]                        │
│ ┌──────────────────────────────────────────┐ │  │ ┌────────────────────┐ ┌───────────────────┐│
│ │                                          │ │  │ │ Case A: Baseline   │ │ Case B: Option 2  ││
│ │          Primary Diagram / Map           │ │  │ │ [Shared Axis Chart]│ │ [Identical Scale] ││
│ │      (with direct local callouts)        │ │  │ └────────────────────┘ └───────────────────┘│
│ └──────────────────────────────────────────┘ │  │ Explanatory contrast notes placed directly  │
│ Concise source, definitions & caveat footer  │  │ beneath the corresponding case               │
└──────────────────────────────────────────────┘  └──────────────────────────────────────────────┘

┌──────────────────────────────────────────────┐  ┌──────────────────────────────────────────────┐
│ [Layered Analytical Page]                    │  │ [Stable Context with Changing Focus]         │
│ Layer 1: Core Action Finding / Decision      │  │ Slide N: Stage 1 active (highlighted color) │
│ ┌──────────────────────┐┌──────────────────┐ │  │ Slide N+1: Stage 2 active (same geometry!)  │
│ │ Primary Trend Chart  ││ Contributing Mix │ │  │ ┌──────────────────────────────────────────┐ │
│ └──────────────────────┘└──────────────────┘ │  │ │ [System Architecture: Node 1 ──> Node 2] │ │
│ Layer 3: Assumptions, caveats, and sources   │  │ └──────────────────────────────────────────┘ │
└──────────────────────────────────────────────┘  └──────────────────────────────────────────────┘
```

1. **Evidence Plate:** The visual explanation (diagram, map, chart) occupies 80%+ of canvas area. Concise annotations point directly to noteworthy features.
2. **Aligned Comparison:** Two or more options arranged side-by-side sharing identical axes, scales, and typography. The reader compares visually rather than decoding text.
3. **Overview Plus Detail:** Macro system diagram on one side with a magnified, connected inset of the critical subsystem on the other.
4. **Layered Analytical Page:** Structured for three reading depths:
   - *Top Layer (First glance):* Core finding or strategic question.
   - *Middle Layer (Inspection):* 2–3 grouped, complementary evidence blocks (e.g. trend + composition breakdown).
   - *Bottom Layer (Verification):* Assumptions, definitions, caveats, and sources.
5. **Image with Interpretation:** Authentic documentary photograph or product screenshot with selective crops, numbered focal callouts, and provenance caption.
6. **Stable Context with Changing Focus:** Across successive slides, keep complex system geometry 100% stationary. Highlight only the active step or path using contrast, weight, or numbered badges. This preserves spatial orientation.

---

## 5. Charts, Tables & Financial Visualizations

### Core Visualization Rules
- **Zero baselines:** Bar and column charts encoding length must start at zero. Line charts showing relative changes may use a focused non-zero range, provided the axis is clearly labeled.
- **Area and volume fidelity:** Bubble and circle sizes must scale with area ($\pi r^2$), never radius or diameter.
- **Direct labeling:** Place labels directly beside lines and bars whenever possible. Eliminate distant legends that force back-and-forth eye saccades.
- **Visual annotations:** Annotate milestones and inflection points directly on the chart canvas. Clearly separate observed data from explanatory hypotheses.
- **Show uncertainty and baselines:** Never present projections without explicit baseline dates, historical vs. forecast dividers, and confidence ranges.

### Corporate Finance & M&A Encodings
- **Valuation Range ("Football Field"):**
  - Use horizontal interval bars grouped by methodology (DCF, Trading Comps, Transaction Comps, 52-week range).
  - Explicitly declare valuation basis: Enterprise Value (EV) vs. Equity Value. Never mix the two on a single chart without clear separation.
  - Draw explicit vertical reference lines for current share price, offer price, or unaffected 30-day VWAP.
- **Bridge / Waterfall Chart:**
  - Verify arithmetic reconciliation: $\text{Starting Base} + \sum(\text{Additions}) - \sum(\text{Deductions}) = \text{Ending Total}$.
  - Distinguish positive contributions, negative drags, and subtotal/total pillars with distinct fills.
  - Footnote any rounding discrepancy rather than fudging figures.
- **Public & M&A Comparables Table:**
  - Aligned data matrix with standardized financial metrics (EV/EBITDA, P/E, EV/Sales, Revenue Growth, EBITDA Margin).
  - Strict period consistency: LTM (Last Twelve Months), NTM (Next Twelve Months), FY1, FY2.
  - Separate peer median and mean rows clearly from individual companies. Highlight the subject target company distinctly.
- **Sensitivity Matrix (Two-Way Table):**
  - Label both axes unambiguously (e.g., WACC on rows, Terminal Growth Rate on columns).
  - Highlight the designated base case cell with a distinct border and background fill.
  - Use a subtle diverging or sequential color ramp; ensure text numbers maintain high contrast (>4.5:1).
- **High-Density Data Tables:**
  - Align all numbers to the right (or on the decimal point); align text to the left; center short codes/dates.
  - Always state unit and currency in column headers (`EURm`, `USDk`, `%`).
  - Use tabular numbers (`tabular-nums`) to align digits vertically. Use subtle horizontal rules; avoid heavy vertical gridlines.

---

## 6. Design System & Presentation Tokens

### Canvas & Grid Standards
- **Reference Resolution:** 1920 × 1080 px widescreen (16:9).
- **PowerPoint Point Equivalence:** In this system, $2\text{ px} = 1\text{ pt}$ (canvas is $960 \times 540\text{ pt}$ equivalent).
- **Grid Layout:** 12-column grid. Standard margins: $96\text{ px}$ left/right, $88\text{ px}$ top, $72\text{ px}$ bottom. Column width: $122\text{ px}$ with $24\text{ px}$ gutters.
- **Spacing Rhythm:** Strictly follow an $8\text{ px}$ baseline grid ($8, 16, 24, 32, 48, 64\text{ px}$).

### Typography System
Keep type roles disciplined (maximum 1–2 typefaces, 5–6 size tiers):

| Role | Self-Read / Slidedoc (pt / px) | Speaker-Led Talk (pt / px) | Purpose & Usage |
| :--- | :--- | :--- | :--- |
| **Display / Cover** | 44–56 pt / 88–112 px | 56–72 pt / 112–144 px | Title slide and closing statement |
| **Action Title** | 24–32 pt / 48–64 px | 32–44 pt / 64–88 px | Main slide takeaway (max 2 lines) |
| **Lead / Subtitle** | 16–20 pt / 32–40 px | 20–26 pt / 40–52 px | Framing sentence or question |
| **Body / Explanation** | 14–16 pt / 28–32 px | 20–26 pt / 40–52 px | Descriptive text and bullet explanations |
| **Table & Chart Labels** | 11–14 pt / 22–28 px | 14–18 pt / 28–36 px | Data points, axis labels, matrix cells |
| **Footnotes & Sources** | 9–11 pt / 18–22 px | 10–12 pt / 20–24 px | Sources, definitions, confidentiality |

*Rules:*
- Always enable `font-variant-numeric: tabular-nums lining-nums`.
- Titles should use `text-wrap: balance`; paragraphs should use `text-wrap: pretty`.
- Ensure proper letter-spacing: $-0.01\text{em}$ to $-0.02\text{em}$ for large titles; normal for body.

### Semantic Color Architecture
Define colors by function, never arbitrary decoration:
1. **Surface & Background (`--bg`, `--raised`):** High clarity light (#FFFFFF / #F6F6F4) or dark surface.
2. **Text & Lines (`--ink`, `--ink-2`, `--ink-3`):** Primary text (#171717), secondary text (#4F4F4F), muted captions/axes (#737373).
3. **Emphasis / Focal (`--accent`):** Reserved for the one metric, bar, or pathway that conveys the primary finding.
4. **Categorical Series (`--category-a`, `--category-b`, etc.):** Consistent color identity for entities across all slides.
5. **Sequential Scale:** Ordered tonal ramp for quantities (e.g. light to deep navy).
6. **Diverging Scale:** Two distinct hues diverging from a neutral midpoint (e.g. negative red to positive green/blue).
7. **Status:** Explicit semantic state (Success, Warning, Failure), always accompanied by text or icons.

*Contrast Requirements:* Minimum 4.5:1 for body and data text against background; minimum 3:1 for large display titles and essential graphical boundaries (WCAG 2.1 AA standard).

---

## 7. Numbers, Sources & Transaction Integrity

### The Absolute Number Rules
1. **One metric, one period = one exact value everywhere:** The same figure appearing in the executive summary, financials slide, chart, and appendix must reconcile perfectly.
2. **Standard precision:**
   - Slide body: 2 to 3 significant figures (`€47.4m`, `46%`, `11.4x`).
   - Appendices / Data rooms: Full financial precision.
   - Estimates: No false precision (write "about €2.4bn", never top-down "€2.374bn").
3. **Mandatory units and measurement periods:** Every number must carry an explicit unit and time frame (`Revenue FY25, M€: 12.4`, not `Revenue: 12.4`). State whether values are Actual, Budget, Forecast, or Pro Forma.
4. **Mandatory source citations:** Every data-bearing slide must feature a complete source line in the footer:
   *Example:* `Source: Management accounts FY21–FY25; S&P Capital IQ, enterprise values as of 31 Oct 2026.`

### Number Formatting Conventions

| Element | English Convention | Finnish Convention |
| :--- | :--- | :--- |
| **Thousands & Decimals** | `1,234.5` (comma thousand, dot decimal) | `1 234,5` (non-breaking space thousand, comma decimal) |
| **Percentage** | `46%` or `46 %` (consistent) | `46 %` (space before sign) |
| **Percentage Points** | `3.2 pp` | `3,2 %-yks.` |
| **Currency & Magnitude** | `€12.4m` or `EUR 12.4m` or `EURm 12.4` | `12,4 M€` or `12,4 milj. €` or `12,4 MEUR` |
| **Negative Values** | `−0.6` (true minus `−` U+2212) or `(0.6)` | `−0,6` (true minus `−` U+2212) |
| **Numerical Ranges** | `2024–2026`, `10.5–12.5x` (en-dash `–`) | `2024–2026`, `10,5–12,5x` (en-dash `–`, no spaces) |
| **Dates** | `31 Oct 2026`, `Q3 2026` | `31.10.2026`, `Q3/2026`, `lokakuu 2026` |
| **Fiscal Periods** | `FY25`, `LTM Sep-26`, `NTM` | `2025`, `LTM 9/2026` |

### Confidentiality & M&A Hygiene
- **Codename Protection:** In confidential M&A, divestment, or PE decks, real corporate names of target, seller, or bidders must **never** appear anywhere: slide canvas, speaker notes, chart series names, image filenames, alt text, or file properties.
- **Confidentiality Footers:** Quietly stamp required notices: `Strictly confidential · Project Aurora`.
- **Zero Placeholder Tolerance:** No deck ships with unresolved placeholders: `[Company]`, `XX`, `TBD`, `YYYY`, `Lorem Ipsum`, `Click to add title`, `Lisää otsikko`.

---

## 8. Finnish & Nordic Deck Guidelines

When producing Finnish presentations, follow Kielitoimisto norms:
1. **Sentence Case Norm:** Finnish titles and headings use sentence case (`Toistuva liikevaihto kasvoi 46 % vuodessa`). Never use English Title Case or ALL CAPS.
2. **No English Loan Structures or Buzzword Clichés:**
   - Eliminate generic hype words: *mullistava, vallankumouksellinen, saumaton, maailmanluokan, huippuluokan, ainutlaatuinen, innovatiivinen, seuraavalle tasolle, pelinmuuttaja, valjastaa*.
   - Replace with factual statements describing the mechanism or result.
   - Cut `Key takeaways` or translate cleanly; replace `Next steps` with `Seuraavat vaiheet` accompanied by firm dates.
3. **Accurate Finnish Business Terminology:**
   - Revenue: *Liikevaihto* | Recurring revenue: *Toistuva liikevaihto*
   - EBITDA: *Käyttökate* | EBIT: *Liikevoitto*
   - Fiscal year: *Tilikausi* | Adjusted: *Oikaistu*
   - Cash flow: *Kassavirta* | Free cash flow: *Vapaa kassavirta*
   - Enterprise Value (EV): *Velaton arvo* | Equity Value: *Oman pääoman arvo*
4. **Finnish Typography:**
   - Quotation marks: `”Näin”` (same character at start and end).
   - Parenthetical dash: En-dash with spaces (` – `).
   - Compound words (*yhdyssanat*): Finnish compound words can be very long (*asiakastyytyväisyyskysely*). Allocate ~10% extra column width, enable `hyphens: auto; lang="fi"`, and use soft hyphens (`&shy;`) to prevent awkward line breaks.
5. **Bilingual Decks:** One language per slide. If parallel text is mandatory, keep language order consistent (Finnish primary, Swedish/English secondary in muted ink). Never mix number conventions on a single slide.

---

## 9. House Brands & Template Measurement

When working with client templates or house brand guidelines, existing brand assets take precedence over generic styling:

### Measuring a PowerPoint Template (`.pptx` / `.potx`)
1. Unzip the `.pptx` and inspect `ppt/theme/theme1.xml`:
   - `a:clrScheme`: Extract `dk1`, `lt1`, `dk2`, `lt2`, and `accent1` through `accent6`.
   - `a:fontScheme`: Extract major (title) and minor (body) fonts.
2. Inspect slide master placeholders using `python-pptx`:
   - Measure coordinates (`left`, `top`, `width`, `height`) in EMU ($914{,}400\text{ EMU} = 1\text{ inch}$; $12{,}700\text{ EMU} = 1\text{ pt}$).
   - The title placeholder on the content layout sets the universal title baseline.

### Verified Brand Profiles

#### Translink Corporate Finance (TLCF)
- **Palette:** Navy `#1B2B4B` (primary structure, titles, main chart series), Orange `#F47920` (accent / emphasis).
- **Contrast Rule:** Orange on white is only 2.8:1 (fails WCAG). Use orange as background fill with navy text (5.1:1), or orange text only on navy (5.1:1). Where orange text on white is unavoidable, use ink shade `#B85A12` (4.7:1).
- **Typography:** Barlow Condensed (titles, headlines, key metrics), Barlow (body text, tables, captions). Fallbacks: Arial Narrow / Arial.
- **Style:** Read decks, high analytical density, codename-compliant.

#### DCM Capital
- **Palette:** Dark Slate `#182B33` (primary ink), Pale Cream `#F5F4EF` (page background), Teal `#006B6B` (primary accent), Rust `#A34B27` (secondary contrast), Muted Slate `#52656B` (metadata).
- **Typography:** Inter / system sans-serif, clean editorial hierarchy, tabular figures.

---

## 10. Multi-Scale Review & Quality Assurance

Review presentations using three distinct visual scales, followed by automated linting:

```
┌───────────────────────────┐      ┌───────────────────────────┐      ┌───────────────────────────┐
│ Scale 1: Contact Sheet    │ ───> │ Scale 2: First Glance     │ ───> │ Scale 3: Micro Inspection │
│ Macro narrative flow,     │      │ 5-second entry point,     │      │ Numbers, sources, units,  │
│ rhythm, visual variety    │      │ hierarchy, main pattern   │      │ wrapping, caveats, bounds │
└───────────────────────────┘      └───────────────────────────┘      └───────────────────────────┘
```

### The 8 Review Questions
1. **Purpose:** What exact takeaway or decision does this page serve?
2. **Evidence Fidelity:** Does the action title match the actual data shown without exaggeration?
3. **Visual Explanation:** What relationship does the visual reveal that text alone cannot?
4. **Visual Hierarchy:** Is there a clear focal point, followed by structured reading layers?
5. **Density & Legibility:** Is text readable at the target viewing distance without eye strain?
6. **Consistency:** Do colors, symbols, and layouts maintain identical meanings across slides?
7. **Craft & Polish:** Are there any text collisions, awkward wraps, clipped labels, or misaligned arrows?
8. **Export & Delivery:** Does the final exported file (PDF, PPTX) preserve all fonts, layouts, and editability?

### Automated Linter Signals (`slop_lint.py`)
Use the bundled linter to detect static candidates:
- **`H1` / `H2`:** Unresolved placeholders (`[Company]`, `TBD`) or accidental scaffolding.
- **`H3`:** Forbidden names in codename decks (confidentiality breach).
- **`N4` / `N7`:** Mixed number conventions or conflicting metric values across slides.
- **`N5` / `N8`:** Unmarked illustrative/synthetic data or false precision.
- **`K6` / `K7`:** Unsupported claims or missing comparison baselines.
- **`G1` / `G5` / `G9`:** Distorted perspective, unreadable chart labels, or misleading axes.
- **`T7` / `L3`:** Text size below legible threshold or layout overflow.

---

## 11. Technical Toolchains & Scripts

### HTML/SVG Presentation Engine (`assets/deck.html`)
- Standalone HTML presentation engine. Zero build steps, zero npm dependencies.
- Uniform 1920 × 1080 canvas scaled with CSS transforms to fit any display.
- Built-in slide navigation (arrows, space, full-screen `F`, print `P`).
- Custom SVG diagrams and chart primitives (`deck.chart.bars()`).

### Helper Scripts
Execute helpers from workspace or allowed scripts directory:

```bash
# 1. Static linter: check formatting, codenames, number consistency, and ghost deck titles
python3 scripts/slop_lint.py deck.html --ghost --mode=read

# 2. Strict codename check (for M&A teasers & confidential materials)
python3 scripts/slop_lint.py deck.html --forbid="Target Oy,Buyer Corp"

# 3. Headless renderer: produce PNG slides, contact sheet, and audit report (Node + Playwright)
node scripts/render.mjs deck.html qa_output --pdf

# 4. Verify test suite
python3 scripts/test_lint.py /tmp/test-scratch
```

---

## 12. Cross-Platform Instructions (Antigravity, Claude, OpenAI)

This skill is designed for full cross-platform compatibility:

### In Antigravity (Gemini Environment)
- This `SKILL.md` is discovered automatically in `.agents/skills/Presentations/` or `Global/Skills/Presentations/`.
- The agent activates the skill when you ask to create, redesign, or review a deck.
- The agent has direct access to run `scripts/slop_lint.py`, `scripts/render.mjs`, and read templates in `assets/` and `references/`.

### In Claude (Claude Projects, Claude Code, or Claude.ai)
- **Claude Projects:** Copy the contents of this `SKILL.md` (or the companion `CLAUDE.md`) into the **Project Instructions**. Add sample decks or templates to Project Knowledge.
- **Claude Code CLI:** Place `CLAUDE.md` in the project root. Claude Code will automatically ingest these design rules for presentation coding.
- **Key instruction prompt for Claude:**
  > *"Act as an expert presentation designer and data visualization architect following the Clear Slides methodology. Prioritize visual explanations, honest chart encodings, structured density, and zero generic AI slop. Select visual grammar from the audience question before choosing layouts."*

### In OpenAI (ChatGPT Custom GPTs, API, or System Prompts)
- **Custom GPTs:** In the GPT Builder, paste the contents of `OPENAI.md` into the **Instructions** field. Upload `assets/deck.html` and key reference documents into **Knowledge**.
- **System Instructions (API / Playground):** Set role to System with the core principles, visual grammar matrix, and number conventions.
- See `agents/openai.yaml` and `agents/openai-instructions.md` for pre-formatted templates.

---

*Authored by Sami Miettinen · Clear Slides Framework v2.0*
