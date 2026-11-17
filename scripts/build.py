import sys, pathlib, importlib, unicodedata, re
from common import render_lesson, render_key, to_pdf, ans_of, CHAPTERS

MODS = {'I': 'ch1', 'VIII': 'ch8', 'IX': 'ch9', 'X': 'ch10'}
out = pathlib.Path('out'); out.mkdir(exist_ok=True)
html = pathlib.Path('html'); html.mkdir(exist_ok=True)

def slug(s):
    s = unicodedata.normalize('NFD', s.replace('đ', 'd').replace('Đ', 'D'))
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return re.sub(r'[^A-Za-z0-9]+', '_', s).strip('_').upper()

for ch in sys.argv[1:]:
    lessons = importlib.import_module(MODS[ch]).LESSONS
    jobs = []
    for L in lessons:
        assert len(L['mc']) == 8 and len(L['ds'][1]) == 4
        ans = ''.join(ans_of(q[1]) for q in L['mc'])
        print(f"Bài {L['num']:>2}: {ans}  " + ' '.join(f'{k}{ans.count(k)}' for k in 'ABCD'))
        h = html / f"bai{L['num']:02d}.html"; h.write_text(render_lesson(L, ch))
        jobs.append((h, out / f"KHTN6_BAI{L['num']:02d}_{slug(L['title'])}.pdf", f"KHTN 6 · Bài {L['num']}. {L['title']}"))
    k = html / f'key_{ch}.html'; k.write_text(render_key(ch, lessons))
    jobs.append((k, out / f'DAP_AN_KHTN6_CHUONG_{ch}.pdf', f"Đáp án · {CHAPTERS[ch]['name']}"))
    to_pdf(jobs)
