# Charts, analytical diagrams and tables

Start with the question and available evidence. Read [visual-grammar.md](visual-grammar.md) for mechanisms, maps, architecture and other forms beyond statistical charts. [human-guides.md](human-guides.md) links fuller visual vocabularies.

## Selection

| Task | Useful alternatives | Decision criterion |
| --- | --- | --- |
| Compare magnitude | Bars, dots, aligned table | Whether precision, rank or the overall pattern matters |
| Compare two states | Dumbbell, slope, paired panels | Matched cases and comparable measures; avoid hiding relevant intermediate states |
| Show change | Lines, columns, small multiples | Continuous trend, discrete periods or comparisons among groups |
| Show composition | Stacked bar, treemap, a simple pie | Whole and denominator are meaningful; choose bars when precise comparison matters |
| Show distribution | Dots, histogram, box or violin | Sample size, spread, outliers and audience familiarity |
| Show relationship | Scatter, connected scatter, faceting | A relationship is not proof of causality |
| Show uncertainty | Interval, range, fan, scenarios | State what the bounds mean; distinguish scenarios from probabilities |
| Explain a balance | Waterfall | Components reconcile to the displayed total |
| Show geographic pattern | Appropriate map, often with an inset | Geography adds information; use rates and denominators appropriately |
| Show flows | Flow diagram, Sankey or alluvial | Quantitative widths require reconciled flow data |

A complex chart is justified by a complex relationship, not by novelty. Explain an unfamiliar encoding with a short key or a worked example. A simpler chart is preferable when it preserves the needed information.

## Honest encodings

- Length-encoded bars start at zero. A line or dot chart can use a tighter labelled range when appropriate. Keep comparison scales consistent or clearly explain the difference.
- Areas and volumes must correspond to the quantities claimed. Do not map values to circle radii when the audience will interpret area.
- Distinguish missing data from zero. Preserve discontinuities, uncertainty, meaningful outliers and actual/forecast boundaries.
- Direct-label where readable. Use a legend when it genuinely reduces clutter. Meaningful categorical colours are allowed; do not force unrelated categories into indistinguishable greys.
- Put annotations near the observation they explain. Separate an observed change from a proposed explanation.
- Use useful reference lines or restrained gridlines. Do not remove context merely to make the chart look cleaner.
- Show measure, unit, period, population or denominator where relevant, and an identifiable source. Reconcile values against source material rather than trusting the static linter.
- Maintain editable chart data when the requested format supports it. For unsupported chart types, preserve an editable vector or reproducible source and disclose any editing limitation.

## Small multiples

Choose panel ordering and consistent scales to support the intended comparison. Put the most important within-panel comparison together. A shared reference can help readers compare across panels. A repeated form is useful here, including across successive slides. If panels become too small, group them or provide a detailed read version rather than silently shrinking labels.

## Finance forms

**Valuation range / football field.** Use horizontal intervals by method, with one value basis and unit. State the underlying period and assumptions. Label the offer or reference line. Do not mix enterprise and equity values. Display uncertainty rather than manufacturing a precise point estimate.

**Bridge.** Verify that the start plus contributions equals the end. Show signs and any residual. Group small items only when the grouping preserves the decision-relevant explanation.

**Comparables.** Use an aligned table with common metric definitions and periods. Dates, adjustments, n/m values and sample exclusions matter. Distinguish medians and the subject company without overwhelming the values.

**Sensitivity.** Label assumptions on both axes. Identify the base case with a label as well as emphasis. Use an ordered or meaningful diverging colour scale where it helps; keep the numbers readable.

**Revenue and margin.** Prefer aligned panels when the units differ. A dual-axis chart needs explicit axes and careful assessment of the comparison it implies; coincident lines do not establish a relationship.

**Cohorts and concentration.** Use comparable cohort ages and denominators. Show material concentration and exceptions rather than a summary that conceals them.

## Tables

Use tables when exact values or several criteria must be inspected together. Align numbers by decimal or right edge, label units in the headers, use consistent precision and distinguish totals. Grouping, whitespace and restrained rules usually suffice. Highlight the row or cells relevant to the question; a heatmap can use more colour when colour represents the data.

## Review

Check the question/form match, source fidelity, units, scale, uncertainty, label legibility, colour meaning and editability. A misleading axis, unsupported title or wrong value is a defect even if every other design check passes. There is no additive score that makes such a defect acceptable.
