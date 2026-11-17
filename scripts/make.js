const fs = require('fs');
const { Document, Packer, Paragraph, TextRun, AlignmentType, TabStopType, Table, TableRow, TableCell, WidthType, BorderStyle, ShadingType, Footer, PageNumber, PageBreak, VerticalAlign } = require('docx');

const FONT = 'Times New Roman', SZ = 26; // 13pt
const MARG = 1134, W = 11906 - MARG - 851; // left 2 cm, right 1.5 cm
const T = (t, o = {}) => new TextRun({ text: t, font: FONT, size: SZ, ...o });
// **bold** and *italic* inline markup
const R = (s, base = {}) => s.split(/(\*\*[^*]+\*\*|\*[^*]+\*)/).filter(Boolean).map(x =>
  x.startsWith('**') ? T(x.slice(2, -2), { ...base, bold: true }) : x.startsWith('*') ? T(x.slice(1, -1), { ...base, italics: true }) : T(x, base));
const P = (s, o = {}) => new Paragraph({ children: typeof s === 'string' ? R(s, o.run || {}) : s, spacing: { before: 0, after: 0, line: 264 }, ...o.p });
const out = [];
const add = (...x) => out.push(...x);
const H = (t, before = 160) => add(P(t, { run: { bold: true }, p: { spacing: { before, after: 60, line: 264 } } }));
const Q = (lab, s) => add(P([T(lab + ' ', { bold: true }), ...R(s)], { p: { spacing: { before: 60, after: 0, line: 264 } } }));
const IND = 340;
const L = s => add(P(s, { p: { indent: { left: IND }, spacing: { before: 0, after: 0, line: 264 } } }));
const q4 = [1, 2, 3].map(i => ({ type: TabStopType.LEFT, position: IND + Math.round((W - IND) * i / 4) }));
const q2 = [{ type: TabStopType.LEFT, position: IND + Math.round((W - IND) / 2) }];
const opts = o => {
  const m = Math.max(...o.map(x => x.length));
  const lab = (i) => T('ABCD'[i] + '. ', { bold: true });
  if (m <= 16) add(new Paragraph({ children: o.flatMap((x, i) => [...(i ? [T('\t')] : []), lab(i), ...R(x)]), indent: { left: IND }, tabStops: q4, spacing: { line: 264 } }));
  else if (m <= 40) [0, 2].forEach(k => add(new Paragraph({ children: [lab(k), ...R(o[k]), T('\t'), lab(k + 1), ...R(o[k + 1])], indent: { left: IND }, tabStops: q2, spacing: { line: 264 } })));
  else o.forEach((x, i) => add(new Paragraph({ children: [lab(i), ...R(x)], indent: { left: IND }, spacing: { line: 264 } })));
};
const bd = { style: BorderStyle.SINGLE, size: 4, color: '000000' };
const borders = { top: bd, bottom: bd, left: bd, right: bd };
const table = (rows, cw, opt = {}) => new Table({
  width: { size: cw.reduce((a, b) => a + b), type: WidthType.DXA }, columnWidths: cw,
  rows: rows.map((r, ri) => new TableRow({ children: r.map((c, i) => new TableCell({
    width: { size: cw[i], type: WidthType.DXA }, borders, verticalAlign: VerticalAlign.CENTER,
    shading: (ri === 0 && opt.head !== false) || (opt.firstCol && i === 0) ? { type: ShadingType.CLEAR, fill: 'E7E6E6', color: 'auto' } : undefined,
    margins: { top: 40, bottom: 40, left: 90, right: 90 },
    children: String(c).split('\n').map(line => P(line, { run: ri === 0 && opt.head !== false ? { bold: true } : {}, p: { alignment: (opt.left || []).includes(i) && ri > 0 ? AlignmentType.LEFT : AlignmentType.CENTER, spacing: { line: 252 } } })) })) })) });

// ===== HEADER =====
add(table([['TRƯỜNG THCS THIÊN LỘC\nNHÓM KHOA HỌC TỰ NHIÊN', 'ĐỀ CƯƠNG ÔN TẬP PHÂN MÔN VẬT LÍ – KHTN 6\nNăm học 2026 – 2027']], [Math.round(W * 0.4), W - Math.round(W * 0.4)], { head: false }).constructor === Table ? new Paragraph({}) : null);
out.pop();
add(new Table({ width: { size: W, type: WidthType.DXA }, columnWidths: [Math.round(W * 0.4), W - Math.round(W * 0.4)],
  borders: { top: { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' }, bottom: { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' }, left: { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' }, right: { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' }, insideHorizontal: { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' }, insideVertical: { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' } },
  rows: [new TableRow({ children: [
    new TableCell({ width: { size: Math.round(W * 0.4), type: WidthType.DXA }, borders: { top: { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' }, bottom: { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' }, left: { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' }, right: { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' } },
      children: [P('TRƯỜNG THCS THIÊN LỘC', { p: { alignment: AlignmentType.CENTER } }), P('NHÓM KHOA HỌC TỰ NHIÊN', { run: { bold: true }, p: { alignment: AlignmentType.CENTER } })] }),
    new TableCell({ width: { size: W - Math.round(W * 0.4), type: WidthType.DXA }, borders: { top: { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' }, bottom: { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' }, left: { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' }, right: { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' } },
      children: [P('ĐỀ CƯƠNG ÔN TẬP PHÂN MÔN VẬT LÍ – KHTN 6', { run: { bold: true }, p: { alignment: AlignmentType.CENTER } }), P('Năm học 2026 – 2027', { run: { italics: true }, p: { alignment: AlignmentType.CENTER } })] })] })] }));
add(P('Phạm vi: Bài 5. Đo độ dài – Bài 6. Đo khối lượng – Bài 7. Đo thời gian – Bài 8. Đo nhiệt độ', { run: { bold: true }, p: { alignment: AlignmentType.CENTER, spacing: { before: 160, after: 0 } } }));
add(P('Mức độ: Khá – Giỏi · Gồm 20 câu/bài: 12 trắc nghiệm nhiều lựa chọn, 2 Đúng/Sai, 4 tự luận – trả lời ngắn, 2 bài thực tiễn/song ngữ/thí nghiệm', { run: { italics: true }, p: { alignment: AlignmentType.CENTER, spacing: { after: 80 } } }));

// ===== A. KIẾN THỨC =====
H('A. KIẾN THỨC TRỌNG TÂM', 80);
const kt = [
  ['Đại lượng', 'Đơn vị chuẩn', 'Dụng cụ đo', 'Lưu ý khi đo'],
  ['Độ dài', 'mét (m)\n1 m = 100 cm = 1 000 mm', 'Thước thẳng, thước cuộn, thước dây, thước kẹp', 'Ước lượng → chọn thước có GHĐ, ĐCNN phù hợp → đặt thước dọc theo vật, một đầu ngang vạch 0 → mắt nhìn vuông góc → ghi kết quả theo ĐCNN'],
  ['Khối lượng', 'kilôgam (kg)\n1 tấn = 1 000 kg; 1 lạng = 100 g', 'Cân đồng hồ, cân điện tử, cân y tế, cân đĩa…', 'Hiệu chỉnh cân về số 0 trước khi cân; khối lượng tịnh là khối lượng sản phẩm, không kể bao bì'],
  ['Thời gian', 'giây (s)\n1 h = 60 min = 3 600 s', 'Đồng hồ treo tường, đồng hồ bấm giây, đồng hồ đo thời gian hiện số + cổng quang', 'Hiệu chỉnh đồng hồ về 0; khoảng thời gian ngắn → dùng đồng hồ hiện số; đo nhiều lần lấy trung bình'],
  ['Nhiệt độ', 'Thang Celsius (°C), Kelvin (K), Fahrenheit (°F)', 'Nhiệt kế y tế, nhiệt kế phòng thí nghiệm, nhiệt kế điện tử, hồng ngoại', 'Chọn nhiệt kế có thang đo phù hợp; T(K) = t(°C) + 273; t(°F) = 1,8·t(°C) + 32'],
];
add(table(kt, [1500, 2100, 2500, W - 6100], { left: [1, 2, 3] }));
add(P('• **GHĐ** (giới hạn đo): giá trị lớn nhất ghi trên dụng cụ đo. **ĐCNN** (độ chia nhỏ nhất): giá trị giữa hai vạch chia liên tiếp. Kết quả đo phải ghi theo ĐCNN.', { p: { spacing: { before: 60, line: 264 } } }));
add(P('• Đo **nhiều lần, lấy giá trị trung bình** để giảm sai số; đo vật rất nhỏ/rất nhẹ/thời gian rất ngắn thì đo **nhiều đơn vị cùng lúc rồi chia**.', { p: { spacing: { line: 264 } } }));

// ===== B. CÂU HỎI =====
H('B. CÂU HỎI ÔN TẬP');
H('PHẦN I. TRẮC NGHIỆM NHIỀU LỰA CHỌN (12 câu)', 60);
add(P('*Mỗi câu hỏi có 4 phương án, chỉ có 1 phương án đúng.*'));
const MC = [
  ['Trên một thước thẳng, số lớn nhất ghi trên thước là 30, đơn vị cm. Giữa vạch số 0 và vạch số 1 có thêm 4 vạch chia nhỏ cách đều nhau. GHĐ và ĐCNN của thước lần lượt là', ['30 cm và 1 mm.', '30 cm và 2 mm.', '30 cm và 0,4 cm.', '30 cm và 0,25 cm.']],
  ['Dùng thước có ĐCNN 0,5 cm đo chiều dài cuốn sách. Kết quả nào sau đây được ghi đúng?', ['24,25 cm.', '24,3 cm.', '24,7 cm.', '24,5 cm.']],
  ['Quấn 40 vòng dây đồng sát nhau, không chồng lên nhau trên thân một chiếc bút chì; đo được chiều dài phần dây quấn là 2,0 cm. Đường kính sợi dây đồng là', ['0,5 mm.', '5 mm.', '0,05 mm.', '2 mm.']],
  ['Cho các nguyên nhân gây sai số khi đo độ dài: (1) thước bị cong, vạch chia không đều; (2) đặt mắt nhìn lệch; (3) đặt thước không dọc theo chiều dài vật; (4) một đầu của vật không ngang với vạch số 0. Sai số người đo có thể khắc phục chỉ bằng cách thao tác đúng là', ['(1) và (2).', '(1), (3) và (4).', '(2), (3) và (4).', 'cả (1), (2), (3), (4).']],
  ['Hộp quả cân của một cân đĩa gồm các quả cân: 1 g; 2 g; 2 g; 5 g; 10 g; 20 g; 20 g; 50 g; 100 g; 200 g; 200 g; 500 g. GHĐ và ĐCNN của cân là', ['500 g và 1 g.', '1 000 g và 1 g.', '1 110 g và 1 g.', '1 110 g và 2 g.']],
  ['Một cân đồng hồ khi chưa đặt vật, kim đã chỉ 0,2 kg. Bạn Lan không hiệu chỉnh mà đặt quả bí lên cân, kim chỉ 3,5 kg. Khối lượng thực của quả bí là', ['3,3 kg.', '3,5 kg.', '3,7 kg.', '3,2 kg.']],
  ['Trước một cây cầu có biển báo "10T". Một xe tải có khối lượng 4,5 tấn chở xi măng, mỗi bao 50 kg. Xe được phép chở tối đa bao nhiêu bao xi măng để qua cầu?', ['200 bao.', '90 bao.', '100 bao.', '110 bao.']],
  ['Đồng hồ bấm giây có ĐCNN 0,01 s. Cách ghi kết quả đo nào sau đây đúng?', ['12,3 s.', '12,35 s.', '12,354 s.', '12 s.']],
  ['Một vận động viên xuất phát lúc 7 h 45 min 20 s và về đích lúc 8 h 02 min 05 s. Thời gian chạy của vận động viên là', ['16,45 min.', '1 045 s.', '965 s.', '1 005 s.']],
  ['Để đo thời gian một viên bi lăn qua một đoạn máng ngắn (chỉ khoảng 0,3 s) trong phòng thí nghiệm, nên dùng', ['đồng hồ đo thời gian hiện số kết nối với cổng quang điện.', 'đồng hồ bấm giây cơ học bấm bằng tay.', 'đồng hồ treo tường có kim giây.', 'đồng hồ cát.']],
  ['Để đo nhiệt độ của nước đang sôi (khoảng 100 °C), nên chọn nhiệt kế nào sau đây?', ['Nhiệt kế y tế thủy ngân (35 °C – 42 °C).', 'Nhiệt kế thủy ngân phòng thí nghiệm (–10 °C – 110 °C).', 'Nhiệt kế rượu (–30 °C – 60 °C).', 'Nhiệt kế hồng ngoại đo trán (34 °C – 42 °C).']],
  ['Biết t(°F) = 1,8·t(°C) + 32. Nhiệt độ cơ thể người bình thường 37 °C ứng với bao nhiêu độ Fahrenheit?', ['66,6 °F.', '310 °F.', '98,6 °F.', '69 °F.']],
];
const ANS = 'BDACCADBDABC';
MC.forEach(([q, o], i) => { Q(`Câu ${i + 1}.`, q); opts(o); });

H('PHẦN II. TRẮC NGHIỆM ĐÚNG/SAI (2 câu)');
add(P('*Trong mỗi ý a), b), c), d) ở mỗi câu, học sinh chọn Đúng (Đ) hoặc Sai (S).*'));
const DS = [
  ['Về đo độ dài và đo khối lượng:', [
    ['Khi đo độ dài, kết quả đo phải được ghi theo ĐCNN của thước.', 'Đ', 'Quy tắc ghi kết quả đo.'],
    ['Thước có GHĐ càng lớn thì kết quả đo càng chính xác.', 'S', 'Độ chính xác phụ thuộc ĐCNN; GHĐ chỉ quyết định đo được vật dài tối đa bao nhiêu trong một lần đo.'],
    ['Trên túi gạo ghi "Khối lượng tịnh 5 kg", đó là khối lượng của gạo trong túi, không kể bao bì.', 'Đ', 'Khối lượng tịnh không tính bao bì.'],
    ['Một quả cân 1 kg khi được mang lên Mặt Trăng thì khối lượng của nó chỉ còn khoảng 1/6 kg.', 'S', 'Khối lượng (lượng chất) không đổi; chỉ trọng lượng giảm.']]],
  ['Bạn Minh bị sốt. Mẹ dùng nhiệt kế y tế thủy ngân để đo nhiệt độ cho Minh và đọc được 39 °C.', [
    ['Trước khi đo, cần vẩy mạnh nhiệt kế cho mực thủy ngân tụt xuống dưới vạch 35 °C.', 'Đ', 'Vì nhiệt kế y tế có chỗ thắt, thủy ngân không tự tụt xuống.'],
    ['Nhiệt kế hồng ngoại đo trán cũng hoạt động dựa trên sự nở vì nhiệt của thủy ngân.', 'S', 'Nhiệt kế hồng ngoại đo bức xạ hồng ngoại phát ra từ cơ thể.'],
    ['Nhiệt độ 39 °C ứng với 312 K.', 'Đ', 'T = 39 + 273 = 312 K.'],
    ['Có thể dùng nhiệt kế y tế này để đo nhiệt độ nước đang sôi.', 'S', 'Thang đo chỉ 35 °C – 42 °C; dùng đo nước sôi sẽ làm hỏng (vỡ) nhiệt kế.']]],
];
DS.forEach(([q, it], i) => { Q(`Câu ${i + 1}.`, q); it.forEach((x, j) => L(`${'abcd'[j]}) ${x[0]}`)); });

H('PHẦN III. TỰ LUẬN – TRẢ LỜI NGẮN (4 câu)');
Q('Câu 1.', 'Ba bạn cùng dùng một thước cuộn có GHĐ 2 m, ĐCNN 1 mm để đo chiều dài bàn học, được các kết quả: 120,2 cm; 120,4 cm; 120,3 cm.');
L('a) Tính giá trị trung bình chiều dài bàn học.');
L('b) Vì sao phải đo nhiều lần và lấy giá trị trung bình?');
L('c) Nếu dùng thước thẳng có GHĐ 1 m thì kết quả đo kém chính xác hơn. Giải thích.');
Q('Câu 2.', 'Một cân đĩa thăng bằng khi: đĩa bên trái có 3 gói kẹo giống nhau và một quả cân 50 g; đĩa bên phải có các quả cân 200 g, 100 g và 20 g.');
L('a) Tính khối lượng của một gói kẹo.');
L('b) Nếu 5 gói kẹo trên cân bằng với 2 hộp sữa giống nhau thì mỗi hộp sữa có khối lượng bao nhiêu?');
Q('Câu 3.', 'Chu kì dao động của một con lắc (thời gian con lắc đi một vòng qua lại) chỉ khoảng hơn 1 giây. Bạn Hà dùng đồng hồ bấm giây đo thời gian con lắc thực hiện 20 dao động, được 28,4 s.');
L('a) Tính chu kì dao động của con lắc.');
L('b) Vì sao bạn Hà không đo trực tiếp thời gian của một dao động?');
Q('Câu 4.', 'Rót nước nóng vào cốc và để trong phòng có nhiệt độ 30 °C. Nhiệt độ của nước được ghi lại trong bảng sau:');
add(table([['Thời gian (phút)', '0', '2', '4', '6', '8', '10'], ['Nhiệt độ (°C)', '80', '64', '52', '44', '39', '36']], [2400, ...Array(6).fill(Math.floor((W - 2400 - IND) / 6))], { firstCol: true }));
L('a) Trong khoảng thời gian nào nhiệt độ của nước giảm nhanh nhất? Giảm bao nhiêu độ?');
L('b) Đổi nhiệt độ ban đầu của nước sang thang Kelvin và thang Fahrenheit.');
L('c) Nếu để rất lâu, nhiệt độ của nước sẽ như thế nào? Giải thích.');

H('PHẦN IV. BÀI TẬP THỰC TIỄN – SONG NGỮ – THÍ NGHIỆM (2 bài)');
Q('Bài 1 (Thí nghiệm – STEM).', 'Một hạt gạo rất nhẹ, cân điện tử trong phòng thí nghiệm của trường có ĐCNN 1 g nên không cân trực tiếp được một hạt gạo.');
L('a) Đề xuất phương án (các bước) dùng cân này để xác định khối lượng trung bình của một hạt gạo.');
L('b) Bạn An đếm 200 hạt gạo, cân được 4 g. Tính khối lượng trung bình một hạt gạo theo đơn vị g và mg.');
L('c) Ước tính 1 kg gạo có khoảng bao nhiêu hạt.');
Q('Bài 2 (Song ngữ – Bilingual).', 'Read the text and answer the questions. *(Đọc đoạn văn và trả lời câu hỏi.)*');
add(P('*"Lan travels from Hanoi to New York in summer. In the USA, temperature is usually measured in degrees Fahrenheit (°F). The weather forecast says: Today\'s high temperature is 95 °F and the low temperature is 68 °F. Water freezes at 32 °F and boils at 212 °F."*', { p: { indent: { left: IND, right: 200 }, spacing: { before: 40, after: 40, line: 264 } } }));
L('a) Translate into Vietnamese: *temperature, degrees Fahrenheit, weather forecast, freezes, boils.*');
L('b) Using t(°C) = [t(°F) – 32] : 1,8, convert the high and low temperatures into °C. *(Đổi nhiệt độ cao nhất, thấp nhất sang °C.)*');
L('c) Should Lan wear a thick coat that day? Explain in one sentence (English or Vietnamese). *(Lan có cần mặc áo khoác dày không? Giải thích.)*');
add(P('— HẾT PHẦN CÂU HỎI —', { run: { bold: true }, p: { alignment: AlignmentType.CENTER, spacing: { before: 160 } } }));

// ===== C. ĐÁP ÁN =====
add(new Paragraph({ children: [new PageBreak()] }));
add(P('C. ĐÁP ÁN – LỜI GIẢI – HƯỚNG DẪN CHẤM', { run: { bold: true, size: 28 }, p: { alignment: AlignmentType.CENTER, spacing: { after: 60 } } }));
add(P('*Thang điểm tham khảo (10 điểm): Phần I – 3,0 điểm; Phần II – 2,0 điểm; Phần III – 3,0 điểm; Phần IV – 2,0 điểm.*', { p: { alignment: AlignmentType.CENTER, spacing: { after: 80 } } }));
H('PHẦN I. Trắc nghiệm nhiều lựa chọn (3,0 điểm – mỗi câu đúng 0,25 điểm)', 60);
const cw12 = Array(13).fill(Math.floor(W / 13));
add(table([['Câu', ...Array.from({ length: 12 }, (_, i) => String(i + 1))], ['Đáp án', ...ANS.split('')]], cw12, { firstCol: true }));
const EX = [
  'Từ vạch 0 đến vạch 1 (1 cm) có 4 vạch chia nhỏ → 5 khoảng → ĐCNN = 1 cm : 5 = 0,2 cm = 2 mm; GHĐ = 30 cm.',
  'Kết quả phải là bội của ĐCNN 0,5 cm → chỉ 24,5 cm thỏa mãn.',
  'Chiều dài phần quấn = 40 lần đường kính → d = 2,0 cm : 40 = 0,05 cm = 0,5 mm.',
  'Sai số (1) do dụng cụ, phải thay thước mới khắc phục được; (2), (3), (4) do thao tác, đo đúng cách là khắc phục được.',
  'GHĐ = tổng khối lượng các quả cân = 1 110 g; ĐCNN = khối lượng quả cân nhỏ nhất = 1 g.',
  'Kim lệch sẵn 0,2 kg nên khối lượng thực = 3,5 – 0,2 = 3,3 kg.',
  '"10T": tổng khối lượng xe và hàng không quá 10 tấn → hàng tối đa 10 – 4,5 = 5,5 tấn = 5 500 kg → 5 500 : 50 = 110 bao.',
  'Kết quả ghi theo ĐCNN 0,01 s → có hai chữ số sau dấu phẩy: 12,35 s.',
  '8 h 02 min 05 s – 7 h 45 min 20 s = 16 min 45 s = 16 × 60 + 45 = 1 005 s. (Lưu ý 16 min 45 s ≠ 16,45 min.)',
  'Khoảng thời gian rất ngắn; thời gian phản xạ bấm tay (cỡ 0,1 – 0,3 s) gây sai số lớn → dùng đồng hồ hiện số với cổng quang điện.',
  'Thang đo phải chứa 100 °C. Nhiệt kế rượu không dùng được vì rượu sôi ở khoảng 78 °C.',
  't(°F) = 1,8 × 37 + 32 = 98,6 °F.',
];
EX.forEach((e, i) => add(P(`**Câu ${i + 1} (${ANS[i]}).** ${e}`, { p: { spacing: { line: 264 } } })));

H('PHẦN II. Trắc nghiệm Đúng/Sai (2,0 điểm – mỗi câu 1,0 điểm)', 120);
add(P('*Điểm mỗi câu: đúng 1 ý – 0,1 điểm; đúng 2 ý – 0,25 điểm; đúng 3 ý – 0,5 điểm; đúng cả 4 ý – 1,0 điểm.*'));
const dsRows = [['Câu', 'Ý', 'Đáp án', 'Giải thích']];
DS.forEach(([_, it], i) => it.forEach((x, j) => dsRows.push([j === 0 ? String(i + 1) : '', 'abcd'[j], x[1], x[2]])));
add(table(dsRows, [800, 700, 1100, W - 2600], { left: [3] }));

H('PHẦN III. Tự luận – trả lời ngắn (3,0 điểm – mỗi câu 0,75 điểm)', 120);
const tl = [
  ['1', 'a) Giá trị trung bình: (120,2 + 120,4 + 120,3) : 3 = 120,3 cm.', '0,25'],
  ['', 'b) Mỗi lần đo đều có sai số (đặt thước, đặt mắt…); đo nhiều lần, lấy trung bình giúp giảm sai số, kết quả gần giá trị thật hơn.', '0,25'],
  ['', 'c) Bàn dài hơn 1 m nên thước GHĐ 1 m phải đặt nhiều lần, mỗi lần đặt lại cộng thêm sai số → kém chính xác.', '0,25'],
  ['2', 'a) Cân thăng bằng: 3m + 50 = 200 + 100 + 20 = 320 → 3m = 270 → m = 90 g.', '0,5'],
  ['', 'b) 5 × 90 = 450 g = 2 hộp sữa → mỗi hộp 225 g.', '0,25'],
  ['3', 'a) Chu kì T = 28,4 : 20 = 1,42 s.', '0,25'],
  ['', 'b) Thời gian một dao động rất ngắn, sai số do phản xạ bấm đồng hồ (cỡ 0,1 – 0,3 s) là đáng kể so với 1,4 s. Đo 20 dao động rồi chia 20 thì sai số chia nhỏ 20 lần → kết quả chính xác hơn.', '0,5'],
  ['4', 'a) Từ phút 0 đến phút 2: giảm 80 – 64 = 16 °C (nhanh nhất).', '0,25'],
  ['', 'b) T = 80 + 273 = 353 K; t(°F) = 1,8 × 80 + 32 = 176 °F.', '0,25'],
  ['', 'c) Nhiệt độ nước giảm dần, ngày càng chậm và cuối cùng bằng nhiệt độ phòng (30 °C), vì nước truyền nhiệt cho không khí đến khi bằng nhiệt độ môi trường.', '0,25'],
];
add(table([['Câu', 'Lời giải – đáp án', 'Điểm'], ...tl], [800, W - 1800, 1000], { left: [1] }));

H('PHẦN IV. Bài tập thực tiễn – song ngữ – thí nghiệm (2,0 điểm – mỗi bài 1,0 điểm)', 120);
const tt = [
  ['1', 'a) Đếm một số lượng lớn hạt gạo (VD 200 hạt) → đặt lên cân (đã hiệu chỉnh về 0) → đọc khối lượng → chia cho số hạt. Có thể lặp lại 2 – 3 lần, lấy trung bình.', '0,5'],
  ['', 'b) m = 4 g : 200 = 0,02 g = 20 mg.', '0,25'],
  ['', 'c) Số hạt trong 1 kg = 1 000 g : 0,02 g = 50 000 hạt.', '0,25'],
  ['2', 'a) temperature: nhiệt độ; degrees Fahrenheit: độ F (thang Fahrenheit); weather forecast: dự báo thời tiết; freezes: đóng băng; boils: sôi.', '0,25'],
  ['', 'b) Cao nhất: (95 – 32) : 1,8 = 35 °C; thấp nhất: (68 – 32) : 1,8 = 20 °C.', '0,5'],
  ['', 'c) No. The weather is hot (20 °C – 35 °C), so Lan does not need a thick coat. (Không cần, vì trời nóng.)', '0,25'],
];
add(table([['Bài', 'Lời giải – đáp án', 'Điểm'], ...tt], [800, W - 1800, 1000], { left: [1] }));
add(P('*Ghi chú: Học sinh giải cách khác đúng, lập luận chặt chẽ vẫn cho điểm tối đa.*', { p: { spacing: { before: 100 } } }));

const doc = new Document({
  styles: { default: { document: { run: { font: FONT, size: SZ } } } },
  sections: [{ properties: { page: { size: { width: 11906, height: 16838 }, margin: { top: 1000, bottom: 1000, left: MARG, right: 851 } } },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [T('Đề cương Vật lí 6 – Trang ', { size: 20 }), new TextRun({ children: [PageNumber.CURRENT], font: FONT, size: 20 })] })] }) },
    children: out }],
});
Packer.toBuffer(doc).then(b => { fs.writeFileSync('DE_CUONG_VAT_LI_6_BAI_5_8.docx', b); console.log('ok'); });
