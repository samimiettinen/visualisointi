#!/usr/bin/env python3
"""Tests for lint.py: contextual design choices survive, integrity and Finnish norm
warnings remain, and the bundled examples stay clean.

Run: python3 scripts/test_lint.py <allowed-scratch-directory>
"""
import json
from pathlib import Path
import subprocess
import sys
import tempfile

if len(sys.argv) != 2:
    raise SystemExit(__doc__)
scratch = Path(sys.argv[1]).resolve()
scratch.mkdir(parents=True, exist_ok=True)
here = Path(__file__).resolve().parent
linter = here / 'lint.py'
root = here.parent


def run(path, *args):
    result = subprocess.run([sys.executable, str(linter), str(path), '--json', *args],
                            text=True, capture_output=True, check=True)
    return json.loads(result.stdout)['findings']


def ids(findings):
    return {f['id'] for f in findings}


def page(title, body, cls='comparison'):
    return f'<section class="slide {cls}"><h2>{title}</h2><p>{body}</p></section>'


def doc(lang, body):
    return f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8"></head><body>{body}</body></html>'


with tempfile.TemporaryDirectory(prefix='visualisointi-', dir=scratch) as tmp:
    tmp = Path(tmp)

    brand = tmp / 'brand.html'
    brand.write_text('<style>.title {font-weight:800;color:#8b5cf6;background:linear-gradient(90deg,#8b5cf6,#22d3ee);}</style>'
                     + ''.join(page('Regional comparison', f'Observed values for region {i}') for i in range(3)), encoding='utf-8')
    default = run(brand)
    assert 'L5' in ids(default), 'Repeated comparisons must remain inspectable'
    assert not any(f['severity'] in ('high', 'medium') for f in default), 'Brand and repetition choices must not mandate redesign'
    strict = run(brand, '--strict-style')
    assert any(f['id'] == 'C1' and f['severity'] == 'high' for f in strict), 'The strict style profile must be available explicitly'
    print('PASS contextual brand and repeated comparison; explicit strict profile')

    integrity = tmp / 'integrity.html'
    integrity.write_text(page('Draft page', '[Company] is Real Target Oy') + page('First source', 'ARR FY2025 €10m')
                         + page('Second source', 'ARR FY2025 €14m'), encoding='utf-8')
    findings = run(integrity, '--forbid=Real Target Oy')
    assert any(f['id'] == 'H1' and f['severity'] == 'high' for f in findings)
    assert any(f['id'] == 'H3' and f['severity'] == 'high' for f in findings)
    assert 'N7' in ids(findings), 'Numerical conflict candidates must survive the style change'
    print('PASS placeholders, forbidden visible name and conflicting metric candidates')

    density = tmp / 'density.html'
    density.write_text(page('Supporting detail', ' '.join(['Evidence supports this decision.'] * 20)), encoding='utf-8')
    assert 'N2' not in ids(run(density, '--mode=read'))
    assert any(f['id'] == 'N2' and f['severity'] == 'low' for f in run(density, '--mode=present'))
    print('PASS reading context changes the density hint without rejecting content')

    zero = tmp / 'zero.html'
    zero.write_text(page('First source', 'ARR FY2025 €0m') + page('Second source', 'ARR FY2025 €2m'), encoding='utf-8')
    assert 'N7' in ids(run(zero)), 'Zero must participate in the heuristic'
    print('PASS zero-valued metric comparison')

    # Finnish norms: every seeded error is found, the corrected version is clean
    bad = tmp / 'suomi-virheet.html'
    bad.write_text(doc('fi',
        page('Liikevaihto Kasvoi Selvästi Vuonna 2025', 'Liikevaihto 2025 oli 12.4 M€ ja käyttökate -0,6 M€. Kasvu 2024-2026 oli 46%.')
        + page('Arvonmääritys ja lähteet', 'Velaton arvo on "noin" €45 milj. Lähde: [Lähde]')), encoding='utf-8')
    found = ids(run(bad))
    for fid in ('F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'H1'):
        assert fid in found, f'{fid} missing from Finnish seeded errors: {sorted(found)}'
    good = tmp / 'suomi-oikein.html'
    good.write_text(doc('fi',
        page('Liikevaihto kasvoi selvästi vuonna 2025', 'Liikevaihto 2025 oli 12,4 M€ ja käyttökate −0,6 M€. Kasvu 2024–2026 oli 46 %.')
        + page('Arvonmääritys ja lähteet', 'Velaton arvo on ”noin” 45 M€. Lähde: johdon raportointi 2025, 31.1.2026.')), encoding='utf-8')
    clean = [f for f in run(good) if f['id'].startswith(('F', 'H', 'N4'))]
    assert not clean, f'Correct Finnish must not trigger norm checks: {clean}'
    print('PASS Finnish norm checks F1–F7 and Finnish placeholders')

    proper = tmp / 'nimet.html'
    proper.write_text(doc('fi', page('Translink Corporate Finance neuvoo myyjää', 'Toimeksianto alkoi 3.11.2026 ja jatkuu.')), encoding='utf-8')
    assert 'F1' not in ids(run(proper)), 'Proper names in a sentence-case title are not Title Case'
    print('PASS proper names do not trigger F1')

    wrong_lang = tmp / 'kieli.html'
    wrong_lang.write_text(doc('en', page('Liikevaihto kasvoi vuonna 2025', 'Liikevaihto ja käyttökate kasvoivat, ja kassavirta oli positiivinen.')), encoding='utf-8')
    assert 'F8' in ids(run(wrong_lang)), 'Finnish text under lang="en" must be reported'
    print('PASS Finnish text with a wrong html lang')

    precision = tmp / 'tarkkuus.html'
    precision.write_text(doc('fi', page('Arvostus perustuu verrokkeihin', 'Arvostus on 2 374 123 € vuoden 2025 luvuilla.')), encoding='utf-8')
    assert 'N8' in ids(run(precision)), 'Full-precision money on a slide must be a precision candidate'
    print('PASS false precision in space-grouped figures')

# The bundled examples are the skill's own reference: they must not trip integrity or norm checks.
for example in sorted((root / 'examples').glob('*.html')) + [root / 'assets' / 'deck.html']:
    if example.name == 'sloppy-deck.html':
        continue
    serious = [f for f in run(example) if f['severity'] in ('high', 'medium')]
    assert not serious, f'{example.name} has findings: {serious}'
    print(f'PASS {example.relative_to(root)} has no high or medium findings')

sloppy = run(root / 'examples' / 'sloppy-deck.html')
assert {'K6', 'N4'} <= ids(sloppy), 'The negative fixture must keep producing integrity findings'
print('PASS examples/sloppy-deck.html still fails as intended')
