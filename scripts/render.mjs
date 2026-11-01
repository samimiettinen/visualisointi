// render.mjs: render a deck slide by slide, measure what the audience will see, and
// lay every slide out on one contact sheet so the deck can be judged as a sequence.
//
//   node render.mjs <deck.html | deck.pptx | deck.pdf> <out-dir> [--width=1920] [--height=1080] [--no-audit] [--pdf]
//
// HTML decks: every `.slide` element (or `section`) becomes one PNG. Decks built on
// assets/deck.html are driven through window.deck.go(i); scroll decks are captured
// element by element. Animations are frozen at their end state.
// PPTX and PDF: converted with LibreOffice (soffice) and Poppler (pdftoppm) when present.
//
// Writes  <out>/slide-01.png …, <out>/contact-sheet.png, and for HTML <out>/audit.json
// plus a readable <out>/audit.md: per slide the smallest text in points, the number of
// sizes, families, left edges and words, low-contrast text and anything overflowing.
// Licensing: ../LICENSE.

import { createRequire } from "node:module";
import { createServer } from "node:http";
import { existsSync, mkdirSync, readFileSync, readdirSync, writeFileSync, copyFileSync, rmSync } from "node:fs";
import { execFileSync } from "node:child_process";
import { basename, dirname, extname, join, normalize, resolve } from "node:path";
import { tmpdir } from "node:os";

const args = process.argv.slice(2);
const flag = (name, dflt) => args.find((a) => a.startsWith(`--${name}=`))?.split("=")[1] ?? dflt;
const [input, outArg] = args.filter((a) => !a.startsWith("--"));
if (!input || !outArg) {
  console.error("usage: node render.mjs <deck.html|deck.pptx|deck.pdf> <out-dir> [--width=1920] [--height=1080] [--no-audit]");
  process.exit(1);
}
const W = Number(flag("width", 1920));
const H = Number(flag("height", 1080));
const audit = !args.includes("--no-audit");
const wantPdf = args.includes("--pdf");
const out = resolve(outArg);
mkdirSync(out, { recursive: true });

async function browserKit() {
  for (const name of ["playwright", "playwright-core"]) {
    try { return await import(name); } catch {}
    try { return createRequire(join(process.cwd(), "package.json"))(name); } catch {}
    for (const root of (process.env.NODE_PATH || "").split(":").filter(Boolean)) {
      try { return createRequire(join(root, "__clear_slides__.cjs"))(name); } catch {}
    }
    try { return createRequire(join(execFileSync("npm", ["root", "-g"]).toString().trim(), "x"))(name); } catch {}
  }
  console.error("Playwright is not installed. Run `npm i -D playwright && npx playwright install chromium`.");
  process.exit(1);
}
const chrome = [process.env.CHROME_PATH, "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome", "/usr/bin/google-chrome", "/usr/bin/chromium"].find((p) => p && existsSync(p));

const has = (cmd) => { try { execFileSync("which", [cmd], { stdio: "ignore" }); return true; } catch { return false; } };
const pad = (n) => String(n).padStart(2, "0");

// ---------------------------------------------------------------- PPTX / PDF → PNG
function officeToPngs(file) {
  let pdf = file;
  if (extname(file).toLowerCase() !== ".pdf") {
    const soffice = ["soffice", "libreoffice", "/Applications/LibreOffice.app/Contents/MacOS/soffice"].find((c) => c.startsWith("/") ? existsSync(c) : has(c));
    if (!soffice) {
      console.error("LibreOffice is needed to render .pptx (brew install --cask libreoffice). Or export the deck to PDF from PowerPoint and pass the PDF.");
      process.exit(1);
    }
    const tmp = join(tmpdir(), `unslop-${Date.now()}`);
    mkdirSync(tmp, { recursive: true });
    execFileSync(soffice, ["--headless", "--convert-to", "pdf", "--outdir", tmp, file], { stdio: "ignore", timeout: 180000 });
    pdf = join(tmp, basename(file).replace(/\.[^.]+$/, ".pdf"));
  }
  if (!has("pdftoppm")) {
    console.error("Poppler's pdftoppm is needed to rasterise the PDF (brew install poppler).");
    process.exit(1);
  }
  execFileSync("pdftoppm", ["-png", "-r", "110", pdf, join(out, "slide")], { stdio: "ignore" });
  // pdftoppm writes slide-1.png or slide-01.png depending on page count; normalise
  const files = readdirSync(out).filter((f) => /^slide-\d+\.png$/.test(f)).sort((a, b) => parseInt(a.slice(6)) - parseInt(b.slice(6)));
  return files.map((f, i) => {
    const target = join(out, `slide-${pad(i + 1)}.png`);
    if (join(out, f) !== target) { copyFileSync(join(out, f), target); rmSync(join(out, f)); }
    return target;
  });
}

// ---------------------------------------------------------------- static server for HTML
function serve(root) {
  const types = { ".html": "text/html", ".css": "text/css", ".js": "text/javascript", ".mjs": "text/javascript", ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".webp": "image/webp", ".avif": "image/avif", ".svg": "image/svg+xml", ".woff2": "font/woff2", ".woff": "font/woff", ".json": "application/json" };
  const server = createServer((req, res) => {
    const path = normalize(join(root, decodeURIComponent(req.url.split("?")[0])));
    if (!path.startsWith(root) || !existsSync(path)) { res.writeHead(404); return res.end(); }
    res.writeHead(200, { "content-type": types[extname(path).toLowerCase()] ?? "application/octet-stream" });
    res.end(readFileSync(path));
  });
  return new Promise((done) => server.listen(0, "127.0.0.1", () => done(server)));
}

const FREEZE = `
  *, *::before, *::after { animation-duration: 0s !important; animation-delay: 0s !important; animation-iteration-count: 1 !important;
    transition: none !important; caret-color: transparent !important; }
  .reveal, [class*="reveal"], [data-build] { opacity: 1 !important; transform: none !important; filter: none !important; }
  html { scroll-behavior: auto !important; scroll-snap-type: none !important; }`;

// Runs inside the page for one slide element: measures what the audience sees.
function measure(slideIndex) {
  const slides = window.__unslopSlides;
  const slide = slides[slideIndex];
  const sr = slide.getBoundingClientRect();
  const scale = 1920 / sr.width; // normalised geometry
  const cssToCanvas = 1920 / slide.offsetWidth; // CSS font size excludes a parent transform
  const parseRGB = (c) => { const m = c.match(/rgba?\(([^)]+)\)/); if (!m) return null; const p = m[1].split(/[\s,\/]+/).filter(Boolean).map(Number); return { r: p[0], g: p[1], b: p[2], a: p.length > 3 ? p[3] : 1 }; };
  const lum = ({ r, g, b }) => { const f = (v) => { v /= 255; return v <= 0.03928 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4; }; return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b); };
  const contrast = (a, b) => { const [x, y] = [lum(a), lum(b)].sort((p, q) => q - p); return (x + 0.05) / (y + 0.05); };
  const bgOf = (el) => {
    let layers = [];
    for (let n = el; n; n = n.parentElement) {
      const cs = getComputedStyle(n);
      if (cs.backgroundImage && cs.backgroundImage !== "none") return null; // image or gradient: unknown, judge by eye
      const c = parseRGB(cs.backgroundColor);
      if (c && c.a > 0) { layers.push(c); if (c.a >= 0.99) break; }
    }
    let base = { r: 255, g: 255, b: 255 };
    for (const l of layers.reverse()) base = { r: l.r * l.a + base.r * (1 - l.a), g: l.g * l.a + base.g * (1 - l.a), b: l.b * l.a + base.b * (1 - l.a) };
    return base;
  };
  const texts = [];
  const walker = document.createTreeWalker(slide, NodeFilter.SHOW_TEXT, { acceptNode: (n) => n.textContent.trim() ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_REJECT });
  const seen = new Set();
  while (walker.nextNode()) {
    const el = walker.currentNode.parentElement;
    if (!el || seen.has(el)) continue;
    seen.add(el);
    const cs = getComputedStyle(el);
    if (cs.visibility === "hidden" || cs.display === "none" || Number(cs.opacity) < 0.05) continue;
    const r = el.getBoundingClientRect();
    if (r.width === 0 || r.height === 0) continue;
    texts.push({ el, cs, r, node: walker.currentNode, text: walker.currentNode.textContent.trim() });
  }
  const sizes = new Set(), families = new Set(), weights = new Set(), lefts = new Set();
  let minPx = Infinity, minText = "", words = 0;
  const lowContrast = [], overflow = [], negTrack = [], caps = [], broken = [];
  for (const t of texts) {
    const svg = t.el.closest("svg");
    const vb = svg?.viewBox?.baseVal;
    const svgScale = svg && vb && vb.width ? svg.getBoundingClientRect().width * scale / vb.width : cssToCanvas;
    const px = parseFloat(t.cs.fontSize) * svgScale;
    sizes.add(Math.round(px));
    families.add(t.cs.fontFamily.split(",")[0].replace(/["']/g, "").trim());
    weights.add(t.cs.fontWeight);
    words += t.text.split(/\s+/).length;
    if (px < minPx) { minPx = px; minText = t.text.slice(0, 40); }
    if (t.cs.display !== "inline" && !svg) lefts.add(Math.round(((t.r.left - sr.left) * scale) / 8) * 8);
    const ls = parseFloat(t.cs.letterSpacing);
    if (!isNaN(ls) && ls < -0.2 && px < 48) negTrack.push(t.text.slice(0, 30));
    if (t.cs.textTransform === "uppercase" && t.text.length > 3) caps.push(t.text.slice(0, 30));
    const fg = parseRGB(svg ? t.cs.fill : t.cs.color);
    const bg = bgOf(t.el);
    if (fg && bg && !(t.cs.webkitTextFillColor || "").includes("rgba(0, 0, 0, 0)")) {
      const ratio = contrast(fg, bg);
      const large = px >= 48 || (px >= 37 && Number(t.cs.fontWeight) >= 600);
      if (ratio < (large ? 3 : 4.5)) lowContrast.push({ text: t.text.slice(0, 30), ratio: Math.round(ratio * 10) / 10 });
    }
    // a short figure or label that wraps, like "118.5" over "%": join number and unit with a non-breaking space
    if (t.text.length <= 24 && /\d/.test(t.text) && !svg) {
      const range = document.createRange(); range.selectNodeContents(t.node);
      const tops = [...range.getClientRects()].filter((q) => q.width > 0).map((q) => q.top);
      const lineGap = parseFloat(t.cs.fontSize) * 0.5;
      if (tops.length > 1 && Math.max(...tops) - Math.min(...tops) > lineGap) broken.push(t.text);
    }
    if (t.r.right > sr.right + 1 || t.r.bottom > sr.bottom + 1 || t.r.left < sr.left - 1 || t.r.top < sr.top - 1) overflow.push(t.text.slice(0, 30));
    if (t.el.scrollHeight > t.el.clientHeight + 2 && /(hidden|clip)/.test(t.cs.overflowY)) overflow.push(`${t.text.slice(0, 30)} (clipped)`);
  }
  const title = slide.querySelector("h1, h2, [data-title], .title")?.textContent.trim().replace(/\s+/g, " ") ?? "";
  return {
    slide: slideIndex + 1,
    title,
    words,
    minPt: Math.round((minPx / 2) * 10) / 10,
    minText,
    sizes: [...sizes].sort((a, b) => a - b),
    families: [...families],
    weights: [...weights].sort(),
    leftEdges: lefts.size,
    lowContrast,
    overflow,
    negativeTracking: negTrack,
    uppercase: caps,
    brokenFigures: broken,
  };
}

async function renderHtml(file) {
  const root = dirname(file);
  const server = await serve(root);
  const { chromium } = await browserKit();
  const browser = await chromium.launch(chrome ? { executablePath: chrome } : {});
  const page = await browser.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 1 });
  const url = `http://127.0.0.1:${server.address().port}/${encodeURIComponent(basename(file))}?render`;
  await page.goto(url, { waitUntil: "networkidle" }).catch(() => page.goto(url));
  await page.addStyleTag({ content: FREEZE });
  await page.evaluate(() => document.fonts.ready);
  const count = await page.evaluate(() => {
    let slides = [...document.querySelectorAll(".slide")];
    if (!slides.length) slides = [...document.querySelectorAll("section")];
    window.__unslopSlides = slides;
    // scroll decks reveal content with .visible / .active classes; the engine shows one slide at a time itself
    if (typeof window.deck?.go !== "function") slides.forEach((s) => s.classList.add("visible", "active", "is-active"));
    return slides.length;
  });
  if (!count) { console.error("No .slide or <section> elements found."); process.exit(1); }
  const driven = await page.evaluate(() => typeof window.deck?.go === "function");
  const pngs = [], report = [];
  for (let i = 0; i < count; i++) {
    if (driven) await page.evaluate((n) => window.deck.go(n, { instant: true }), i);
    else await page.evaluate((n) => window.__unslopSlides[n].scrollIntoView({ block: "start" }), i);
    await page.waitForTimeout(120);
    const target = join(out, `slide-${pad(i + 1)}.png`);
    const handle = driven ? (await page.$("#stage, .stage")) ?? (await page.evaluateHandle((n) => window.__unslopSlides[n], i))
                          : await page.evaluateHandle((n) => window.__unslopSlides[n], i);
    await handle.screenshot({ path: target });
    pngs.push(target);
    if (audit) report.push(await page.evaluate(measure, i));
  }
  if (wantPdf) {
    const pdfPath = join(out, basename(file).replace(/\.[^.]+$/, ".pdf"));
    await page.emulateMedia({ media: "print" });
    await page.pdf({ path: pdfPath, width: `${W}px`, height: `${H}px`, printBackground: true, preferCSSPageSize: true });
    console.log(`pdf → ${pdfPath}`);
  }
  await browser.close();
  server.close();
  return { pngs, report };
}

async function contactSheet(pngs) {
  const { chromium } = await browserKit();
  const browser = await chromium.launch(chrome ? { executablePath: chrome } : {});
  const cols = pngs.length <= 4 ? 2 : pngs.length <= 9 ? 3 : 4;
  const page = await browser.newPage({ viewport: { width: 1800, height: 900 } });
  const cells = pngs.map((p, i) => {
    const data = readFileSync(p).toString("base64");
    return `<figure><img src="data:image/png;base64,${data}"><figcaption>${i + 1}</figcaption></figure>`;
  }).join("");
  await page.setContent(`<style>body{margin:0;background:#e9e9ea;font:500 15px/1 ui-monospace,Menlo,monospace;color:#555}
    main{display:grid;grid-template-columns:repeat(${cols},1fr);gap:24px;padding:32px}
    figure{margin:0}img{width:100%;display:block;box-shadow:0 1px 2px rgba(0,0,0,.08),0 4px 16px rgba(0,0,0,.06)}
    figcaption{padding-top:8px}</style><main>${cells}</main>`);
  await page.waitForTimeout(200);
  const target = join(out, "contact-sheet.png");
  await page.screenshot({ path: target, fullPage: true });
  await browser.close();
  return target;
}

function writeAudit(report) {
  writeFileSync(join(out, "audit.json"), JSON.stringify(report, null, 1));
  const allSizes = new Set(report.flatMap((r) => r.sizes));
  const allFamilies = new Set(report.flatMap((r) => r.families));
  const lines = ["# Render audit", "", `${report.length} slides · ${allSizes.size} text sizes across the deck · families: ${[...allFamilies].join(", ")}`, "",
    "Sizes use the 1920-wide design convention of 2 canvas px per presentation point, not CSS physical points. Evaluate type roles and intended viewing distance. Counts and style flags below are review hints, not defects. Contrast over complex images or SVG backgrounds requires visual inspection.", "",
    "| # | Title | Words | Min pt | Sizes | Left edges | Issues |", "|---|---|---|---|---|---|---|"];
  for (const r of report) {
    const issues = [];
    if (r.minPt < 9) issues.push(`text at ${r.minPt} pt (“${r.minText}”)`);
    if (r.words > 180) issues.push(`density review: ${r.words} words`);
    if (r.sizes.length > 5) issues.push(`type-role review: ${r.sizes.length} sizes`);
    if (r.families.length > 2) issues.push(`${r.families.length} families`);
    if (r.leftEdges > 5) issues.push(`alignment review: ${r.leftEdges} left edges`);
    if (r.lowContrast.length) issues.push(`low contrast: ${r.lowContrast.map((c) => `“${c.text}” ${c.ratio}:1`).slice(0, 3).join("; ")}`);
    if (r.overflow.length) issues.push(`overflow: ${r.overflow.slice(0, 3).join("; ")}`);
    if (r.negativeTracking.length) issues.push(`negative tracking on small text`);
    if (r.uppercase.length) issues.push(`uppercase: ${r.uppercase.slice(0, 2).join("; ")}`);
    if (r.brokenFigures.length) issues.push(`figure broken across lines: ${r.brokenFigures.slice(0, 2).map((x) => `“${x}”`).join("; ")}`);
    lines.push(`| ${r.slide} | ${r.title.slice(0, 60).replace(/\|/g, "/")} | ${r.words} | ${r.minPt} | ${r.sizes.length} | ${r.leftEdges} | ${issues.join(" · ") || "–"} |`);
  }
  lines.push("", "## Title sequence", "", "Read the titles in order. For an argument, check the logic; for an explanation or reference, check the progression or navigation. Titles alone cannot verify the evidence.", "");
  report.forEach((r) => lines.push(`${r.slide}. ${r.title || "(no title)"}`));
  writeFileSync(join(out, "audit.md"), lines.join("\n") + "\n");
}

const file = resolve(input);
const ext = extname(file).toLowerCase();
let pngs, report = [];
if (ext === ".html" || ext === ".htm") ({ pngs, report } = await renderHtml(file));
else if ([".pptx", ".potx", ".ppt", ".key", ".odp", ".pdf"].includes(ext)) pngs = officeToPngs(file);
else { console.error(`Unsupported file type: ${ext}`); process.exit(1); }

const sheet = await contactSheet(pngs);
if (report.length) writeAudit(report);
console.log(`${pngs.length} slides → ${out}`);
console.log(`contact sheet → ${sheet}`);
if (report.length) console.log(`audit → ${join(out, "audit.md")}`);
