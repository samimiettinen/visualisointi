# Google Antigravity & Gemini -opas: Visualisointi

Tämä ohje opastaa **Visualisointi**-skillin (`visualisointi`) käyttöönottoon ja hyödyntämiseen **Google Antigravityssä** ja **Gemini CLI / IDE** -ympäristöissä.

---

## 1. Miten Antigravity-skilli toimii?

Antigravity käyttää modulaarista taitojärjestelmää (*Skills*), joka hyödyntää **progressiivista paljastamista (Progressive Disclosure)**:
1. Käynnistyessään Antigravity lukee vain skillin nimen ja kuvauksen (`name: visualisointi`, `description: ...`) `SKILL.md`-tiedoston YAML-frontmatterista.
2. Kun käyttäjä pyytää esityksen suunnittelua, uudistamista tai auditointia, agentti aktivoi skillin ja lataa täyden suomenkielisen ohjeistuksen kontekstiin.
3. Agentti osaa itsenäisesti lukea syventävät viitedokumentit (`references/`) ja ajaa tarkistusskriptit (`scripts/`).

---

## 2. Asennus ja käyttöönotto Antigravityssä

### Vaihtoehto A: Globaali taito (Kaikissa projekteissa käytettävissä)
Sijoita kansio koneesi globaaliin taitohakemistoon:
```bash
mkdir -p ~/.gemini/config/skills
git clone https://github.com/samimiettinen/visualisointi.git ~/.gemini/config/skills/visualisointi
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

Voit aktivoida skillin nimellä `$visualisointi` tai suoralla luonnollisen kielen pyynnöllä:

- **Uuden esityksen luominen:**
  > *"Suunnittele $visualisointi -skillillä 5 dian sijoitusmuistio yrityskaupan kohteesta. Käytä koodinimeä Projekti Aurora, Translinkin brändivärejä ja rakenna taloussivulle EBITDA-bridge."*

- **Olemassa olevan esityksen parantaminen:**
  > *"Käy läpi tämä board pack. Korvaa yleiset luettelomerkit visuaalisen kieliopin mukaisilla kaavioilla ja säilytä kaikki päätöksenteon kannalta oleelliset reunaehdot."*

- **Auditointi ja laaduntarkastus ilman muokkausta:**
  > *"Auditoi deck.html 3-vaiheisella tarkastuksella (Kontaktikartta, Ensisilmäys, Mikrotarkastus) ja aja slop_lint.py. Raportoi havainnot."*

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
