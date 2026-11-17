"""Renderer for KHTN 6 physics worksheets (one lesson per sheet) + chapter answer keys."""
import pathlib, math

CSS = """
@page { size: A4; }
:root{--ink:#1e293b;--muted:#64748b;--line:#cbd5e1;--ds:#0f766e;--nghe:#15803d;--nghe-bg:#eaf7ee}
*{box-sizing:border-box}
body{font-family:"Inter","DejaVu Sans","Noto Color Emoji",sans-serif;color:var(--ink);font-size:10.4pt;line-height:1.45;margin:0}
sub,sup{font-size:70%;line-height:0}
b{font-weight:650}
.keep{break-inside:avoid}
.hero{border-radius:14px;padding:13px 18px 12px;background:var(--grad);color:#fff;position:relative;overflow:hidden}
.hero .tag{display:inline-block;background:rgba(255,255,255,.22);border:1px solid rgba(255,255,255,.45);border-radius:20px;padding:2px 10px;font-size:8.3pt;font-weight:600;letter-spacing:.4px}
.hero h1{margin:6px 0 1px;font-size:18.5pt;line-height:1.15;font-weight:800}
.hero .en{font-size:9.5pt;opacity:.92;font-style:italic}
.hero .deco{position:absolute;right:-6px;top:-18px;font-size:78pt;opacity:.18}
.student{display:grid;grid-template-columns:2.4fr 1fr 1.2fr;gap:10px;margin:9px 0 4px;font-size:9.8pt}
.student div{border-bottom:1.5px dotted #94a3b8;padding:2px 2px 3px;color:var(--muted)}
.road{display:flex;margin:6px 0 4px}
.stop{flex:1;text-align:center;font-size:7.6pt;line-height:1.2;color:var(--muted);position:relative}
.stop .dot{width:26px;height:26px;border-radius:50%;margin:0 auto 2px;display:flex;align-items:center;justify-content:center;font-size:11.5pt;position:relative;z-index:2}
.stop:not(:last-child)::after{content:"";position:absolute;top:13px;left:50%;width:100%;height:3px;background:repeating-linear-gradient(90deg,#cbd5e1 0 6px,transparent 6px 10px);z-index:1}
.stop b{display:block;color:var(--ink);font-size:8pt}
.sec{display:flex;align-items:center;gap:10px;margin:13px 0 7px;break-after:avoid}
.sec .num{flex:none;width:32px;height:32px;border-radius:10px;color:#fff;display:flex;align-items:center;justify-content:center;font-size:14pt}
.sec h2{margin:0;font-size:13pt;font-weight:800;line-height:1.15}
.sec small{display:block;font-weight:500;color:var(--muted);font-size:8.5pt;margin-top:1px}
.sec .stars{margin-left:auto;font-size:8pt;color:var(--muted);border:1px dashed var(--line);border-radius:8px;padding:3px 8px;white-space:nowrap}
.sec .stars span{color:#f59e0b;font-size:10pt;letter-spacing:1px}
/* tree */
.tree{border-radius:14px;padding:11px 11px 9px;margin:4px 0 8px;break-inside:avoid;background:var(--cbg)}
.root{display:block;width:max-content;max-width:94%;margin:0 auto;color:#fff;font-weight:800;font-size:11.5pt;padding:6px 18px;border-radius:30px;box-shadow:0 3px 0 rgba(0,0,0,.12);position:relative;background:var(--c);text-align:center}
.root::after{content:"";position:absolute;left:50%;bottom:-12px;width:2.5px;height:12px;background:var(--c)}
.branches{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-top:12px;padding-top:12px;position:relative}
.branches::before{content:"";position:absolute;top:0;height:2.5px;left:16.66%;right:16.66%;background:var(--c)}
.br{background:#fff;border-radius:10px;padding:0 0 6px;position:relative;border:1.5px solid var(--csoft)}
.br::before{content:"";position:absolute;top:-13.5px;left:50%;width:2.5px;height:12px;background:var(--c)}
.br h4{margin:0 0 4px;padding:5px 8px;border-radius:8px 8px 0 0;font-size:9.3pt;text-align:center;font-weight:800;color:#fff}
.leaf{font-size:8.7pt;line-height:1.38;margin:4px 7px 0 15px;position:relative}
.leaf::before{content:"";position:absolute;left:-9px;top:6px;width:5px;height:5px;border-radius:50%;background:var(--c)}
.f{display:inline-block;background:#f1f5f9;border:1px solid #e2e8f0;border-radius:5px;padding:0 5px;font-weight:650;white-space:nowrap}
.figbox{background:#fff;border:1.5px solid var(--line);border-radius:12px;padding:7px 10px;margin:4px 0 6px;break-inside:avoid;text-align:center}
.figbox .cap{font-size:8.5pt;color:var(--muted);margin-top:2px}
/* questions */
.lv{display:block;width:fit-content;font-weight:800;font-size:9.8pt;margin:8px 0 4px;padding:2px 10px;border-radius:6px}
.lv.l1{background:#dcfce7;color:#15803d} .lv.l2{background:#fef3c7;color:#b45309} .lv.l3{background:#ffe4e6;color:#be123c}
.q{margin:0 0 6px;break-inside:avoid}
.q .qh{display:flex;gap:6px}
.q .qn{flex:none;font-weight:800;min-width:44px;color:var(--c)}
.opts{display:grid;gap:1px 14px;margin:2px 0 0 50px}
.opts.c4{grid-template-columns:repeat(4,1fr)} .opts.c2{grid-template-columns:1fr 1fr} .opts.c1{grid-template-columns:1fr}
.opts span b{display:inline-block;width:18px}
.items{margin:2px 0 0 50px}
.items div{margin:2px 0}
.sheet{border:1.5px dashed #94a3b8;border-radius:10px;padding:6px 10px;margin:6px 0 4px;background:#fcfdff;break-inside:avoid}
.sheet h6{margin:0 0 4px;font-size:8.8pt;color:var(--muted);font-weight:700}
.bub{display:grid;grid-template-columns:repeat(4,1fr);gap:4px 8px;font-size:8.6pt}
.bub b{display:inline-block;width:18px}
.o{display:inline-block;width:14px;height:14px;border:1.3px solid #64748b;border-radius:50%;text-align:center;line-height:12px;font-size:7pt;margin-right:1px;color:#64748b}
.ds-q{border-left:3px solid var(--csoft);padding-left:9px}
.ds-items div{display:flex;gap:6px;margin:2px 0}
.ds-items div span:first-child{flex:1}
.box2{display:inline-flex;gap:3px;flex:none}
.box2 i{font-style:normal;display:inline-block;width:18px;height:16px;border:1.2px solid #94a3b8;border-radius:3px;font-size:7pt;text-align:center;line-height:14px;color:#94a3b8}
.tag-l{display:inline-block;font-size:7.6pt;font-weight:800;border-radius:4px;padding:0 6px;margin-right:5px;vertical-align:1px;color:#fff}
.tag-l.cb{background:#0ea5e9} .tag-l.nc{background:#e11d48}
.lines{margin:3px 0 0 50px}
.lines div{border-bottom:1px dotted #94a3b8;height:20px}
.feature{border-radius:14px;padding:9px 12px;margin:6px 0;break-inside:avoid;background:var(--nghe-bg);border:1.5px solid #bbe5c8}
.feature .q .qn{color:var(--nghe)}
.fact{display:grid;grid-template-columns:1.6fr 1fr;gap:8px;margin:6px 0;break-inside:avoid}
.fact > div{border-radius:12px;padding:7px 10px;font-size:8.8pt}
.fact .k{background:#fff7ed;border:1.5px solid #fed7aa}
.fact .k b:first-child{color:#c2410c}
.fact .j{background:#eef2ff;border:1.5px solid #c7d2fe}
.fact .j b:first-child{color:#4338ca}
.foot{margin-top:8px;text-align:center;font-size:8.8pt;color:var(--muted)}
table.t{border-collapse:collapse;width:calc(100% - 50px);margin:3px 0 4px 50px;font-size:9.2pt}
table.t td,table.t th{border:1px solid var(--line);padding:4px 6px;text-align:center}
table.t th{background:var(--cbg);font-weight:700}
table.t td.l{text-align:left}
table.t td.e{height:24px}
/* key */
.kk h2{font-size:12pt;margin:12px 0 4px;padding:4px 10px;border-radius:6px;color:#fff;background:var(--c);break-after:avoid}
.kk p{font-size:9.3pt;margin:3px 0}
.kk table.g{border-collapse:collapse;font-size:9pt;margin:2px 0 4px}
.kk table.g td,.kk table.g th{border:1px solid var(--line);padding:2px 8px;text-align:center}
.kk table.g th{background:#f1f5f9}
.kk .blk{break-inside:avoid}
"""

CHAPTERS = {
  'I':   dict(name='CHƯƠNG I – MỞ ĐẦU VỀ KHOA HỌC TỰ NHIÊN', c='#0f766e', cbg='#e6f6f4', csoft='#b7e4dd',
              grad='linear-gradient(120deg,#0f766e 0%,#14b8a6 55%,#5eead4 100%)', shades=['#0f766e','#13897f','#1aa596']),
  'VIII':dict(name='CHƯƠNG VIII – LỰC TRONG ĐỜI SỐNG', c='#1d4ed8', cbg='#e8f0fe', csoft='#c7d7fb',
              grad='linear-gradient(120deg,#1e3a8a 0%,#2563eb 50%,#60a5fa 100%)', shades=['#1d4ed8','#2563eb','#3b82f6']),
  'IX':  dict(name='CHƯƠNG IX – NĂNG LƯỢNG', c='#c2410c', cbg='#fff1e8', csoft='#fcd9c3',
              grad='linear-gradient(120deg,#9a3412 0%,#ea580c 50%,#fbbf24 100%)', shades=['#c2410c','#d9541a','#e8692b']),
  'X':   dict(name='CHƯƠNG X – TRÁI ĐẤT VÀ BẦU TRỜI', c='#4338ca', cbg='#eef0fd', csoft='#cdd2f7',
              grad='linear-gradient(120deg,#1e1b4b 0%,#4338ca 50%,#7c3aed 100%)', shades=['#4338ca','#5146d6','#6d4fe0']),
}

def _opts(opts):
    clean = [o.lstrip('*') for o in opts]
    m = max(len(o) for o in clean)
    cls = 'c4' if m <= 20 else ('c2' if m <= 52 else 'c1')
    return f'<div class="opts {cls}">' + ''.join(f'<span><b>{l}.</b>{o}</span>' for l, o in zip('ABCD', clean)) + '</div>'

def ans_of(opts):
    idx = [i for i, o in enumerate(opts) if o.startswith('*')]
    assert len(idx) == 1, opts
    return 'ABCD'[idx[0]]

def lines(n, indent=50):
    return f'<div class="lines" style="margin-left:{indent}px">' + '<div></div>' * n + '</div>'

def sec(icon, color, title, small, stars=True):
    s = '<div class="stars">Tự đánh giá: <span>☆☆☆</span></div>' if stars else ''
    return f'<div class="sec"><div class="num" style="background:{color}">{icon}</div><h2>{title}<small>{small}</small></h2>{s}</div>'

def render_lesson(L, ch):
    C = CHAPTERS[ch]
    vars_ = f"--c:{C['c']};--cbg:{C['cbg']};--csoft:{C['csoft']};--grad:{C['grad']}"
    br = ''.join(
        f'<div class="br"><h4 style="background:{C["shades"][i]}">{"①②③"[i]} {t}</h4>' + ''.join(f'<div class="leaf">{x}</div>' for x in leaves) + '</div>'
        for i, (t, leaves) in enumerate(L['br']))
    tree = f'<div class="tree"><span class="root">{L["icon"]} {L["root"]}</span><div class="branches">{br}</div></div>'
    fig = f'<div class="figbox">{L["fig"]}</div>' if L.get('fig') else ''

    # MCQ
    levels = [('l1', '🟢 Mức 1 – Nhận biết', 0, 3), ('l2', '🟡 Mức 2 – Thông hiểu', 3, 6), ('l3', '🔴 Mức 3 – Vận dụng', 6, 8)]
    mc = ''
    for cls, lab, a, b in levels:
        qs = []
        for k in range(a, b):
            stem, opts = L['mc'][k][0], L['mc'][k][1]
            extra = L['mc'][k][2] if len(L['mc'][k]) > 2 else ''
            qs.append(f'<div class="q"><div class="qh"><span class="qn">Câu {k+1}.</span><span>{stem}</span></div>{extra}{_opts(opts)}</div>')
        mc += f'<div class="keep"><div class="lv {cls}">{lab}</div>{qs[0]}</div>' + ''.join(qs[1:])
    cells = ''.join(f'<div><b>{i}</b>' + ''.join(f'<span class="o">{l}</span>' for l in 'ABCD') + '</div>' for i in range(1, 9))
    mc += f'<div class="sheet"><h6>✏️ PHIẾU TRẢ LỜI – tô kín đáp án em chọn</h6><div class="bub">{cells}</div></div>'

    stem, items = L['ds']
    ds = (f'<div class="q ds-q"><div class="qh"><span class="qn">Câu 1.</span><span>{stem}</span></div><div class="items ds-items">'
          + ''.join(f'<div><span>{l}) {t}</span><span class="box2"><i>Đ</i><i>S</i></span></div>' for l, (t, _) in zip('abcd', items)) + '</div></div>')

    tl = ''
    for k, it in enumerate(L['tl'], 1):
        lvl, text, subs, nl = it['lvl'], it['q'], it.get('sub', []), it.get('lines', 3)
        tag = '<span class="tag-l cb">CƠ BẢN</span>' if lvl == 'cb' else '<span class="tag-l nc">★ NÂNG CAO</span>'
        body = ''.join(f'<div>{s}</div>' for s in subs)
        extra = it.get('html', '')
        tl += (f'<div class="q"><div class="qh"><span class="qn">Bài {k}.</span><span>{tag}{text}</span></div>'
               + (f'<div class="items">{body}</div>' if body else '') + extra + (lines(nl) if nl else '') + '</div>')

    tt = ''
    for k, it in enumerate(L['tt'], 1):
        tt += (f'<div class="q"><div class="qh"><span class="qn">Câu {k}.</span><span><b>{it["t"]}</b> {it["q"]}</span></div>'
               + (lines(it.get('lines', 2)) if it.get('lines', 2) else '') + '</div>')

    road = ''.join(f'<div class="stop"><div class="dot" style="background:{c}">{e}</div><b>{t}</b>{d}</div>' for e, c, t, d in [
        ('🌳', '#e2e8f0', 'Bước 1', 'Sơ đồ kiến thức'), ('🎯', '#dbeafe', 'Bước 2', 'Trắc nghiệm 3 mức'),
        ('⚖️', '#ccfbf1', 'Bước 3', 'Đúng hay Sai?'), ('✍️', '#ffe4e6', 'Bước 4', 'Tự luận'), ('🌏', '#dcfce7', 'Bước 5', 'Thực tiễn')])

    html = f"""<!doctype html><html lang="vi"><head><meta charset="utf-8"><title>KHTN 6 – Bài {L['num']}</title>
<style>{CSS}</style></head><body style="{vars_}">
<div class="hero"><div class="deco">{L['icon']}</div><span class="tag">KHTN 6 · {C['name']} · PHIẾU HỌC TẬP</span>
<h1>Bài {L['num']}. {L['title']}</h1><div class="en">{L['en']}</div></div>
<div class="student"><div>Họ và tên:</div><div>Lớp: 6</div><div>Ngày: &nbsp;&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;&nbsp;&nbsp;/</div></div>
<div class="road">{road}</div>
{sec('🌳', '#475569', 'I. Sơ đồ kiến thức', 'Đọc từ gốc → nhánh → lá trước khi làm bài.', False)}
{tree}{fig}
{sec('🎯', '#2563eb', 'II. Trắc nghiệm', 'Làm lần lượt từ mức 1 đến mức 3, tô đáp án vào phiếu trả lời.')}
{mc}
{sec('⚖️', 'var(--ds)', 'III. Đúng hay Sai?', 'Đánh dấu ✓ vào ô Đ (đúng) hoặc S (sai) cho từng ý.')}
{ds}
{sec('✍️', '#e11d48', 'IV. Tự luận', 'Bài cơ bản làm trước, bài ★ nâng cao dành cho em muốn thử thách.')}
{tl}
{sec('🌏', 'var(--nghe)', 'V. Thực tiễn – Khoa học quanh em', 'Dùng kiến thức vừa học để giải thích điều em gặp hằng ngày.', False)}
<div class="feature">{tt}</div>
<div class="fact"><div class="k"><b>💡 Em có biết?</b> {L['fact']}</div><div class="j"><b>🎯 Nghề nghiệp liên quan:</b> {L['job']}</div></div>
<div class="foot">🌟 Tô sao tự đánh giá ở mỗi phần. Điều em muốn hỏi thầy cô: ……………………………………</div>
</body></html>"""
    return html

def render_key(ch, lessons):
    C = CHAPTERS[ch]
    vars_ = f"--c:{C['c']};--cbg:{C['cbg']};--csoft:{C['csoft']};--grad:{C['grad']}"
    out = ''
    for L in lessons:
        ans = [ans_of(q[1]) for q in L['mc']]
        g = '<table class="g"><tr><th>Câu</th>' + ''.join(f'<th>{i}</th>' for i in range(1, 9)) + '</tr><tr><th>Đáp án</th>' + ''.join(f'<td>{a}</td>' for a in ans) + '</tr></table>'
        ds = '; '.join(f'{l}) {v}' for l, (_, v) in zip('abcd', L['ds'][1]))
        note = f'<p><i>{L["mc_note"]}</i></p>' if L.get('mc_note') else ''
        tl = ''.join(f'<p><b>Bài {k}.</b> {it["a"]}</p>' for k, it in enumerate(L['tl'], 1))
        tt = ''.join(f'<p><b>Câu {k}.</b> {it["a"]}</p>' for k, it in enumerate(L['tt'], 1))
        out += f"""<div class="blk"><h2>Bài {L['num']}. {L['title']}</h2>
<p><b>II. Trắc nghiệm</b></p>{g}{note}
<p><b>III. Đúng – Sai:</b> {ds}{('. ' + L['ds_note']) if L.get('ds_note') else ''}</p>
<p><b>IV. Tự luận</b></p>{tl}<p><b>V. Thực tiễn (gợi ý)</b></p>{tt}</div>"""
    return f"""<!doctype html><html lang="vi"><head><meta charset="utf-8"><title>Đáp án {C['name']}</title><style>{CSS}</style></head>
<body class="kk" style="{vars_}"><div class="hero"><span class="tag">DÀNH CHO GIÁO VIÊN</span><h1 style="font-size:16pt">Đáp án phiếu học tập KHTN 6</h1><div class="en">{C['name']}</div></div>{out}</body></html>"""

def to_pdf(jobs):
    """jobs: list of (html_path, pdf_path, footer_text)"""
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch()
        for h, o, t in jobs:
            pg = b.new_page(); pg.goto(pathlib.Path(h).resolve().as_uri()); pg.wait_for_timeout(300)
            foot = f'<div style="width:100%;font-family:Inter,sans-serif;font-size:8px;color:#94a3b8;text-align:center;">{t} — Trang <span class="pageNumber"></span>/<span class="totalPages"></span></div>'
            pg.pdf(path=o, format='A4', print_background=True, display_header_footer=True, header_template='<span></span>',
                   footer_template=foot, margin={'top': '11mm', 'bottom': '13mm', 'left': '12mm', 'right': '12mm'})
            pg.close()

# ---------- figures ----------
def ruler_svg(length_cm=6.7, gh=10):
    W = 560; x0 = 30; s = 50  # px per cm
    ticks = ''
    for mm in range(gh * 10 + 1):
        x = x0 + mm * s / 10
        h = 22 if mm % 10 == 0 else (15 if mm % 5 == 0 else 9)
        ticks += f'<line x1="{x:.1f}" y1="60" x2="{x:.1f}" y2="{60+h}" stroke="#334155" stroke-width="{1.4 if mm%10==0 else 0.8}"/>'
        if mm % 10 == 0:
            ticks += f'<text x="{x:.1f}" y="96" font-size="11" text-anchor="middle" fill="#334155">{mm//10}</text>'
    pen = x0 + length_cm * s
    return f'''<svg viewBox="0 0 {W} 112" width="100%" height="118" font-family="Inter">
<rect x="{x0-12}" y="58" width="{gh*s+24}" height="46" rx="4" fill="#fef9c3" stroke="#a16207"/>{ticks}
<text x="{x0+gh*s+4}" y="96" font-size="10" fill="#334155">cm</text>
<polygon points="{x0},40 {x0+14},32 {pen-30},32 {pen-30},48 {x0+14},48" fill="#f59e0b" stroke="#92400e"/>
<polygon points="{pen-30},32 {pen},40 {pen-30},48" fill="#fde68a" stroke="#92400e"/><polygon points="{pen-8},38 {pen},40 {pen-8},42" fill="#1e293b"/>
<rect x="{x0}" y="32" width="10" height="16" fill="#f472b6" stroke="#92400e"/>
<line x1="{pen}" y1="26" x2="{pen}" y2="58" stroke="#e11d48" stroke-dasharray="3 2"/>
</svg>'''

def thermo_svg(reading=28, lo=-10, hi=50, step=2):
    H = 300; top = 20; bot = 250; x = 70
    def y(t): return bot - (t - lo) / (hi - lo) * (bot - top)
    ticks = ''
    for t in range(lo, hi + 1, step):
        major = t % 10 == 0
        ticks += f'<line x1="{x+14}" y1="{y(t):.1f}" x2="{x+14+(14 if major else 7)}" y2="{y(t):.1f}" stroke="#334155" stroke-width="{1.3 if major else .8}"/>'
        if major:
            ticks += f'<text x="{x+34}" y="{y(t)+4:.1f}" font-size="11" fill="#334155">{t}</text>'
    return f'''<svg viewBox="0 0 160 {H}" width="120" height="230" font-family="Inter">
<rect x="{x-8}" y="{top-8}" width="22" height="{bot-top+20}" rx="11" fill="#f8fafc" stroke="#64748b"/>
<circle cx="{x+3}" cy="{bot+26}" r="17" fill="#ef4444" stroke="#64748b"/>
<rect x="{x}" y="{y(reading):.1f}" width="6" height="{bot+12-y(reading):.1f}" fill="#ef4444"/>{ticks}
<text x="{x+52}" y="{top}" font-size="11" fill="#334155">°C</text></svg>'''

def force_svg():
    cell = 34; ox = 30; oy = 20
    grid = ''.join(f'<line x1="{ox+i*cell}" y1="{oy}" x2="{ox+i*cell}" y2="{oy+3*cell}" stroke="#cbd5e1"/>' for i in range(8))
    grid += ''.join(f'<line x1="{ox}" y1="{oy+j*cell}" x2="{ox+7*cell}" y2="{oy+j*cell}" stroke="#cbd5e1"/>' for j in range(4))
    ax, ay = ox + 2 * cell, oy + 1.5 * cell
    bx = ax + 3 * cell
    return f'''<svg viewBox="0 0 330 140" width="300" height="128" font-family="Inter">{grid}
<rect x="{ax-50}" y="{ay-22}" width="50" height="44" rx="4" fill="#fde68a" stroke="#92400e"/>
<line x1="{ax}" y1="{ay}" x2="{bx-10}" y2="{ay}" stroke="#e11d48" stroke-width="3"/><polygon points="{bx},{ay} {bx-12},{ay-6} {bx-12},{ay+6}" fill="#e11d48"/>
<circle cx="{ax}" cy="{ay}" r="4" fill="#1e293b"/><text x="{ax-4}" y="{ay+18}" font-size="12" font-weight="700">A</text>
<text x="{bx+6}" y="{ay-6}" font-size="13" fill="#e11d48" font-weight="700">F</text>
<line x1="{ox}" y1="{oy+3*cell+12}" x2="{ox+cell}" y2="{oy+3*cell+12}" stroke="#1e293b" stroke-width="2"/>
<text x="{ox+cell+6}" y="{oy+3*cell+16}" font-size="11">1 ô ứng với 10 N</text></svg>'''

def moon_phase(f, cx, cy, r):
    k = math.cos(2 * math.pi * f); rx = abs(k) * r
    dark = f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#334155" stroke="#94a3b8"/>'
    if f == 0: return dark
    if f == 0.5: return dark + f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#fde68a"/>'
    top, botm = f'{cx},{cy-r}', f'{cx},{cy+r}'
    if f < 0.5:   # waxing: right side lit
        outer = f'A {r} {r} 0 0 1 {botm}'
        sweep = 0 if f < 0.25 else 1
    else:         # waning: left side lit
        outer = f'A {r} {r} 0 0 0 {botm}'
        sweep = 1 if f > 0.75 else 0
    return dark + f'<path d="M {top} {outer} A {rx:.2f} {r} 0 0 {sweep} {top} Z" fill="#fde68a"/>'

def moon_svg():
    r = 22; out = ''
    for i in range(8):
        cx = 40 + i * 70
        out += moon_phase(i / 8, cx, 40, r) + f'<text x="{cx}" y="84" font-size="13" text-anchor="middle" font-weight="700" fill="#334155">{i+1}</text>'
    return f'<svg viewBox="0 0 560 92" width="100%" height="96" font-family="Inter"><rect width="560" height="92" rx="10" fill="#0f172a"/>{out}</svg>'
