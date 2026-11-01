# Linter signals

`scripts/lint.py` reports candidates with short ids. A candidate is a place to look, not proof of a defect and not a sign of who or what made the deck. By default, style signals are reported as context (low severity with a question to ask); `--strict-style` reports them at full severity when a brief explicitly wants a restrained look.

## Integrity and readability

| IDs | Inspect | Remedy when confirmed |
| --- | --- | --- |
| H1 | Unresolved placeholders, English or Finnish (`[Company]`, `[Lähde]`, `XX`, `TBD`, `Lisää otsikko`) | Fill from the source or state plainly that the value is unavailable |
| H3 | Forbidden names in a codename deck (text, notes, file properties) | Inspect visible and embedded material; remove genuine leaks |
| X0 | Unreadable input or a missing inspection dependency | Repair the input or report the check as not done |
| N4, N7 | Mixed number formats, or possibly different values for one metric and period | Reconcile definition, period, entity, unit and source |
| N5, N8 | Suspicious example data, or more precision than the decision needs | Check provenance; label synthetic data; round, or keep precision that is warranted |
| K6, K7 | Claim without source and scope, or change without a baseline | Source and scope the claim; state what the change compares to |
| G1 | Perspective that distorts quantities | Use an accurate 2D encoding |
| G5, G7, G9 | Unreadable labels, missing context, misleading axes | Repair the reading or interpretation problem |
| T7, L3 | Text below 9 pt, or content running off the slide | Check the intended display size, the text role and any intentional bleed |

## Finnish norms (F)

Run when the deck is Finnish: `--lang=fi`, `<html lang="fi">` or Finnish text. These follow Kielitoimisto and are not matters of taste; fix them unless a brand's official spelling says otherwise.

| ID | Finding | Correct form |
| --- | --- | --- |
| F1 | Title Case or ALL CAPS heading | Sentence case: `Toistuva liikevaihto kasvoi 46 % vuodessa` |
| F2 | Percent sign without a space | `46 %`, `3,2 %-yks.` |
| F3 | Hyphen as a minus sign | `−0,6` (U+2212) |
| F4 | Hyphen in a range | `2024–2026`, `10,5–12,5x` |
| F5 | Straight, English or German quotation marks | `”näin”` and `’näin’` |
| F6 | Decimal point before a unit | `12,4 M€`, `11,4x` |
| F7 | Currency symbol before the number | `12,4 M€`, `12,4 milj. €` |
| F8 | Finnish text under a non-Finnish `<html lang>` | `lang="fi"` |

F1 ignores titles that contain lowercase words, so proper names in a sentence-case title (`Translink Corporate Finance neuvoo myyjää`) pass.

## Contextual signals

| IDs | Potential concern | Valid exceptions, or the better question |
| --- | --- | --- |
| N1, N3, N6 | Vague titles, filler pages, a count in the title that the page does not show | Descriptive diagram titles, real questions and useful agendas are valid. A promised count should still match. |
| N2, N9 | Unstructured density | Self-read pages can be dense. Are the details grouped and readable? |
| N10–N13, N15–N17 | Generic structure, repetition, weak ending | Repeated forms help comparison; close according to the occasion. |
| K1, K2, K4, K5, K8–K11 | Empty or inconsistent copy | Keep quotations, names and technical terms. Correct a vague claim rather than deleting a word mechanically. |
| T1–T6, T8–T10 | Unclear type hierarchy or font problems | Bold, serif, italics and short uppercase labels can work. Verify the font and the hierarchy. |
| C1–C10 | Distracting effects or inconsistent colour roles | Gradients can encode quantity; categorical palettes and real brand colours are legitimate. |
| L1, L2, L4–L8, S1 | Weak grouping, drift, generic composition | Compare within layout families. Diagram geometry need not follow the text grid. |
| D1–D13 | Decoration in place of explanation | A box can define a boundary, an arrow a route, a label plus colour improves accessibility. |
| G2–G4, G6, G8, G10 | Chart form or styling mismatch | Choose by the task; legends, markers and several hues can be useful. |
| I1, I2, P1–P4 | Filler images or icons | Prefer relevant, authentic evidence; keep an informative image even if its treatment is expressive. |
| M1–M6 | Motion competing with the explanation | A controlled reveal or meaningful simulation can help; keep a readable static state. |
| H2, H4 | Tool traces or missing disclosure | Remove accidental scaffolding; keep required credits, provenance and confidentiality notices. |

## What a static scan cannot see

The number check uses text proximity and can confuse entities, adjusted and reported values, periods or rounding. The scan does not read images, chart workbooks or embedded files, so it cannot certify confidentiality. "No findings" is not a factual or security certificate: render the pages and read them.

## The opposite failure: too little

A rich explanation reduced to a slogan, a distribution reduced to one average, a mechanism reduced to unconnected nouns, a comparison split across pages or an essential caveat moved into an unreadable footnote can all pass the linter and still be poor design. Look for these in the review.
