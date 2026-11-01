#!/usr/bin/env python3
"""Check that contextual design choices survive while integrity warnings remain.
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
linter = Path(__file__).with_name('slop_lint.py')

def run(path, *args):
    result = subprocess.run([sys.executable, str(linter), str(path), '--json', *args], text=True, capture_output=True, check=True)
    return json.loads(result.stdout)['findings']

def page(title, body):
    return f'<section class="slide comparison"><h2>{title}</h2><p>{body}</p></section>'

with tempfile.TemporaryDirectory(prefix='clear-slides-', dir=scratch) as tmp:
    tmp = Path(tmp)
    brand = tmp/'brand.html'
    brand.write_text('<style>.title {font-weight:800;color:#8b5cf6;background:linear-gradient(90deg,#8b5cf6,#22d3ee);}</style>'+''.join(page('Regional comparison', f'Observed values for region {i}') for i in range(3)))
    default = run(brand)
    assert any(f['id']=='L5' for f in default), 'Repeated comparisons must remain inspectable'
    assert not any(f['severity'] in ('high','medium') for f in default), 'Brand and repetition choices must not mandate redesign'
    strict = run(brand, '--strict-style')
    assert any(f['id']=='C1' and f['severity']=='high' for f in strict), 'Legacy profile should be available explicitly'
    print('PASS contextual brand and repeated comparison; explicit legacy profile')

    integrity = tmp/'integrity.html'
    integrity.write_text(page('Draft page','[Company] is Real Target Oy')+page('First source','ARR FY2025 €10m')+page('Second source','ARR FY2025 €14m'))
    findings = run(integrity, '--forbid=Real Target Oy')
    assert any(f['id']=='H1' and f['severity']=='high' for f in findings)
    assert any(f['id']=='H3' and f['severity']=='high' for f in findings)
    assert any(f['id']=='N7' for f in findings), 'Numerical conflict candidates must survive the style change'
    print('PASS placeholders, forbidden visible name and conflicting metric candidates')

    density = tmp/'density.html'
    density.write_text(page('Supporting detail', ' '.join(['Evidence supports this decision.']*20)))
    assert not any(f['id']=='N2' for f in run(density,'--mode=read'))
    assert any(f['id']=='N2' and f['severity']=='low' for f in run(density,'--mode=present'))
    print('PASS reading context changes the density hint without rejecting content')

    zero = tmp/'zero.html'
    zero.write_text(page('First source','ARR FY2025 €0m')+page('Second source','ARR FY2025 €2m'))
    assert any(f['id']=='N7' for f in run(zero)), 'Zero must participate in the heuristic'
    print('PASS zero-valued metric comparison')
