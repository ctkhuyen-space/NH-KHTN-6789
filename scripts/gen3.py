import pathlib
base = pathlib.Path('gen2.py').read_text().splitlines()
exec('\n'.join(base[:162]))  # shared CSS/helpers, Lí sheet, tree_hoa, card_hoa2

extra3 = """
.lv{display:inline-flex;align-items:center;gap:6px;font-weight:800;font-size:10pt;margin:10px 0 5px;padding:3px 10px;border-radius:6px;break-after:avoid}
.lv.l1{background:#dcfce7;color:#15803d} .lv.l2{background:#fef3c7;color:#b45309} .lv.l3{background:#ffe4e6;color:#be123c}
.dang{font-weight:800;font-size:10pt;color:var(--hoa);margin:10px 0 4px;break-after:avoid}
.dang span{display:inline-block;background:var(--hoa);color:#fff;border-radius:5px;padding:0 7px;margin-right:6px;font-size:8.6pt}
table.eq{border-collapse:collapse;width:100%;font-size:9.6pt;margin:3px 0 6px}
table.eq td,table.eq th{border:1px solid var(--line);padding:5px 7px}
table.eq th{background:var(--hoa-bg);color:var(--hoa);font-weight:700;text-align:center}
table.eq td.n{width:28px;text-align:center;font-weight:700;color:var(--hoa)}
table.eq td.e{letter-spacing:.2px}
table.eq tr{break-inside:avoid}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:4px 18px;font-size:9.8pt;margin:3px 0 6px 6px}
.g2 div{padding:3px 0;border-bottom:1px dotted #e2e8f0}
.g2 b{color:var(--hoa)}
.chain{background:#fff;border:1.5px solid var(--hoa-soft);border-radius:10px;padding:6px 10px;margin:4px 0;font-size:10.5pt;font-weight:650;text-align:center;letter-spacing:.3px}
.chain i{font-style:normal;color:var(--hoa);font-size:8.5pt;font-weight:800;vertical-align:4px}
.blk{display:inline-block;border-bottom:1.2px dotted #475569;min-width:44px}
.blk.l{min-width:80px}
.intro{font-size:9pt;color:var(--muted);font-style:italic;margin:0 0 4px}
"""
B = '<span class="blk"></span>'; BL = '<span class="blk l"></span>'
t, dp = '→<sup>t°</sup>', '→<sup>đpnc</sup>'

mc = [
 ('l1', '🟢 Mức 1 – Nhận biết', [
  mcq(1,'hoa','Trong công nghiệp, kim loại Na được điều chế bằng cách',['điện phân NaCl nóng chảy.','điện phân dung dịch NaCl.','dùng CO khử Na<sub>2</sub>O.','cho Fe tác dụng với dung dịch NaCl.'],False),
  mcq(2,'hoa','Phương pháp thủy luyện thường dùng để điều chế các kim loại',['hoạt động mạnh như Na, K.','hoạt động yếu như Cu, Ag.','chỉ dùng điều chế Al.','chỉ dùng điều chế Mg.'],False),
  mcq(3,'hoa','Thép là hợp kim của sắt với carbon, trong đó hàm lượng carbon',['lớn hơn 2%.','bằng 10%.','nhỏ hơn 2%.','lớn hơn 50%.']),
  mcq(4,'hoa','Kim loại ở thể lỏng ở điều kiện thường là',['Fe.','Cu.','Al.','Hg.']),
  mcq(5,'hoa','Phi kim tồn tại ở thể lỏng ở điều kiện thường là',['sulfur.','bromine.','carbon.','chlorine.']),
  mcq(6,'hoa','Thành phần chính của hợp kim dural (dùng làm vỏ máy bay) là',['Fe.','Cu.','Al.','Zn.']),
 ]),
 ('l2', '🟡 Mức 2 – Thông hiểu', [
  mcq(7,'hoa','Phản ứng nào sau đây thuộc phương pháp thủy luyện?',['CuO + H<sub>2</sub> '+t+' Cu + H<sub>2</sub>O','2Al<sub>2</sub>O<sub>3</sub> '+dp+' 4Al + 3O<sub>2</sub>','Fe<sub>2</sub>O<sub>3</sub> + 3CO '+t+' 2Fe + 3CO<sub>2</sub>','Fe + CuSO<sub>4</sub> → FeSO<sub>4</sub> + Cu'],False),
  mcq(8,'hoa','Ở nhiệt độ cao, khí H<sub>2</sub> khử được oxide nào sau đây?',['Na<sub>2</sub>O.','CuO.','MgO.','Al<sub>2</sub>O<sub>3</sub>.']),
  mcq(9,'hoa','Kim loại nào sau đây được điều chế bằng phương pháp nhiệt luyện (dùng CO khử oxide)?',['Na.','K.','Fe.','Mg.']),
  mcq(10,'hoa','Dãy gồm các oxide acid là',['SO<sub>2</sub>, CO<sub>2</sub>, P<sub>2</sub>O<sub>5</sub>.','Na<sub>2</sub>O, MgO, CaO.','SO<sub>2</sub>, MgO, CO<sub>2</sub>.','Al<sub>2</sub>O<sub>3</sub>, Na<sub>2</sub>O, SO<sub>2</sub>.']),
  mcq(11,'hoa','Phản ứng nào sau đây <b>không</b> xảy ra?',['Fe + CuSO<sub>4</sub>','Zn + CuSO<sub>4</sub>','Cu + AgNO<sub>3</sub>','Cu + FeSO<sub>4</sub>']),
  mcq(12,'hoa','Không dùng CO khử Al<sub>2</sub>O<sub>3</sub> để sản xuất nhôm vì',['Al hoạt động hóa học mạnh, Al<sub>2</sub>O<sub>3</sub> rất bền nên CO không khử được.','CO có giá thành quá cao.','Al<sub>2</sub>O<sub>3</sub> tan trong nước.','nhôm không có trong tự nhiên.'],False),
 ]),
 ('l3', '🔴 Mức 3 – Vận dụng', [
  mcq(13,'hoa','Khử hoàn toàn 8 gam CuO bằng khí H<sub>2</sub> ở nhiệt độ cao. Khối lượng Cu thu được là',['3,2 g.','6,4 g.','8,0 g.','12,8 g.']),
  mcq(14,'hoa','Cho Fe vào dung dịch CuSO<sub>4</sub> dư, sau phản ứng thu được 6,4 gam Cu. Khối lượng Fe đã phản ứng là',['2,8 g.','6,4 g.','5,6 g.','11,2 g.']),
  mcq(15,'hoa','Dùng CO dư khử hoàn toàn 24 gam Fe<sub>2</sub>O<sub>3</sub>. Khối lượng Fe thu được là',['16,8 g.','8,4 g.','11,2 g.','33,6 g.']),
  mcq(16,'hoa','Đốt cháy hoàn toàn 5,4 gam Al trong oxygen dư. Khối lượng Al<sub>2</sub>O<sub>3</sub> thu được là',['5,1 g.','20,4 g.','15,3 g.','10,2 g.']),
 ]),
]
mc_html = ''.join(f'<div class="lv {c}">{h}</div>' + '\n'.join(qs) for c, h, qs in mc)
cells = ''.join(f'<div><b>{i}</b>' + ''.join(f'<span class="o">{l}</span>' for l in 'ABCD') + '</div>' for i in range(1, 17))
mc_html += f'<div class="sheet"><h6>✏️ PHIẾU TRẢ LỜI – tô kín đáp án em chọn</h6><div class="bub" style="grid-template-columns:repeat(4,1fr)">{cells}</div></div>'

d1 = [  # (equation with blanks, method)
 f'CuO + H<sub>2</sub> {t} {BL} + {BL}',
 f'Fe<sub>2</sub>O<sub>3</sub> + {B}CO {t} {B}Fe + {B}{BL}',
 f'Fe<sub>3</sub>O<sub>4</sub> + {B}CO {t} {B}Fe + {B}CO<sub>2</sub>',
 f'ZnO + C {t} {BL} + CO',
 f'Fe<sub>2</sub>O<sub>3</sub> + {B}Al {t} {BL} + {B}Fe',
 f'{B}NaCl {dp} {B}Na + {BL}',
 f'{B}Al<sub>2</sub>O<sub>3</sub> {dp} {B}Al + {B}O<sub>2</sub>',
 f'Fe + CuSO<sub>4</sub> → {BL} + {BL}',
 f'Zn + CuSO<sub>4</sub> → {BL} + {BL}',
 f'Cu + {B}AgNO<sub>3</sub> → {BL} + {B}Ag',
]
rows1 = ''.join(f'<tr><td class="n">{i}</td><td class="e">{e}</td><td></td></tr>' for i, e in enumerate(d1, 1))
d2 = [f'{B}Na + O<sub>2</sub> {t} {B}Na<sub>2</sub>O', f'{B}Mg + O<sub>2</sub> {t} {B}{BL}', f'{B}Al + {B}O<sub>2</sub> {t} {B}Al<sub>2</sub>O<sub>3</sub>',
      f'{B}Fe + {B}O<sub>2</sub> {t} Fe<sub>3</sub>O<sub>4</sub>', f'S + O<sub>2</sub> {t} {BL}', f'C + O<sub>2</sub> {t} {BL}',
      f'{B}P + {B}O<sub>2</sub> {t} {B}P<sub>2</sub>O<sub>5</sub>', f'{B}Fe + {B}Cl<sub>2</sub> {t} {B}FeCl<sub>3</sub>',
      f'Fe + S {t} {BL}', f'{B}Na + Cl<sub>2</sub> {t} {B}{BL}']
g2 = ''.join(f'<div><b>{chr(96+i)})</b> {e}</div>' for i, e in enumerate(d2, 1))
pairs = ['Fe + CuSO<sub>4</sub>', 'Cu + FeSO<sub>4</sub>', 'Mg + FeSO<sub>4</sub>', 'Ag + CuSO<sub>4</sub>', 'Cu + AgNO<sub>3</sub>', 'CuO + H<sub>2</sub> (t°)', 'Al<sub>2</sub>O<sub>3</sub> + CO (t°)', 'Zn + FeSO<sub>4</sub>']
rows4 = ''.join(f'<tr><td class="n">{i}</td><td>{p}</td><td style="text-align:center;font-size:8pt;color:#94a3b8">Có ☐ &nbsp; Không ☐</td><td></td></tr>' for i, p in enumerate(pairs, 1))

tl = f"""
<div class="lv" style="background:var(--hoa-bg);color:var(--hoa)">A. VIẾT PHƯƠNG TRÌNH HÓA HỌC</div>
<p class="intro">Nhớ: viết đúng công thức → cân bằng số nguyên tử mỗi nguyên tố ở hai vế → ghi điều kiện phản ứng (t°, đpnc).</p>

<div class="dang"><span>Dạng 1</span>Hoàn thành, cân bằng phương trình tách kim loại và ghi tên phương pháp</div>
<table class="eq"><tr><th>TT</th><th>Phương trình hóa học (điền chất / hệ số vào chỗ trống)</th><th style="width:27%">Phương pháp</th></tr>{rows1}</table>

<div class="dang"><span>Dạng 2</span>Kim loại và phi kim tác dụng với oxygen, chlorine, sulfur – hoàn thành và cân bằng</div>
<div class="g2">{g2}</div>
<div class="q hoa" style="margin-top:4px"><div class="qh"><span class="qn" style="min-width:0">→</span><span>Xếp các oxide sau vào đúng nhóm: Na<sub>2</sub>O, MgO, SO<sub>2</sub>, CO<sub>2</sub>, P<sub>2</sub>O<sub>5</sub>, CaO.</span></div>
<table class="eq" style="margin-left:22px;width:calc(100% - 22px)"><tr><th style="width:50%">Oxide base (của kim loại)</th><th>Oxide acid (của phi kim)</th></tr><tr><td style="height:28px"></td><td></td></tr></table></div>

<div class="dang"><span>Dạng 3</span>Viết phương trình hóa học thực hiện chuỗi chuyển hóa (ghi rõ điều kiện)</div>
<div class="chain">a) Fe<sub>2</sub>O<sub>3</sub> <i>(1)</i>→ Fe <i>(2)</i>→ Cu <i>(3)</i>→ Ag</div>
<div class="chain">b) NaCl <i>(1)</i>→ Na <i>(2)</i>→ Na<sub>2</sub>O <i>(3)</i>→ NaOH</div>
<div class="chain">c) Al<sub>2</sub>O<sub>3</sub> <i>(1)</i>→ Al <i>(2)</i>→ AlCl<sub>3</sub></div>
{lines(5).replace('class="lines"','class="lines" style="margin-left:6px"')}

<div class="dang"><span>Dạng 4</span>Phản ứng có xảy ra không? Đánh dấu ✓ và viết phương trình nếu có</div>
<table class="eq"><tr><th>TT</th><th style="width:25%">Cặp chất</th><th style="width:20%">Xảy ra?</th><th>Phương trình hóa học (nếu có)</th></tr>{rows4}</table>
<div class="hint" style="margin-left:0">💡 Dựa vào dãy hoạt động hóa học: kim loại đứng <b>trước</b> đẩy được kim loại đứng <b>sau</b> ra khỏi dung dịch muối.</div>

<div class="dang"><span>Dạng 5</span>Điều chế kim loại bằng nhiều cách</div>
<div class="q hoa"><div class="qh"><span class="qn" style="min-width:24px">a)</span><span>Viết 2 phương trình điều chế Fe từ Fe<sub>2</sub>O<sub>3</sub> bằng hai chất khử khác nhau.</span></div>{lines(2).replace('class="lines"','class="lines" style="margin-left:30px"')}</div>
<div class="q hoa"><div class="qh"><span class="qn" style="min-width:24px">b)</span><span>Viết 2 phương trình điều chế Cu: một phương trình theo phương pháp nhiệt luyện (từ CuO), một phương trình theo phương pháp thủy luyện (từ CuSO<sub>4</sub>).</span></div>{lines(2).replace('class="lines"','class="lines" style="margin-left:30px"')}</div>

<div class="lv" style="background:var(--hoa-bg);color:var(--hoa)">B. BÀI TOÁN TÍNH THEO PHƯƠNG TRÌNH</div>
<div class="q hoa"><div class="qh"><span class="qn">Bài 1.</span><span>Ngâm 5,6 gam bột sắt vào dung dịch CuSO<sub>4</sub> dư, sắt phản ứng hết.</span></div>
<div class="steps">
  <div><span class="st">B1</span>Viết phương trình hóa học: <span class="dots w"></span><span class="dots w"></span></div>
  <div><span class="st">B2</span>Số mol sắt: n<sub>Fe</sub> = m : M = 5,6 : 56 = <span class="dots"></span> mol.</div>
  <div><span class="st">B3</span>Theo phương trình: n<sub>Cu</sub> = n<sub>CuSO₄ phản ứng</sub> = n<sub>Fe</sub> = <span class="dots"></span> mol.</div>
  <div><span class="st">B4</span>Khối lượng Cu tạo thành: m<sub>Cu</sub> = <span class="dots"></span> × 64 = <span class="dots"></span> g.</div>
  <div><span class="st">B5</span>Khối lượng CuSO<sub>4</sub> đã phản ứng (M = 160 g/mol): m = <span class="dots"></span> × 160 = <span class="dots"></span> g.</div>
</div></div>
<div class="q hoa"><div class="qh"><span class="qn">Bài 2.</span><span>Dùng khí CO dư khử hoàn toàn 32 gam Fe<sub>2</sub>O<sub>3</sub> ở nhiệt độ cao.</span></div>
<div class="steps">
  <div><span class="st">B1</span>Phương trình: Fe<sub>2</sub>O<sub>3</sub> + 3CO {t} 2Fe + 3CO<sub>2</sub></div>
  <div><span class="st">B2</span>n<sub>Fe₂O₃</sub> = 32 : 160 = <span class="dots"></span> mol.</div>
  <div><span class="st">B3</span>Theo phương trình: n<sub>Fe</sub> = 2 × n<sub>Fe₂O₃</sub> = <span class="dots"></span> mol ⇒ m<sub>Fe</sub> = <span class="dots"></span> × 56 = <span class="dots"></span> g.</div>
  <div><span class="st">B4</span>n<sub>CO₂</sub> = 3 × n<sub>Fe₂O₃</sub> = <span class="dots"></span> mol.</div>
</div>
<div class="hint">💡 Nhớ 3 bước vàng: <b>đổi ra mol → dựa vào tỉ lệ trong phương trình → đổi ra đại lượng cần tìm</b>.</div></div>
"""

def sec(icon, color, title, small, stars=True, h2style=''):
    s = '<div class="stars">Tự đánh giá: <span>☆☆☆</span></div>' if stars else ''
    return f'<div class="sec"><div class="num" style="background:{color}">{icon}</div><h2 style="{h2style}">{title}<small>{small}</small></h2>{s}</div>'

road = ''.join(f'<div class="stop"><div class="dot" style="background:{c}">{e}</div><b>{tt}</b>{d}</div>' for e, c, tt, d in [
    ('🌳', '#475569', 'Bước 1', 'Sơ đồ kiến thức'), ('🎯', '#2563eb', 'Bước 2', 'Trắc nghiệm 3 mức'),
    ('⚖️', 'var(--ds)', 'Bước 3', 'Đúng hay Sai?'), ('✍️', '#e11d48', 'Bước 4', 'Viết PTHH & bài toán'), ('🌏', 'var(--nghe)', 'Bước 5', 'Thực tiễn')])

hoa = f"""<!doctype html><html lang="vi"><head><meta charset="utf-8"><title>Phiếu học tập Hóa học 9 – Kim loại</title>
<style>{css}{extra}{extra3}.hero{{background:linear-gradient(120deg,#9a3412 0%,#ea580c 45%,#fbbf24 100%)}}</style></head><body>
<div class="hero"><div class="deco">⚗️</div><span class="tag">KHOA HỌC TỰ NHIÊN 9 · HÓA HỌC · PHIẾU HỌC TẬP</span>
<h1>Kim loại quanh em – Tách kim loại, hợp kim, kim loại và phi kim</h1><div class="en">Extracting Metals &amp; Alloys · Metals vs Non-metals</div>
<div class="lessons"><span class="h"><i>Hóa học</i> · Bài 20. Tách kim loại và việc sử dụng hợp kim</span><span class="h"><i>Hóa học</i> · Bài 21. Sự khác nhau cơ bản giữa phi kim và kim loại</span></div></div>
<div class="student"><div>Họ và tên:</div><div>Lớp: 9</div><div>Ngày: &nbsp;&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;&nbsp;&nbsp;/</div></div>
<div class="road">{road}</div>
<div class="data"><b>🧰 Dữ kiện:</b> Nguyên tử khối: H = 1; C = 12; O = 16; Al = 27; S = 32; Fe = 56; Cu = 64. Được dùng máy tính cầm tay.</div>

{sec('🌳','#475569','I. Sơ đồ kiến thức','Đọc từ gốc → nhánh → lá trước khi làm bài.',False)}
{tree_hoa}
{card_hoa2}

{sec('🎯','#2563eb','II. Trắc nghiệm','Làm lần lượt từ mức 1 đến mức 3, tô đáp án vào phiếu trả lời.')}
{mc_html}

{sec('⚖️','var(--ds)','III. Đúng hay Sai?','Đánh dấu ✓ vào ô Đ (đúng) hoặc S (sai) cho từng ý.')}
{ds_hoa}

{sec('✍️','#e11d48','IV. Tự luận','Phần A luyện viết phương trình hóa học, phần B luyện tính toán theo phương trình.')}
{tl}

{sec('🌏','var(--nghe)','V. Thực tiễn – Khoa học quanh em','Dùng kiến thức vừa học để giải thích những điều em gặp hằng ngày.',False,'color:var(--nghe)')}
<div class="feature ng">{tt_hoa}</div>
<div class="feature ng"><div style="font-weight:800;color:var(--nghe);margin-bottom:6px">🎯 Nghề nào dùng kiến thức hôm nay?</div>
<div class="careers" style="grid-template-columns:repeat(3,1fr)">{car_hoa}</div></div>
<div class="foot">🌟 <b>Hoàn thành!</b> Tô sao tự đánh giá ở mỗi phần. Phương trình em thấy khó nhất: ……………………………</div>
</body></html>"""
pathlib.Path('phieu_hoa.html').write_text(hoa)

# ---------- answer key ----------
def rowN(ans):
    n = len(ans)
    return '<table class="grid"><tr><th>Câu</th>' + ''.join(f'<th>{i}</th>' for i in range(1, n + 1)) + '</tr><tr><th>Đáp án</th>' + ''.join(f'<td>{a}</td>' for a in ans) + '</tr></table>'
old = pathlib.Path('dap_an.html').read_text()
ly_part = old.split('<div class="H"')[0]
hoa_key = f"""<div class="H" style="break-before:page"><h2 style="background:var(--hoa)">PHIẾU HÓA HỌC – BÀI 20, 21</h2>
<h3>II. Trắc nghiệm</h3>{rowN('ABCDBCDBCADABCAD')}
<p>Mức 1: câu 1–6 · Mức 2: câu 7–12 · Mức 3: câu 13–16.</p>
<p>Câu 13: n<sub>CuO</sub> = 0,1 mol ⇒ m<sub>Cu</sub> = 6,4 g. Câu 14: n<sub>Fe</sub> = n<sub>Cu</sub> = 0,1 mol ⇒ 5,6 g. Câu 15: n<sub>Fe₂O₃</sub> = 0,15 mol ⇒ n<sub>Fe</sub> = 0,3 mol ⇒ 16,8 g. Câu 16: 4Al + 3O<sub>2</sub> → 2Al<sub>2</sub>O<sub>3</sub>; n<sub>Al</sub> = 0,2 mol ⇒ n<sub>Al₂O₃</sub> = 0,1 mol ⇒ 10,2 g.</p>
<h3>III. Đúng – Sai</h3>
<p>Câu 1: a Đ; b Đ; c Đ; d S. &nbsp; Câu 2: a Đ; b S; c Đ; d S.</p>
<h3>IV-A. Viết phương trình hóa học</h3>
<p><b>Dạng 1.</b> (1) CuO + H<sub>2</sub> → Cu + H<sub>2</sub>O – nhiệt luyện; (2) Fe<sub>2</sub>O<sub>3</sub> + 3CO → 2Fe + 3CO<sub>2</sub> – nhiệt luyện; (3) Fe<sub>3</sub>O<sub>4</sub> + 4CO → 3Fe + 4CO<sub>2</sub> – nhiệt luyện; (4) ZnO + C → Zn + CO – nhiệt luyện; (5) Fe<sub>2</sub>O<sub>3</sub> + 2Al → Al<sub>2</sub>O<sub>3</sub> + 2Fe – nhiệt luyện (chất khử là kim loại mạnh); (6) 2NaCl → 2Na + Cl<sub>2</sub> – điện phân nóng chảy; (7) 2Al<sub>2</sub>O<sub>3</sub> → 4Al + 3O<sub>2</sub> – điện phân nóng chảy; (8) Fe + CuSO<sub>4</sub> → FeSO<sub>4</sub> + Cu – thủy luyện; (9) Zn + CuSO<sub>4</sub> → ZnSO<sub>4</sub> + Cu – thủy luyện; (10) Cu + 2AgNO<sub>3</sub> → Cu(NO<sub>3</sub>)<sub>2</sub> + 2Ag – thủy luyện.</p>
<p><b>Dạng 2.</b> a) 4Na + O<sub>2</sub> → 2Na<sub>2</sub>O; b) 2Mg + O<sub>2</sub> → 2MgO; c) 4Al + 3O<sub>2</sub> → 2Al<sub>2</sub>O<sub>3</sub>; d) 3Fe + 2O<sub>2</sub> → Fe<sub>3</sub>O<sub>4</sub>; e) S + O<sub>2</sub> → SO<sub>2</sub>; f) C + O<sub>2</sub> → CO<sub>2</sub>; g) 4P + 5O<sub>2</sub> → 2P<sub>2</sub>O<sub>5</sub>; h) 2Fe + 3Cl<sub>2</sub> → 2FeCl<sub>3</sub>; i) Fe + S → FeS; j) 2Na + Cl<sub>2</sub> → 2NaCl.<br>
Oxide base: Na<sub>2</sub>O, MgO, CaO. Oxide acid: SO<sub>2</sub>, CO<sub>2</sub>, P<sub>2</sub>O<sub>5</sub>.</p>
<p><b>Dạng 3.</b> a) (1) Fe<sub>2</sub>O<sub>3</sub> + 3CO → 2Fe + 3CO<sub>2</sub> (t°); (2) Fe + CuSO<sub>4</sub> → FeSO<sub>4</sub> + Cu; (3) Cu + 2AgNO<sub>3</sub> → Cu(NO<sub>3</sub>)<sub>2</sub> + 2Ag.<br>
b) (1) 2NaCl → 2Na + Cl<sub>2</sub> (đpnc); (2) 4Na + O<sub>2</sub> → 2Na<sub>2</sub>O; (3) Na<sub>2</sub>O + H<sub>2</sub>O → 2NaOH.<br>
c) (1) 2Al<sub>2</sub>O<sub>3</sub> → 4Al + 3O<sub>2</sub> (đpnc); (2) 2Al + 3Cl<sub>2</sub> → 2AlCl<sub>3</sub> (t°).<br><i>Chấp nhận chất phản ứng khác nếu đúng (ví dụ (1a) dùng H<sub>2</sub> hoặc Al; (2a) dùng CuCl<sub>2</sub>).</i></p>
<p><b>Dạng 4.</b> Xảy ra: (1) Fe + CuSO<sub>4</sub> → FeSO<sub>4</sub> + Cu; (3) Mg + FeSO<sub>4</sub> → MgSO<sub>4</sub> + Fe; (5) Cu + 2AgNO<sub>3</sub> → Cu(NO<sub>3</sub>)<sub>2</sub> + 2Ag; (6) CuO + H<sub>2</sub> → Cu + H<sub>2</sub>O; (8) Zn + FeSO<sub>4</sub> → ZnSO<sub>4</sub> + Fe.<br>
Không xảy ra: (2) Cu kém hoạt động hơn Fe; (4) Ag kém hoạt động hơn Cu; (7) Al hoạt động mạnh, Al<sub>2</sub>O<sub>3</sub> không bị CO khử.</p>
<p><b>Dạng 5.</b> a) Fe<sub>2</sub>O<sub>3</sub> + 3CO → 2Fe + 3CO<sub>2</sub>; Fe<sub>2</sub>O<sub>3</sub> + 3H<sub>2</sub> → 2Fe + 3H<sub>2</sub>O (hoặc dùng Al, C). b) CuO + H<sub>2</sub> → Cu + H<sub>2</sub>O (hoặc CO, C); Fe + CuSO<sub>4</sub> → FeSO<sub>4</sub> + Cu (hoặc Zn, Mg…).</p>
<h3>IV-B. Bài toán</h3>
<p><b>Bài 1.</b> Fe + CuSO<sub>4</sub> → FeSO<sub>4</sub> + Cu; n<sub>Fe</sub> = 0,1 mol; m<sub>Cu</sub> = 6,4 g; m<sub>CuSO₄</sub> = 16 g. &nbsp; <b>Bài 2.</b> n<sub>Fe₂O₃</sub> = 0,2 mol; n<sub>Fe</sub> = 0,4 mol ⇒ m<sub>Fe</sub> = 22,4 g; n<sub>CO₂</sub> = 0,6 mol.</p>
<h3>V. Thực tiễn (gợi ý)</h3>
<p><b>Câu 1.</b> Nhôm, inox dẫn nhiệt tốt nên đun nấu nhanh; inox chống gỉ, nhôm có lớp oxide bảo vệ. Nhựa, gỗ dẫn nhiệt kém nên cầm không bị bỏng.
<b>Câu 2.</b> Đồng dẫn điện rất tốt, dẻo, dễ kéo sợi; vỏ nhựa cách điện, tránh điện giật và chập điện.
<b>Câu 3.</b> Sắt thường dễ gỉ trong không khí ẩm, nước mưa; nhôm có lớp oxide bảo vệ, inox là hợp kim chống gỉ, bền và đẹp.
<b>Câu 4.</b> Chấp nhận mọi đề xuất hợp lí.</p></div>
</body></html>"""
pathlib.Path('dap_an.html').write_text(ly_part + hoa_key)
print('ok')
