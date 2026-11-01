# Formats and file mechanics

Keep the requested destination and format. When improving an existing editable deck, preserve its format, masters and editability unless the user asks for a conversion. Use the available presentation authoring skill or connector for file operations; this skill supplies design judgment.

## HTML

`assets/deck.html` is a fixed-canvas starter with navigation, optional builds, print styling and a basic non-negative bar helper. It is not the only permitted layout or a general charting library. The example content is illustrative and must be replaced.

Set the language, title, type roles and colour roles. Use native HTML for text and SVG for custom diagrams. The starter supports full-width evidence, paired comparisons, read pages and image-led pages as well as the original split. Add structure when the content needs it; do not force the evidence into its default sample.

For more complex charts use an appropriate chart library or deterministic drawing code. Keep the dataset and transformation reproducible. The small bar helper is only for finite non-negative values; use another chart for negative values, intervals or multiple axes.

The starter uses installed system fonts and has no remote assets by default. To use a specific licensed font, supply local font files or an approved hosted source. Confirm availability and disclose any external dependency. Test offline if offline operation is required.

```bash
python3 scripts/slop_lint.py deck.html --ghost --mode=read
node scripts/render.mjs deck.html qa --pdf
```

The PDF export uses the HTML canvas's print dimensions; its physical page size is not the reference PowerPoint size. Check the target export requirements separately.

## PowerPoint

Use the available presentation tooling for native text, shapes, charts, notes, themes and masters. Keep house templates in place when polishing. Preserve chart editability where the format supports it; complex custom diagrams may use grouped editable shapes or vectors with accompanying source.

Use masters and placeholders for recurring elements where they help revision. Reuse an approved example by its purpose, then replace inherited data, notes, dates and conclusions. Test the longest real label and densest required case before propagating a layout. Do not force an explanatory diagram into an unsuitable placeholder grid.

Inspect fonts and text wrapping in the intended renderer. A substitute-font preview is a limited check. The bundled linter can inspect PPTX with python-pptx installed; that dependency is for inspection, not a requirement to author with it.

## Google Slides and hosted slide artifacts

Use the connected editing tools and destination guidance available in the host. Do not assume a named artifact type exists or create a parallel file unnecessarily. Use exports only when requested or needed for a permitted verification step.

## PDF and screenshots

For review, inspect the pages directly; no rebuild is needed. For improvement, reconstruct directly into the requested editable format if necessary. State that reconstruction cannot recover missing source data, hidden notes or original chart editability. Do not make an intermediate HTML clone unless it serves a concrete purpose.

## Tools and limitations

- `slop_lint.py` provides static candidates and a title sequence. It does not read every embedded object or verify all numerical definitions and source claims. The default profile treats aesthetic choices as contextual; `--strict-style` restores older style warnings when that brief is desired. `--mode=present` changes density hints, not the page's design.
- `render.mjs` uses Node with Playwright. PPTX/PDF rasterisation additionally needs LibreOffice/Poppler as applicable. Its computed-style audit cannot fully resolve text over images, complex SVG backgrounds, intentional clipping or font substitution. Inspect rendered output.
- `NODE_PATH` can point to an existing Node package directory. Prefer available runtimes; install project dependencies only in an allowed development directory. Never bundle node_modules in the skill.
- Use a fresh QA folder for a new render to avoid mixing pages from different versions.

A visual one-pager may use a similar approach at its own page size. Responsive websites and dashboards should use their own design and implementation workflows.
