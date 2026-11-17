"""Renderer: phiếu ôn tập giữa HK1 KHTN 9 (lý thuyết + luyện tập) và file đáp án riêng."""
import sys, pathlib
sys.path.insert(0, '/home/claude/l9')
from common import CSS as BASE, to_pdf, lines, sec

CSS = BASE + """
.th-sub{font-weight:800;font-size:10.5pt;margin:8px 0 3px;color:var(--c)}
.box{border-radius:12px;padding:7px 11px;margin:5px 0;break-inside:avoid;font-size:9.2pt}
.box h5{margin:0 0 3px;font-size:9.6pt;font-weight:800}
.box.fm{background:#f8fafc;border:1.5px solid var(--csoft)} .box.fm h5{color:var(--c)}
.box.warn{background:#fff7ed;border:1.5px solid #fed7aa} .box.warn h5{color:#c2410c}
.box ul{margin:2px 0 0;padding-left:18px} .box li{margin:1px 0}
.fgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:5px 10px}
.fgrid div{background:#fff;border:1px solid #e2e8f0;border-radius:8px;padding:4px 7px;font-size:8.9pt}
.fgrid div b{color:var(--c)}
.sa-ans{display:flex;flex-wrap:wrap;gap:6px 16px;margin:4px 0 2px 50px;font-size:9pt}
.sa-ans span{display:inline-flex;align-items:center;gap:5px}
.sa-ans i{font-style:normal;display:inline-block;min-width:92px;height:20px;border:1.5px solid var(--c);border-radius:5px;background:#fff}
.series{display:flex;gap:3px;margin:4px 0 2px;justify-content:center;flex-wrap:nowrap}
.series div{flex:1;text-align:center;border-radius:6px;padding:4px 0 3px;color:#fff;font-weight:800;font-size:10pt;line-height:1.1}
.series div small{display:block;font-size:6.6pt;font-weight:600;opacity:.92}
.arrow-note{display:flex;justify-content:space-between;font-size:8.3pt;color:var(--muted);margin:1px 2px 0;font-weight:600}
table.pn{border-collapse:collapse;margin:3px auto;font-size:9.5pt}
table.pn td,table.pn th{border:1.3px solid var(--csoft);padding:3px 10px;text-align:center;min-width:44px}
table.pn th{background:var(--cbg);color:var(--c)}
.two{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.pb{break-before:page}
.kk .ex{font-size:9pt;margin:1px 0 1px 12px;color:#334155}
"""

def _opts(opts):
    m = max(len(o) for o in opts)
    cls = 'c4' if m <= 20 else ('c2' if m <= 50 else 'c1')
    return f'<div class="opts {cls}">' + ''.join(f'<span><b>{l}.</b>{o}</span>' for l, o in zip('ABCD', opts)) + '</div>'

def arrange(P):
    """Đặt đáp án đúng vào vị trí cân bằng A/B/C/D bằng phép xoay vòng (giữ thứ tự tương đối)."""
    from collections import Counter
    qs = P['mc']
    for q in qs:
        idx = [i for i, o in enumerate(q['o']) if o.startswith('*')]
        assert len(idx) == 1, q['q']
        q['ci'] = idx[0]
        q['o'] = [o.lstrip('*') for o in q['o']]
        assert len(set(q['o'])) == 4, q['q']
    cnt = Counter('ABCD'[q['ci']] for q in qs if q.get('fix'))
    n = len(qs); quota = {l: n // 4 + (1 if i < n % 4 else 0) for i, l in enumerate('ABCD')}
    pattern = [l for l in 'BDACCADBDBCAACBD' * 3]
    k = 0
    for q in qs:
        if q.get('fix'):
            continue
        while True:
            l = pattern[k % len(pattern)]; k += 1
            if cnt[l] < quota[l]:
                break
        t = 'ABCD'.index(l); s = (t - q['ci']) % 4
        q['o'] = q['o'][-s:] + q['o'][:-s] if s else q['o']
        q['ci'] = t; cnt[l] += 1
    P['answers'] = ''.join('ABCD'[q['ci']] for q in qs)

def tree(root, icon, brs, shades):
    n = len(brs)
    b = ''.join(f'<div class="br"><h4 style="background:{shades[i % 3]}">{"①②③④"[i]} {t}</h4>' + ''.join(f'<div class="leaf">{x}</div>' for x in leaves) + '</div>'
                for i, (t, leaves) in enumerate(brs))
    edge = 100 / (2 * n)
    return (f'<div class="tree"><span class="root">{icon} {root}</span>'
            f'<div class="branches" style="grid-template-columns:repeat({n},1fr)"><style></style>{b}</div></div>').replace(
            '<div class="branches"', f'<div class="branches" data-e="{edge}"')

def render(P):
    t = P['theme']
    vars_ = f"--c:{t['c']};--cbg:{t['cbg']};--csoft:{t['csoft']};--grad:{t['grad']}"
    th = ''
    for blk in P['theory']:
        if blk[0] == 'tree':
            _, root, icon, brs = blk
            th += tree(root, icon, brs, t['shades'])
        elif blk[0] == 'sub':
            th += f'<div class="th-sub">{blk[1]}</div>'
        elif blk[0] == 'fm':
            th += f'<div class="box fm"><h5>📐 {blk[1]}</h5><div class="fgrid">' + ''.join(f'<div>{x}</div>' for x in blk[2]) + '</div></div>'
        elif blk[0] == 'warn':
            th += f'<div class="box warn"><h5>⚠️ {blk[1]}</h5><ul>' + ''.join(f'<li>{x}</li>' for x in blk[2]) + '</ul></div>'
        elif blk[0] == 'html':
            th += blk[1]
    # MCQ
    mc = ''; k = 0
    labels = [('l1', '🟢 Mức 1 – Nhận biết'), ('l2', '🟡 Mức 2 – Thông hiểu'), ('l3', '🔴 Mức 3 – Vận dụng')]
    for (cls, lab), n in zip(labels, P['levels']):
        qs = []
        for q in P['mc'][k:k + n]:
            k += 1
            qs.append(f'<div class="q"><div class="qh"><span class="qn">Câu {k}.</span><span>{q["q"]}</span></div>{q.get("x", "")}{_opts(q["o"])}</div>')
        mc += f'<div class="keep"><div class="lv {cls}">{lab}</div>{qs[0]}</div>' + ''.join(qs[1:])
    N = len(P['mc'])
    cells = ''.join(f'<div><b>{i}</b>' + ''.join(f'<span class="o">{l}</span>' for l in 'ABCD') + '</div>' for i in range(1, N + 1))
    mc += f'<div class="sheet"><h6>✏️ PHIẾU TRẢ LỜI – tô kín đáp án em chọn</h6><div class="bub">{cells}</div></div>'
    # Đúng/Sai
    ds = ''
    for i, d in enumerate(P['ds'], 1):
        ds += (f'<div class="q ds-q"><div class="qh"><span class="qn">Câu {i}.</span><span>{d["q"]}</span></div>{d.get("x", "")}<div class="items ds-items">'
               + ''.join(f'<div><span>{l}) {s}</span><span class="box2"><i>Đ</i><i>S</i></span></div>' for l, (s, _, _) in zip('abcd', d['it'])) + '</div></div>')
    # Trả lời ngắn
    sa = ''
    for i, s in enumerate(P['sa'], 1):
        subs = ''.join(f'<div>{x}</div>' for x in s.get('sub', []))
        boxes = ''.join(f'<span>{lab} <i></i> {u}</span>' for lab, u in s['box'])
        sa += (f'<div class="q"><div class="qh"><span class="qn">Câu {i}.</span><span>{s["q"]}</span></div>'
               + (f'<div class="items">{subs}</div>' if subs else '') + (lines(s['lines']) if s.get('lines') else '')
               + f'<div class="sa-ans">{boxes}</div></div>')
    # Tự luận
    tl = ''
    for i, it in enumerate(P['tl'], 1):
        tag = '<span class="tag-l cb">CƠ BẢN</span>' if it['lvl'] == 'cb' else '<span class="tag-l nc">★ NÂNG CAO</span>'
        subs = ''.join(f'<div>{x}</div>' for x in it.get('sub', []))
        tl += (f'<div class="q"><div class="qh"><span class="qn">Bài {i}.</span><span>{tag}{it["q"]}</span></div>'
               + (f'<div class="items">{subs}</div>' if subs else '') + it.get('html', '') + (lines(it['lines']) if it.get('lines') else '') + '</div>')
    tt = ''.join(f'<div class="q"><div class="qh"><span class="qn">Câu {i}.</span><span><b>{x["t"]}</b> {x["q"]}</span></div>{lines(x.get("lines", 2))}</div>'
                 for i, x in enumerate(P['tt'], 1))
    road = ''.join(f'<div class="stop"><div class="dot" style="background:{c}">{e}</div><b>{a}</b>{d}</div>' for e, c, a, d in [
        ('🌳', '#e2e8f0', 'Bước 1', 'Lý thuyết'), ('🎯', '#dbeafe', 'Bước 2', 'Trắc nghiệm'), ('⚖️', '#ccfbf1', 'Bước 3', 'Đúng – Sai'),
        ('🔢', '#ede9fe', 'Bước 4', 'Trả lời ngắn'), ('✍️', '#ffe4e6', 'Bước 5', 'Tự luận'), ('🌏', '#dcfce7', 'Bước 6', 'Thực tiễn')])
    html = f"""<!doctype html><html lang="vi"><head><meta charset="utf-8"><title>{P['title']}</title><style>{CSS}</style></head><body style="{vars_}">
<div class="hero"><div class="deco">{P['icon']}</div><span class="tag">KHTN 9 · ÔN TẬP GIỮA HỌC KÌ I · PHIẾU {P['num']} · {P['subject']}</span>
<h1>{P['title']}</h1><div class="en">{P['en']}</div></div>
<div class="student"><div>Họ và tên:</div><div>Lớp: 9</div><div>Ngày: &nbsp;&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;&nbsp;&nbsp;/</div></div>
<div class="road">{road}</div>
{sec('🌳', '#475569', 'A. Hệ thống lý thuyết', 'Đọc kĩ sơ đồ, công thức và các lỗi hay gặp trước khi luyện tập.', False)}
{th}
{sec('🎯', '#2563eb', 'B. Phần I – Trắc nghiệm nhiều lựa chọn', 'Mỗi câu chỉ có một phương án đúng. Tô đáp án vào phiếu trả lời.')}
{mc}
{sec('⚖️', 'var(--ds)', 'C. Phần II – Trắc nghiệm Đúng/Sai', 'Trong mỗi ý a), b), c), d), đánh dấu ✓ vào ô Đ hoặc S.')}
{ds}
{sec('🔢', '#7c3aed', 'D. Phần III – Trả lời ngắn', 'Trình bày ngắn gọn phần tính ra nháp, ghi kết quả cuối cùng vào ô.')}
{sa}
{sec('✍️', '#e11d48', 'E. Tự luận', 'Bài cơ bản làm trước, bài ★ nâng cao dành cho em muốn thử thách.')}
{tl}
{sec('🌏', 'var(--nghe)', 'F. Thực tiễn – Khoa học quanh em', 'Vận dụng kiến thức để giải thích hiện tượng trong đời sống.', False)}
<div class="feature">{tt}</div>
<div class="fact"><div class="k"><b>💡 Em có biết?</b> {P['fact']}</div><div class="j"><b>🎯 Nghề nghiệp liên quan:</b> {P['job']}</div></div>
</body></html>"""
    return html

def render_key(phieus, extra=''):
    out = ''
    for P in phieus:
        t = P['theme']
        st = f"--c:{t['c']};--cbg:{t['cbg']}"
        N = len(P['mc'])
        rows = ''
        for a in range(0, N, 10):
            rng = range(a, min(a + 10, N))
            rows += '<tr><th>Câu</th>' + ''.join(f'<th>{i+1}</th>' for i in rng) + '</tr><tr><th>Đáp án</th>' + ''.join(f'<td><b>{P["answers"][i]}</b></td>' for i in rng) + '</tr>'
        ex = ''.join(f'<p class="ex"><b>Câu {i}{(" (ĐC câu " + str(q["dc"]) + ")") if q.get("dc") else ""} – {"ABCD"[q["ci"]]}.</b> {q["e"]}</p>' for i, q in enumerate(P['mc'], 1))
        ds = ''.join(f'<p><b>Câu {i}{(" (ĐC " + d["dc"] + ")") if d.get("dc") else ""}.</b> ' + '; '.join(f'{l}) <b>{v}</b> – {why}' for l, (_, v, why) in zip('abcd', d['it'])) + '</p>' for i, d in enumerate(P['ds'], 1))
        sa = ''.join(f'<p><b>Câu {i}{(" (ĐC câu " + str(s["dc"]) + ")") if s.get("dc") else ""}.</b> {s["a"]}</p>' for i, s in enumerate(P['sa'], 1))
        tl = ''.join(f'<p><b>Bài {i}.</b> {x["a"]}</p>' for i, x in enumerate(P['tl'], 1))
        tt = ''.join(f'<p><b>Câu {i}.</b> {x["a"]}</p>' for i, x in enumerate(P['tt'], 1))
        out += f"""<div style="{st}"><h2>Phiếu {P['num']}. {P['title']}</h2>
<div class="blk"><p><b>Phần I – Trắc nghiệm</b></p><table class="g">{rows}</table></div>{ex}
<p><b>Phần II – Đúng/Sai</b></p>{ds}<p><b>Phần III – Trả lời ngắn</b></p>{sa}<p><b>Tự luận</b></p>{tl}<p><b>Thực tiễn (gợi ý)</b></p>{tt}</div>"""
    return f"""<!doctype html><html lang="vi"><head><meta charset="utf-8"><title>Đáp án ôn tập giữa HK1 KHTN 9</title><style>{CSS}</style></head>
<body class="kk" style="--c:#1e3a8a;--grad:linear-gradient(120deg,#1e3a8a 0%,#2563eb 55%,#38bdf8 100%)"><div class="hero"><span class="tag">DÀNH CHO GIÁO VIÊN</span><h1 style="font-size:16pt">Đáp án & lời giải – Phiếu ôn tập giữa học kì I KHTN 9</h1><div class="en">Năm học 2026 – 2027 · "ĐC câu n" = câu tương ứng trong đề cương của trường</div></div>{out}{extra}</body></html>"""
