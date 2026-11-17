import re, pathlib
src = pathlib.Path('/home/claude/hs/phieu_hs.html').read_text()
css = re.search(r'<style>(.*?)</style>', src, re.S).group(1)
duo = re.search(r'<div class="duo">(.*?)\n\n<!-- Tree Chemistry -->', src, re.S).group(1)
cards = re.findall(r'(<div class="card">.*?</div>\n  </div>)', duo, re.S)
card_ly, card_hoa = cards[0], cards[1]

extra = """
.steps{margin:3px 0 0 52px;font-size:9.8pt}
.steps div{margin:4px 0;display:flex;gap:6px;align-items:baseline;flex-wrap:wrap}
.steps .st{flex:none;font-size:7.6pt;font-weight:800;color:#fff;border-radius:4px;padding:0 5px}
.ly .steps .st{background:var(--ly)} .hoa .steps .st{background:var(--hoa)}
.dots{display:inline-block;border-bottom:1.2px dotted #64748b;min-width:70px;height:13px}
.dots.w{min-width:160px}
.hint{background:#fffbeb;border:1px dashed #f59e0b;border-radius:8px;padding:4px 9px;font-size:8.7pt;margin:5px 0 0 52px;color:#78350f}
.side{display:grid;grid-template-columns:1.25fr 1fr;gap:10px;align-items:start;break-inside:avoid}
.lines div{height:21px}
.road .stop{flex:1}
"""

def mcq(n, cls, stem, opts, four=True):
    o = ''.join(f'<span><b>{l}.</b>{t}</span>' for l, t in zip('ABCD', opts))
    return f'<div class="q {cls}"><div class="qh"><span class="qn">Câu {n}.</span><span>{stem}</span></div><div class="opts{" four" if four else ""}">{o}</div></div>'

def ds(n, cls, stem, items):
    it = ''.join(f'<div><span>{l}) {t}</span><span class="box2"><i>Đ</i><i>S</i></span></div>' for l, t in zip('abcd', items))
    return f'<div class="q {cls} ds-q"><div class="qh"><span class="qn">Câu {n}.</span><span>{stem}</span></div><div class="items ds-items">{it}</div></div>'

def lines(n): return '<div class="lines">' + '<div></div>' * n + '</div>'

def bubbles(n):
    cells = ''.join(f'<div><b>{i}</b>' + ''.join(f'<span class="o">{l}</span>' for l in 'ABCD') + '</div>' for i in range(1, n + 1))
    return f'<div class="sheet"><h6>✏️ PHIẾU TRẢ LỜI – tô kín đáp án em chọn</h6><div class="bub" style="grid-template-columns:repeat(4,1fr)">{cells}</div></div>'

def page(title, tag, h1, en, lesson, grad, color, data, tree, card, mc, dsq, tl, tt, careers):
    road = ''.join(f'<div class="stop"><div class="dot" style="background:{c}">{e}</div><b>{t}</b>{d}</div>' for e, c, t, d in [
        ('🌳', '#475569', 'Bước 1', 'Sơ đồ kiến thức'), ('🎯', '#2563eb', 'Bước 2', 'Trắc nghiệm'),
        ('⚖️', 'var(--ds)', 'Bước 3', 'Đúng hay Sai?'), ('✍️', '#e11d48', 'Bước 4', 'Tự luận'), ('🌏', 'var(--nghe)', 'Bước 5', 'Thực tiễn')])
    return f"""<!doctype html><html lang="vi"><head><meta charset="utf-8"><title>{title}</title><style>{css}{extra}
.hero{{background:{grad}}}</style></head><body>
<div class="hero"><div class="deco">{'💡' if 'Vật lí' in tag else '⚗️'}</div><span class="tag">{tag}</span><h1>{h1}</h1><div class="en">{en}</div>
<div class="lessons">{lesson}</div></div>
<div class="student"><div>Họ và tên:</div><div>Lớp: 9</div><div>Ngày: &nbsp;&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;&nbsp;&nbsp;/</div></div>
<div class="road">{road}</div>
<div class="data"><b>🧰 Dữ kiện:</b> {data}</div>

<div class="sec"><div class="num" style="background:#475569">🌳</div><h2>I. Sơ đồ kiến thức<small>Đọc từ gốc → nhánh → lá trước khi làm bài.</small></h2></div>
{tree}
{card}

<div class="sec"><div class="num" style="background:#2563eb">🎯</div><h2>II. Trắc nghiệm<small>Chọn một đáp án đúng và tô vào phiếu trả lời.</small></h2><div class="stars">Tự đánh giá: <span>☆☆☆</span></div></div>
{mc}
{bubbles(8)}

<div class="sec"><div class="num" style="background:var(--ds)">⚖️</div><h2>III. Đúng hay Sai?<small>Đánh dấu ✓ vào ô Đ (đúng) hoặc S (sai) cho từng ý.</small></h2><div class="stars">Tự đánh giá: <span>☆☆☆</span></div></div>
{dsq}

<div class="sec"><div class="num" style="background:#e11d48">✍️</div><h2>IV. Tự luận<small>Làm theo từng bước gợi ý, điền vào chỗ trống.</small></h2><div class="stars">Tự đánh giá: <span>☆☆☆</span></div></div>
{tl}

<div class="sec"><div class="num" style="background:var(--nghe)">🌏</div><h2 style="color:var(--nghe)">V. Thực tiễn – Khoa học quanh em<small>Dùng kiến thức vừa học để giải thích những điều em gặp hằng ngày.</small></h2></div>
<div class="feature ng">{tt}</div>
<div class="feature ng"><div style="font-weight:800;color:var(--nghe);margin-bottom:6px">🎯 Nghề nào dùng kiến thức hôm nay?</div>
<div class="careers" style="grid-template-columns:repeat(3,1fr)">{careers}</div></div>
<div class="foot">🌟 <b>Hoàn thành!</b> Tô sao tự đánh giá ở mỗi phần. Câu em thấy khó nhất: ……………………………</div>
</body></html>"""

# ================= VẬT LÍ =================
tree_ly = """<div class="tree ly"><span class="root">💡 KHÚC XẠ ÁNH SÁNG</span>
  <div class="branches" style="grid-template-columns:repeat(3,1fr);--edge:16.66%">
    <div class="br"><h4 style="background:#0b63c5">① Hiện tượng là gì?</h4>
      <div class="leaf">Tia sáng truyền <b>xiên</b> từ môi trường trong suốt này sang môi trường trong suốt khác thì bị <b>gãy khúc</b> tại mặt phân cách.</div>
      <div class="leaf">Tia tới <b>vuông góc</b> với mặt phân cách → truyền <b>thẳng</b>.</div>
      <div class="leaf">Ví dụ: chiếc thìa trong cốc nước trông như <b>bị gãy</b>; đáy bể trông <b>nông hơn</b>.</div>
    </div>
    <div class="br"><h4 style="background:#1d74d6">② Công thức cần nhớ</h4>
      <div class="leaf">Định luật khúc xạ: <span class="f">n<sub>1</sub>sin i = n<sub>2</sub>sin r</span></div>
      <div class="leaf">Chiết suất: <span class="f">n = c / v</span></div>
      <div class="leaf">Chân không n = 1; không khí ≈ 1; nước ≈ 1,33; thủy tinh ≈ 1,5.</div>
      <div class="leaf">n càng lớn → ánh sáng đi càng <b>chậm</b>.</div>
    </div>
    <div class="br"><h4 style="background:#2f86e6">③ Tia sáng lệch về đâu?</h4>
      <div class="leaf">Góc i, r đo với <b>pháp tuyến</b> (không đo với mặt phân cách).</div>
      <div class="leaf">Sang môi trường n <b>lớn hơn</b> (không khí → nước): <b>r &lt; i</b>, lệch <b>gần</b> pháp tuyến.</div>
      <div class="leaf">Sang môi trường n <b>nhỏ hơn</b> (nước → không khí): <b>r &gt; i</b>, lệch <b>xa</b> pháp tuyến.</div>
    </div>
  </div></div>"""
card_ly2 = card_ly.replace('<div class="card">', '<div class="card keep" style="max-width:62%;margin:0 auto">')

mc_ly = '\n'.join([
 mcq(1,'ly','Hiện tượng khúc xạ ánh sáng là hiện tượng tia sáng',['bị hắt trở lại môi trường cũ.','bị gãy khúc tại mặt phân cách khi truyền xiên qua hai môi trường trong suốt.','luôn truyền thẳng.','bị hấp thụ hoàn toàn.'],False),
 mcq(2,'ly','Khi tia tới vuông góc với mặt phân cách giữa hai môi trường thì',['tia sáng truyền thẳng, không đổi hướng.','góc khúc xạ bằng 90°.','không có tia khúc xạ.','tia sáng bị hắt lại hoàn toàn.'],False),
 mcq(3,'ly','Công thức tính chiết suất tuyệt đối của một môi trường là',['n = v/c.','n = c·v.','n = c/v.','n = c − v.']),
 mcq(4,'ly','Chiếu tia sáng xiên góc từ không khí vào thủy tinh. Góc khúc xạ',['lớn hơn góc tới.','bằng góc tới.','bằng 90°.','nhỏ hơn góc tới.']),
 mcq(5,'ly','Hiện tượng nào sau đây liên quan đến khúc xạ ánh sáng?',['Nhìn thấy ảnh của mình trong gương phẳng.','Chiếc thìa cắm trong cốc nước trông như bị gãy.','Bóng tối phía sau vật cản sáng.','Nghe thấy tiếng vang trong hang.'],False),
 mcq(6,'ly','Nước có chiết suất 4/3. Tốc độ ánh sáng trong nước là',['4·10<sup>8</sup> m/s.','3·10<sup>8</sup> m/s.','2,25·10<sup>8</sup> m/s.','1,33·10<sup>8</sup> m/s.']),
 mcq(7,'ly','Góc khúc xạ là góc tạo bởi',['tia khúc xạ và pháp tuyến tại điểm tới.','tia khúc xạ và mặt phân cách.','tia tới và tia khúc xạ.','tia tới và pháp tuyến tại điểm tới.'],False),
 mcq(8,'ly','Chiếu tia sáng từ nước ra không khí với góc tới 30°. Kết luận đúng là',['góc khúc xạ nhỏ hơn 30°.','góc khúc xạ bằng 30°.','góc khúc xạ lớn hơn 30°.','tia sáng truyền thẳng.'],False),
])
ds_ly = ds(1,'ly','Về hiện tượng khúc xạ ánh sáng:',['Ánh sáng truyền từ không khí vào nước thì tia khúc xạ lệch lại gần pháp tuyến.','Góc tới là góc tạo bởi tia tới và mặt phân cách.','Tốc độ ánh sáng trong nước nhỏ hơn trong không khí.','Chiết suất của mọi môi trường đều nhỏ hơn 1.']) + \
        ds(2,'ly','Chiếu tia sáng từ không khí vào thủy tinh có chiết suất 1,5 với góc tới 30°.',['sin r = 1/3.','Góc khúc xạ r ≈ 19,5°.','Góc khúc xạ lớn hơn góc tới.','Tốc độ ánh sáng trong thủy tinh là 2·10<sup>8</sup> m/s.'])
tl_ly = """
<div class="q ly"><div class="qh"><span class="qn">Bài 1.</span><span>Chiếu một tia sáng từ không khí (n<sub>1</sub> = 1) vào nước (n<sub>2</sub> = 4/3) với góc tới i, biết sin i = 0,8.</span></div>
<div class="steps">
  <div><span class="st">B1</span>Viết định luật khúc xạ: <span class="dots w"></span></div>
  <div><span class="st">B2</span>Suy ra: sin r = (n<sub>1</sub> · sin i) : n<sub>2</sub> = (1 · 0,8) : (4/3) = <span class="dots"></span></div>
  <div><span class="st">B3</span>Dùng máy tính (SHIFT sin): i ≈ <span class="dots"></span>°; &nbsp; r ≈ <span class="dots"></span>° (làm tròn đến độ).</div>
  <div><span class="st">B4</span>So sánh: r <span class="dots"></span> i, vì ánh sáng đi từ môi trường có chiết suất <span class="dots"></span> sang môi trường có chiết suất <span class="dots"></span>.</div>
</div></div>
<div class="q ly"><div class="qh"><span class="qn">Bài 2.</span><span>Thủy tinh có chiết suất n = 1,5.</span></div>
<div class="steps">
  <div><span class="st">B1</span>Từ n = c/v suy ra v = <span class="dots"></span></div>
  <div><span class="st">B2</span>Thay số: v = 3·10<sup>8</sup> : 1,5 = <span class="dots w"></span> m/s.</div>
  <div><span class="st">B3</span>Khi ánh sáng đi từ không khí vào thủy tinh, tốc độ ánh sáng <span class="dots"></span> (tăng / giảm).</div>
</div></div>
<div class="q ly"><div class="qh"><span class="qn">Bài 3.</span><span>Chiếu tia sáng từ không khí vào một chất lỏng với góc tới 45° thì góc khúc xạ là 30°.</span></div>
<div class="steps">
  <div><span class="st">B1</span>Áp dụng định luật khúc xạ với n<sub>1</sub> = 1: 1 · sin 45° = n · sin 30° ⇒ n = <span class="dots"></span> : <span class="dots"></span></div>
  <div><span class="st">B2</span>Dùng máy tính: n ≈ <span class="dots"></span> (làm tròn đến hai chữ số thập phân).</div>
  <div><span class="st">B3</span>Tốc độ ánh sáng trong chất lỏng: v = c : n ≈ <span class="dots w"></span> m/s.</div>
</div>
<div class="hint">💡 Nhớ: trước khi bấm máy, kiểm tra máy tính đang ở chế độ <b>độ (D)</b>.</div></div>
"""
tt_ly = """
<div class="q ng"><div class="qh"><span class="qn">Câu 1.</span><span><b>🏊 Bể bơi "đánh lừa" mắt.</b> Nhìn từ trên bờ, đáy bể bơi trông nông hơn thực tế. Một bể sâu h = 1,2 m, nếu nhìn gần vuông góc thì đáy bể trông như chỉ sâu khoảng h′ = h : n. Hãy tính h′ và cho biết vì sao không nên nhảy xuống bể khi chỉ ước lượng độ sâu bằng mắt.</span></div>""" + lines(3) + """</div>
<div class="q ng"><div class="qh"><span class="qn">Câu 2.</span><span><b>🥄 Chiếc thìa "gãy".</b> Đặt một chiếc thìa nghiêng trong cốc nước, nhìn từ bên cạnh thấy thìa như bị gãy tại mặt nước. Thìa có bị gãy thật không? Giải thích.</span></div>""" + lines(2) + """</div>
<div class="q ng" style="margin-bottom:0"><div class="qh"><span class="qn">Câu 3.</span><span><b>🐟 Bắt cá bằng xiên.</b> Người đánh cá có kinh nghiệm luôn đâm xiên <b>thấp hơn</b> chỗ mình nhìn thấy con cá. Vì sao?</span></div>""" + lines(2) + """</div>"""
car_ly = """<div class="career"><b>👓 Kĩ thuật viên khúc xạ nhãn khoa</b>Đo mắt, cắt kính cận, kính viễn cho mọi người.</div>
<div class="career"><b>📷 Kĩ sư quang học</b>Thiết kế thấu kính camera điện thoại, máy ảnh, kính hiển vi.</div>
<div class="career"><b>🌐 Kĩ thuật viên cáp quang</b>Lắp đặt đường truyền Internet tốc độ cao bằng sợi quang.</div>"""

ly = page('Phiếu học tập Vật lí 9 cơ bản – Khúc xạ ánh sáng', 'KHOA HỌC TỰ NHIÊN 9 · VẬT LÍ · PHIẾU HỌC TẬP CƠ BẢN',
          'Ánh sáng đổi hướng – Khúc xạ ánh sáng', 'Refraction of Light',
          '<span class="l"><i>Vật lí</i> · Bài 5. Khúc xạ ánh sáng</span>',
          'linear-gradient(120deg,#0b4fa0 0%,#0b63c5 40%,#38bdf8 100%)', 'var(--ly)',
          'c = 3·10<sup>8</sup> m/s; chiết suất không khí ≈ 1; n<sub>nước</sub> = 4/3. Được dùng máy tính cầm tay.',
          tree_ly, card_ly2, mc_ly, ds_ly, tl_ly, tt_ly, car_ly)
pathlib.Path('phieu_ly.html').write_text(ly)

# ================= HÓA HỌC =================
tree_hoa = """<div class="tree hoa"><span class="root">⚗️ KIM LOẠI: TÁCH – HỢP KIM – SO SÁNH VỚI PHI KIM</span>
  <div class="branches" style="grid-template-columns:repeat(3,1fr);--edge:16.66%">
    <div class="br"><h4 style="background:#c2410c">① Tách kim loại</h4>
      <div class="leaf"><b>⚡ Điện phân nóng chảy</b> – cho kim loại mạnh (K → Al). Ví dụ: NaCl nóng chảy → Na; Al<sub>2</sub>O<sub>3</sub> nóng chảy → Al.</div>
      <div class="leaf"><b>🔥 Nhiệt luyện</b> – khử oxide bằng C, CO, H<sub>2</sub> ở nhiệt độ cao. Ví dụ: CuO + H<sub>2</sub> → Cu + H<sub>2</sub>O.</div>
      <div class="leaf"><b>💧 Thủy luyện</b> – kim loại mạnh đẩy kim loại yếu khỏi dung dịch muối. Ví dụ: Fe + CuSO<sub>4</sub> → FeSO<sub>4</sub> + Cu.</div>
    </div>
    <div class="br"><h4 style="background:#d9541a">② Hợp kim</h4>
      <div class="leaf">Là vật liệu gồm <b>một kim loại cơ bản</b> và thêm một số nguyên tố khác.</div>
      <div class="leaf"><b>Gang</b>: C &gt; 2% – cứng, giòn. <b>Thép</b>: C &lt; 2% – cứng, bền.</div>
      <div class="leaf"><b>Inox</b>: chống gỉ. <b>Dural</b> (nhôm): nhẹ, bền – làm máy bay. <b>Đồng thau</b>: Cu – Zn.</div>
      <div class="leaf">Hợp kim thường <b>cứng, bền</b> hơn kim loại nguyên chất.</div>
    </div>
    <div class="br"><h4 style="background:#e8692b">③ Kim loại hay phi kim?</h4>
      <div class="leaf"><b>Kim loại</b>: có ánh kim, dẫn điện, dẫn nhiệt tốt, dẻo. Hầu hết ở thể rắn (trừ Hg lỏng).</div>
      <div class="leaf"><b>Phi kim</b>: thường dẫn điện, dẫn nhiệt kém; rắn (S, C), lỏng (Br<sub>2</sub>), khí (O<sub>2</sub>, Cl<sub>2</sub>).</div>
      <div class="leaf">Đặc biệt: <b>than chì</b> dẫn điện; <b>silicon</b> là chất bán dẫn.</div>
    </div>
  </div></div>"""
card_hoa2 = card_hoa.replace('<div class="card">', '<div class="card keep" style="max-width:78%;margin:0 auto">')

mc_hoa = '\n'.join([
 mcq(1,'hoa','Trong công nghiệp, kim loại Na được điều chế bằng cách',['điện phân NaCl nóng chảy.','điện phân dung dịch NaCl.','dùng CO khử Na<sub>2</sub>O.','cho Fe tác dụng với dung dịch NaCl.'],False),
 mcq(2,'hoa','Phản ứng nào sau đây thuộc phương pháp thủy luyện?',['CuO + H<sub>2</sub> → Cu + H<sub>2</sub>O (t°)','2Al<sub>2</sub>O<sub>3</sub> → 4Al + 3O<sub>2</sub> (điện phân nóng chảy)','Fe<sub>2</sub>O<sub>3</sub> + 3CO → 2Fe + 3CO<sub>2</sub> (t°)','Fe + CuSO<sub>4</sub> → FeSO<sub>4</sub> + Cu'],False),
 mcq(3,'hoa','Thép là hợp kim của sắt với carbon, trong đó hàm lượng carbon',['lớn hơn 2%.','nhỏ hơn 2%.','bằng 10%.','lớn hơn 50%.']),
 mcq(4,'hoa','Kim loại ở thể lỏng ở điều kiện thường là',['Fe.','Cu.','Hg.','Al.']),
 mcq(5,'hoa','Phi kim dẫn điện được, dùng làm điện cực và ruột bút chì là',['sulfur.','phosphorus.','iodine.','than chì (graphite).']),
 mcq(6,'hoa','Khử hoàn toàn 8 gam CuO bằng khí H<sub>2</sub> ở nhiệt độ cao. Khối lượng Cu thu được là',['3,2 g.','6,4 g.','8,0 g.','12,8 g.']),
 mcq(7,'hoa','Kim loại nào sau đây được điều chế bằng phương pháp nhiệt luyện (dùng CO khử oxide)?',['Na.','Fe.','K.','Mg.']),
 mcq(8,'hoa','Hợp kim nhẹ, bền, được dùng để chế tạo vỏ máy bay là',['gang.','đồng thau.','dural.','thép.']),
])
ds_hoa = ds(1,'hoa','Về tách kim loại và hợp kim:',['Có thể thu được Cu bằng cách cho Fe vào dung dịch CuSO<sub>4</sub>.','Nhôm được sản xuất bằng cách điện phân nóng chảy Al<sub>2</sub>O<sub>3</sub>.','Hợp kim thường cứng hơn kim loại nguyên chất tạo nên nó.','Inox dễ bị gỉ hơn sắt thường.']) + \
         ds(2,'hoa','Về kim loại và phi kim:',['Kim loại có ánh kim, dẫn điện và dẫn nhiệt tốt.','Ở điều kiện thường, mọi phi kim đều ở thể khí.','Bromine là phi kim ở thể lỏng.','Sulfur dẫn điện tốt nên được dùng làm dây điện.'])
tl_hoa = """
<div class="q hoa"><div class="qh"><span class="qn">Bài 1.</span><span>Hoàn thành các phương trình hóa học và ghi tên phương pháp tách kim loại (điện phân nóng chảy / nhiệt luyện / thủy luyện).</span></div>
<table class="grid" style="margin:4px 0 0 52px;width:calc(100% - 52px)">
<tr><th style="width:58%">Phương trình hóa học</th><th>Phương pháp</th></tr>
<tr><td style="text-align:left;height:26px">a) CuO + H<sub>2</sub> →<sup>t°</sup> ………… + …………</td><td></td></tr>
<tr><td style="text-align:left;height:26px">b) Fe<sub>2</sub>O<sub>3</sub> + …CO →<sup>t°</sup> …Fe + ………………</td><td></td></tr>
<tr><td style="text-align:left;height:26px">c) Fe + CuSO<sub>4</sub> → ………… + …………</td><td></td></tr>
<tr><td style="text-align:left;height:26px">d) …Al<sub>2</sub>O<sub>3</sub> →<sup>đpnc</sup> …Al + …O<sub>2</sub></td><td></td></tr>
</table></div>
<div class="q hoa"><div class="qh"><span class="qn">Bài 2.</span><span>Ngâm 5,6 gam bột sắt vào dung dịch CuSO<sub>4</sub> dư, sắt phản ứng hết.</span></div>
<div class="steps">
  <div><span class="st">B1</span>Viết phương trình hóa học: <span class="dots w"></span><span class="dots w"></span></div>
  <div><span class="st">B2</span>Số mol sắt: n<sub>Fe</sub> = m : M = 5,6 : 56 = <span class="dots"></span> mol.</div>
  <div><span class="st">B3</span>Theo phương trình: n<sub>Cu</sub> = n<sub>CuSO₄ phản ứng</sub> = n<sub>Fe</sub> = <span class="dots"></span> mol.</div>
  <div><span class="st">B4</span>Khối lượng Cu tạo thành: m<sub>Cu</sub> = <span class="dots"></span> × 64 = <span class="dots"></span> g.</div>
  <div><span class="st">B5</span>Khối lượng CuSO<sub>4</sub> đã phản ứng (M = 160 g/mol): m = <span class="dots"></span> × 160 = <span class="dots"></span> g.</div>
</div></div>
<div class="q hoa"><div class="qh"><span class="qn">Bài 3.</span><span>Dùng khí CO dư khử hoàn toàn 32 gam Fe<sub>2</sub>O<sub>3</sub> ở nhiệt độ cao.</span></div>
<div class="steps">
  <div><span class="st">B1</span>Phương trình: Fe<sub>2</sub>O<sub>3</sub> + 3CO →<sup>t°</sup> 2Fe + 3CO<sub>2</sub></div>
  <div><span class="st">B2</span>n<sub>Fe₂O₃</sub> = 32 : 160 = <span class="dots"></span> mol.</div>
  <div><span class="st">B3</span>Theo phương trình: n<sub>Fe</sub> = 2 × n<sub>Fe₂O₃</sub> = <span class="dots"></span> mol ⇒ m<sub>Fe</sub> = <span class="dots"></span> × 56 = <span class="dots"></span> g.</div>
  <div><span class="st">B4</span>n<sub>CO₂</sub> = 3 × n<sub>Fe₂O₃</sub> = <span class="dots"></span> mol.</div>
</div>
<div class="hint">💡 Nhớ 3 bước vàng: <b>đổi ra mol → dựa vào tỉ lệ trong phương trình → đổi ra đại lượng cần tìm</b>.</div></div>
"""
tt_hoa = """
<div class="q ng"><div class="qh"><span class="qn">Câu 1.</span><span><b>🍳 Đồ dùng trong bếp.</b> Vì sao xoong nồi thường làm bằng nhôm hoặc inox, nhưng tay cầm lại làm bằng nhựa hoặc gỗ?</span></div>""" + lines(2) + """</div>
<div class="q ng"><div class="qh"><span class="qn">Câu 2.</span><span><b>🔌 Dây điện trong nhà.</b> Vì sao lõi dây điện làm bằng đồng, còn bên ngoài được bọc nhựa?</span></div>""" + lines(2) + """</div>
<div class="q ng"><div class="qh"><span class="qn">Câu 3.</span><span><b>🚪 Chọn vật liệu làm cửa.</b> Cửa sổ, lan can ngoài trời thường làm bằng nhôm hoặc inox thay vì sắt thường. Hãy giải thích.</span></div>""" + lines(2) + """</div>
<div class="q ng" style="margin-bottom:0"><div class="qh"><span class="qn">Câu 4.</span><span><b>♻️ Tái chế vỏ lon.</b> Tái chế nhôm từ vỏ lon tiết kiệm tới khoảng 95% năng lượng so với sản xuất nhôm mới từ quặng. Em hãy đề xuất một việc làm cụ thể ở lớp hoặc ở nhà để góp phần tái chế kim loại.</span></div>""" + lines(2) + """</div>"""
car_hoa = """<div class="career"><b>🏭 Kĩ sư luyện kim</b>Sản xuất gang, thép, nhôm trong các nhà máy luyện kim.</div>
<div class="career"><b>🔧 Thợ cơ khí – hàn</b>Gia công thép, inox, nhôm làm cửa, khung nhà, chi tiết máy.</div>
<div class="career"><b>♻️ Kĩ thuật viên tái chế</b>Phân loại, thu hồi kim loại từ phế liệu, bảo vệ môi trường.</div>"""

hoa = page('Phiếu học tập Hóa học 9 cơ bản – Kim loại', 'KHOA HỌC TỰ NHIÊN 9 · HÓA HỌC · PHIẾU HỌC TẬP CƠ BẢN',
           'Kim loại quanh em – Tách kim loại, hợp kim, kim loại và phi kim', 'Extracting Metals &amp; Alloys · Metals vs Non-metals',
           '<span class="h"><i>Hóa học</i> · Bài 20. Tách kim loại và việc sử dụng hợp kim</span><span class="h"><i>Hóa học</i> · Bài 21. Sự khác nhau cơ bản giữa phi kim và kim loại</span>',
           'linear-gradient(120deg,#9a3412 0%,#ea580c 45%,#fbbf24 100%)', 'var(--hoa)',
           'Nguyên tử khối: H = 1; C = 12; O = 16; S = 32; Fe = 56; Cu = 64. Được dùng máy tính cầm tay.',
           tree_hoa, card_hoa2, mc_hoa, ds_hoa, tl_hoa, tt_hoa, car_hoa)
pathlib.Path('phieu_hoa.html').write_text(hoa)

# ================= ĐÁP ÁN =================
def row(ans): return '<table class="grid"><tr><th>Câu</th>' + ''.join(f'<th>{i}</th>' for i in range(1, 9)) + '</tr><tr><th>Đáp án</th>' + ''.join(f'<td>{a}</td>' for a in ans) + '</td></tr></table>'
key = f"""<!doctype html><html lang="vi"><head><meta charset="utf-8"><title>Đáp án phiếu cơ bản</title>
<style>{css}
.k h3{{font-size:11pt;margin:10px 0 4px}} .k p{{font-size:9.6pt;margin:3px 0}}
.k .L h3{{color:var(--ly)}} .k .H h3{{color:var(--hoa)}}
.k h2{{font-size:13pt;margin:14px 0 4px;padding:4px 10px;border-radius:6px;color:#fff}}
</style></head><body class="k">
<div class="hero" style="background:linear-gradient(120deg,#334155,#64748b)"><span class="tag">DÀNH CHO GIÁO VIÊN</span><h1 style="font-size:16pt">Đáp án – Phiếu học tập cơ bản KHTN 9</h1><div class="en">Vật lí: Bài 5 · Hóa học: Bài 20, 21</div></div>
<div class="L"><h2 style="background:var(--ly)">PHIẾU VẬT LÍ – BÀI 5. KHÚC XẠ ÁNH SÁNG</h2>
<h3>II. Trắc nghiệm</h3>{row('BACDBCAC')}
<p>Câu 6: v = c/n = 3·10<sup>8</sup> : (4/3) = 2,25·10<sup>8</sup> m/s. Câu 8: từ nước ra không khí (sang môi trường chiết suất nhỏ hơn) ⇒ r &gt; i (r ≈ 41,8°).</p>
<h3>III. Đúng – Sai</h3>
<p>Câu 1: a Đ; b S (đo với pháp tuyến); c Đ; d S (n ≥ 1). &nbsp; Câu 2: a Đ (sin r = sin 30° : 1,5 = 1/3); b Đ; c S (r &lt; i); d Đ.</p>
<h3>IV. Tự luận</h3>
<p><b>Bài 1.</b> n<sub>1</sub>sin i = n<sub>2</sub>sin r; sin r = 0,8 : (4/3) = 0,6; i ≈ 53°; r ≈ 37°; r &lt; i vì ánh sáng đi từ môi trường chiết suất nhỏ (không khí) sang môi trường chiết suất lớn (nước).</p>
<p><b>Bài 2.</b> v = c/n = 3·10<sup>8</sup> : 1,5 = 2·10<sup>8</sup> m/s; tốc độ giảm.</p>
<p><b>Bài 3.</b> n = sin 45° : sin 30° ≈ 1,41; v = c : n ≈ 2,12·10<sup>8</sup> m/s.</p>
<h3>V. Thực tiễn (gợi ý)</h3>
<p><b>Câu 1.</b> h′ = 1,2 : (4/3) = 0,9 m. Ánh sáng từ đáy bể khúc xạ ra không khí bị lệch xa pháp tuyến, mắt thấy ảnh đáy bể cao hơn thực tế; nước sâu hơn mình tưởng nên dễ bị đuối nước.</p>
<p><b>Câu 2.</b> Thìa không gãy. Ánh sáng từ phần thìa dưới nước bị khúc xạ khi ra không khí, mắt thấy ảnh của phần đó ở vị trí cao hơn nên thìa trông như gãy tại mặt nước.</p>
<p><b>Câu 3.</b> Do khúc xạ, ảnh của con cá mà người nhìn thấy nằm cao hơn vị trí thật của cá, nên phải đâm thấp hơn chỗ nhìn thấy.</p></div>
<div class="H"><h2 style="background:var(--hoa)">PHIẾU HÓA HỌC – BÀI 20, 21</h2>
<h3>II. Trắc nghiệm</h3>{row('ADBCDBBC')}
<p>Câu 6: n<sub>CuO</sub> = 8 : 80 = 0,1 mol ⇒ m<sub>Cu</sub> = 6,4 g. Câu 7: Fe hoạt động trung bình, oxide sắt bị CO khử; Na, K, Mg hoạt động mạnh phải điện phân nóng chảy.</p>
<h3>III. Đúng – Sai</h3>
<p>Câu 1: a Đ; b Đ; c Đ; d S. &nbsp; Câu 2: a Đ; b S; c Đ; d S.</p>
<h3>IV. Tự luận</h3>
<p><b>Bài 1.</b> a) CuO + H<sub>2</sub> → Cu + H<sub>2</sub>O – nhiệt luyện; b) Fe<sub>2</sub>O<sub>3</sub> + 3CO → 2Fe + 3CO<sub>2</sub> – nhiệt luyện; c) Fe + CuSO<sub>4</sub> → FeSO<sub>4</sub> + Cu – thủy luyện; d) 2Al<sub>2</sub>O<sub>3</sub> → 4Al + 3O<sub>2</sub> – điện phân nóng chảy.</p>
<p><b>Bài 2.</b> Fe + CuSO<sub>4</sub> → FeSO<sub>4</sub> + Cu; n<sub>Fe</sub> = 0,1 mol; n<sub>Cu</sub> = n<sub>CuSO₄</sub> = 0,1 mol; m<sub>Cu</sub> = 6,4 g; m<sub>CuSO₄</sub> = 16 g.</p>
<p><b>Bài 3.</b> n<sub>Fe₂O₃</sub> = 0,2 mol; n<sub>Fe</sub> = 0,4 mol ⇒ m<sub>Fe</sub> = 22,4 g; n<sub>CO₂</sub> = 0,6 mol.</p>
<h3>V. Thực tiễn (gợi ý)</h3>
<p><b>Câu 1.</b> Nhôm, inox dẫn nhiệt tốt nên đun nấu nhanh; inox chống gỉ, nhôm có lớp oxide bảo vệ. Nhựa, gỗ dẫn nhiệt kém nên cầm không bị bỏng.</p>
<p><b>Câu 2.</b> Đồng dẫn điện rất tốt, dẻo, dễ kéo sợi; vỏ nhựa là chất cách điện, giúp an toàn, tránh điện giật và chập điện.</p>
<p><b>Câu 3.</b> Sắt thường dễ bị gỉ khi tiếp xúc với không khí ẩm, nước mưa; nhôm có lớp oxide bảo vệ, inox là hợp kim chống gỉ, lại bền và đẹp.</p>
<p><b>Câu 4.</b> Chấp nhận mọi đề xuất hợp lí: thùng thu gom vỏ lon ở lớp, phân loại rác tại nhà, bán phế liệu gây quỹ lớp…</p></div>
</body></html>"""
pathlib.Path('dap_an.html').write_text(key)
print(len(cards))
