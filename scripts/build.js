const fs = require('fs');
const D = require('docx');
const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType, AlignmentType,
  BorderStyle, ShadingType, TabStopType, PageBreak, Footer, PageNumber, LevelFormat } = D;

const FONT = 'Times New Roman', SZ = 26; // 13pt
const W = 9638; // A4 width minus 2cm margins (DXA)

// markup: **bold**, *italic*, _{sub}, ^{sup}
function runs(text, base = {}) {
  const out = [];
  const re = /(\*\*[^*]+\*\*|\*[^*]+\*|_\{[^}]*\}|\^\{[^}]*\})/g;
  let last = 0, m;
  const push = (t, o) => { if (t) out.push(new TextRun({ text: t, font: FONT, size: SZ, ...base, ...o })); };
  while ((m = re.exec(text))) {
    push(text.slice(last, m.index), {});
    const s = m[0];
    if (s.startsWith('**')) runs(s.slice(2, -2), { ...base, bold: true }).forEach(r => out.push(r));
    else if (s.startsWith('*')) push(s.slice(1, -1), { italics: true });
    else if (s.startsWith('_{')) push(s.slice(2, -1), { subScript: true });
    else push(s.slice(2, -1), { superScript: true });
    last = m.index + s.length;
  }
  push(text.slice(last), {});
  return out;
}
const P = (text, o = {}) => new Paragraph({
  children: runs(text, o.run || {}), alignment: o.align || AlignmentType.JUSTIFIED,
  spacing: { before: o.before ?? 40, after: o.after ?? 40, line: 276 },
  indent: o.indent, tabStops: o.tabs, numbering: o.numbering, keepNext: o.keepNext,
});
const H = (text, color = '1F4E79') => new Paragraph({
  children: runs(text, { bold: true, color, size: 28 }), spacing: { before: 200, after: 80 }, keepNext: true,
  border: { bottom: { style: BorderStyle.SINGLE, size: 8, color, space: 2 } },
});
const SUB = (text) => P(`**${text}**`, { run: { color: 'C00000' }, before: 120, keepNext: true });
const B = (text) => P(text, { numbering: { reference: 'bul', level: 0 } });
const Q = (label, text) => P(`**${label}** ${text}`, { before: 100, keepNext: true });
const OPT = (a, b) => P(`${a}\t${b}`, { indent: { left: 400 }, tabs: [{ type: TabStopType.LEFT, position: 5000 }], before: 0, after: 0 });
const ITEM = (text) => P(text, { indent: { left: 400 }, before: 20, after: 20 });
const LINES = (n) => Array.from({ length: n }, () => P('.'.repeat(150), { run: { color: '999999', size: 20 }, align: AlignmentType.LEFT, before: 60, after: 60 }));
const BR = () => new Paragraph({ children: [new PageBreak()] });

const none = { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' };
const noB = { top: none, bottom: none, left: none, right: none };
const thin = { style: BorderStyle.SINGLE, size: 4, color: '808080' };
const allB = { top: thin, bottom: thin, left: thin, right: thin };

function box(title, paras, fill = 'EAF3E6', color = '38761D') {
  return new Table({
    width: { size: W, type: WidthType.DXA }, columnWidths: [W],
    rows: [new TableRow({ children: [new TableCell({
      width: { size: W, type: WidthType.DXA },
      borders: { top: { style: BorderStyle.SINGLE, size: 12, color }, bottom: { style: BorderStyle.SINGLE, size: 12, color }, left: { style: BorderStyle.SINGLE, size: 12, color }, right: { style: BorderStyle.SINGLE, size: 12, color } },
      shading: { type: ShadingType.CLEAR, color: 'auto', fill },
      margins: { top: 100, bottom: 100, left: 160, right: 160 },
      children: [P(`**${title}**`, { run: { color } }), ...paras],
    })] })],
  });
}
function table(rows, widths, headFill = 'DDEBF7') {
  return new Table({
    width: { size: W, type: WidthType.DXA }, columnWidths: widths,
    rows: rows.map((r, i) => new TableRow({ children: r.map((c, j) => new TableCell({
      width: { size: widths[j], type: WidthType.DXA }, borders: allB,
      shading: i === 0 ? { type: ShadingType.CLEAR, color: 'auto', fill: headFill } : undefined,
      margins: { top: 40, bottom: 40, left: 100, right: 100 },
      children: [P(i === 0 ? `**${c}**` : c, { align: AlignmentType.CENTER, before: 0, after: 0 })],
    })) })),
  });
}

// ---------- HEADER ----------
const header = new Table({
  width: { size: W, type: WidthType.DXA }, columnWidths: [4300, 5338],
  rows: [new TableRow({ children: [
    new TableCell({ width: { size: 4300, type: WidthType.DXA }, borders: noB, children: [
      P('UBND XÃ THIÊN LỘC', { align: AlignmentType.CENTER, before: 0, after: 0 }),
      P('**TRƯỜNG THCS THIÊN LỘC**', { align: AlignmentType.CENTER, before: 0, after: 0 }),
      P('Tổ Khoa học tự nhiên', { align: AlignmentType.CENTER, before: 0, after: 0, run: { italics: true } })] }),
    new TableCell({ width: { size: 5338, type: WidthType.DXA }, borders: noB, children: [
      P('**PHIẾU BÀI TẬP DẠY THÊM**', { align: AlignmentType.CENTER, before: 0, after: 0 }),
      P('Môn: Khoa học tự nhiên 9 (Vật lí – Hóa học)', { align: AlignmentType.CENTER, before: 0, after: 0 }),
      P('Năm học 2026 – 2027', { align: AlignmentType.CENTER, before: 0, after: 0, run: { italics: true } })] }),
  ] })],
});

const body = [
  header,
  P('', { before: 60 }),
  P('**CHỦ ĐỀ: NĂNG LƯỢNG CƠ HỌC & KIM LOẠI**', { align: AlignmentType.CENTER, run: { size: 32, color: '1F4E79' } }),
  P('*Mechanical Energy & Metals*', { align: AlignmentType.CENTER, run: { color: '1F4E79' } }),
  P('Họ và tên: ……………………………………………… Lớp: 9A…… Ngày: ……/……/2026', { align: AlignmentType.CENTER, before: 120 }),
  P('*Mức độ: Biết → Hiểu → Vận dụng → Vận dụng cao → Thử thách quốc tế. Lấy g = 10 m/s² (trọng lượng P = 10m). Thể tích khí đo ở điều kiện chuẩn (25 °C, 1 bar): 1 mol khí = 24,79 L. Nguyên tử khối: H = 1; O = 16; Na = 23; Mg = 24; Al = 27; S = 32; Cl = 35,5; Fe = 56; Cu = 64; Zn = 65; Ag = 108.*', { run: { size: 22 } }),

  // ---------- I ----------
  H('PHẦN I. TÓM TẮT KIẾN THỨC TRỌNG TÂM'),
  SUB('A. Vật lí – Năng lượng cơ học'),
  B('**Động năng** là năng lượng vật có do chuyển động: W_{đ} = ½·m·v² (m: kg; v: m/s; W_{đ}: J). Vận tốc tăng 2 lần → động năng tăng 4 lần.'),
  B('**Thế năng trọng trường** là năng lượng vật có do ở độ cao h so với mốc: W_{t} = P·h = 10·m·h (J).'),
  B('**Cơ năng** W = W_{đ} + W_{t}. Khi chỉ có trọng lực thực hiện công (bỏ qua ma sát, sức cản) thì cơ năng được **bảo toàn**: động năng và thế năng chuyển hóa qua lại, tổng không đổi.'),
  B('**Công cơ học** A = F·s (J); **công suất** P = A/t (W); 1 kW = 1000 W; 1 kWh = 3 600 000 J. **Hiệu suất** H = A_{có ích}/A_{toàn phần} × 100%.'),
  SUB('B. Hóa học – Kim loại'),
  B('**Tính chất vật lí chung:** dẫn điện, dẫn nhiệt, có ánh kim, có tính dẻo. Dẫn điện tốt nhất: Ag > Cu > Au > Al > Fe.'),
  B('**Tính chất hóa học:** tác dụng với phi kim (O_{2}, Cl_{2}, S…); với dung dịch acid (HCl, H_{2}SO_{4} loãng) → muối + H_{2}; với dung dịch muối của kim loại yếu hơn; một số kim loại mạnh (Na, K, Ca…) tác dụng với nước ở nhiệt độ thường.'),
  B('**Dãy hoạt động hóa học:** K, Na, Ca, Mg, Al, Zn, Fe, Pb, (H), Cu, Ag, Au. Kim loại đứng **trước H** đẩy được H khỏi dung dịch acid; kim loại đứng **trước** (trừ K, Na, Ca…) đẩy được kim loại đứng **sau** ra khỏi dung dịch muối.'),
  SUB('C. Thuật ngữ song ngữ (Bilingual Glossary)'),
  table([
    ['Tiếng Việt', 'English', 'Tiếng Việt', 'English'],
    ['Động năng', 'Kinetic energy', 'Kim loại', 'Metal'],
    ['Thế năng trọng trường', 'Gravitational potential energy', 'Dãy hoạt động hóa học', 'Reactivity series'],
    ['Cơ năng', 'Mechanical energy', 'Ánh kim', 'Metallic lustre'],
    ['Bảo toàn năng lượng', 'Conservation of energy', 'Phản ứng thế', 'Displacement reaction'],
    ['Công / Công suất', 'Work / Power', 'Hợp kim', 'Alloy'],
    ['Hiệu suất', 'Efficiency', 'Ăn mòn kim loại', 'Corrosion'],
  ], [2300, 2519, 2300, 2519]),

  // ---------- II ----------
  H('PHẦN II. TRẮC NGHIỆM (Mức Biết – Hiểu)'),
  P('*Khoanh tròn vào chữ cái đứng trước đáp án đúng.*'),
  Q('Câu 1.', 'Động năng của một vật phụ thuộc vào'),
  OPT('A. khối lượng và vận tốc của vật.', 'B. độ cao của vật.'),
  OPT('C. khối lượng và độ cao của vật.', 'D. vận tốc và độ cao của vật.'),
  Q('Câu 2.', 'Một vật khối lượng 2 kg chuyển động với vận tốc 3 m/s. Động năng của vật là'),
  OPT('A. 3 J.', 'B. 6 J.'), OPT('C. 9 J.', 'D. 18 J.'),
  Q('Câu 3.', 'Giữ nguyên khối lượng, nếu vận tốc của vật tăng gấp đôi thì động năng của vật'),
  OPT('A. tăng 2 lần.', 'B. tăng 4 lần.'), OPT('C. giảm 2 lần.', 'D. không đổi.'),
  Q('Câu 4.', 'Đơn vị của công suất là'),
  OPT('A. jun (J).', 'B. oát (W).'), OPT('C. niutơn (N).', 'D. niutơn mét (N·m).'),
  Q('Câu 5.', 'Thả rơi một vật từ độ cao h (bỏ qua sức cản không khí). Trong quá trình vật rơi'),
  OPT('A. thế năng tăng, động năng giảm.', 'B. thế năng giảm, cơ năng giảm.'),
  OPT('C. thế năng giảm, động năng tăng, cơ năng không đổi.', 'D. động năng và thế năng đều tăng.'),
  Q('Câu 6.', 'Tính chất vật lí chung của kim loại gồm'),
  OPT('A. dẫn điện, dẫn nhiệt, ánh kim, tính dẻo.', 'B. dẫn điện, giòn, dễ vỡ.'),
  OPT('C. cách điện, cách nhiệt, ánh kim.', 'D. tan tốt trong nước.'),
  Q('Câu 7.', 'Kim loại **không** tác dụng với dung dịch HCl là'),
  OPT('A. Fe.', 'B. Zn.'), OPT('C. Mg.', 'D. Cu.'),
  Q('Câu 8.', 'Kim loại dẫn điện tốt nhất là'),
  OPT('A. Ag.', 'B. Cu.'), OPT('C. Au.', 'D. Al.'),
  Q('Câu 9.', 'Dãy kim loại được sắp xếp theo chiều **giảm dần** mức độ hoạt động hóa học là'),
  OPT('A. K, Mg, Fe, Cu.', 'B. Cu, Fe, Mg, K.'), OPT('C. Mg, K, Cu, Fe.', 'D. Fe, Cu, K, Mg.'),
  Q('Câu 10.', 'Ngâm một đinh sắt sạch trong dung dịch CuSO_{4}. Hiện tượng quan sát được là'),
  ITEM('A. không có hiện tượng gì.'),
  ITEM('B. có khí không màu thoát ra.'),
  ITEM('C. có lớp kim loại màu đỏ bám trên đinh sắt, màu xanh của dung dịch nhạt dần.'),
  ITEM('D. đinh sắt tan hết, dung dịch chuyển sang màu đỏ.'),

  // ---------- III ----------
  H('PHẦN III. TỰ LUẬN'),
  SUB('Mức Vận dụng'),
  Q('Câu 1.', 'Một ô tô khối lượng 1,2 tấn đang chuyển động thẳng với vận tốc 54 km/h.'),
  ITEM('a) Tính động năng của ô tô.'),
  ITEM('b) Ô tô hãm phanh và dừng lại sau quãng đường 30 m. Coi toàn bộ động năng của ô tô đã dùng để thực hiện công chống lại lực hãm. Tính độ lớn lực hãm trung bình.'),
  Q('Câu 2.', 'Từ độ cao 1,5 m so với mặt đất, một quả bóng khối lượng 200 g được ném thẳng đứng lên trên với vận tốc 8 m/s. Bỏ qua sức cản không khí, chọn mốc thế năng tại mặt đất.'),
  ITEM('a) Tính cơ năng của quả bóng tại vị trí ném.'),
  ITEM('b) Tính độ cao cực đại mà quả bóng đạt được.'),
  ITEM('c) Tính vận tốc của quả bóng ngay trước khi chạm đất.'),
  ITEM('d) Ở độ cao nào thì động năng của quả bóng bằng thế năng của nó?'),
  Q('Câu 3.', 'Một cần cẩu nâng đều một container khối lượng 2,5 tấn lên cao 12 m trong thời gian 30 s.'),
  ITEM('a) Tính công có ích mà cần cẩu thực hiện.'),
  ITEM('b) Tính công suất có ích của cần cẩu.'),
  ITEM('c) Biết công suất toàn phần của động cơ cần cẩu là 12,5 kW. Tính hiệu suất của cần cẩu.'),
  Q('Câu 4.', 'a) Hoàn thành các phương trình hóa học sau (ghi rõ điều kiện nếu có):'),
  ITEM('(1) Al + Cl_{2} → ……          (2) Na + H_{2}O → ……'),
  ITEM('(3) Fe + O_{2} → ……            (4) Mg + H_{2}SO_{4} (loãng) → ……'),
  ITEM('b) Phản ứng nào sau đây xảy ra được? Viết phương trình hóa học và giải thích dựa vào dãy hoạt động hóa học: (1) Cu + HCl; (2) Fe + CuSO_{4}; (3) Ag + CuSO_{4}; (4) Zn + FeSO_{4}; (5) Fe + ZnSO_{4}.'),
  Q('Câu 5.', 'Cho 6,5 gam Zn tác dụng vừa đủ với dung dịch HCl 7,3%.'),
  ITEM('a) Tính thể tích khí H_{2} thu được ở điều kiện chuẩn.'),
  ITEM('b) Tính khối lượng dung dịch HCl đã dùng.'),
  ITEM('c) Tính nồng độ phần trăm của dung dịch muối thu được sau phản ứng.'),
  SUB('Mức Vận dụng cao'),
  Q('Câu 6.', 'Ngâm một lá sắt khối lượng 20 gam vào 200 mL dung dịch CuSO_{4} 1M. Sau một thời gian lấy lá sắt ra, rửa nhẹ, làm khô, cân được 20,8 gam (giả sử toàn bộ Cu sinh ra bám hết vào lá sắt).'),
  ITEM('a) Tính khối lượng Cu bám vào lá sắt và khối lượng Fe đã phản ứng.'),
  ITEM('b) Tính nồng độ mol của các chất trong dung dịch sau phản ứng (coi thể tích dung dịch không đổi).'),
  Q('Câu 7.', 'Cho 10 gam hỗn hợp bột Fe và Cu vào dung dịch HCl dư, thu được 2,479 L khí H_{2} (đkc).'),
  ITEM('a) Tính phần trăm khối lượng mỗi kim loại trong hỗn hợp.'),
  ITEM('b) Tính thể tích dung dịch HCl 1M tối thiểu cần dùng để hòa tan hết phần kim loại phản ứng được.'),

  // ---------- IV ----------
  H('PHẦN IV. KHOA HỌC QUANH TA & ĐỊNH HƯỚNG NGHỀ NGHIỆP', '38761D'),
  Q('Câu 8. (Xe điện và phanh tái sinh)', 'Trên nhiều xe điện hiện nay có hệ thống **phanh tái sinh** (regenerative braking): khi phanh, động cơ điện hoạt động như máy phát, chuyển một phần động năng của xe thành điện năng nạp lại vào pin. Một xe điện khối lượng 1,5 tấn đang chạy với vận tốc 72 km/h thì phanh đến khi dừng hẳn.'),
  ITEM('a) Tính động năng của xe trước khi phanh.'),
  ITEM('b) Nếu hệ thống thu hồi được 60% động năng đó thành điện năng, tính phần điện năng thu được (theo J và kWh).'),
  ITEM('c) Phần điện năng ở câu b đủ để thắp sáng một bóng đèn LED 10 W trong bao lâu?'),
  ITEM('d) Vì sao hệ thống không thể thu hồi 100% động năng?'),
  Q('Câu 9. (Thủy điện tích năng – "cục pin nước khổng lồ")', 'Nhà máy thủy điện tích năng dùng điện lúc thấp điểm (ban đêm, hoặc khi điện mặt trời, điện gió dư thừa) để bơm nước lên hồ trên cao; lúc cao điểm, xả nước xuống làm quay tua bin phát điện. Giả sử hồ trên cao hơn tua bin 400 m, mỗi giây có 100 m³ nước chảy qua tua bin (khối lượng riêng của nước 1000 kg/m³).'),
  ITEM('a) Tính thế năng của lượng nước chảy qua tua bin trong mỗi giây.'),
  ITEM('b) Biết 85% thế năng đó được chuyển thành điện năng. Tính công suất điện của nhà máy (theo MW).'),
  ITEM('c) Tính điện năng nhà máy phát ra nếu hoạt động liên tục 5 giờ ở công suất trên (theo MWh).'),
  ITEM('d) Năng lượng tiêu tốn để bơm nước lên luôn lớn hơn điện năng thu lại. Vậy vì sao các nước vẫn xây dựng loại nhà máy này?'),
  Q('Câu 10. (Tái chế lon nhôm – liên môn Lí – Hóa)', 'Giả sử để sản xuất 1 kg nhôm mới từ quặng cần khoảng 14 kWh điện năng, còn tái chế 1 kg nhôm từ vỏ lon chỉ cần khoảng 5% lượng năng lượng đó *(số liệu gần đúng, dùng cho bài tập)*. Trường em thu gom được 50 kg vỏ lon nhôm.'),
  ITEM('a) Tính điện năng tiết kiệm được khi tái chế 50 kg nhôm thay vì sản xuất nhôm mới.'),
  ITEM('b) Điện năng đó đủ để một bóng đèn LED 10 W sáng liên tục trong khoảng bao nhiêu năm?'),
  ITEM('c) Nhôm đứng trước sắt trong dãy hoạt động hóa học, nhưng vỏ lon nhôm lại hầu như không bị gỉ như đồ vật bằng sắt. Hãy giải thích và viết phương trình hóa học minh họa.'),
  P(''),
  box('🎯 GÓC ĐỊNH HƯỚNG NGHỀ NGHIỆP', [
    B('**Kĩ sư năng lượng tái tạo / hệ thống điện:** thiết kế nhà máy điện gió, điện mặt trời, thủy điện tích năng, hệ thống lưu trữ năng lượng.'),
    B('**Kĩ sư ô tô điện:** phát triển động cơ, pin và hệ thống phanh tái sinh – lĩnh vực đang phát triển mạnh tại Việt Nam.'),
    B('**Kĩ sư vật liệu – luyện kim:** nghiên cứu hợp kim nhẹ, bền cho máy bay, ô tô; công nghệ chống ăn mòn kim loại.'),
    B('**Kĩ sư môi trường – tái chế:** thu hồi kim loại từ rác thải điện tử, pin cũ, vỏ lon… góp phần xây dựng kinh tế tuần hoàn.'),
    P('*Câu hỏi suy ngẫm: Em hứng thú nhất với nghề nào ở trên? Theo em, nghề đó cần vận dụng những kiến thức nào trong phiếu bài tập này?*'),
  ]),

  // ---------- V ----------
  H('PHẦN V. THỬ THÁCH QUỐC TẾ (Theo định dạng đề Olympic Khoa học trẻ quốc tế – IJSO)', '7030A0'),
  Q('Bài 1. (Vật lí)', 'Một viên bi nhỏ được thả không vận tốc đầu từ điểm A ở độ cao 0,8 m trên một máng trượt nhẵn (bỏ qua mọi ma sát và sức cản). Viên bi trượt xuống điểm thấp nhất B (ở mặt đất) rồi đi lên điểm C ở độ cao 0,35 m. Chọn mốc thế năng tại mặt đất.'),
  ITEM('a) Chứng minh rằng vận tốc của viên bi tại một vị trí bất kì **không phụ thuộc** vào khối lượng của viên bi.'),
  ITEM('b) Tính vận tốc của viên bi tại B và tại C.'),
  ITEM('c) Trên máng có điểm D ở độ cao 1,0 m. Viên bi có lên tới D được không? Giải thích.'),
  Q('Bài 2. (Hóa học – suy luận)', 'Có bốn kim loại W, X, Y, Z là Fe, Cu, Ag, Na (không theo thứ tự). Biết:'),
  ITEM('• W tác dụng mãnh liệt với nước ở nhiệt độ thường.'),
  ITEM('• X không tác dụng với nước ở nhiệt độ thường nhưng tác dụng với dung dịch HCl giải phóng khí H_{2}.'),
  ITEM('• Y và Z không tác dụng với dung dịch HCl; Y đẩy được Z ra khỏi dung dịch muối nitrate của Z.'),
  ITEM('Xác định W, X, Y, Z; sắp xếp chúng theo chiều giảm dần mức độ hoạt động hóa học và viết các phương trình hóa học minh họa.'),
  Q('Bài 3. (English – Science in English)', 'A student of mass 50 kg runs up a staircase of vertical height 6 m in 12 s. Take g = 10 N/kg.'),
  ITEM('(a) Calculate the work done by the student against gravity.'),
  ITEM('(b) Calculate the student\'s average useful power.'),
  ITEM('(c) Assume the human body converts food energy into useful mechanical work with an efficiency of 25%. How much food energy does the student use?'),

  // ---------- ANSWERS ----------
  BR(),
  H('ĐÁP ÁN VÀ HƯỚNG DẪN GIẢI', 'C00000'),
  SUB('Phần II. Trắc nghiệm'),
  table([
    ['Câu', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
    ['Đáp án', 'A', 'C', 'B', 'B', 'C', 'A', 'D', 'A', 'A', 'C'],
  ], [1338, 830, 830, 830, 830, 830, 830, 830, 830, 830, 830]),
  P('*Gợi ý Câu 2:* W_{đ} = ½·2·3² = 9 J. *Câu 3:* W_{đ} tỉ lệ với v² → v tăng 2 lần thì W_{đ} tăng 2² = 4 lần. *Câu 7:* Cu đứng sau H trong dãy hoạt động hóa học.', { run: { size: 24 } }),
  SUB('Phần III. Tự luận'),
  P('**Câu 1.** m = 1200 kg; v = 54 km/h = 15 m/s.'),
  ITEM('a) W_{đ} = ½·1200·15² = 135 000 J = 135 kJ.'),
  ITEM('b) A_{hãm} = W_{đ} ⇒ F·s = 135 000 ⇒ F = 135 000 : 30 = 4 500 N.'),
  P('**Câu 2.** m = 0,2 kg; h_{0} = 1,5 m; v_{0} = 8 m/s.'),
  ITEM('a) W_{t} = 10·0,2·1,5 = 3 J; W_{đ} = ½·0,2·8² = 6,4 J ⇒ W = 9,4 J.'),
  ITEM('b) Tại độ cao cực đại v = 0: 10·0,2·h_{max} = 9,4 ⇒ h_{max} = 4,7 m.'),
  ITEM('c) Khi chạm đất W_{t} = 0: ½·0,2·v² = 9,4 ⇒ v² = 94 ⇒ v ≈ 9,7 m/s.'),
  ITEM('d) W_{đ} = W_{t} ⇒ W_{t} = W/2 = 4,7 J ⇒ 10·0,2·h = 4,7 ⇒ h = 2,35 m.'),
  P('**Câu 3.** P = 10·2500 = 25 000 N.'),
  ITEM('a) A_{ci} = P·h = 25 000·12 = 300 000 J.'),
  ITEM('b) P_{ci} = A/t = 300 000 : 30 = 10 000 W = 10 kW.'),
  ITEM('c) H = 10 : 12,5 × 100% = 80%.'),
  P('**Câu 4.** a) (1) 2Al + 3Cl_{2} →^{t°} 2AlCl_{3}     (2) 2Na + 2H_{2}O → 2NaOH + H_{2}↑'),
  ITEM('(3) 3Fe + 2O_{2} →^{t°} Fe_{3}O_{4}     (4) Mg + H_{2}SO_{4} → MgSO_{4} + H_{2}↑'),
  ITEM('b) Xảy ra: (2) Fe + CuSO_{4} → FeSO_{4} + Cu (Fe hoạt động mạnh hơn Cu); (4) Zn + FeSO_{4} → ZnSO_{4} + Fe (Zn mạnh hơn Fe).'),
  ITEM('Không xảy ra: (1) Cu đứng sau H; (3) Ag kém hoạt động hơn Cu; (5) Fe kém hoạt động hơn Zn.'),
  P('**Câu 5.** n_{Zn} = 6,5 : 65 = 0,1 mol. Zn + 2HCl → ZnCl_{2} + H_{2}↑'),
  ITEM('a) n_{H₂} = 0,1 mol ⇒ V = 0,1·24,79 = 2,479 L.'),
  ITEM('b) n_{HCl} = 0,2 mol ⇒ m_{HCl} = 0,2·36,5 = 7,3 g ⇒ m_{dd HCl} = 7,3·100 : 7,3 = 100 g.'),
  ITEM('c) m_{ZnCl₂} = 0,1·136 = 13,6 g; m_{dd sau} = 6,5 + 100 − 0,1·2 = 106,3 g ⇒ C% = 13,6 : 106,3 × 100% ≈ 12,79%.'),
  P('**Câu 6.** Fe + CuSO_{4} → FeSO_{4} + Cu. Cứ 1 mol Fe phản ứng (56 g tan ra) thì 1 mol Cu (64 g) bám vào ⇒ khối lượng lá tăng 8 g.'),
  ITEM('a) Khối lượng tăng 20,8 − 20 = 0,8 g ⇒ n_{Fe pư} = 0,8 : 8 = 0,1 mol ⇒ m_{Cu} = 6,4 g; m_{Fe pư} = 5,6 g.'),
  ITEM('b) n_{CuSO₄ ban đầu} = 0,2 mol. Sau phản ứng: FeSO_{4} 0,1 mol; CuSO_{4} dư 0,1 mol ⇒ C_{M}(FeSO_{4}) = C_{M}(CuSO_{4}) = 0,1 : 0,2 = 0,5M.'),
  P('**Câu 7.** Chỉ Fe phản ứng: Fe + 2HCl → FeCl_{2} + H_{2}↑; n_{H₂} = 2,479 : 24,79 = 0,1 mol.'),
  ITEM('a) m_{Fe} = 5,6 g ⇒ %Fe = 56%; %Cu = 44%.'),
  ITEM('b) n_{HCl} = 0,2 mol ⇒ V = 0,2 : 1 = 0,2 L = 200 mL.'),
  SUB('Phần IV. Khoa học quanh ta'),
  P('**Câu 8.** m = 1500 kg; v = 72 km/h = 20 m/s.'),
  ITEM('a) W_{đ} = ½·1500·20² = 300 000 J.'),
  ITEM('b) A_{điện} = 60%·300 000 = 180 000 J = 180 000 : 3 600 000 = 0,05 kWh.'),
  ITEM('c) t = A/P = 180 000 : 10 = 18 000 s = 5 giờ.'),
  ITEM('d) Một phần động năng chuyển thành nhiệt năng (ma sát ở phanh, lốp, ổ trục; tỏa nhiệt trong dây dẫn, động cơ, pin) và âm thanh – không thể chuyển hóa hoàn toàn thành điện năng.'),
  P('**Câu 9.** Mỗi giây: m = 100·1000 = 100 000 kg.'),
  ITEM('a) W_{t} = 10·100 000·400 = 4·10^{8} J (= 400 MJ).'),
  ITEM('b) Điện năng mỗi giây = 85%·4·10^{8} = 3,4·10^{8} J ⇒ P = 3,4·10^{8} W = 340 MW.'),
  ITEM('c) A = P·t = 340 MW·5 h = 1 700 MWh.'),
  ITEM('d) Nhà máy đóng vai trò "kho lưu trữ" năng lượng: tích lại điện dư thừa lúc thấp điểm (hoặc khi điện mặt trời, điện gió phát nhiều) và phát lại lúc cao điểm, giúp ổn định lưới điện và tận dụng tốt nguồn năng lượng tái tạo vốn không ổn định theo thời tiết.'),
  P('**Câu 10.**'),
  ITEM('a) Tiết kiệm mỗi kg: 14 − 5%·14 = 13,3 kWh ⇒ 50 kg: 50·13,3 = 665 kWh.'),
  ITEM('b) t = 665 000 Wh : 10 W = 66 500 h ≈ 2 771 ngày ≈ 7,6 năm.'),
  ITEM('c) Nhôm phản ứng với oxygen trong không khí tạo lớp Al_{2}O_{3} rất mỏng, bền, đặc khít, ngăn không cho nhôm bên trong tiếp xúc với không khí và nước: 4Al + 3O_{2} → 2Al_{2}O_{3}. Còn gỉ sắt xốp, dễ bong nên không bảo vệ được lớp sắt bên trong.'),
  SUB('Phần V. Thử thách quốc tế'),
  P('**Bài 1.** a) Cơ năng bảo toàn: 10·m·h_{A} = ½·m·v² + 10·m·h ⇒ v² = 20·(h_{A} − h). Khối lượng m bị triệt tiêu ở hai vế nên v không phụ thuộc m.'),
  ITEM('b) Tại B (h = 0): v² = 20·0,8 = 16 ⇒ v_{B} = 4 m/s. Tại C: v² = 20·(0,8 − 0,35) = 9 ⇒ v_{C} = 3 m/s.'),
  ITEM('c) Không. Muốn tới D cần W_{t} tại D = 10·m·1,0 lớn hơn cơ năng ban đầu 10·m·0,8 – trái với định luật bảo toàn cơ năng. Viên bi chỉ lên tối đa tới độ cao 0,8 m.'),
  P('**Bài 2.** W = Na; X = Fe; Y = Cu; Z = Ag. Thứ tự hoạt động giảm dần: Na > Fe > Cu > Ag.'),
  ITEM('2Na + 2H_{2}O → 2NaOH + H_{2}↑;   Fe + 2HCl → FeCl_{2} + H_{2}↑;   Cu + 2AgNO_{3} → Cu(NO_{3})_{2} + 2Ag'),
  P('**Bài 3.** (a) W = mgh = 50·10·6 = 3 000 J.  (b) P = W/t = 3 000 : 12 = 250 W.  (c) Food energy = 3 000 : 0,25 = 12 000 J = 12 kJ.'),
  P('*(Công chống trọng lực 3 000 J; công suất trung bình 250 W; năng lượng thức ăn tiêu hao 12 kJ.)*'),
];

const doc = new Document({
  styles: { default: { document: { run: { font: FONT, size: SZ } } } },
  numbering: { config: [{ reference: 'bul', levels: [{ level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 400, hanging: 260 } } } }] }] },
  sections: [{
    properties: { page: { size: { width: 11906, height: 16838 }, margin: { top: 1134, bottom: 1134, left: 1134, right: 1134 } } },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [
      new TextRun({ text: 'Phiếu bài tập KHTN 9 – Năng lượng cơ học & Kim loại – Trang ', font: FONT, size: 20, italics: true }),
      new TextRun({ children: [PageNumber.CURRENT], font: FONT, size: 20, italics: true })] })] }) },
    children: body,
  }],
});
Packer.toBuffer(doc).then(b => { fs.writeFileSync('Phieu_BT_day_them_KHTN9_Nang_luong_co_hoc_Kim_loai.docx', b); console.log('ok'); });
