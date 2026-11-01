# Numbers and sources

People act on the numbers in a deck. They have to be consistent, sourced and stated at a precision that fits the decision.

## One convention per deck

| | English | Finnish |
| --- | --- | --- |
| Thousands, decimals | 1,234.5 | 1 234,5 (non-breaking space) |
| Percent | 46% or 46 % (pick one) | 46 % |
| Percentage points | 3.2 pp | 3,2 %-yks. |
| Currency, millions | €12.4m or EUR 12.4m or EURm 12.4 | 12,4 M€ or 12,4 milj. € or 12,4 MEUR |
| Negative | −0.6 (minus sign) or (0.6) | −0,6 |
| Ranges | 2024–2026, 10.5–12.5x | 2024–2026, 10,5–12,5x |
| Dates | 31 Oct 2026, Q3 2026 | 31.10.2026, Q3/2026 |
| Fiscal periods | FY25, LTM Sep-26, NTM | 2025, LTM 9/2026 |

Pick one row per item at the start of the build and hold it. The linter's N4 finds mixtures.

## Same metric, same value

The same metric for the same period has one value everywhere: summary, financials slide, appendix, notes. The linter's N7 flags possible disagreements near metric names. It is a proximity heuristic with incomplete period/entity matching and a rounding tolerance, not a source reconciliation. Verify values against their definition, entity, period and unit. When two values disagree, inspect the owning sources and resolve them where the evidence permits; ask only when the conflict remains unresolved; it is often a different definition (ARR vs revenue, adjusted vs reported EBITDA, FTE vs heads). Label the definition when both appear.

## Precision

- Slides: two to three significant figures. `€47.4m`, `46 %`, `11.4x`. Full precision belongs in the appendix or the data room.
- One set, one precision: values in one table or chart share their decimals.
- Rounding makes totals disagree by a unit sometimes; footnote it once rather than fudging a component.
- No fake precision on estimates: a market size of `€2.37bn` from a top-down estimate is `about €2.4bn`.

## Units and periods

Every figure carries a unit and a period, in the label, the caption or the column head. `Revenue 12.4` is not a figure; `Revenue FY25, M€: 12.4` is. Say whether it is actual, budget, forecast or pro forma when that is not obvious.

## Sources

- Every slide with data has a source line in the footer: `Source: company management accounts FY21–FY25; Capital IQ, prices as of 30 Oct 2026`.
- Name the document and the date, not just the provider.
- For long read decks keep a source ledger beside the deck (`sources.md` or a sheet): figure, slide, source, locator (page, table, cell), date. It turns the number check into a lookup.
- Claims without a source (`market leader`, `#1 in the Nordics`) are asked about and either sourced with scope (`largest by revenue among Finnish field-service vendors, Inven, Oct 2026`) or removed.

## Codenames and confidentiality

- In a codename deck the real names of the target, the seller and the bidders never appear: not in text, speaker notes, chart data labels, image file names, alt text, file names or document properties. Use `lint.py --forbid="Real Name Oy,Other Name"` as one check, then inspect filenames, image/alt text, notes, chart data, linked or embedded objects and properties separately. The linter does not cover all of these surfaces.
- A confidentiality line in the footer where the deal needs it, quietly: `Strictly confidential · Project Aurora`.
- File properties must be truthful and match the project. Remove accidental scaffolding where appropriate; preserve required attribution, disclosures and provenance. Do not invent an adviser as author.
- Disclaimers at the back of teasers and IMs, set in the body size, never in 6 pt grey.

## Placeholders

Nothing ships with `[Company]`, `XX`, `TBD`, `YYYY`, `Lorem ipsum`, `Click to add title`, `Lisää otsikko`. The linter's H1 finds the usual ones in English and Finnish. Illustrative numbers in a template are marked as illustrative in the caption.
