# Google Antigravity & Gemini Guide: Clear Visualizations

Tämä ohje opastaa visualisointiskillin (`clear-slides`) käyttöönottoon ja hyödyntämiseen **Google Antigravityssä** ja **Gemini CLI / IDE** -ympäristöissä.

---

## 1. Miten Antigravity-skilli toimii?

Antigravity käyttää modulaarista taitojärjestelmää (*Skills*), joka hyödyntää **progressiivista paljastamista (Progressive Disclosure)**:
1. Käynnistyessään Antigravity lukee vain skillin nimen ja kuvauksen (`name: clear-slides`, `description: ...`) `SKILL.md`-tiedoston YAML-frontmatterista.
2. Kun käyttäjä pyytää esityksen suunnittelua, uudistamista tai auditointia, agentti aktivoi skillin ja lataa täyden ohjeistuksen kontekstiin.
3. Agentti osaa itsenäisesti lukea syventävät viitedokumentit (`references/`) ja ajaa tarkistusskriptit (`scripts/`).

---

## 2. Asennus ja käyttöönotto Antigravityssä

### Vaihtoehto A: Globaali taito (Kaikissa projekteissa käytettävissä)
Sijoita kansio koneesi globaaliin taitohakemistoon:
```bash
# Esimerkki: Kloonaa tai linkitä taito globaaliin polkuun
mkdir -p ~/.gemini/config/skills
git clone https://github.com/samimiettinen/visualisointi.git ~/.gemini/config/skills/Presentations
```

### Vaihtoehto B: Työtilakohtainen taito (Projektikohtainen)
Voit lisätä taidon suoraan minkä tahansa projektin `.agents/skills/`-hakemistoon:
```bash
mkdir -p .agents/skills
git clone https://github.com/samimiettinen/visualisointi.git .agents/skills/visualisointi
```
Kun avaat työtilan Antigravityssä, skilli on heti käytettävissä.

---

## 3. Skillin aktivointi ja esimerkkikomennot

Voit aktivoida skillin nimellä `$clear-slides` tai suoralla luonnollisen kielen pyynnöllä:

- **Uuden esityksen luominen:**
  > *"Suunnittele $clear-slides -skillillä 5 dian sijoitusmuistio yrityskaupan kohteesta. Käytä koodinimeä Project Aurora, Translinkin brändivärejä ja rakenna taloussivulle EBITDA-bridge."*

- **Olemassa olevan esityksen parantaminen:**
  > *"Käy läpi tämä board pack. Korvaa yleiset luettelomerkit visual grammar -matriisin mukaisilla kaavioilla ja säilytä kaikki päätöksenteon kannalta oleelliset reunaehdot."*

- **Auditointi ja laaduntarkastus ilman muokkausta:**
  > *"Auditoi deck.html 3-vaiheisella tarkastuksella (Contact sheet, First glance, Micro inspection) ja aja slop_lint.py. Raportoi havainnot."*

---

## 4. Työkalujen ja skriptien ajo Antigravityssä

Antigravity voi suorittaa kansion Python- ja Node-apuohjelmia suoraan työkalukutsuilla:

```bash
# 1. Staattinen tarkastus (formaatit, luvut, ghost deck)
python3 scripts/slop_lint.py deck.html --ghost --mode=read

# 2. Tiukka koodinimitarkastus (varmistaa ettei oikeita nimiä vuoda)
python3 scripts/slop_lint.py deck.html --forbid="Yritys Oy,Ostaja Ab"

# 3. Headless-renderöinti ja auditointiraportti (Node + Playwright)
node scripts/render.mjs deck.html qa_output --pdf

# 4. Yksikkötestit
python3 scripts/test_lint.py /tmp/scratch
```
