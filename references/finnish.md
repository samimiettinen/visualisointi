# Finnish and Nordic decks

Rules that make a Finnish deck read as written in Finnish, not translated. Follow Kielitoimisto norms. If the suomen-kieli skill is available, run all Finnish copy through it. `lint.py` checks the mechanical part (F1–F8, see [signs.md](signs.md)); wording, compounds and register still need reading.

## Language

- Set `lang="fi"` on the HTML root (and `lang="sv"` on Swedish passages), so hyphenation, quotes and screen readers follow the language.
- Sentence case is the Finnish norm. Never Title Case, never ALL CAPS labels.
- Action titles work in Finnish too, often shorter: `Toistuva liikevaihto kasvoi 46 % vuodessa, ja käyttökate kääntyi positiiviseksi vuonna 2024`.
- Avoid English loan structures in titles (`Key takeaways` → cut; `Next steps` → `Seuraavat vaiheet` with dates).
- Hype words in Finnish: mullistava, vallankumouksellinen, saumaton, maailmanluokan, huippuluokan, ainutlaatuinen, innovatiivinen, seuraavalle tasolle, pelinmuuttaja, valjastaa. Replace with what the thing does.
- Common terms: liikevaihto (revenue), toistuva liikevaihto (recurring revenue), käyttökate (EBITDA), liikevoitto (EBIT), tilikausi (fiscal year), oikaistu (adjusted), nettokassavirta, velaton arvo (EV), oman pääoman arvo (equity value).

## Numbers and symbols

- Decimal comma: `12,4`. Thousands with a non-breaking space: `1 234 567`. In HTML use `&nbsp;` or U+202F; in PowerPoint a non-breaking space (Ctrl+Shift+Space on Windows, Option+Space on Mac) so numbers never break across lines.
- Percent with a space: `46 %`. Percentage points: `3,2 %-yks.`
- Currency after the number with a space: `12,4 milj. €`, `12,4 M€` or `12,4 MEUR` in finance tables. One form per deck.
- Minus sign `−` (U+2212), not a hyphen, in tables.
- Ranges with an en dash, no spaces: `2024–2026`, `10,5–12,5x`.
- Dates `31.10.2026`, months in lowercase (`lokakuu 2026`), quarters `Q3/2026` or `3. neljännes 2026`. Times `9.30`.
- Multiples: `11,4x`.

## Typography

- Quotes are the same on both sides: `”Näin”` and `’näin’`. Apostrophe `’`.
- Dashes: en dash with spaces as a sentence dash (` – `), no em dashes.
- Abbreviations with a full stop: `milj.`, `mrd.`, `esim.`, `n.`; but `M€` and `MEUR` without.
- Long compound words (`asiakastyytyväisyyskysely`, `toiminnanohjausjärjestelmä`) break narrow columns. Give Finnish text about 10 % more width than English, use `hyphens: auto` with `lang="fi"` in HTML, and insert soft hyphens (`&shy;`) in long title words. Never justify text.
- Fonts must have proper å, ä and ö at every weight used. Check a bold title and a light label before committing to a family.

## Bilingual decks

- One language per slide; keep the same order everywhere when a slide carries two (Finnish first, then Swedish or English, the second in secondary colour).
- Numbers follow the language of the slide. A Finnish slide uses `12,4 M€`; the English appendix uses `€12.4m`. Never mixed on one slide.
- Titles stay parallel across language versions so the ghost decks match.

## Check

```bash
python3 scripts/lint.py deck.html --lang=fi --ghost
```

Read the ghost deck aloud: Finnish titles that sound translated (`Avainhavainnot`, `Seuraavat askeleet`) usually need rewriting rather than translating.

