import sys, pathlib, importlib, subprocess
from ot import render, render_key, arrange, to_pdf

MODS = ['p1', 'p2', 'p3', 'p4']
NAMES = {1: 'MO_DAU_BAO_CAO_THUYET_TRINH', 2: 'NANG_LUONG_CO_HOC_CONG_CONG_SUAT', 3: 'KIM_LOAI_DAY_HOAT_DONG_HOA_HOC', 4: 'DI_TRUYEN_MENDEL'}
out = pathlib.Path('out'); out.mkdir(exist_ok=True); html = pathlib.Path('html'); html.mkdir(exist_ok=True)
want = sys.argv[1:] or MODS
phieus = []
for m in MODS:
    try:
        P = importlib.import_module(m).P
    except ModuleNotFoundError:
        continue
    arrange(P); phieus.append(P)
    from collections import Counter
    print(f"Phiếu {P['num']}: {P['answers']} {dict(sorted(Counter(P['answers']).items()))}")
jobs = []
for P in phieus:
    if f"p{P['num']}" not in want:
        continue
    h = html / f"p{P['num']}.html"; h.write_text(render(P), encoding='utf-8')
    jobs.append((str(h), str(out / f"ON_TAP_GK1_KHTN9_PHIEU_{P['num']}_{NAMES[P['num']]}.pdf"), f"KHTN 9 · Ôn tập giữa HK I · Phiếu {P['num']}"))
extra = ''
try:
    extra = importlib.import_module('dc_key').HTML
except ModuleNotFoundError:
    pass
h = html / 'key.html'; h.write_text(render_key(phieus, extra), encoding='utf-8')
jobs.append((str(h), str(out / 'DAP_AN_ON_TAP_GK1_KHTN9.pdf'), 'Đáp án ôn tập giữa HK I KHTN 9'))
to_pdf(jobs)
