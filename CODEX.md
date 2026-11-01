# OpenAI Codex & API Guide: Clear Visualizations

Tämä ohje opastaa visualisointiskillin käyttöön **OpenAI Codexissa**, **ChatGPT:ssä (Custom GPT / System Prompt)** sekä **OpenAI API / Assistants** -ympäristöissä.

---

## 1. Pika-asetus: Custom GPT tai ChatGPT System Prompt

Kopioi alla oleva ohjeistus ChatGPT:n tai Custom GPT:n **Instructions**-kenttään:

```markdown
You are Clear Slides, an expert presentation designer and data visualization architect.
Your mission is to replace generic AI aesthetics ("slop") with audience- and evidence-tailored visual explanations.

Key directives:
1. Visual grammar before layout: Map the core question to the right form (dumbbell/slope for change, small multiples for pattern differences, waterfall for financial bridge, swimlanes for process, layered architecture for mechanisms).
2. Advanced compositions: Use Evidence Plate (visual dominates >80%), Aligned Comparison (shared axes), Layered Analytical Page (3 cognitive depths: finding, evidence, caveats), and Stable Context with Changing Focus.
3. Financial rigor: Bar charts MUST start at zero. Bubble sizes scale by area (pi*r^2). Football field shows EV vs Equity distinctly. Waterfall arithmetic reconciles exactly.
4. Precision & units: 2–3 significant figures on slides. Every figure must have an explicit unit and timeframe (e.g. "Liikevaihto FY25, M€: 12,4").
5. Finnish norms: Sentence case for titles. No hype buzzwords ("mullistava", "pelinmuuttaja"). Decimal comma (12,4), non-breaking space for thousands (1 234 567), space before % (46 %), currency after figure (12,4 M€), true minus sign (− U+2212).
6. Codename hygiene: Never leak real corporate names in confidential M&A decks. Zero tolerance for unpopulated placeholders ([Company], XX, TBD).
```

Lataa Custom GPT:n **Knowledge**-tiedostoiksi:
- `SKILL.md` (täysi visualisointiohjeistus)
- `assets/deck.html` (valmis 1920×1080 canvas-moottori)

---

## 2. OpenAI Codex / Koodausassistentin käyttö

Kun OpenAI Codexia käytetään esitysten tai datavisualisointien koodaamiseen (HTML/SVG, Python tai React):

### A. Itsenäinen HTML/SVG-esitysmoottori (`assets/deck.html`)
Codex voi generoida dioja suoraan `deck.html`-tiedoston pohjalle:
- **Canvas:** Kiinteä 1920 × 1080 px (`#stage`), skaalautuu automaattisesti ikkunan kokoon (`fit()`).
- **Typografia:** $2\text{ px} = 1\text{ pt}$ (vastaa PowerPoint-mittoja).
- **Värit ja tokenit:** Käytä `:root`-muuttujia (`--bg`, `--ink`, `--accent`, `--category-a` jne.).
- **Kaaviot:** Suora inline SVG puhtailla vektoreilla tai sisäänrakennettu `deck.chart.bars()`.

### B. Python-koodaus (`python-pptx`)
Kun pyydät Codexia luomaan PowerPoint-esityksiä:
```python
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

prs = Presentation()
prs.slide_width = Inches(13.333)  # 16:9 widescreen
prs.slide_height = Inches(7.5)

# Käytä token-järjestelmän mukaisia värejä
NAVY = RGBColor(0x1B, 0x2B, 0x4B)
ORANGE = RGBColor(0xF4, 0x79, 0x20)
PALE_BG = RGBColor(0xF5, 0xF4, 0xEF)
```

---

## 3. OpenAI Assistants / API -integraatio

Käytä API-kutsussa `system`-viestinä:

```python
from openai import OpenAI

client = OpenAI()

with open("OPENAI.md", "r", encoding="utf-8") as f:
    system_prompt = f.read()

response = client.chat.completions.create(
    model="gpt-4o",  # tai o1 / o3-mini
    messages=[
        {"role": "system", "content": system_prompt},
        {
            "role": "user",
            "content": "Suunnittele hallitukselle sivu: Toistuva liikevaihto ja churn 2024–2026.",
        },
    ],
)
print(response.choices[0].message.content)
```
