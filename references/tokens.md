# Design system: the reference values

This file is the single source for sizes, grid and colour values. SKILL.md, the engine in `assets/deck.html` and `lint.py` refer here. A measured house template takes precedence over everything below (see [brands.md](brands.md)).

## Canvas and grid

- Keep an existing aspect ratio. A new widescreen deck uses a fixed 1920 × 1080 canvas that the engine scales to the window.
- The PowerPoint widescreen page is 13⅓ × 7½ in, or 960 × 540 pt, so **2 canvas px = 1 presentation pt**. This is a convention of this design system, not the browser's CSS px-to-pt conversion.
- Default grid in `assets/deck.html`: 96 px side margins, 88 px top, 72 px bottom, 12 columns of 122 px with 24 px gutters, 8 px spacing steps (8, 16, 24, 32, 48, 64).
- The grid is a convenience for text and recurring layouts. A chart may span the page, a comparison may use equal halves and a diagram follows its own geometry. Optical adjustments are legitimate.
- Keep title and footer positions stable within each recurring layout family.

## Type sizes

Presentation points; canvas px are twice these values.

| Role | Self-read deck | Speaker-led deck |
| --- | --- | --- |
| Cover or statement | 44–56 | 56–72 |
| Action title (two lines at most) | 24–36 | 28–44 |
| Lead sentence | 16–20 | 20–26 |
| Body and annotations | 14–18 | 22–30 |
| Chart labels and table text | 12–16 | 18–24 |
| Sources and footnotes | 9–11 | 10–12 |

- Nothing goes below 9 pt. A caveat the reader must see is not a footnote.
- The engine defaults are a self-read deck: title 26 pt (52 px), body 15 pt (30 px), labels 12 pt (24 px), sources 10 pt (20 px).
- One family, or one deliberate pair, and five or six sizes are usually enough. A rich diagram may need more label roles; that is fine when each size has a job.
- Use tabular lining figures where columns must align (`font-variant-numeric: tabular-nums lining-nums`), `text-wrap: balance` for titles and `text-wrap: pretty` for paragraphs.
- Large titles take −0.01 to −0.02 em letter-spacing; body text stays at normal spacing.
- Check glyph coverage (å, ä, ö at every weight) and whether the recipient has the font. A LibreOffice render does not prove a PowerPoint recipient has it.

## Colour roles

Name the roles before choosing swatches:

- **Surface and text:** `--bg`, `--raised`, `--ink`, `--ink-2`, `--ink-3`.
- **Emphasis:** `--accent`, for the item the page is about.
- **Categorical:** `--category-a`, `--category-b`, … stable identities across charts and pages.
- **Context series:** `--series-1` to `--series-3`, neutrals for series that are not the point.
- **Sequential and diverging:** ordered ramps for magnitude, two hues around a meaningful midpoint.
- **Status:** `--positive`, `--negative`, always with a word or symbol as well.

There is no fixed number of accents. Use the smallest palette that keeps the distinctions accurate, and label categories directly as well as by hue.

## Contrast

- Text: at least 4.5:1 against its actual background; 3:1 for large text (24 px or more, or 18.5 px bold, on screen; on the canvas 48 px, or 37 px bold).
- Data marks and boundaries the reader needs: at least 3:1 against the surface they sit on.
- Check the real background, including `--raised` panels, images and transparency.

Engine defaults, checked against both surfaces:

| Token | Value | On `--bg` #ffffff | On `--raised` #f3f3f2 |
| --- | --- | --- | --- |
| `--ink` | #171717 | 17.9:1 | 16.1:1 |
| `--ink-2` | #4f4f4f | 8.2:1 | 7.4:1 |
| `--ink-3` | #666666 | 5.7:1 | 5.2:1 |
| `--series-2` | #6b6b6b | 5.3:1 | 4.8:1 |
| `--series-3` | #8a8a8a | 3.5:1 | 3.1:1 |
| `--accent` | #ae5029 | 5.3:1 | 4.8:1 |

The engine's categorical defaults (teal #006b6b, blue #3559a6, rust #a34b27) are placeholders for a deck without a brand. Replace them with the brand's roles and re-check.

## Images, lines and motion

- Use authentic images at sufficient resolution. Full bleed is fine; a crop must keep the evidential detail.
- Connectors and rules must survive the final display size. Arrowheads and labels define direction and meaning; colour reinforces them.
- Motion explains a change or guides a live reveal. Honour reduced-motion settings and keep every static state readable, because the PDF and the printout have no animation.
