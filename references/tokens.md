# Design system and starting values

A measured house template takes precedence. The following values are starting points for a new deck, not a signature look. Choose type and colour for the subject and reading conditions, then verify the rendering.

## Canvas and grid

Preserve an existing aspect ratio. For a new widescreen HTML deck, the supplied engine uses a fixed 1920 × 1080 canvas that scales uniformly. Its reference PowerPoint size is 13⅓ × 7½ inches, or 960 × 540 presentation points. Thus 2 canvas pixels correspond to 1 presentation point **in this particular design system**; this is not the browser's CSS px-to-pt conversion.

Start around 80–100 canvas pixels for outer margins, 24–40 for gutters and an 8-pixel spacing rhythm. A 12-column grid is a convenience. With 96-pixel side margins and 24-pixel gutters, the columns are 122 pixels wide. A chart may span the page; a comparison may use equal halves; a read page may combine columns and aligned panels. Optical adjustments are legitimate.

Establish stable title and footer placements within each recurring layout. An image-led page or large diagram may use a different composition while preserving the same hierarchy. Avoid squeezing every visual into a chart-and-commentary split.

## Typography

| Role | Self-read deck, presentation pt | Speaker-led deck, presentation pt |
| --- | --- | --- |
| Main title | 24–36 | 28–44 |
| Body | 14–18 | 22–30 |
| Chart labels and table text | 12–16 | 18–24, larger in a large room |
| Source and optional reference text | 9–11 | 10–12 if not part of the spoken explanation |
| Statement or headline figure | As the composition requires | As the composition requires |

These are starting ranges. Assess legibility at the expected view size and distance. A source footnote cannot carry an essential caveat the audience must read. A font's x-height, weight and rendering affect usable size.

Use a small set of type roles. One family or a deliberate complementary pair is usually sufficient. Weight 700, a serif title, a meaningful italic or a compact uppercase label can be appropriate. Avoid all-heavy text, ornamental emphasis on random words and tiny tightly tracked labels. Keep the supplied brand fonts when possible.

Use tabular figures where columns must align. Verify required language glyphs. No named font is guaranteed on every recipient device; inspect installation/embedding or test the intended export. A successful LibreOffice render does not prove a PowerPoint recipient has the font.

## Colour roles

Name the roles before selecting swatches:

- **Surface and text:** clear contrast and a coherent light or dark system.
- **Emphasis:** the item currently discussed or compared.
- **Categorical:** stable identities across charts, diagrams and pages.
- **Sequential:** increasing magnitude with an ordered ramp.
- **Diverging:** departure around a meaningful midpoint.
- **Status:** an explicitly defined state, accompanied by a word or symbol.

There is no universal one-accent limit. Use the smallest palette that communicates the distinctions accurately. Distinguish categories through labels or shape as well as hue. Sequential and diverging data ramps are useful gradients; a decorative wash is a different design choice.

For readability, aim for at least 4.5:1 text contrast, or 3:1 for sufficiently large text. Essential non-text marks need visible contrast too. Check actual backgrounds, including images, transparency and neighbouring fills. This is a design check, not a claim of complete accessibility conformance.

A possible starting palette is dark ink #182B33, pale background #F5F4EF, teal #006B6B, rust #A34B27 and blue #3559A6. This is an example, not a prescribed palette; any text/fill combination still needs checking.

## Images, lines and emphasis

Use authentic imagery at sufficient resolution. Intentional full bleed is allowed; cropping must preserve evidential details. Frame a screenshot only when the frame helps orientation. Do not add generic visuals just to occupy space.

Connectors and rules must survive the final display size. Diagram colour can encode roles; arrowheads and labels define direction and meaning. Use emphasis consistently. Colour plus a direct label can improve accessibility and is not redundant decoration.

Use motion to explain a transformation or guide a live reveal. Honour reduced-motion settings and make final static states readable. Avoid effects that compete with the explanation.

---
