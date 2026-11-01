---
name: visualisointi
description: Suunnittele, paranna tai arvioi esityksiä, visualisointeja, hallituksen aineistoja, sijoitusmuistioita ja kaavioita. Korvaa tekoälyn geneerisen "slopin" ja liiallisen minimalismin aitoon tietoon ja yleisön lukutilanteeseen pohjautuvalla visuaalisella selittämisellä. Sisältää visuaalisen kieliopin, kaaviovalinnan, finanssimallit, token-järjestelmän, Kielitoimiston normit ja 3-vaiheisen laaduntarkastuksen.
metadata:
  author: Sami Miettinen
  version: 2.0.0
---

# Visualisointi: Esityssuunnittelu ja visuaalinen selittäminen

Kattava asiantuntijatason suunnitteluskilli, joka muuntaa monimutkaisen aineiston ja numeerisen näytön selkeiksi, vaikuttaviksi ja ihmisen tekemiltä näyttäviksi visuaalisiksi esityksiksi. Skilli karsii tekoälyn geneerisen estetiikan ("slopin"), kunnioittaa yrityksen brändiä, säilyttää analyyttisen tarkkuuden ja tuottaa muokattavaa, kestävää jälkeä Antigravityssä, Claudessa ja OpenAI:ssa.

---

## 1. Perusfilosofia

1. **Visuaalinen selittäminen korvaa koristelun:** Auta yleisöä ymmärtämään suhteita, mekanismeja, pullonkauloja ja malleja, joita tekstikappaleesta ei nopeasti hahmota. Otsikko ja kolme samanlaista laatikkoa ei ole yleispätevä vastaus.
2. **Muoto valitaan yleisön ja näytön perusteella:** Valitse visuaalinen esitystapa suoraan datan ja lukutilanteen mukaan (puhujan taustaesitys vs. itsenäisesti luettava hallituksen aineisto vs. sijoitusmuistio).
3. **Rakenteellinen tiheys on ominaisuus:** Älä karsi nimittäjiä, epävarmuushaarukoita, vasta-argumentteja, määritelmiä tai päätöksenteon kannalta kriittisiä reunaehtoja keinotekoisen sanakiintiön saavuttamiseksi. Rakenna tiheys selkeän visuaalisen hierarkian avulla.
4. **Rikkaus kuuluu selitykseen:** Käytä mittakaavasuhteita, suoria nimilappuja, rinnakkaisia pienoiskuvaajia, mekanismien leikkauskuvia, prosessireittejä ja aitoja kuvakaappauksia. Poista koristeelliset muodot ja täyteikonit, jotka eivät tuo merkitystä.
5. **Nollatoleranssi AI-slopille:** Vältä geneerisiä liukuväripintoja, kelluvia pastellisilintereitä, merkityksettömiä tarkistusmerkkejä, onttoja iskusanoja ja yliyksinkertaistettuja iskulauseita.
6. **Monialustainen yhteensopivuus:** Toimii saumattomasti Antigravityssä (ajettavat skriptit ja progressiivinen paljastus) sekä suoraan vietävissä Claudelle (Claude Projects / Claude Code) ja OpenAI:lle (Custom GPT / ChatGPT / Codex).

---

## 2. 7-vaiheinen työnkulku

Noudata tätä prosessia kaikessa esitysten suunnittelussa, uudistamisessa ja arvioinnissa:

```
[1. Diagnosoi tehtävä & yleisö] ──> [2. Käsikirjoita merkitys & muoto] ──> [3. Valitse esitysmuoto]
                                                                                     │
[7. Toimita & dokumentoi] <── [6. 3-tasoinen laaduntarkastus] <── [5. Rakenna tokeneilla] <── [4. Tee vaativin sivu ensin]
```

### Vaihe 1: Diagnosoi tehtävä ja lukutilanne
Määritä toimeksiannosta ja lähdemateriaalista:
- **Toiminto:** Uuden luominen, olemassa olevan esityksen parantaminen tai auditointi/arviointi (auditointi tuottaa korjausehdotukset ilman lähteen muokkaamista).
- **Yleisö ja päätös:** Kuka aineistoa lukee tai katsoo? Mihin päätökseen tai ymmärrykseen esityksellä tähdätään?
- **Lukutilanne:**
  - *Puhujan vetämä esitys (Talk/Keynote):* Suuri typografia (28–44 pt), vahva visuaalinen fokus, vähän tekstiä kalvolla, puhuja kantaa kerronnan.
  - *Itsenäisesti luettava esitys (Board pack / Slidedoc / M&A-muistio):* Korkea rakenteellinen tiheys, itsenäisesti ymmärrettävät selitykset, 14–18 pt leipäteksti, kattavat määritelmät, reunaehdot ja lähteet.
  - *Yhdistelmä (Dual-use):* Selkeä ensisijainen lukupolku, paikalliset huomiot ja täydentävät alaviitteet/liitteet.
- **Reunaehdot:** Brändi, luottamuksellisuus (esim. yrityskauppojen koodinimet), pituus, kuvasuhde (16:9 widescreen oletuksena) ja muokattava formaatti (HTML, PPTX, Google Slides).

### Vaihe 2: Käsikirjoita merkitys ja muoto yhdessä
Älä kirjoita otsikoita erillään visuaalisesta ratkaisusta. Määritä jokaiselle sivulle:
1. **Yleisön kysymys / tarkoitus:** Mihin kysymykseen sivu vastaa?
2. **Päähavainto (väite):** Mikä on vastaus tai johtopäätös?
3. **Näyttö ja lähde:** Mitkä datapisteet tai mekanismit todistavat väitteen?
4. **Visuaalinen muoto:** Mikä kaavio tai tilarakenne kantaa selityksen?
5. **Oleelliset reunaehdot:** Mikä oletus, riski tai määritelmä voi muuttaa johtopäätöstä?

*Ghost deck -testi:* Lue luonnostellut otsikot järjestyksessä. Pelkkien otsikoiden on muodostettava looginen, aukoton tarina ilman toistoa.

### Vaihe 3: Valitse esitystapa ennen asettelua
Valitse kaavio, matriisi tai tilarakenne suoraan yleisön kysymyksen ja näytön perusteella (katso *Visuaalinen kielioppi* alla). Älä koskaan tyydy automaattisesti luettelomerkkeihin tai 2–3 laatikon perusjakoon.

### Vaihe 4: Rakenna haastavin sivu ensin
Ennen kuin taitat koko esityksen, rakenna monimutkaisin analyyttinen sivu, tekninen mekanismi tai tihein vertailu. Kun testaat ääritapauksen (pisimmät nimilaput, tihein data, vaikein selitys), varmistat että visuaalinen järjestelmä kestää.

### Vaihe 5: Rakenna token-järjestelmän avulla
Käytä yhdenmukaisia typografisia rooleja, semanttista värikoodausta, lukittua 12 sarakkeen ruudukkoa ja 8 px rytmiä läpi koko esityksen. Toista hyväksyttyjä rakenteita aina, kun vastataan samanlaiseen kysymykseen.

### Vaihe 6: 3-tasoinen laaduntarkastus
Tarkasta faktat erillään ulkoasusta. Arvioi esitys kolmella eri mittakaavalla: Kontaktikartta (makrotarina), Ensisilmäys (visuaalinen hierarkia) ja Täysi koko (mikrotarkkuus ja luvut).

### Vaihe 7: Toimita ja dokumentoi
Toimita muokattava esitys (HTML/SVG, natiivi PPTX tai Google Slides). Dokumentoi selkeästi tehdyt ratkaisut, täsmäytetyt luvut ja mahdolliset avoimet oletukset.

---

## 3. Visuaalinen kielioppi ja esitysmuotojen valintamatriisi

Kytke yleisön taustalla oleva kysymys suoraan oikeaan visuaaliseen muotoon:

| Yleisön kysymys | Optimaalinen muoto | Rakennusperiaate | Vältä tätä virhettä |
| :--- | :--- | :--- | :--- |
| **Miten kaksi tilaa eroavat?** | Dumbbell plot, slope chart, rinnakkaiset paneelit | Yhteinen asteikko, täsmäytetyt luokat, suorat nimilaput päissä | Väliaikaisen trendin piilottaminen; eripariset otokset |
| **Miten kaava vaihtelee ryhmien välillä?** | Pienoiskuvaajat (*Small multiples*) | Identtiset akselit kaikissa paneeleissa; looginen järjestys | Paneelikohtainen automaattiskaalaus, joka vääristää eroja |
| **Mistä kokonaistulos muodostuu?** | Vesiputous (*Waterfall / Bridge*) | Täsmäytetty alkuarvo, erilliset lisäykset ja vähennykset, selkeä loppusumma | Päällekkäiset erät tai selittämätön jäännöserä |
| **Miten vaihtoehdot eroavat toisistaan?** | Vertailumatriisi / Ominaisuusprofiili | Täsmälleen samat kriteerit samassa järjestyksessä; vertailukelpoinen näyttö | Mielivaltaiset tähtiarviot ilman todellista dataa |
| **Kuka hoitaa minkäkin vaiheen?** | Uintiradat (*Swimlane*) / Prosessikaavio | Toimijat omilla kaistoillaan; kronologinen eteneminen; selkeät paluureitit | Koristenuolet, jotka vihjaavat todentamattomaan syy-seuraukseen |
| **Miten järjestelmä toimii?** | Kerrosarkkitehtuuri / Mekanismikaavio | Nimetyt moduulit, eksplisiittiset rajapinnat ja virtaussuunnat | Irralliset laatikot ilman vuorovaikutussuhteita |
| **Miten fyysinen laite tai esine toimii?** | Havainnollistettu valokuva / Leikkauskuva | Aito valokuva tai deklaroitu kaavio; paikalliset osoittimet | Koristeellinen kuvapankkikuva oikeana anatomialla |
| **Missä asia tapahtuu maantieteellisesti?** | Kartta paikallisilla lisäkkeillä (insets) | Merkityksellinen maantiede; suhteutetut osuudet (per asukas) | Maantieteellinen kartta silloin, kun sijainti ei selitä mitään |
| **Kuinka epävarma ennuste on?** | Fan-kaavio, intervallipalkit, skenaariot | Määritellyt todennäköisyysrajat (esim. 80/95%); selkeät skenaario-oletukset | Vale-tarkkuus; nimeämättömät luottamusvälit |
| **Miten tapaukset jakautuvat?** | Histogrammi, pisteparvi (dot plot), laatikkokuvaaja | Ilmoitettu otoskoko, järkevät luokkavälit, poikkeavat havainnot | Laajan hajonnan korvaaminen pelkällä keskiarvolla |
| **Miten kokonaisuus jakautuu osiin?** | Puukartta (*Treemap*), pinottu palkki, 100% palkki | Yhteinen nimittäjä; toisensa poissulkevat osat; suorat nimilaput | 3D-piirakat; suhteettomat pinta-alat; summat jotka eivät täsmää |
| **Mikä on todellinen käyttäjäkokemus?** | Havainnollistettu kuvakaappaussarja | Aidot käyttöliittymärajaukset; numeroitu vaihejärjestys; huomiomerkinnät | Geneeriset tekomockupit; lukukelvottomat kokoruutukaappaukset |
| **Mitä lukijan on päätettävä?** | Analyyttinen luettava sivu (*Analytical page*) | Päähavainto ylhäällä; rinnakkaiset näyttölohkot; näkyvä reunaehtotaso | Yksittäiset irralliset luettelomerkit ilman analyyttistä tukea |

---

## 4. Kehittyneet sommittelumallit

Hylkää puuduttava "otsikko + kaavio vasemmalla + teksti oikealla" -asettelu. Käytä kognitiiviseen tehtävään sovitettuja sommitelmia:

1. **Evidence Plate (Näyttöpinta):** Visuaalinen selitys (kaavio, kartta, arkkitehtuuri) hallitsee yli 80 % tilasta. Tiiviit huomiot sijoitetaan suoraan selitettävän kohteen viereen.
2. **Aligned Comparison (Rinnakkaisvertailu):** Kaksi tai useampi tapaus vierekkäin identtisillä akseleilla, asteikoilla ja typografialla. Lukija vertailee suoraan visuaalisesti.
3. **Overview Plus Detail (Yleiskuva ja detalji):** Makrotason järjestelmäkaavio toisella puolella ja siihen selkeästi kytketty suurennettu leikkaus kriittisestä osasta.
4. **Layered Analytical Page (Kerrostettu analyysisivu):** Rakennettu kolmelle lukusyvyydelle:
   - *Taso 1 (Silmäys):* Päähavainto tai strateginen kysymys.
   - *Taso 2 (Tarkastelu):* 2–3 toisiaan täydentävää data- tai näyttölohkoa (esim. trendi + rakenteen jakautuminen).
   - *Taso 3 (Todentaminen):* Oletukset, määritelmät, reunaehdot ja lähteet.
5. **Image with Interpretation (Tulkittu kuva):** Aito dokumentaarinen valokuva tai tuotekuvakaappaus harkituilla rajauksilla, numeroiduilla huomiopisteillä ja alkuperämerkinnällä.
6. **Stable Context with Changing Focus (Vakaa konteksti, vaihtuva fokus):** Useamman dian sarjassa monimutkainen arkkitehtuuri pidetään täsmälleen samassa geometriassa. Vain aktiivinen vaihe tai reitti korostetaan kontrastilla tai numeromerkein. Tämä säilyttää lukijan spatiaalisen orientoitumisen.

---

## 5. Kaaviot, taulukot ja talousvisualisoinnit

### Rehellisen visualisoinnin perussäännöt
- **Nollapohjaisuus:** Palkki- ja pylväskaavioiden pituusakselin on **aina** elettävä nollasta. Suhteellisia muutoksia kuvaavassa viivakaaviossa rajattu akseli on sallittu, kunhan akseli on selkeästi merkitty.
- **Pinta-alan totuudenmukaisuus:** Kuplien ja ympyröiden koon tulee skaalautua pinta-alan ($\pi r^2$), ei halkaisijan mukaan.
- **Suorat nimilaput:** Sijoita sarjojen nimet suoraan viivojen ja palkkien päihin. Vältä etäisiä legendoja, jotka pakottavat katseen hyppimään edestakaisin.
- **Epävarmuus ja aikasarjojen taitteet:** Erota toteuma, budjetti ja ennuste toisistaan selkeällä pystyviivalla.

### Yritysjärjestelyiden ja talouden mallit
- **Arvonmäärityshaarukka ("Football Field"):**
  - Vaakasuuntaiset intervallipalkit menetelmittäin (DCF, kauppaverrokit, pörssiverrokit, 52 vk vaihteluväli).
  - Ilmoita selkeästi arvon perusta: Velaton arvo (Enterprise Value, EV) vs. Oman pääoman arvo (Equity Value). Älä koskaan sekoita näitä samassa kuvaajassa.
  - Piirrä selkeät pystysuuntaiset referenssiviivat (nykykurssi, tarjoushinta tai 30 pv VWAP).
- **Vesiputouskaavio ("Bridge"):**
  - Varmista matemaattinen täsmäävyys: $\text{Alku} + \sum(\text{Lisäykset}) - \sum(\text{Vähennykset}) = \text{Loppu}$.
  - Erottele positiiviset erät, negatiiviset erät ja välisummat selkein värein.
  - Selitä mahdolliset pyöristyserot alaviitteessä sen sijaan, että vääristelisit komponentteja.
- **Pörssi- ja kauppaverrokkitaulukko (Comps):**
  - Standardoidut tunnusluvut (EV/EBITDA, P/E, EV/Sales, Liikevaihdon kasvu, EBITDA-%).
  - Tarkka kausien yhtenäisyys: LTM (viimeiset 12 kk), NTM (seuraavat 12 kk), tilikaudet FY1 ja FY2.
  - Erota vertailuryhmän mediaani ja keskiarvo selkeästi yksittäisistä yhtiöistä. Korosta kohdeyhtiö erikseen.
- **Herkkyysmatriisi (Two-Way Sensitivity Table):**
  - Nimeä kummatkin akselit yksiselitteisesti (esim. WACC riveillä, terminaalikasvu sarakkeilla).
  - Korosta määritelty perusskenaario (*Base Case*) erillisellä kehyksellä ja taustavärillä.
  - Käytä hienovaraista väriporrastusta; varmista että numerot säilyttävät korkean kontrastin (>4.5:1).
- **Tiheät datataulukot:**
  - Tasaa luvut aina oikealle (tai desimaalipilkun kohdalle); tasaa teksti vasemmalle; keskitä lyhyet koodit ja päivämäärät.
  - Merkitse yksikkö ja valuutta aina sarakkeen otsikkoon (`milj. €`, `MEUR`, `EURk`, `%`).
  - Käytä tasalevyisiä numeroita (`tabular-nums`) numeroiden pystysuoraan kohdistamiseen.

---

## 6. Design-järjestelmä ja esitystokenit

### Canvas ja ruudukko
- **Referenssiresoluutio:** 1920 × 1080 px laajakuva (16:9).
- **PowerPoint-pistevastaavuus:** Tässä järjestelmässä $2\text{ px} = 1\text{ pt}$ (kangas vastaa $960 \times 540\text{ pt}$).
- **Ruudukko:** 12 saraketta. Vakiomarginaalit: $96\text{ px}$ sivuilla, $88\text{ px}$ ylhäällä, $72\text{ px}$ alhaalla. Sarakkeen leveys: $122\text{ px}$, väli: $24\text{ px}$.
- **Pystysuuntainen rytmi:** Noudata tiukasti $8\text{ px}$ perusrytmiä ($8, 16, 24, 32, 48, 64\text{ px}$).

### Typografia
Pidä fonttiroolit kurinalaisina (enintään 1–2 kirjasinperhettä, 5–6 kokotasoa):

| Rooli | Luettava esitys / Slidedoc (pt / px) | Puhujan esitys (pt / px) | Tarkoitus ja käyttö |
| :--- | :--- | :--- | :--- |
| **Kansi / Iskulause** | 44–56 pt / 88–112 px | 56–72 pt / 112–144 px | Kansi ja suuret välisivut |
| **Väiteotsikko (Action Title)**| 24–32 pt / 48–64 px | 32–44 pt / 64–88 px | Dian päähavainto (enintään 2 riviä) |
| **Johdantolause (Lead)** | 16–20 pt / 32–40 px | 20–26 pt / 40–52 px | Otsikkoa tarkentava kehyslause |
| **Leipäteksti / Selitys** | 14–16 pt / 28–32 px | 20–26 pt / 40–52 px | Kuvaileva teksti ja huomiot |
| **Taulukko- ja kaavioluvut** | 11–14 pt / 22–28 px | 14–18 pt / 28–36 px | Datapisteet, akselit, matriisin solut |
| **Alaviitteet ja lähteet** | 9–11 pt / 18–22 px | 10–12 pt / 20–24 px | Lähteet, määritelmät, luottamuksellisuus |

*Typografiasäännöt:*
- Aseta aina `font-variant-numeric: tabular-nums lining-nums`.
- Otsikoissa käytetään `text-wrap: balance` ja leipätekstissä `text-wrap: pretty`.
- Huolehdi merkkivälistä (*letter-spacing*): $-0.01\text{em}$ – $-0.02\text{em}$ suurissa otsikoissa, normaali leipätekstissä.

### Semanttinen väriarkkitehtuuri
Määritä värit funktion, älä koristeellisuuden mukaan:
1. **Pinta ja tausta (`--bg`, `--raised`):** Kirkas valkoinen (#FFFFFF) tai vaaleanharmaa (#F6F6F4).
2. **Teksti ja viivat (`--ink`, `--ink-2`, `--ink-3`):** Pääteksti (#171717), toissijainen teksti (#4F4F4F), vaimennetut tekstit/akselit (#737373).
3. **Pääkorostus (`--accent`):** Varattu vain sille yhdelle luvulle, pylväälle tai reitille, joka kantaa pääviestin.
4. **Kategoriat (`--category-a`, `--category-b`, jne.):** Pysyvä identiteetti entiteeteille läpi kaikkien diojen.
5. **Sekventiaalinen asteikko:** Järjestetty sävyramppi määrille (esim. vaaleasta tummansiniseen).
6. **Divergoiva asteikko:** Kaksi toisistaan erottuvaa väriä neutraalin keskipisteen ympärillä (esim. negatiivinen punainen ja positiivinen vihreä/sininen).
7. **Statusväri:** Määritelty tila (Onnistuminen, Varoitus, Virhe), johon liittyy aina myös teksti tai symboli.

*Kontrastivaatimus:* Vähintään 4.5:1 leipätekstille ja datalle taustaa vasten; vähintään 3:1 suurille otsikoille ja olennaisille graafisille rajoille (WCAG 2.1 AA).

---

## 7. Luvut, lähteet ja transaktiotarkkuus

### Ehdottomat lukusäännöt
1. **Yksi metriikka, yksi kausi = täsmälleen sama luku kaikkialla:** Tiivistelmässä, talouskalvolla, kaaviossa ja liitteissä esiintyvän luvun on täsmättävä sentilleen.
2. **Standardi tarkkuustaso:**
   - Dioissa: 2–3 merkitsevää numeroa (`47,4 M€`, `46 %`, `11,4x`).
   - Liitteissä ja datahuoneessa: Täysi kirjanpidollinen tarkkuus.
   - Ennusteissa: Ei vale-tarkkuutta (kirjoita "noin 2,4 mrd. €", älä laskennallista "2,374 mrd. €").
3. **Yksiköt ja mittauskaudet aina pakollisia:** Jokaisessa luvussa on oltava yksikkö ja aikajänne (`Liikevaihto FY25, M€: 12,4`, ei pelkkä `Liikevaihto: 12,4`).
4. **Pakollinen lähdeviite:** Jokaisella datasivulla on oltava täsmällinen lähderivi alalaidassa:
   *Esimerkki:* `Lähde: Yhtiön johdon laskelmat FY21–FY25; S&P Capital IQ, velattomat arvot 31.10.2026.`

### Lukujen ja merkintöjen konventiot (Suomi vs. Englanti)

| Elementti | Suomalainen käytäntö | Englantilainen käytäntö |
| :--- | :--- | :--- |
| **Tuhannet ja desimaalit** | `1 234,5` (sitova välilyönti tuhansissa, pilkku desimaalissa) | `1,234.5` (pilkku tuhansissa, piste desimaalissa) |
| **Prosentit** | `46 %` (välilyönti ennen merkkiä) | `46%` tai `46 %` |
| **Prosenttiyksiköt** | `3,2 %-yks.` | `3.2 pp` |
| **Valuutta ja suuruusluokka**| `12,4 M€` tai `12,4 milj. €` tai `12,4 MEUR` | `€12.4m` tai `EUR 12.4m` tai `EURm 12.4` |
| **Negatiiviset luvut** | `−0,6` (oikea miinusmerkki `−` U+2212) | `−0.6` tai `(0.6)` |
| **Lukuvälit** | `2024–2026`, `10,5–12,5x` (en-dash `–`, ei välejä) | `2024–2026`, `10.5–12.5x` |
| **Päivämäärät** | `31.10.2026`, `Q3/2026`, `lokakuu 2026` | `31 Oct 2026`, `Q3 2026` |
| **Tilikaudet** | `2025`, `LTM 9/2026` | `FY25`, `LTM Sep-26`, `NTM` |

### Luottamuksellisuus ja koodinimihygienia
- **Koodinimen suojaus:** Luottamuksellisissa yrityskauppa-, irtautumis- tai pääomasijoitusmateriaaleissa kohdeyhtiön, myyjän tai ostajaehdokkaiden oikeat nimet **eivät saa koskaan** näkyä missään: ei kalvolla, puhujan muistiinpanoissa, kaavion sarjanimissä, kuvatiedostojen nimissä, alt-teksteissä eikä tiedoston metatiedoissa.
- **Luottamuksellisuusmerkintä:** Merkitse alalaitaan hillitysti: `Erittäin luottamuksellinen · Projekti Aurora`.
- **Nollatoleranssi paikanpitäjille:** Yksikään esitys ei lähde eteenpäin sisältäen merkintöjä: `[Yhtiö]`, `XX`, `TBD`, `YYYY`, `Lorem Ipsum`, `Lisää otsikko`.

---

## 8. Suomen kieli ja Kielitoimiston normit

Kun esitys laaditaan suomeksi, noudata Kielitoimiston normeja:
1. **Virkemuoto (Sentence case):** Suomenkieliset otsikot ja väliotsikot kirjoitetaan virkemuodossa (vain ensimmäinen sana ja erisnimet isolla): *"Toistuva liikevaihto kasvoi 46 % vuodessa"*. Älä koskaan käytä englannin Title Casea tai huutavia SUURAAKKOSIA.
2. **Karsi ontot hypesanat:**
   - Poista kliseet: *mullistava, vallankumouksellinen, saumaton, maailmanluokan, huippuluokan, ainutlaatuinen, innovatiivinen, seuraavalle tasolle, pelinmuuttaja, valjastaa*.
   - Korvaa suoralla kuvauksella siitä, mitä toiminto tekee tai mitä tuloksia saavutettiin.
   - Poista `Key takeaways` tai käännä suomeksi; korvaa `Next steps` termillä `Seuraavat vaiheet` ja liitä mukaan konkreettiset päivämäärät.
3. **Tarkka taloussanasto:**
   - Liikevaihto (Revenue) | Toistuva liikevaihto (Recurring revenue / ARR)
   - Käyttökate (EBITDA) | Liikevoitto (EBIT)
   - Tilikausi (Fiscal year) | Oikaistu (Adjusted)
   - Kassavirta (Cash flow) | Vapaa kassavirta (Free cash flow)
   - Velaton arvo (Enterprise value, EV) | Oman pääoman arvo (Equity value)
4. **Suomalainen typografia:**
   - Lainausmerkit: `”Näin”` (sama kaareva merkki alussa ja lopussa).
   - Ajatusviiva: En-dash välilyönneillä virkkeen osien välissä (` – `).
   - Yhdyssanat: Pitkät sanat (*asiakastyytyväisyyskysely*) rikkovat kapeat sarakkeet. Varaa suomenkieliselle tekstille noin 10 % enemmän leveyttä, käytä CSS:ssä `hyphens: auto; lang="fi"` ja pehmeitä tavuviivoja (`&shy;`). Älä koskaan tasoita tekstiä molempiin reunoihin (*justify*).
5. **Kaksikieliset diat:** Yksi kieli per dia. Jos rinnakkaiset kielet ovat välttämättömiä, pidä järjestys vakiona (suomi ensin, ruotsi/englanti toissijaisella värillä). Älä koskaan sekoita suomalaisia ja englantilaisia lukumerkintöjä samalla dialla.

---

## 9. Brändit ja mallipohjien mittaus

Asiakkaan oma brändi ja mallipohja menevät aina yleisen tyylin edelle:

### PowerPoint-mallipohjan mittaaminen (`.pptx` / `.potx`)
1. Pura `.pptx` zip-arkistona ja lue `ppt/theme/theme1.xml`:
   - `a:clrScheme`: Poimi värit `dk1`, `lt1`, `dk2`, `lt2` sekä `accent1`–`accent6`.
   - `a:fontScheme`: Poimi otsikko- ja leipätekstifontit.
2. Mittaa asettelut `python-pptx` -kirjastolla:
   - Mittaa paikanpitäjien koordinaatit (`left`, `top`, `width`, `height`) EMU-yksikköinä ($914{,}400\text{ EMU} = 1\text{ tuuma}$; $12{,}700\text{ EMU} = 1\text{ pt}$).

### Todennetut brändiprofiilit

#### Translink Corporate Finance (TLCF)
- **Värit:** Tummansininen `#1B2B4B` (päärakenne, otsikot, pääsarja), Oranssi `#F47920` (korostus).
- **Kontrastisääntö:** Oranssi valkoisella taustalla on vain 2.8:1 (ei täytä esteettömyyttä). Käytä oranssia taustapintana tummansinisellä tekstillä (5.1:1) tai oranssia tekstiä vain tummansinisellä taustalla (5.1:1). Jos oranssin tekstin on oltava valkoisella, käytä tummempaa sävyä `#B85A12` (4.7:1).
- **Fontit:** Barlow Condensed (otsikot, avainluvut), Barlow (leipäteksti, taulukot).

#### DCM Capital
- **Värit:** Liuskekivi `#182B33` (pääteksti), Vaalea kerma `#F5F4EF` (tausta), Sinivihreä `#006B6B` (pääkorostus), Ruoste `#A34B27` (toissijainen kontrasti), Harmaa `#52656B` (metadata).
- **Fontit:** Inter / järjestelmän sans-serif, korkea toimituksellinen selkeys, tasalevyiset numerot.

---

## 10. 3-tasoinen laaduntarkastus

Tarkasta esitys kolmella eri mittakaavalla:

```
┌───────────────────────────┐      ┌───────────────────────────┐      ┌───────────────────────────┐
│ Taso 1: Kontaktikartta    │ ───> │ Taso 2: Ensisilmäys       │ ───> │ Taso 3: Mikrotarkastus   │
│ Koko tarinan kulku,       │      │ 5 sekunnin tulokohta,     │      │ Luvut, lähteet, yksiköt,  │
│ rytmi, visuaalinen vaihtelu│     │ hierarkia, päänäyttö      │      │ rivitykset, reunaehdot    │
└───────────────────────────┘      └───────────────────────────┘      └───────────────────────────┘
```

### 8 tarkastuskysymystä
1. **Tarkoitus:** Mikä täsmällinen havainto tai päätös sivulla välitetään?
2. **Näytön aitous:** Seuraako väiteotsikko suoraan esitetystä datasta ilman liioittelua?
3. **Visuaalinen selitys:** Minkä suhteen visuaalinen muoto paljastaa paremmin kuin pelkkä teksti?
4. **Hierarkia:** Onko sivulla selkeä tulokohta ja loogiset lukutasot?
5. **Tiheys ja luettavuus:** Onko teksti helposti luettavissa ilman siristelyä?
6. **Yhdenmukaisuus:** Säilyttävätkö värit ja symbolit saman merkityksen dialta toiselle?
7. **Viimeistely:** Esiintyykö tekstin törmäyksiä, outoja rivityksiä tai leikkautuvia nimilappuja?
8. **Toimitus:** Säilyttääkö vienti (PDF, PPTX) kaikki fontit ja muokattavuuden?

### Automaattisen linterin tunnukset (`slop_lint.py`)
- **`H1` / `H2`:** Täyttämättömät paikanpitäjät (`[Yhtiö]`, `TBD`) tai työkoneiston jäänteet.
- **`H3`:** Kielletyt nimet koodinimiesityksessä (luottamuksellisuusvuoto).
- **`N4` / `N7`:** Ristiriitaiset lukumerkinnät tai eriävät arvot samalle metriikalle eri dioissa.
- **`N5` / `N8`:** Merkitsemätön havainnollistava data tai perusteeton tarkkuus.
- **`K6` / `K7`:** Perustelematon väite tai puuttuva vertailupohja.
- **`G1` / `G5` / `G9`:** Vääristävä perspektiivi, lukukelvottomat nimilaput tai harhaanjohtavat akselit.
- **`T7` / `L3`:** Liian pieni fonttikoko tai asettelun ylivuoto.

---

## 11. Tekniset työkalut ja skriptit

### HTML/SVG-esitysmoottori (`assets/deck.html`)
- Itsenäinen HTML-esitysmoottori ilman asennusvaihetta tai npm-riippuvuuksia.
- Kiinteä 1920 × 1080 canvas, joka skaalautuu CSS:llä mihin tahansa näyttöön.
- Sisäänrakennettu dianvaihto (nuolinäppäimet, välilyönti, kokoruutu `F`, tulostus `P`).
- Vektorikaaviot suorana SVG:nä tai kevyenä apurakenteena (`deck.chart.bars()`).

### Komentorivityökalut
Aja skriptit suoraan komentoriviltä:

```bash
# 1. Staattinen analyysi: tarkasta luvut, muodot, koodinimet ja ghost deck
python3 scripts/slop_lint.py deck.html --ghost --mode=read

# 2. Tiukka koodinimitarkastus (M&A- ja sijoitusmateriaalit)
python3 scripts/slop_lint.py deck.html --forbid="Kohdeyhtiö Oy,Ostaja Corp"

# 3. Headless-renderöinti: tuota PNG-diat, kontaktikartta ja audit-raportti (Node + Playwright)
node scripts/render.mjs deck.html qa_output --pdf

# 4. Yksikkötestit
python3 scripts/test_lint.py /tmp/test-scratch
```

---

## 12. Monialustainen käyttö (Antigravity, Claude, OpenAI)

### Antigravity (Gemini-ympäristö)
- Skilli aktivoidaan komennolla `$visualisointi` tai vapaalla suomenkielisellä pyynnöllä.
- Agentti lukee tarvittaessa kansion `references/`-dokumentit ja ajaa tarkistusskriptit suoraan.

### Anthropic Claude (Claude Projects & Claude Code)
- **Claude Projects:** Kopioi [CLAUDE.md](CLAUDE.md) -tiedoston sisältö projektin **Project Instructions** -kenttään. Lataa [SKILL.md](SKILL.md) tiedostoihin.
- **Claude Code CLI:** Sijoita [CLAUDE.md](CLAUDE.md) projektin juureen. Claude Code ottaa säännöt heti käyttöön.

### OpenAI (ChatGPT Custom GPT, Codex & API)
- **Custom GPT:** Kopioi [OPENAI.md](OPENAI.md) suoraan **Instructions**-kenttään. Lataa [SKILL.md](SKILL.md) ja [assets/deck.html](assets/deck.html) tietopankkiin (*Knowledge*).
- **Codex / API:** Anna järjestelmäkehotteeksi [CODEX.md](CODEX.md) -ohjeistus koodatessasi visualisointeja.

---

*Tekijä: Sami Miettinen · Visualisointi Framework v2.0*
