---
name: visualisointi
description: "Suunnittelee, parantaa ja arvioi esityksiä, hallitusaineistoja, teasereita, IM:iä ja kaavioita: muoto, luvut, lähteet ja suomen normit. Use for slides, decks, board packs, pitch decks."
license: MIT
metadata:
  author: Sami Miettinen
  version: 3.0.0
---

# Visualisointi

Tämä skill tekee esityksistä ja visualisoinneista näyttöön perustuvia. Esitysmuoto valitaan sen mukaan, mitä yleisön pitää nähdä. Luvut täsmäävät läpi aineiston, ja lähteet näkyvät. Skill tuo suunnittelupäätökset. Tiedoston tekee se väline, jota käyttäjä pyytää (ks. [Työnjako](#työnjako-muiden-välineiden-kanssa)).

## Periaatteet

1. **Selitys ennen koristetta.** Visualisoinnin tehtävä on näyttää suhde, mekanismi tai vertailu, jota tekstistä ei hahmota yhtä nopeasti. Otsikko ja kolme samanlaista laatikkoa eivät selitä mitään.
2. **Muoto yleisön ja näytön mukaan.** Puhujan tukena oleva esitys, itsenäisesti luettava hallitusaineisto ja molempiin käytettävä aineisto tarvitsevat eri tiheyden ja kirjainkoot.
3. **Tiheys on sallittua, sekasotku ei.** Nimittäjiä, epävarmuushaarukoita, määritelmiä ja päätökseen vaikuttavia reunaehtoja ei poisteta sanamäärän takia. Ne järjestetään hierarkiaksi.
4. **Väitteet ja luvut ovat todennettavia.** Otsikko ei väitä enempää kuin data näyttää. Sama metriikka samalta kaudelta on sama luku kaikkialla, ja jokaisella datasivulla on lähde.
5. **Olemassa oleva brändi ja rakenne voittavat.** Käyttäjän pohja, värit ja fontit säilyvät. Skill korjaa sitä, mitä pohjaan sijoitetaan.

## Työnkulku

1. **Selvitä tehtävä.** Luodaanko uusi, parannetaanko olemassa olevaa vai arvioidaanko ilman muutoksia? Kuka lukee, mitä hänen pitää ymmärtää tai päättää, ja luetaanko aineisto itsenäisesti vai puhujan kanssa? Kirjaa rajoitteet: brändi, koodinimi, kieli, sivumäärä ja tiedostomuoto.
2. **Käsikirjoita merkitys ja muoto yhdessä.** Määritä jokaiselle sivulle kysymys, väite, näyttö ja lähde, visuaalinen muoto sekä reunaehto, joka voisi muuttaa johtopäätöstä. Lue otsikot peräkkäin (ghost deck): niiden pitää muodostaa aukoton kertomus. Laajempaan työhön sopii [suunnittelupohja](assets/design-worksheet.md).
3. **Valitse esitysmuoto ennen asettelua.** Lähde yleisön kysymyksestä, älä luettelomerkeistä tai kahden palstan oletuksesta. Pikataulukko on alla, tarkemmat ohjeet [visual-grammar.md](references/visual-grammar.md):ssä.
4. **Tee vaikein sivu ensin.** Pisimmät nimet, tihein data ja vaikein selitys paljastavat, kestääkö rakenne.
5. **Rakenna roolien ja tokenien varaan.** Kirjainkoot, ruudukko ja värit ovat [tokens.md](references/tokens.md):ssä, talo- ja asiakasbrändien profiilit [brands.md](references/brands.md):ssä.
6. **Tarkasta.** Aja `lint.py` ja `render.mjs` ja katso sivut kolmessa mittakaavassa: kontaktikartta, ensisilmäys ja täysi koko. Tarkasta faktat erikseen ulkoasusta ([review.md](references/review.md)).
7. **Toimita ja kerro.** Kerro lyhyesti, mitä muutit, mitkä luvut täsmäytit ja mitä jäi auki. Älä raportoi tarkastusta, jota et tehnyt.

## Muodon valinta lyhyesti

| Yleisön kysymys | Muoto |
| --- | --- |
| Miten kaksi tilannetta eroavat? | Dumbbell- tai slope-kaavio, rinnakkaiset paneelit |
| Missä ryhmät eroavat toisistaan? | Rinnakkaiset pienkaaviot (small multiples) yhteisellä asteikolla |
| Mistä tulos muodostuu? | Siltakaavio (vesiputous) |
| Miten vaihtoehdot eroavat? | Vertailumatriisi samoin kriteerein samassa järjestyksessä |
| Kuka tekee mitä ja missä järjestyksessä? | Uimaratakaavio, prosessikaavio |
| Miten järjestelmä tai laite toimii? | Kerrosarkkitehtuuri, mekanismikaavio, leikkauskuva |
| Kuinka epävarma arvio on? | Vaihteluväli, viuhkakuvio, erilliset skenaariot |
| Miten tapaukset jakautuvat? | Pistekaavio, histogrammi, laatikkokaavio |
| Mitä lukijan pitää päättää? | Kerroksellinen analyysisivu: havainto, näyttö, reunaehdot |
| Mikä on yrityksen arvo? | Football field, verrokkitaulukko, herkkyysmatriisi |

Sommitelmat (näyttöpinta, rinnakkaisvertailu, yleiskuva ja yksityiskohta, kerroksellinen analyysisivu, tulkittu kuva, vakaa konteksti ja vaihtuva fokus) on kuvattu [visual-grammar.md](references/visual-grammar.md):ssä.

## Lue tarvittaessa

| Tiedosto | Avaa, kun |
| --- | --- |
| [references/visual-grammar.md](references/visual-grammar.md) | valitset muotoa tai sommitelmaa: mekanismit, kartat, vertailut, prosessit |
| [references/charts.md](references/charts.md) | teet kaavion, taulukon tai finanssimuodon (football field, silta, verrokit, herkkyys) |
| [references/story.md](references/story.md) | rakennat järjestystä, otsikoita ja tiheyttä tai erotat puhutun ja luettavan esityksen |
| [references/numbers.md](references/numbers.md) | esityksessä on lukuja, lähteitä, koodinimi tai paikkamerkkejä |
| [references/finnish.md](references/finnish.md) | esitys on suomeksi tai kaksikielinen |
| [references/tokens.md](references/tokens.md) | tarvitset kirjainkoot, ruudukon, värien roolit tai kontrastirajat |
| [references/brands.md](references/brands.md) | käytössä on talon tai asiakkaan pohja tai mittaat .pptx-pohjaa |
| [references/formats.md](references/formats.md) | tuotat tai muokkaat HTML:ää, PPTX:ää, Google Slidesia tai PDF:ää |
| [references/review.md](references/review.md) | arvioit esitystä tai teet laaduntarkastuksen |
| [references/signs.md](references/signs.md) | tulkitset `lint.py`:n tunnuksia |
| [references/human-guides.md](references/human-guides.md) | tarvitset ulkoisen esimerkin muotovalinnan tueksi |

Valmiit toteutukset: [examples/visual-grammar.html](examples/visual-grammar.html) (selittävät muodot) ja [examples/rahoitus.html](examples/rahoitus.html) (finanssimuodot suomeksi). Niiden luvut ovat kuvitteellisia.

## Työnjako muiden välineiden kanssa

- Tämä skill tekee suunnittelupäätökset. Tiedoston tekee pyydetty väline: PowerPoint-tiedosto PPTX-työkalulla tai -skillillä, isäntäympäristön oma esitysmuoto silloin, kun käyttäjä pyytää sitä (esimerkiksi Clauden Slides), ja HTML-esitys [assets/deck.html](assets/deck.html)-pohjalle.
- Jos käyttäjä pyytää muokkaamaan olemassa olevaa tiedostoa, muokkaa sitä samassa muodossa. Älä tee rinnakkaista kopiota toiseen formaattiin.
- Erillinen kaavio ilman esitystä (dashboard, sovellus) kuuluu yleiselle kaavioskillille, jos sellainen on käytössä. Tämän skillin luku- ja lähdesäännöt pätevät silti.
- Suomenkielinen teksti kulkee suomen-kieli-skillin kautta, jos se on käytettävissä.

## Ennen toimitusta

- Palkki- ja pylväskaavion pituusakseli alkaa nollasta. Kuplan ja ympyrän pinta-ala, ei säde, vastaa arvoa.
- Otsikon väite pitää paikkansa sivun datalla.
- Sama metriikka samalta kaudelta on sama luku tiivistelmässä, kaaviossa, taulukossa ja liitteessä.
- Jokaisella datasivulla on lähderivi, jossa on dokumentti ja päivämäärä.
- Koodinimiesityksessä oikeat nimet eivät näy missään: tekstissä, muistiinpanoissa, kaavion datassa, tiedostonimissä, alt-teksteissä tai metatiedoissa.
- Paikkamerkkejä (`[Yhtiö]`, `XX`, `TBD`, `Lisää otsikko`) ei ole.
- Suomeksi: otsikot virkemuodossa, `12,4 M€`, `46 %`, `−0,6`, `2024–2026` ja `”lainaus”`.

## Työkalut

```bash
python3 scripts/lint.py deck.html --ghost                          # staattiset havainnot ja otsikkojono
python3 scripts/lint.py deck.pptx --forbid="Oikea Nimi Oy,Ostaja Ab" # koodinimen vuodot
node scripts/render.mjs deck.html qa --pdf                          # PNG-diat, kontaktikartta, audit.md
```

- `lint.py` tarvitsee vain Pythonin, `.pptx`-tiedostoihin lisäksi python-pptx:n. Se tunnistaa suomen kielen ja tarkistaa Kielitoimiston merkintätavat (F-tunnukset). Havainto on ehdokas, ei tuomio: tulkinta on [signs.md](references/signs.md):ssä.
- `render.mjs` tarvitsee Noden ja Playwrightin ja käyttää koneen Chromea, jos sellainen löytyy. PPTX- ja PDF-tiedostoihin se tarvitsee lisäksi LibreOfficen ja Popplerin. Jos renderöinti ei onnistu ympäristössä, sano se ja tarkasta sivut muulla tavalla.
- Aja skriptit skillin kansiosta ja kirjoita tarkastustulosteet uuteen, tyhjään kansioon, jotta eri versioiden sivut eivät sekoitu.
