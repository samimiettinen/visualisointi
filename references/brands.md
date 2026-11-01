# House brands and templates

A real brand wins over this skill's defaults. Keep its logo, colours, fonts and layouts, and use the skill to fix what is placed inside them. If the brand itself contains a problem (a gradient logo tile, an accent that fails contrast as text), keep it unless the user agrees to a change, and mention it in the delivery note.

## Measuring a template

From a .pptx or .potx:

- Theme colours and fonts: unzip and read `ppt/theme/theme1.xml`: `a:clrScheme` gives dk1, lt1, dk2, lt2 and accent1–6; `a:fontScheme` gives the major (title) and minor (body) fonts.
- Layouts and positions: with python-pptx, read `prs.slide_layouts` and each placeholder's `left`, `top`, `width` and `height` in EMU (914 400 per inch, 12 700 per point). The title placeholder of the content layout sets the title position for every content slide.
- Keep footer, page number and confidentiality placeholders on the layout.
- Render a few template slides with `render.mjs` to see the intended look.

From a PDF or a website: sample colours from the rendered pages, identify the fonts and write them into the `:root` tokens of `assets/deck.html`.

Record measured values in the task notes. Change the profiles below only when the user asks for that maintenance.

## Profile format

```
### Name
- Status: measured from <source, date> | provisional
- Colours: role → hex, with contrast notes for text use
- Fonts: titles, body, figures; fallbacks for machines without them
- Layout: title position, footer content, logo placement
- Use: what the accent is for, what never to do with the brand
```

## Profiles

A profile is a starting point. The organisation's current official template wins wherever the two differ; check it before client use.

### Translink Corporate Finance (TLCF)

- Status: provisional, from the TLCF design system (2026).
- Colours: navy #1B2B4B for titles, dark surfaces and the main chart series; orange #F47920 as the accent.
- Contrast: orange on white is 2.8:1, so it fails as text of any size. Use orange as a fill (key bar, key figure block) with navy text on it (5.1:1), or orange text only on navy (5.1:1). Where orange must be text on white, use the darker shade #B85A12 (4.7:1 on white, 4.2:1 on #F5F4EF, so on a cream surface only at 24 pt or larger). Navy on white is 14.1:1.
- Fonts: Barlow Condensed for titles and key figures, Barlow for body and tables (both free on Google Fonts). In .pptx files sent outside TLCF, embed them or fall back to Arial Narrow and Arial.
- Use: navy carries the structure, orange marks the one thing the page is about. Sell-side teasers and IMs are read decks under a codename; run `lint.py --forbid` with the real names.

### DCM Capital

- Status: provisional; confirm against DCM Capital's own template before external use.
- Colours: dark slate #182B33 (text), pale cream #F5F4EF (page), teal #006B6B (main accent), rust #A34B27 (second accent), muted slate #52656B (metadata).
- Contrast: all four text colours pass 4.5:1 on white and on cream (slate 14.7:1 on white, teal 6.3:1, rust 5.8:1, muted slate 6.1:1). White text on teal is 6.3:1 and on rust 5.8:1.
- Fonts: Inter or the system sans-serif, tabular figures.
- Use: teal for the main finding, rust for a contrasting case; keep the cream page calm.

Add further profiles (client templates, Neuvottelija) in the same format as they are measured.
