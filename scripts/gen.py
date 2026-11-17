import re, pathlib
src = pathlib.Path('/home/claude/hs/phieu_hs.html').read_text()
css = re.search(r'<style>(.*?)</style>', src, re.S).group(1)
duo = re.search(r'(<div class="duo">.*?)\n\n<!-- Tree Chemistry -->', src, re.S).group(1)

extra = """
.hero{background:linear-gradient(120deg,#0e7490 0%,#22c55e 55%,#f59e0b 100%)}
.hint{background:#fffbeb;border:1px dashed #f59e0b;border-radius:8px;padding:4px 9px;font-size:8.6pt;margin:4px 0 0 52px;color:#78350f}
.steps{margin:3px 0 0 52px;font-size:9.6pt}
.steps div{margin:3px 0;display:flex;gap:6px;align-items:baseline}
.steps .st{flex:none;font-size:7.6pt;font-weight:800;color:#fff;background:#0e7490;border-radius:4px;padding:0 5px}
.dots{display:inline-block;border-bottom:1.2px dotted #64748b;min-width:70px;height:13px}
.dots.w{min-width:150px}
.bank{display:flex;flex-wrap:wrap;gap:6px;margin:6px 0}
.bank span{background:#fff;border:1.5px solid #0e7490;color:#0e7490;border-radius:20px;padding:1px 10px;font-weight:650;font-size:9pt}
.fill{font-size:10pt;line-height:2.0}
.fill .bl{display:inline-block;border-bottom:1.3px dotted #475569;min-width:95px;text-align:center;color:#94a3b8;font-size:8pt}
.match{display:grid;grid-template-columns:1fr 60px 1.4fr;gap:4px 0;align-items:center;margin:4px 0 8px;break-inside:avoid}
.match .a,.match .b{border-radius:8px;padding:4px 9px;font-size:9.3pt;border:1.5px solid}
.match .a{background:var(--ly-bg);border-color:var(--ly-soft)}
.match.h .a{background:var(--hoa-bg);border-color:var(--hoa-soft)}
.match .b{background:#fff;border-color:var(--line)}
.match .mid{text-align:center;color:#94a3b8;font-size:12pt}
.ans{display:flex;gap:10px;font-size:9.3pt;margin:2px 0 6px}
.ans span{border:1.3px dashed #94a3b8;border-radius:6px;padding:2px 10px}
.cw{border-collapse:separate;border-spacing:3px;margin:6px auto}
.cw td{width:27px;height:27px;text-align:center;font-weight:800;font-size:10pt}
.cw td.c{border:1.5px solid #64748b;background:#fff;border-radius:4px}
.cw td.k{border:2px solid #7c3aed;background:#ede9fe;border-radius:4px}
.cw td.n{font-size:8.5pt;color:#7c3aed;font-weight:800}
.clues{font-size:9.2pt;columns:1}
.clues div{margin:2px 0}
.clues b{color:#7c3aed}
.key{margin-top:6px;font-size:9.5pt}
.key span{display:inline-block;width:24px;height:24px;border:2px solid #7c3aed;background:#ede9fe;border-radius:4px;margin-right:3px;vertical-align:middle}
"""

def mcq(n, cls, stem, opts, four=True):
    o = ''.join(f'<span><b>{l}.</b>{t}</span>' for l, t in zip('ABCD', opts))
    return f'<div class="q {cls}"><div class="qh"><span class="qn">Câu {n}.</span><span>{stem}</span></div><div class="opts{" four" if four else ""}">{o}</div></div>'

def ds(n, cls, stem, items):
    it = ''.join(f'<div><span>{l}) {t}</span><span class="box2"><i>Đ</i><i>S</i></span></div>' for l, t in zip('abcd', items))
    return f'<div class="q {cls} ds-q"><div class="qh"><span class="qn">Câu {n}.</span><span>{stem}</span></div><div class="items ds-items">{it}</div></div>'

# crossword
words = [('THUYLUYEN', 'H', 'Phương pháp dùng kim loại mạnh hơn đẩy kim loại yếu hơn ra khỏi dung dịch muối (9 chữ cái).'),
         ('OXIDE', 'O', 'Hợp chất của kim loại với oxygen, ví dụ CuO, Fe<sub>2</sub>O<sub>3</sub> (5 chữ cái).'),
         ('PHAPTUYEN', 'P', 'Đường thẳng vuông góc với mặt phân cách tại điểm tới; góc tới và góc khúc xạ đều đo so với đường này (9 chữ cái).'),
         ('KHUCXA', 'K', 'Hiện tượng tia sáng bị gãy khúc khi truyền xiên qua mặt phân cách hai môi trường trong suốt (6 chữ cái).'),
         ('CHIETSUAT', 'I', 'Đại lượng được tính bằng tỉ số c/v của một môi trường (9 chữ cái).'),
         ('NHOM', 'M', 'Kim loại nhẹ, được sản xuất bằng điện phân nóng chảy oxide, là thành phần chính của hợp kim dural (4 chữ cái).')]
L = max(w.index(k) for w, k, _ in words)
R = max(len(w) - w.index(k) - 1 for w, k, _ in words)
rows = ''
for i, (w, k, _) in enumerate(words, 1):
    off = L - w.index(k)
    cells = '<td></td>' * off + f'<td class="n">{i}</td>'[0:0]
    tds = ''
    for j in range(L + R + 1):
        p = j - off
        if 0 <= p < len(w):
            tds += f'<td class="{"k" if j == L else "c"}"></td>'
        else:
            tds += '<td></td>'
    rows += f'<tr><td class="n">{i}</td>{tds}</tr>'
cw = f'<table class="cw">{rows}</table>'
clues = ''.join(f'<div><b>Hàng {i}.</b> {c}</div>' for i, (_, _, c) in enumerate(words, 1))

html = f"""<!doctype html><html lang="vi"><head><meta charset="utf-8"><title>Phiếu học tập KHTN 9 cơ bản</title>
<style>{css}{extra}</style></head><body>

<div class="hero">
  <div class="deco">🔍</div>
  <span class="tag">KHOA HỌC TỰ NHIÊN 9 · PHIẾU HỌC TẬP CƠ BẢN</span>
  <h1>Ánh sáng đổi hướng &amp; Kim loại quanh em</h1>
  <div class="en">Refraction of Light · Extracting Metals &amp; Alloys · Metals vs Non-metals</div>
  <div class="lessons">
    <span class="l"><i>Vật lí</i> · Bài 5. Khúc xạ ánh sáng</span>
    <span class="h"><i>Hóa học</i> · Bài 20. Tách kim loại và việc sử dụng hợp kim</span>
    <span class="h"><i>Hóa học</i> · Bài 21. Sự khác nhau cơ bản giữa phi kim và kim loại</span>
  </div>
</div>

<div class="student"><div>Họ và tên:</div><div>Lớp: 9</div><div>Ngày: &nbsp;&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;&nbsp;&nbsp;/</div></div>

<div class="road">
  <div class="stop"><div class="dot" style="background:#475569">🌳</div><b>Trạm 1</b>Sơ đồ kiến thức</div>
  <div class="stop"><div class="dot" style="background:#2563eb">🎯</div><b>Trạm 2</b>Trắc nghiệm</div>
  <div class="stop"><div class="dot" style="background:var(--ds)">⚖️</div><b>Trạm 3</b>Đúng hay Sai?</div>
  <div class="stop"><div class="dot" style="background:#0891b2">🔗</div><b>Trạm 4</b>Ghép đôi</div>
  <div class="stop"><div class="dot" style="background:#e11d48">✍️</div><b>Trạm 5</b>Bài tập từng bước</div>
  <div class="stop"><div class="dot" style="background:var(--nghe)">🌏</div><b>Trạm 6</b>Khoa học quanh ta</div>
  <div class="stop"><div class="dot" style="background:var(--qt)">🧩</div><b>Trạm 7</b>Giải ô chữ</div>
</div>

<div class="data"><b>🧰 Hộp dữ kiện:</b> c = 3·10<sup>8</sup> m/s; chiết suất không khí ≈ 1; n<sub>nước</sub> = 4/3. Nguyên tử khối: H = 1; O = 16; S = 32; Fe = 56; Cu = 64. Được dùng máy tính cầm tay.</div>

<!-- TRẠM 1 -->
<div class="sec"><div class="num" style="background:#475569">🌳</div><h2>Trạm 1 · Sơ đồ kiến thức<small>Đọc từ gốc → nhánh → lá, sau đó làm bài điền từ ở cuối trạm.</small></h2></div>

<div class="tree ly">
  <span class="root">💡 KHÚC XẠ ÁNH SÁNG</span>
  <div class="branches" style="grid-template-columns:repeat(3,1fr);--edge:16.66%">
    <div class="br"><h4 style="background:#0b63c5">① Hiện tượng là gì?</h4>
      <div class="leaf">Tia sáng truyền <b>xiên</b> từ môi trường trong suốt này sang môi trường trong suốt khác thì bị <b>gãy khúc</b> tại mặt phân cách.</div>
      <div class="leaf">Tia tới <b>vuông góc</b> với mặt phân cách → truyền <b>thẳng</b>.</div>
      <div class="leaf">Ví dụ: chiếc thìa trong cốc nước trông như <b>bị gãy</b>; đáy bể trông <b>nông hơn</b>.</div>
    </div>
    <div class="br"><h4 style="background:#1d74d6">② Công thức cần nhớ</h4>
      <div class="leaf">Định luật khúc xạ: <span class="f">n<sub>1</sub>sin i = n<sub>2</sub>sin r</span></div>
      <div class="leaf">Chiết suất: <span class="f">n = c / v</span></div>
      <div class="leaf">Chân không: n = 1; không khí ≈ 1; nước ≈ 1,33; thủy tinh ≈ 1,5.</div>
      <div class="leaf">n càng lớn → ánh sáng đi càng <b>chậm</b>.</div>
    </div>
    <div class="br"><h4 style="background:#2f86e6">③ Tia sáng lệch về đâu?</h4>
      <div class="leaf">Góc i, r đo với <b>pháp tuyến</b> (không đo với mặt phân cách).</div>
      <div class="leaf">Không khí → nước, thủy tinh: <b>r &lt; i</b> (lệch <b>gần</b> pháp tuyến).</div>
      <div class="leaf">Nước, thủy tinh → không khí: <b>r &gt; i</b> (lệch <b>xa</b> pháp tuyến).</div>
    </div>
  </div>
</div>

{duo}

<div class="tree hoa">
  <span class="root">⚗️ KIM LOẠI QUANH EM</span>
  <div class="branches" style="grid-template-columns:repeat(3,1fr);--edge:16.66%">
    <div class="br"><h4 style="background:#c2410c">① Tách kim loại</h4>
      <div class="leaf"><b>⚡ Điện phân nóng chảy</b> – cho kim loại mạnh (K → Al). Ví dụ: NaCl nóng chảy → Na; Al<sub>2</sub>O<sub>3</sub> nóng chảy → Al.</div>
      <div class="leaf"><b>🔥 Nhiệt luyện</b> – khử oxide bằng C, CO, H<sub>2</sub>. Ví dụ: CuO + H<sub>2</sub> → Cu + H<sub>2</sub>O (t°).</div>
      <div class="leaf"><b>💧 Thủy luyện</b> – kim loại mạnh đẩy kim loại yếu. Ví dụ: Fe + CuSO<sub>4</sub> → FeSO<sub>4</sub> + Cu.</div>
    </div>
    <div class="br"><h4 style="background:#d9541a">② Hợp kim</h4>
      <div class="leaf">Là vật liệu gồm <b>một kim loại cơ bản</b> và thêm một số nguyên tố khác.</div>
      <div class="leaf"><b>Gang</b>: C &gt; 2% – cứng, giòn. <b>Thép</b>: C &lt; 2% – cứng, bền.</div>
      <div class="leaf"><b>Inox</b> (thép không gỉ): chống gỉ. <b>Dural</b> (nhôm): nhẹ, bền. <b>Đồng thau</b>: Cu – Zn.</div>
    </div>
    <div class="br"><h4 style="background:#e8692b">③ Kim loại hay phi kim?</h4>
      <div class="leaf"><b>Kim loại</b>: có ánh kim, dẫn điện, dẫn nhiệt tốt, dẻo. Hầu hết ở thể rắn (trừ Hg lỏng).</div>
      <div class="leaf"><b>Phi kim</b>: thường dẫn điện, dẫn nhiệt kém; có thể ở thể rắn (S, C), lỏng (Br<sub>2</sub>), khí (O<sub>2</sub>, Cl<sub>2</sub>).</div>
      <div class="leaf">Đặc biệt: <b>than chì</b> dẫn điện; <b>silicon</b> là chất bán dẫn.</div>
    </div>
  </div>
</div>

<div class="card keep">
  <h5>📝 Điền từ vào chỗ trống – chọn từ trong ngân hàng (có từ không dùng đến)</h5>
  <div class="bank"><span>gãy khúc</span><span>pháp tuyến</span><span>mặt phân cách</span><span>c/v</span><span>v/c</span><span>nhanh</span><span>chậm</span><span>nhỏ hơn</span><span>lớn hơn</span><span>điện phân nóng chảy</span><span>thủy luyện</span><span>ánh kim</span></div>
  <div class="fill">
  Tia sáng truyền xiên từ môi trường trong suốt này sang môi trường trong suốt khác bị <span class="bl">(1)</span> tại mặt phân cách, gọi là hiện tượng khúc xạ ánh sáng. Góc tới và góc khúc xạ được đo so với <span class="bl">(2)</span>. Chiết suất của một môi trường được tính bằng n = <span class="bl">(3)</span>; chiết suất càng lớn thì ánh sáng truyền càng <span class="bl">(4)</span>. Khi ánh sáng đi từ không khí vào nước, góc khúc xạ <span class="bl">(5)</span> góc tới.
  Kim loại có <span class="bl">(6)</span>, dẫn điện và dẫn nhiệt tốt. Nhôm được sản xuất bằng phương pháp <span class="bl">(7)</span> Al<sub>2</sub>O<sub>3</sub>; còn dùng sắt để lấy đồng ra khỏi dung dịch CuSO<sub>4</sub> là phương pháp <span class="bl">(8)</span>.
  </div>
</div>

<!-- TRẠM 2 -->
<div class="sec"><div class="num" style="background:#2563eb">🎯</div><h2>Trạm 2 · Trắc nghiệm<small>Khoanh tròn một chữ cái đứng trước đáp án đúng.</small></h2><div class="stars">Tự đánh giá: <span>☆☆☆</span></div></div>
<div class="sub ly">A. Vật lí</div>
{mcq(1,'ly','Hiện tượng khúc xạ ánh sáng là hiện tượng tia sáng',
 ['bị hắt trở lại môi trường cũ.','bị gãy khúc tại mặt phân cách khi truyền xiên qua hai môi trường trong suốt.','luôn truyền thẳng.','bị hấp thụ hoàn toàn.'], False)}
{mcq(2,'ly','Khi tia tới vuông góc với mặt phân cách giữa hai môi trường thì',
 ['tia sáng truyền thẳng, không đổi hướng.','góc khúc xạ bằng 90°.','không có tia khúc xạ.','tia sáng bị hắt lại hoàn toàn.'], False)}
{mcq(3,'ly','Công thức tính chiết suất tuyệt đối của một môi trường là',['n = v/c.','n = c·v.','n = c/v.','n = c − v.'])}
{mcq(4,'ly','Chiếu tia sáng xiên góc từ không khí vào thủy tinh. Góc khúc xạ',['lớn hơn góc tới.','bằng góc tới.','bằng 90°.','nhỏ hơn góc tới.'])}
{mcq(5,'ly','Hiện tượng nào sau đây liên quan đến khúc xạ ánh sáng?',
 ['Nhìn thấy ảnh của mình trong gương phẳng.','Chiếc thìa cắm trong cốc nước trông như bị gãy.','Bóng tối phía sau vật cản sáng.','Nghe thấy tiếng vang trong hang.'], False)}
{mcq(6,'ly','Nước có chiết suất 4/3. Tốc độ ánh sáng trong nước là',['4·10<sup>8</sup> m/s.','3·10<sup>8</sup> m/s.','2,25·10<sup>8</sup> m/s.','1,33·10<sup>8</sup> m/s.'])}
<div class="sub hoa">B. Hóa học</div>
{mcq(7,'hoa','Trong công nghiệp, kim loại Na được điều chế bằng cách',
 ['điện phân NaCl nóng chảy.','điện phân dung dịch NaCl.','dùng CO khử Na<sub>2</sub>O.','cho Fe tác dụng với dung dịch NaCl.'], False)}
{mcq(8,'hoa','Phản ứng nào sau đây thuộc phương pháp thủy luyện?',
 ['CuO + H<sub>2</sub> → Cu + H<sub>2</sub>O (t°)','2Al<sub>2</sub>O<sub>3</sub> → 4Al + 3O<sub>2</sub> (điện phân nóng chảy)','Fe<sub>2</sub>O<sub>3</sub> + 3CO → 2Fe + 3CO<sub>2</sub> (t°)','Fe + CuSO<sub>4</sub> → FeSO<sub>4</sub> + Cu'], False)}
{mcq(9,'hoa','Thép là hợp kim của sắt với carbon, trong đó hàm lượng carbon',['lớn hơn 2%.','nhỏ hơn 2%.','bằng 10%.','lớn hơn 50%.'])}
{mcq(10,'hoa','Kim loại ở thể lỏng ở điều kiện thường là',['Fe.','Cu.','Hg.','Al.'])}
{mcq(11,'hoa','Phi kim dẫn điện được, dùng làm điện cực và ruột bút chì là',['than chì (graphite).','sulfur.','phosphorus.','iodine.'])}
{mcq(12,'hoa','Khử hoàn toàn 8 gam CuO bằng khí H<sub>2</sub> ở nhiệt độ cao. Khối lượng Cu thu được là',['3,2 g.','6,4 g.','8,0 g.','12,8 g.'])}

<!-- TRẠM 3 -->
<div class="sec"><div class="num" style="background:var(--ds)">⚖️</div><h2>Trạm 3 · Đúng hay Sai?<small>Đánh dấu ✓ vào ô Đ (đúng) hoặc S (sai).</small></h2><div class="stars">Tự đánh giá: <span>☆☆☆</span></div></div>
{ds(1,'ly','Về hiện tượng khúc xạ ánh sáng:',['Ánh sáng truyền từ không khí vào nước thì tia khúc xạ lệch lại gần pháp tuyến.','Góc tới là góc tạo bởi tia tới và mặt phân cách.','Tốc độ ánh sáng trong nước nhỏ hơn trong không khí.','Chiết suất của mọi môi trường đều nhỏ hơn 1.'])}
{ds(2,'hoa','Về tách kim loại và hợp kim:',['Có thể thu được Cu bằng cách cho Fe vào dung dịch CuSO<sub>4</sub>.','Nhôm được sản xuất bằng cách điện phân nóng chảy Al<sub>2</sub>O<sub>3</sub>.','Hợp kim thường cứng hơn kim loại nguyên chất tạo nên nó.','Inox dễ bị gỉ hơn sắt thường.'])}
{ds(3,'hoa','Về kim loại và phi kim:',['Kim loại có ánh kim, dẫn điện và dẫn nhiệt tốt.','Ở điều kiện thường, mọi phi kim đều ở thể khí.','Bromine là phi kim ở thể lỏng.','Sulfur dẫn điện tốt nên được dùng làm dây điện.'])}

<!-- TRẠM 4 -->
<div class="sec"><div class="num" style="background:#0891b2">🔗</div><h2>Trạm 4 · Ghép đôi<small>Nối mỗi ô ở cột trái với một ô phù hợp ở cột phải, ghi kết quả vào ô trả lời.</small></h2><div class="stars">Tự đánh giá: <span>☆☆☆</span></div></div>
<div class="sub hoa">A. Kim loại ↔ Cách tách kim loại</div>
<div class="match h">
  <div class="a">1. Natri (Na)</div><div class="mid">•———•</div><div class="b">a. Dùng CO khử oxide sắt ở nhiệt độ cao (nhiệt luyện)</div>
  <div class="a">2. Sắt (Fe)</div><div class="mid">•———•</div><div class="b">b. Điện phân NaCl nóng chảy</div>
  <div class="a">3. Đồng (Cu) từ dung dịch CuSO<sub>4</sub></div><div class="mid">•———•</div><div class="b">c. Dùng sắt đẩy ra khỏi dung dịch muối (thủy luyện)</div>
  <div class="a">4. Nhôm (Al)</div><div class="mid">•———•</div><div class="b">d. Điện phân Al<sub>2</sub>O<sub>3</sub> nóng chảy</div>
</div>
<div class="ans"><span>1 – ……</span><span>2 – ……</span><span>3 – ……</span><span>4 – ……</span></div>
<div class="sub hoa">B. Hợp kim ↔ Ứng dụng</div>
<div class="match h">
  <div class="a">1. Thép</div><div class="mid">•———•</div><div class="b">a. Vỏ và khung máy bay (nhẹ, bền)</div>
  <div class="a">2. Inox (thép không gỉ)</div><div class="mid">•———•</div><div class="b">b. Dao, kéo, xoong nồi, bồn rửa (không gỉ)</div>
  <div class="a">3. Dural</div><div class="mid">•———•</div><div class="b">c. Cốt bê tông, khung nhà, đường ray (cứng, chịu lực)</div>
  <div class="a">4. Đồng thau (Cu – Zn)</div><div class="mid">•———•</div><div class="b">d. Kèn trumpet, van nước, ổ khóa</div>
</div>
<div class="ans"><span>1 – ……</span><span>2 – ……</span><span>3 – ……</span><span>4 – ……</span></div>

<!-- TRẠM 5 -->
<div class="sec"><div class="num" style="background:#e11d48">✍️</div><h2>Trạm 5 · Bài tập từng bước<small>Điền vào chỗ trống theo từng bước gợi ý.</small></h2><div class="stars">Tự đánh giá: <span>☆☆☆</span></div></div>

<div class="q ly"><div class="qh"><span class="qn">Bài 1.</span><span>Chiếu một tia sáng từ không khí (n<sub>1</sub> = 1) vào nước (n<sub>2</sub> = 4/3) với góc tới i, biết sin i = 0,8.</span></div>
<div class="steps">
  <div><span class="st">B1</span>Viết định luật khúc xạ: <span class="dots w"></span></div>
  <div><span class="st">B2</span>Suy ra: sin r = (n<sub>1</sub> · sin i) : n<sub>2</sub> = (1 · 0,8) : (4/3) = <span class="dots"></span></div>
  <div><span class="st">B3</span>Dùng máy tính (phím SHIFT sin): i ≈ <span class="dots"></span>°; &nbsp; r ≈ <span class="dots"></span>° (làm tròn đến độ).</div>
  <div><span class="st">B4</span>So sánh: r <span class="dots"></span> i, vì tia sáng đi từ môi trường có chiết suất <span class="dots"></span> sang môi trường có chiết suất <span class="dots"></span>.</div>
</div></div>

<div class="q ly"><div class="qh"><span class="qn">Bài 2.</span><span>Thủy tinh có chiết suất n = 1,5.</span></div>
<div class="steps">
  <div><span class="st">B1</span>Từ n = c/v suy ra v = <span class="dots"></span></div>
  <div><span class="st">B2</span>Thay số: v = 3·10<sup>8</sup> : 1,5 = <span class="dots w"></span> m/s.</div>
  <div><span class="st">B3</span>Khi ánh sáng đi từ không khí vào thủy tinh, tốc độ ánh sáng <span class="dots"></span> (tăng / giảm).</div>
</div></div>

<div class="q hoa"><div class="qh"><span class="qn">Bài 3.</span><span>Hoàn thành các phương trình hóa học và ghi tên phương pháp tách kim loại (điện phân nóng chảy / nhiệt luyện / thủy luyện).</span></div>
<table class="grid" style="margin:4px 0 0 52px;width:calc(100% - 52px)">
<tr><th style="width:56%">Phương trình hóa học</th><th>Phương pháp</th></tr>
<tr><td style="text-align:left">a) CuO + H<sub>2</sub> →<sup>t°</sup> ………… + …………</td><td class="blank"></td></tr>
<tr><td style="text-align:left">b) Fe<sub>2</sub>O<sub>3</sub> + …CO →<sup>t°</sup> …Fe + ………………</td><td class="blank"></td></tr>
<tr><td style="text-align:left">c) Fe + CuSO<sub>4</sub> → ………… + …………</td><td class="blank"></td></tr>
<tr><td style="text-align:left">d) …Al<sub>2</sub>O<sub>3</sub> → …Al + …O<sub>2</sub></td><td class="blank"></td></tr>
</table></div>

<div class="q hoa"><div class="qh"><span class="qn">Bài 4.</span><span>Ngâm 5,6 gam bột sắt vào dung dịch CuSO<sub>4</sub>, sắt phản ứng hết.</span></div>
<div class="steps">
  <div><span class="st">B1</span>Viết phương trình hóa học: <span class="dots w"></span><span class="dots w"></span></div>
  <div><span class="st">B2</span>Số mol sắt: n<sub>Fe</sub> = m : M = 5,6 : 56 = <span class="dots"></span> mol.</div>
  <div><span class="st">B3</span>Theo phương trình: n<sub>Cu</sub> = n<sub>CuSO₄</sub> = n<sub>Fe</sub> = <span class="dots"></span> mol.</div>
  <div><span class="st">B4</span>Khối lượng Cu tạo thành: m<sub>Cu</sub> = <span class="dots"></span> × 64 = <span class="dots"></span> g.</div>
  <div><span class="st">B5</span>Khối lượng CuSO<sub>4</sub> đã phản ứng (M = 160 g/mol): m = <span class="dots"></span> × 160 = <span class="dots"></span> g.</div>
</div>
<div class="hint">💡 Nhớ 3 bước vàng: <b>đổi ra mol → dựa vào tỉ lệ trong phương trình → đổi ra đại lượng cần tìm</b>.</div></div>

<!-- TRẠM 6 -->
<div class="sec"><div class="num" style="background:var(--nghe)">🌏</div><h2 style="color:var(--nghe)">Trạm 6 · Khoa học quanh ta<small>Dùng kiến thức vừa học để giải thích những điều em gặp hằng ngày.</small></h2></div>
<div class="feature ng">
<div class="q ng"><div class="qh"><span class="qn">Câu 1.</span><span><b>🏊 Bể bơi "đánh lừa" mắt.</b> Nhìn từ trên bờ, đáy bể bơi trông nông hơn thực tế. Một bể sâu 1,2 m, nếu nhìn gần vuông góc thì đáy bể trông như chỉ sâu khoảng h′ = h : n. Hãy tính h′ và cho biết vì sao không nên nhảy xuống bể khi chỉ "ước lượng bằng mắt".</span></div>
<div class="lines"><div></div><div></div></div></div>
<div class="q ng"><div class="qh"><span class="qn">Câu 2.</span><span><b>🍳 Đồ dùng trong bếp.</b> Vì sao xoong nồi thường làm bằng nhôm hoặc inox, nhưng tay cầm lại làm bằng nhựa hoặc gỗ? Vì sao dây điện trong nhà làm bằng đồng và bọc nhựa bên ngoài?</span></div>
<div class="lines"><div></div><div></div><div></div></div></div>
<div class="q ng" style="margin-bottom:0"><div class="qh"><span class="qn">Câu 3.</span><span><b>♻️ Tái chế vỏ lon.</b> Tái chế nhôm từ vỏ lon tiết kiệm tới khoảng 95% năng lượng so với sản xuất nhôm mới từ quặng. Em hãy đề xuất một việc làm cụ thể ở lớp hoặc ở nhà để góp phần tái chế kim loại.</span></div>
<div class="lines"><div></div><div></div></div></div>
</div>
<div class="feature ng">
<div style="font-weight:800;color:var(--nghe);margin-bottom:6px">🎯 Nghề nào dùng kiến thức hôm nay?</div>
<div class="careers" style="grid-template-columns:repeat(3,1fr)">
  <div class="career"><b>👓 Kĩ thuật viên quang học</b>Đo mắt, lắp kính cận, kính viễn; sửa chữa camera, ống nhòm.</div>
  <div class="career"><b>🔧 Thợ cơ khí – hàn</b>Gia công thép, inox, nhôm làm cửa, khung nhà, chi tiết máy.</div>
  <div class="career"><b>♻️ Nhân viên tái chế</b>Phân loại, thu gom kim loại phế liệu, góp phần bảo vệ môi trường.</div>
</div>
</div>

<!-- TRẠM 7 -->
<div class="sec"><div class="num" style="background:var(--qt)">🧩</div><h2 style="color:var(--qt)">Trạm 7 · Giải ô chữ<small>Viết chữ in hoa, không dấu, mỗi chữ cái một ô. Các ô tô tím ghép lại thành từ khóa.</small></h2></div>
<div class="feature qt">
<div style="display:grid;grid-template-columns:1.05fr 1fr;gap:12px;align-items:center">
  <div>{cw}</div>
  <div class="clues">{clues}
  <div class="key">🔑 <b>Từ khóa:</b> <span></span><span></span><span></span><span></span><span></span><span></span></div>
  <div style="font-size:8.6pt;color:var(--muted);margin-top:4px">Gợi ý: Đây là loại vật liệu làm nên vỏ máy bay, khung xe đạp, nồi inox…</div>
  </div>
</div>
</div>

<div class="foot">🌟 <b>Hoàn thành hành trình!</b> Tô sao tự đánh giá ở mỗi trạm. Câu em thấy khó nhất: ……………………………</div>
</body></html>"""
pathlib.Path('phieu_co_ban.html').write_text(html)

# ---------------- answer key ----------------
key = f"""<!doctype html><html lang="vi"><head><meta charset="utf-8"><title>Đáp án phiếu cơ bản</title>
<style>{css}
.k h3{{font-size:11pt;margin:10px 0 4px;color:#0e7490}}
.k p,.k li{{font-size:9.6pt;margin:2px 0}}
</style></head><body class="k">
<div class="hero" style="background:linear-gradient(120deg,#334155,#64748b)"><span class="tag">DÀNH CHO GIÁO VIÊN</span><h1 style="font-size:16pt">Đáp án – Phiếu học tập cơ bản KHTN 9 (Bài 5, 20, 21)</h1></div>
<h3>Trạm 1 · Điền từ</h3>
<p>(1) gãy khúc; (2) pháp tuyến; (3) c/v; (4) chậm; (5) nhỏ hơn; (6) ánh kim; (7) điện phân nóng chảy; (8) thủy luyện. <i>Từ không dùng: mặt phân cách, v/c, nhanh, lớn hơn.</i></p>
<h3>Trạm 2 · Trắc nghiệm</h3>
<table class="grid"><tr><th>Câu</th>{''.join(f'<th>{i}</th>' for i in range(1,13))}</tr>
<tr><th>Đáp án</th>{''.join(f'<td>{a}</td>' for a in 'BACDBCADBCAB')}</tr></table>
<p>Câu 6: v = c/n = 3·10<sup>8</sup> : (4/3) = 2,25·10<sup>8</sup> m/s. Câu 12: n<sub>CuO</sub> = 8 : 80 = 0,1 mol ⇒ m<sub>Cu</sub> = 0,1 · 64 = 6,4 g.</p>
<h3>Trạm 3 · Đúng – Sai</h3>
<p>Câu 1: a Đ; b S (đo với pháp tuyến); c Đ; d S (n ≥ 1). &nbsp; Câu 2: a Đ; b Đ; c Đ; d S. &nbsp; Câu 3: a Đ; b S; c Đ; d S.</p>
<h3>Trạm 4 · Ghép đôi</h3>
<p>A: 1 – b; 2 – a; 3 – c; 4 – d. &nbsp;&nbsp; B: 1 – c; 2 – b; 3 – a; 4 – d.</p>
<h3>Trạm 5 · Bài tập từng bước</h3>
<p><b>Bài 1.</b> n<sub>1</sub>sin i = n<sub>2</sub>sin r; sin r = 0,8 : (4/3) = 0,6; i ≈ 53°; r ≈ 37°; r &lt; i vì ánh sáng đi từ môi trường chiết suất nhỏ (không khí) sang môi trường chiết suất lớn (nước).</p>
<p><b>Bài 2.</b> v = c/n = 3·10<sup>8</sup> : 1,5 = 2·10<sup>8</sup> m/s; tốc độ giảm.</p>
<p><b>Bài 3.</b> a) CuO + H<sub>2</sub> → Cu + H<sub>2</sub>O – nhiệt luyện; b) Fe<sub>2</sub>O<sub>3</sub> + 3CO → 2Fe + 3CO<sub>2</sub> – nhiệt luyện; c) Fe + CuSO<sub>4</sub> → FeSO<sub>4</sub> + Cu – thủy luyện; d) 2Al<sub>2</sub>O<sub>3</sub> → 4Al + 3O<sub>2</sub> – điện phân nóng chảy.</p>
<p><b>Bài 4.</b> Fe + CuSO<sub>4</sub> → FeSO<sub>4</sub> + Cu; n<sub>Fe</sub> = 0,1 mol; n<sub>Cu</sub> = n<sub>CuSO₄</sub> = 0,1 mol; m<sub>Cu</sub> = 6,4 g; m<sub>CuSO₄</sub> = 16 g.</p>
<h3>Trạm 6 · Khoa học quanh ta (gợi ý)</h3>
<p><b>Câu 1.</b> h′ = 1,2 : (4/3) = 0,9 m. Ánh sáng từ đáy bể khúc xạ ra không khí bị lệch xa pháp tuyến nên mắt thấy ảnh đáy bể cao hơn thực tế. Nước sâu hơn mình tưởng, nhảy xuống dễ bị đuối nước nếu không biết bơi.</p>
<p><b>Câu 2.</b> Nhôm, inox dẫn nhiệt tốt nên đun nấu nhanh; inox còn chống gỉ, nhôm có lớp oxide bảo vệ. Nhựa và gỗ dẫn nhiệt kém nên cầm không bị bỏng. Đồng dẫn điện rất tốt và dễ kéo sợi; vỏ nhựa cách điện, giúp an toàn.</p>
<p><b>Câu 3.</b> Chấp nhận mọi đề xuất hợp lí, ví dụ: đặt thùng thu gom vỏ lon ở lớp, phân loại rác tại nhà, bán phế liệu để gây quỹ lớp.</p>
<h3>Trạm 7 · Ô chữ</h3>
<p>1. THUYLUYEN · 2. OXIDE · 3. PHAPTUYEN · 4. KHUCXA · 5. CHIETSUAT · 6. NHOM &nbsp;⇒ <b>Từ khóa: HOPKIM (HỢP KIM)</b>.</p>
</body></html>"""
pathlib.Path('dap_an_co_ban.html').write_text(key)
print('ok', L, R)
