# Visualisointi: Esityssuunnittelu ja informaatiomuotoilu

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Platforms: Antigravity | Claude | OpenAI Codex](https://img.shields.io/badge/Platforms-Antigravity%20%7C%20Claude%20%7C%20OpenAI-purple.svg)]()
[![Status: Production](https://img.shields.io/badge/Status-Production--Ready-success.svg)]()

Kattava, monialustainen esitys- ja visualisointiskilli (**Visualisointi**), joka korvaa tekoälyn geneerisen estetiikan ("slopin"), yliyksinkertaistamisen ja kaavamaiset luettelomerkit aitoon näyttöön ja yleisön tarpeisiin pohjautuvalla visuaalisella selittämisellä.

Tämä repositorio tarjoaa suorat suomenkieliset ohjeet ja valmiit konfiguraatiot käyttöön **Claudessa**, **OpenAI Codexissa / ChatGPT:ssä** ja **Google Antigravityssä**.

---

## Sisällys

- [Miksi Visualisointi?](#miksi-visualisointi)
- [Pikaohjeet alustoittain](#pikaohjeet-alustoittain)
  - [1. Anthropic Claude (Claude Projects & Claude Code)](#1-anthropic-claude-claude-projects--claude-code)
  - [2. OpenAI Codex & ChatGPT (Custom GPT / API)](#2-openai-codex--chatgpt-custom-gpt--api)
  - [3. Google Antigravity & Gemini CLI](#3-google-antigravity--gemini-cli)
- [Visuaalinen kielioppi (Valintamatriisi)](#visuaalinen-kielioppi-valintamatriisi)
- [Kehittyneet sommittelumallit](#kehittyneet-sommittelumallit)
- [Finanssi- ja transaktiolaatu (M&A / Talous)](#finanssi--ja-transaktiolaatu-ma--talous)
- [Suomen kieli ja Kielitoimiston normit](#suomen-kieli-ja-kielitoimiston-normit)
- [Laaduntarkastus (3-tasoinen QA)](#laaduntarkastus-3-tasoinen-qa)
- [Repositorion rakenne](#repositorion-rakenne)
- [Lisenssi](#lisenssi)

---

## Miksi Visualisointi?

Perinteiset tekoälymallit tuottavat esityksiin usein geneeristä "slopia": kolme vaaleansinistä laatikkoa, kelluvia koristesfäärejä, irrallisia ikoneita ja tyhjiä iskulauseita. Samalla dioista karsitaan numeerinen tarkkuus, nimittäjät, epävarmuushaarukat ja päätöksenteon kannalta kriittiset reunaehdot.

**Visualisointi-skilli tekee päinvastoin:**
1. **Visuaalinen selittäminen korvaa koristelun:** Auta lukijaa näkemään suhteita, mekanismeja, pullonkauloja ja vertailuja, joita tekstikappaleesta ei nopeasti hahmota.
2. **Edustettu muoto valitaan ennen asettelua:** Yleisön kysymys ratkaisee muodon (dumbbell, pienoiskuvaajat, vesiputous, uintiradat, leikkauskuvat).
3. **Rakenteellinen tiheys on ominaisuus:** Itsenäisesti luettavat esitykset (*slidedocs*, hallituksen aineistot, M&A-muistiot) vaativat täydet määritelmät, lähteet ja reunaehdot.
4. **Koodinimihygienia ja numerotarkkuus:** Sama metriikka ja sama kausi täsmäävät sentilleen läpi koko aineiston. Täysi suoja yrityskauppojen koodinimille.

---

## Pikaohjeet alustoittain

### 1. Anthropic Claude (Claude Projects & Claude Code)
Tarkat ohjeet tiedostossa: **[CLAUDE.md](CLAUDE.md)**

- **Claude Projects (Web):**
  1. Luo uusi projekti (esim. *"Visualisointi & Esitykset"*).
  2. Avaa **Project Instructions** ja liitä sinne [CLAUDE.md](CLAUDE.md) -tiedoston sisältö.
  3. Lataa projektin **Project Knowledge** -tietopankkiin [SKILL.md](SKILL.md) ja [assets/deck.html](assets/deck.html).
- **Claude Code CLI:**
  - Sijoita [CLAUDE.md](CLAUDE.md) projektisi juureen. Claude Code lukee ohjeet automaattisesti taustalla.

### 2. OpenAI Codex & ChatGPT (Custom GPT / API)
Tarkat ohjeet tiedostoissa: **[CODEX.md](CODEX.md)** ja **[OPENAI.md](OPENAI.md)**

- **ChatGPT Custom GPT:**
  1. Luo uusi GPT (`Explore GPTs` -> `Create` -> `Configure`).
  2. Nimeksi `Visualisointi`.
  3. Kopioi [OPENAI.md](OPENAI.md) -tiedoston ohjeet suoraan **Instructions**-kenttään.
  4. Lataa **Knowledge**-kenttään [SKILL.md](SKILL.md) ja [assets/deck.html](assets/deck.html).
- **OpenAI Codex / API:**
  - Anna järjestelmäkehotteeksi (`system prompt`) [OPENAI.md](OPENAI.md) tai [CODEX.md](CODEX.md) koodatessasi HTML/SVG- tai `python-pptx`-esityksiä.

### 3. Google Antigravity & Gemini CLI
Tarkat ohjeet tiedostossa: **[ANTIGRAVITY.md](ANTIGRAVITY.md)**

- **Globaali asennus koneelle:**
  ```bash
  mkdir -p ~/.gemini/config/skills
  git clone https://github.com/samimiettinen/visualisointi.git ~/.gemini/config/skills/visualisointi
  ```
- **Projektikohtainen asennus:**
  ```bash
  mkdir -p .agents/skills
  git clone https://github.com/samimiettinen/visualisointi.git .agents/skills/visualisointi
  ```
- **Käyttö chatissa:**
  Kutsu taitoa nimellä `$visualisointi` tai pyydä suoraan suomeksi:
  > *"Suunnittele $visualisointi -skillillä hallitukselle analyyttinen katsaus Q3-kannattavuudesta käyttäen layered analytical page -rakennetta."*

---

## Visuaalinen kielioppi (Valintamatriisi)

Valitse esitysmuoto suoraan yleisön taustalla olevan kysymyksen perusteella:

| Yleisön kysymys | Optimaalinen muoto | Rakennusperiaate | Vältä tätä virhettä |
| :--- | :--- | :--- | :--- |
| **Miten kaksi tilaa eroavat?** | Dumbbell plot, slope chart | Yhteinen asteikko, suorat nimilaput päissä | Väliaikaisen trendin piilottaminen |
| **Miten kaava vaihtelee ryhmittäin?** | Pienoiskuvaajat (*Small multiples*) | Lukitut, identtiset asteikot kaikissa | Paneelikohtainen automaattiskaalaus |
| **Mistä kokonaistulos muodostuu?** | Vesiputous (*Waterfall / Bridge*) | Täsmäytetty alku, lisäykset, vähennykset | Päällekkäiset erät tai selittämätön jäännös |
| **Miten vaihtoehdot eroavat toisistaan?** | Vertailumatriisi / Ominaisuusprofiili | Täsmälleen samat kriteerit samassa järjestyksessä | Mielivaltaiset tähtiarviot ilman dataa |
| **Kuka hoitaa minkäkin vaiheen?** | Uintiradat (*Swimlane*) | Toimijat riveillä, selkeät luovutukset ja paluut | Koristenuolet ilman verifioitua syy-seurausta |
| **Miten järjestelmä toimii?** | Kerrosarkkitehtuuri / Mekanismikaavio | Nimetyt moduulit, rajapinnat ja virtaussuunnat | Irralliset laatikot ilman vuorovaikutuksia |
| **Miten fyysinen laite toimii?** | Leikkauskuva / Havainnollistettu valokuva | Aito valokuva tai deklaroitu kaavio, paikalliset osoittimet | Koristeellinen kuvapankkikuva oikeana anatomialla |
| **Kuinka epävarma arvio on?** | Fan-kaavio, intervallipalkit, skenaariot | Määritellyt todennäköisyysrajat (esim. 80/95%) | Selittämättömät virhemarginaalit |
| **Mitä lukijan on päätettävä?** | Analyyttinen luettava sivu (*Analytical page*) | Päähavainto ylhäällä, rinnakkaiset näyttölohkot, reunaehdot | Pelkät luettelomerkit ilman numeerista tukea |

---

## Kehittyneet sommittelumallit

1. **Evidence Plate (Näyttöpinta):** Visuaalinen selitys vie yli 80 % tilasta; lyhyet huomiot osoittavat suoraan kohteeseen.
2. **Aligned Comparison (Rinnakkaisvertailu):** Rinnakkaiset paneelit, joilla on täsmälleen identtiset pysty- ja vaaka-akselit.
3. **Overview Plus Detail (Yleiskuva ja detalji):** Makrotason yleiskuva ja siihen kytketty zoomattu alijärjestelmä.
4. **Layered Analytical Page (Kerrostettu analyysisivu):** Kolme lukusyvyyttä:
   - *Taso 1 (Silmäys):* Päähavainto tai strateginen kysymys.
   - *Taso 2 (Tarkastelu):* 2–3 toisiaan täydentävää data- tai kaaviolohkoa.
   - *Taso 3 (Todentaminen):* Oletukset, määritelmät, reunaehdot ja lähteet.
5. **Stable Context with Changing Focus (Vakaa konteksti, vaihtuva fokus):** Monisivuisissa esityksissä järjestelmän geometria pidetään täysin paikallaan; vain aktiivinen reitti tai vaihe korostetaan värein tai numeroin.

---

## Finanssi- ja transaktiolaatu (M&A / Talous)

- **Arvonmäärityshaarukka (Football Field):** Menetelmäkohtaiset vaakahaitarit (DCF, verrokit, transaktiot), selkeä EV:n ja oman pääoman erottelu, referenssitasot (tarjoushinta, 30 pv VWAP).
- **Täsmäytetty Bridge-kaavio:** $\text{Alku} + \sum(\text{Lisäykset}) - \sum(\text{Vähennykset}) = \text{Loppu}$. Pyöristyserot selitetään alaviitteessä.
- **Verrokkitaulukot (Comps):** Yhtenäiset kaudet (LTM, NTM), mediaanirivit eroteltuina, kohdeyhtiö korostettuna.
- **Nollapohjaisuus:** Pylväs- ja palkkikaavioiden pituusakseli alkaa **aina nollasta**. Pinta-alakaavioissa koot skaalataan pinta-alan ($\pi r^2$), ei halkaisijan mukaan.

---

## Suomen kieli ja Kielitoimiston normit

- **Virkemuoto (Sentence case):** Otsikoissa vain ensimmäinen sana ja erisnimet isolla (*"Toistuva liikevaihto kasvoi 46 % vuodessa"*).
- **Hypesanojen kielto:** Karsi sanat *mullistava, saumaton, huippuluokan, ainutlaatuinen, pelinmuuttaja, valjastaa*. Korvaa faktalla.
- **Numerot ja typografia:**
  - Desimaalipilkku: `12,4`
  - Tuhaterottimena sitova välilyönti: `1 234 567` (HTML: `&nbsp;` tai U+202F)
  - Prosentti välilyönnillä: `46 %`, prosenttiyksikkö: `3,2 %-yks.`
  - Valuutta luvun perään: `12,4 M€` tai `12,4 MEUR`
  - Oikea miinusmerkki: `−` (U+2212)
  - Lukuvälit en-dashilla ilman välejä: `2024–2026`, kertoimet: `11,4x`
  - Suomalaiset lainausmerkit: `”Näin”`, ajatusviiva: ` – `

---

## Laaduntarkastus (3-tasoinen QA)

Tarkasta esitys kolmella eri mittakaavalla:
1. **Taso 1 (Kontaktikartta / Ghost deck):** Koko esityksen pienoiskuvakartta. Tarkista pelkät otsikot järjestyksessä, tarinan kulku ja visuaalinen rytmi.
2. **Taso 2 (Ensisilmäys / 5 s):** Yhden dian pikasilmäys. Hahmottuuko päänäyttö heti?
3. **Taso 3 (Mikrotarkastus):** Lukujen täsmäytys, yksiköt, alaviitteet, lähteet ja tekstien rivitykset.

Mukana toimitettavat työkalut:
```bash
# Staattinen analyysi ja ghost deck -tulostus
python3 scripts/slop_lint.py deck.html --ghost --mode=read

# Renderöinti kontaktikartaksi ja auditoinniksi
node scripts/render.mjs deck.html qa_output --pdf
```

---

## Repositorion rakenne

```
visualisointi/
├── SKILL.md                 # Kattava suomenkielinen master-skilli
├── CLAUDE.md                # Optimoidut ohjeet Anthropic Claudelle (Projects & CLI)
├── CODEX.md                 # Optimoidut ohjeet OpenAI Codexille ja koodaukseen
├── OPENAI.md                # Optimoidut ohjeet ChatGPT:lle (Custom GPT & API)
├── ANTIGRAVITY.md           # Asennus- ja käyttöohje Google Antigravitylle
├── README.md                # Tämä esittely
├── LICENSE                  # MIT-lisenssi
├── assets/
│   ├── deck.html            # 1920×1080 puhdas HTML/SVG-esitysmoottori
│   └── design-worksheet.md  # Suunnittelijan työkirjapohja
├── references/              # Syventävät oppaat (Visual grammar, charts, tokens jne.)
├── examples/                # Esimerkkiatlas (HTML, PNG, PDF)
└── scripts/                 # slop_lint.py, render.mjs, test_lint.py
```

---

## Lisenssi

MIT License © 2026 Sami Miettinen. Vapaasti hyödynnettävissä ja muokattavissa.
