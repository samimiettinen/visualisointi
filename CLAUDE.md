# Ylläpito-ohjeet

Tämä repo on Visualisointi-skill. Käyttäjälle näkyvät ohjeet ovat tiedostossa `SKILL.md` ja `references/`-kansiossa. Tämä tiedosto koskee vain repon kehittämistä.

## Yksi totuuden lähde

- Kirjainkoot, ruudukko, värien roolit ja kontrastiluvut ovat vain tiedostossa `references/tokens.md`. Muut tiedostot viittaavat siihen eivätkä toista arvoja.
- Brändiprofiilit ovat vain tiedostossa `references/brands.md`.
- Linterin tunnukset selitetään vain tiedostossa `references/signs.md`. Kun lisäät tai muutat tunnuksen `scripts/lint.py`:ssä, päivitä taulukko samassa muutoksessa.
- `SKILL.md` pysyy alle 500 rivin ja ohjaa referensseihin Lue tarvittaessa -taulukon kautta. Jokainen uusi referenssitiedosto lisätään taulukkoon.
- Kun muutat `assets/deck.html`:n tokeneita, tarkista kontrasti sekä `--bg`- että `--raised`-pintaa vasten ja päivitä `tokens.md`:n taulukko.

## Kieli

- `SKILL.md`, `README.md` ja tämä tiedosto ovat suomeksi, referenssit ja skriptien tulosteet englanniksi.
- Suomenkielinen teksti noudattaa Kielitoimiston normeja; aja se suomen-kieli-skillin kautta, jos se on käytettävissä.
- `description`-kenttä on enintään 200 merkkiä, koska Clauden sovellus ei hyväksy pidempää. `scripts/package.py` tarkistaa tämän.

## Lähteet ja lisenssi

Älä kopioi koodia, tekstiä tai kuvia muista projekteista. Kirjoita uusi koodi itse; ulkoisiin esimerkkeihin linkitetään `references/human-guides.md`:ssä, eikä niiden aineistoa tuoda repoon. Esimerkkien yritykset ja luvut ovat kuvitteellisia, ja se mainitaan esimerkin lähderivillä.

## Tarkistukset ennen committia

```bash
python3 scripts/test_lint.py /tmp/visualisointi-testit
python3 scripts/package.py
node scripts/render.mjs examples/rahoitus.html /tmp/qa-rahoitus --pdf
```

Kun muutat esimerkkiä, renderöi se uudelleen ja päivitä sen PNG- ja PDF-versio `examples/`-kansiossa.

## Evalit

Testitapaukset ovat `evals/<tapaus>/`-kansioissa (`prompt.md`, `case.yaml`, `graders/`). Lisää uusi tapaus aina, kun korjaat skillin käytöksessä havaitun virheen. Aja ne skill-creator-skillillä tai komennolla `claude plugin eval . --allow-tools Write,Edit,Bash`.
