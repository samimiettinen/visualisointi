# Visualisointi

Visualisointi on tekoälyavustajan skill esitysten, hallitusaineistojen, sijoitusmuistioiden ja kaavioiden suunnitteluun, parantamiseen ja arviointiin. Se valitsee esitysmuodon yleisön tarpeen mukaan, pitää luvut ja lähteet täsmällisinä ja noudattaa suomen kielen merkintätapoja. Mukana ovat HTML-esityspohja, staattinen tarkistin ja renderöintityökalu.

Skill toimii Claudessa, Claude Codessa, Codexissa ja Antigravityssä. ChatGPT:n omiin GPT:ihin on erillinen ohje [OPENAI.md](OPENAI.md).

## Mitä skill tekee

- **Valitsee muodon kysymyksen mukaan.** Muutos kahden tilanteen välillä, ryhmien erot, tuloksen muodostuminen, prosessit, mekanismit ja epävarmuus saavat kukin niille sopivan kaavion tai sommitelman. Luettelomerkit ja kolme samanlaista laatikkoa eivät ole oletus.
- **Sovittaa tiheyden lukutilanteeseen.** Puhujan tukena oleva esitys ja itsenäisesti luettava hallitusaineisto tarvitsevat eri kirjainkoot ja eri määrän tekstiä. Nimittäjiä, epävarmuushaarukoita ja reunaehtoja ei poisteta lyhyyden vuoksi.
- **Pitää luvut kunnossa.** Sama metriikka samalta kaudelta on sama luku kaikkialla, jokaisella datasivulla on lähde, ja koodinimiesityksessä oikeat nimet eivät näy missään.
- **Tuntee finanssimuodot.** Football field, siltakaavio, verrokkitaulukko ja herkkyysmatriisi on kuvattu ja toteutettu suomenkielisessä esimerkissä.
- **Noudattaa Kielitoimiston normeja.** Otsikot virkemuodossa, `12,4 M€`, `46 %`, `−0,6`, `2024–2026` ja `”lainaus”`. Tarkistin löytää poikkeamat automaattisesti.

## Asennus

### Claude

1. Rakenna paketti repon juuressa:
   ```bash
   python3 scripts/package.py
   ```
   Komento tarkistaa SKILL.md:n kentät ja tekee tiedoston `dist/visualisointi.zip`.
2. Lisää paketti Clauden asetuksissa kohdassa Customize > Skills ja ota skill käyttöön.

### Claude Code

```bash
git clone https://github.com/samimiettinen/visualisointi.git ~/.claude/skills/visualisointi
```

Projektikohtaisesti kansio on `.claude/skills/visualisointi`. Päivitys tapahtuu komennolla `git pull`.

### Codex

```bash
git clone https://github.com/samimiettinen/visualisointi.git ~/.agents/skills/visualisointi
```

Codexissa skillin voi kutsua nimellä `$visualisointi` tai pyytää työtä omin sanoin.

### Antigravity

```bash
git clone https://github.com/samimiettinen/visualisointi.git ~/.gemini/config/skills/visualisointi   # kaikkiin projekteihin
git clone https://github.com/samimiettinen/visualisointi.git .agents/skills/visualisointi            # yhteen projektiin
```

### ChatGPT

Kopioi [OPENAI.md](OPENAI.md):n ohje oman GPT:n Instructions-kenttään ja lataa tietopankkiin `SKILL.md`, `references/`-kansion tiedostot ja `assets/deck.html`.

## Käyttöesimerkkejä

> Tee neljän dian suomenkielinen teaser koodinimellä Projekti Aurora. Käytä Translinkin värejä ja tee taloussivulle EBITDA-silta.

> Käy tämä hallitusaineisto läpi. Korvaa luettelot sopivilla kaavioilla ja säilytä päätöksen kannalta olennaiset reunaehdot.

> Arvioi deck.html muuttamatta sitä ja aja tarkistin. Kerro havainnot sivuittain.

## Työkalut

```bash
python3 scripts/lint.py deck.html --ghost                           # havainnot ja otsikkojono
python3 scripts/lint.py deck.pptx --forbid="Oikea Nimi Oy,Ostaja Ab" # koodinimen vuodot
node scripts/render.mjs deck.html qa --pdf                           # PNG-diat, kontaktikartta, audit.md
```

- `lint.py` toimii pelkällä Pythonilla. PowerPoint-tiedostoihin tarvitaan lisäksi `python-pptx`. Havaintojen tunnukset on selitetty tiedostossa [references/signs.md](references/signs.md).
- `render.mjs` tarvitsee Noden ja Playwrightin. Se käyttää koneen Chromea, jos sellainen löytyy. PowerPoint- ja PDF-tiedostojen renderöintiin tarvitaan LibreOffice ja Poppler.

## Esimerkit

| Tiedosto | Sisältö |
| --- | --- |
| [examples/visual-grammar.html](examples/visual-grammar.html) | Kahdeksan selittävää muotoa: prosessi, pienkaaviot, analyysisivu, vertailu, leikkauskuva, yleiskuva ja yksityiskohta sekä vaihtuva fokus |
| [examples/rahoitus.html](examples/rahoitus.html) | Finanssimuodot suomeksi: football field, EBITDA-silta, verrokkitaulukko ja herkkyysmatriisi |
| [examples/clean-deck.html](examples/clean-deck.html) | Lyhyt englanninkielinen teaser |
| [examples/sloppy-deck.html](examples/sloppy-deck.html) | Tahallisen huolimaton esitys, jonka tarkistimen pitää hylätä |

Esimerkkien yritykset ja luvut ovat kuvitteellisia.

## Rakenne

```
visualisointi/
├── SKILL.md            ohjeet, jotka avustaja lukee ensin
├── references/         syventävät ohjeet, jotka luetaan tarpeen mukaan
├── assets/             HTML-esityspohja ja suunnittelupohja
├── examples/           valmiit esimerkit ja niiden PNG- ja PDF-versiot
├── scripts/            lint.py, render.mjs, test_lint.py ja package.py
├── evals/              testitapaukset skillin arviointiin
├── agents/openai.yaml  Codexin näyttönimi ja oletuskehote
├── OPENAI.md           ohje ChatGPT:n omaan GPT:hen
└── CLAUDE.md           ylläpito-ohjeet tämän repon kehittämiseen
```

## Kehitys

```bash
python3 scripts/test_lint.py /tmp/visualisointi-testit   # tarkistimen testit ja esimerkkien tarkistus
python3 scripts/package.py                              # kenttien tarkistus ja zip-paketti
```

GitHub Actions ajaa samat tarkistukset ja renderöi esimerkit jokaisesta muutoksesta. Testitapaukset `evals/`-kansiossa ovat Claude Coden `claude plugin eval` -muodossa.

## Lisenssi

MIT © 2026 Sami Miettinen. Ks. [LICENSE](LICENSE).
