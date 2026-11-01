# House brands and templates

A real brand wins over the brief's world. Keep its logo, colours, fonts and layouts, and use this skill to fix what is placed inside them. A slop element inside a brand (a gradient logo tile, a neon accent) stays unless the user agrees to change it; suggest it in the report.

## Measuring a template

From a .pptx or .potx:

- Theme colours and fonts: unzip and read `ppt/theme/theme1.xml` (`a:clrScheme` for dk1, lt1, dk2, lt2, accent1–6; `a:fontScheme` for the major and minor fonts).
- Layouts and positions: python-pptx, `prs.slide_layouts` and each placeholder's `left`, `top`, `width`, `height` in EMU (914 400 per inch, 12 700 per point). The title placeholder of the content layout sets the title position for every content slide.
- Footer, page number and confidentiality placeholders: keep them on the layout.
- Render a few template slides with `render.mjs` to see the intended look.

From a PDF or a website: sample the colours from the rendered pages, identify the fonts, and write them into the `:root` tokens of `assets/deck.html`.

Record measured values in the task material. Update reusable profiles only when that maintenance is requested.

## Profile format

```
### Name
- Source: where the values came from, and when
- Colours: role → hex, with contrast notes for text use
- Fonts: titles, body, figures; fallbacks for machines without them
- Layout: title position, footer content, logo placement
- Use: what the accent is for, what never to do with the brand
```

## Profiles

### Translink Corporate Finance (TLCF)

- Source: Sami's tlcf-design system (2026). Verify against the current official PowerPoint template before client use; the template wins where they differ.
- Colours: navy #1B2B4B for titles, dark surfaces and the main chart series; orange #F47920 as the accent.
- Contrast: orange on white is 2.8:1, so it fails as text of any size. Use orange as a fill (key bar, key figure block, signature) with navy text on it (5.1:1), or orange text only on navy (5.1:1). Where orange must be text on white, use the ink shade #B85A12 (4.7:1). Navy on white is 14.1:1.
- Fonts: Barlow Condensed for titles and key figures, Barlow for body and tables (both free, Google Fonts). In .pptx files sent outside TLCF, embed them or fall back to Arial Narrow and Arial.
- Use: navy carries the structure, orange provides emphasis; use additional defined chart roles when needed. Sell-side teasers and IMs are read decks, codename only; run the linter with `--forbid` and the real names.

Add more profiles here as they are measured: DCM Capital, Neuvottelija, client templates.
