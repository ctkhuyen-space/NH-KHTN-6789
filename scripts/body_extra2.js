
H('PHẦN II. TRẮC NGHIỆM ĐÚNG/SAI (2 câu)');
add(P('*Trong mỗi ý a), b), c), d) ở mỗi câu, học sinh chọn Đúng (Đ) hoặc Sai (S).*'));
const DS = [
  ['Về quá trình tiêu hóa thức ăn ở người:', [
    ['Ở khoang miệng, enzyme amylase biến đổi một phần tinh bột chín thành đường maltose.', 'Đ', 'Tiêu hóa hóa học ở miệng.'],
    ['Dạ dày là nơi hấp thụ chủ yếu các chất dinh dưỡng.', 'S', 'Ruột non mới là nơi hấp thụ chủ yếu.'],
    ['Ở ruột non, thức ăn được biến đổi hoàn toàn thành các chất đơn giản nhờ dịch tụy, dịch mật và dịch ruột.', 'Đ', 'Ruột non là nơi tiêu hóa hóa học quan trọng nhất.'],
    ['Ruột già tiết ra nhiều enzyme để tiêu hóa protein.', 'S', 'Ruột già chủ yếu hấp thụ nước và tạo, thải phân.']]],
  ['Một bệnh nhân có nhóm máu AB cần truyền máu gấp. Có 4 người tình nguyện cho máu với nhóm máu A, B, AB, O (đã xét nghiệm không mang mầm bệnh).', [
    ['Hồng cầu của người có nhóm máu AB có cả kháng nguyên A và kháng nguyên B.', 'Đ', 'Đặc điểm nhóm máu AB.'],
    ['Huyết tương của người có nhóm máu AB có cả kháng thể α và β.', 'S', 'Nhóm AB không có kháng thể α, β.'],
    ['Về nguyên tắc, cả 4 người trên đều có thể truyền máu cho bệnh nhân.', 'Đ', 'Huyết tương nhóm AB không có kháng thể nên không làm ngưng kết hồng cầu người cho (thực tế ưu tiên truyền cùng nhóm).'],
    ['Người có nhóm máu AB có thể truyền máu cho người có nhóm máu O.', 'S', 'Huyết tương nhóm O có α và β sẽ làm ngưng kết hồng cầu nhóm AB.']]],
];
DS.forEach(([q, it], i) => { Q(`Câu ${i + 1}.`, q); it.forEach((x, j) => L(`${'abcd'[j]}) ${x[0]}`)); });

H('PHẦN III. TỰ LUẬN – TRẢ LỜI NGẮN (4 câu)');
Q('Câu 1.', 'Hoàn thành bảng sau:');
add(table([['Hệ cơ quan', 'Các cơ quan chính', 'Chức năng chính'], ['Hệ tiêu hóa', '', ''], ['Hệ tuần hoàn', '', ''], ['Hệ hô hấp', '', ''], ['Hệ bài tiết', '', ''], ['Hệ thần kinh', '', '']], [2200, 3200, W - 5400], { left: [0] }));
Q('Câu 2.', 'Vì sao nói ruột non là nơi hấp thụ chủ yếu các chất dinh dưỡng? Nêu các đặc điểm cấu tạo của ruột non phù hợp với chức năng hấp thụ.');
Q('Câu 3.', 'Bữa trưa của bạn Nam (học sinh lớp 8) cung cấp 80 g carbohydrate, 25 g protein và 15 g lipid. Biết 1 g carbohydrate cung cấp 4,3 kcal; 1 g protein cung cấp 4,1 kcal; 1 g lipid cung cấp 9,3 kcal.');
L('a) Tính năng lượng bữa trưa cung cấp cho Nam.');
L('b) Giả sử nhu cầu năng lượng của Nam là 2 300 kcal/ngày, bữa trưa đáp ứng khoảng bao nhiêu phần trăm nhu cầu?');
L('c) Nêu nguyên tắc lập khẩu phần ăn hằng ngày.');
Q('Câu 4.', 'Kết quả đo huyết áp của ông bạn Lan là 150/95 mmHg.');
L('a) Hai con số 150 và 95 cho biết điều gì?');
L('b) Biết huyết áp ở mức bình thường của người trưởng thành khoảng dưới 120/80 mmHg và được xem là tăng huyết áp khi từ 140/90 mmHg trở lên. Nhận xét kết quả đo của ông bạn Lan.');
L('c) Đề xuất 3 lời khuyên giúp ông phòng tránh biến chứng của bệnh.');

H('PHẦN IV. BÀI TẬP THỰC TIỄN – SONG NGỮ – THÍ NGHIỆM (2 bài)');
Q('Bài 1 (Thực tiễn – An toàn thực phẩm).', 'Trên một hộp sữa chua có ghi: "Ngày sản xuất: 01/10/2026. Hạn sử dụng: 30 ngày kể từ ngày sản xuất. Bảo quản lạnh ở 2 °C – 6 °C."');
L('a) Hộp sữa chua còn hạn sử dụng đến ngày nào?');
L('b) Ngày 14/10/2026, Hà thấy hộp sữa chua bị để quên ngoài tủ lạnh qua đêm, nắp hộp bị phồng lên. Hà có nên ăn hộp sữa chua đó không? Giải thích.');
L('c) Nêu 3 việc em và gia đình nên làm để bảo quản, chế biến thực phẩm an toàn.');
Q('Bài 2 (Song ngữ – Bilingual).', 'Read the text and answer the questions. *(Đọc đoạn văn và trả lời câu hỏi.)*');
add(P('*"Blood is made of plasma and blood cells. Red blood cells carry oxygen, white blood cells protect the body against germs, and platelets help the blood to clot. In the ABO system, there are four blood groups: A, B, AB and O. People with blood group O are often called universal donors, while people with blood group AB are called universal recipients."*', { p: { indent: { left: IND, right: 200 }, spacing: { before: 40, after: 40, line: 264 } } }));
L('a) Translate into Vietnamese: *plasma, red blood cells, white blood cells, platelets, blood group.*');
L('b) Why are people with blood group O called "universal donors"? *(Giải thích bằng tiếng Việt.)*');
L('c) Which blood cells help to stop bleeding when you cut your finger? *(Trả lời bằng tiếng Anh.)*');
add(P('— HẾT PHẦN CÂU HỎI —', { run: { bold: true }, p: { alignment: AlignmentType.CENTER, spacing: { before: 160 } } }));

// ===== C. ĐÁP ÁN =====
add(new Paragraph({ children: [new PageBreak()] }));
add(P('C. ĐÁP ÁN – LỜI GIẢI – HƯỚNG DẪN CHẤM', { run: { bold: true, size: 28 }, p: { alignment: AlignmentType.CENTER, spacing: { after: 60 } } }));
add(P('*Thang điểm tham khảo (10 điểm): Phần I – 3,0 điểm; Phần II – 2,0 điểm; Phần III – 3,0 điểm; Phần IV – 2,0 điểm.*', { p: { alignment: AlignmentType.CENTER, spacing: { after: 80 } } }));
H('PHẦN I. Trắc nghiệm nhiều lựa chọn (3,0 điểm – mỗi câu đúng 0,25 điểm)', 60);
const cw12 = [1300, ...Array(12).fill(Math.floor((W - 1300) / 12))];
add(table([['Câu', ...Array.from({ length: 12 }, (_, i) => String(i + 1))], ['Đáp án', ...ANS.split('')]], cw12, { firstCol: true }));
MC.forEach(([, , e], i) => add(P(`**Câu ${i + 1} (${ANS[i]}).** ${e}`, { p: { spacing: { line: 264 } } })));

H('PHẦN II. Trắc nghiệm Đúng/Sai (2,0 điểm – mỗi câu 1,0 điểm)', 120);
add(P('*Điểm mỗi câu: đúng 1 ý – 0,1 điểm; đúng 2 ý – 0,25 điểm; đúng 3 ý – 0,5 điểm; đúng cả 4 ý – 1,0 điểm.*'));
const dsRows = [['Câu', 'Ý', 'Đáp án', 'Giải thích']];
DS.forEach(([_, it], i) => it.forEach((x, j) => dsRows.push([j === 0 ? String(i + 1) : '', 'abcd'[j], x[1], x[2]])));
add(table(dsRows, [800, 700, 1100, W - 2600], { left: [3] }));

H('PHẦN III. Tự luận – trả lời ngắn (3,0 điểm – mỗi câu 0,75 điểm)', 120);
const tl = [
  ['1', 'Tiêu hóa: ống tiêu hóa (miệng, thực quản, dạ dày, ruột…) và tuyến tiêu hóa – biến đổi thức ăn, hấp thụ chất dinh dưỡng. Tuần hoàn: tim, hệ mạch – vận chuyển các chất. Hô hấp: đường dẫn khí, phổi – trao đổi khí. Bài tiết: thận, da, phổi – thải chất thải, duy trì môi trường trong. Thần kinh: não, tủy sống, dây thần kinh – tiếp nhận, xử lí thông tin, điều khiển hoạt động. (Mỗi hệ đúng: 0,15 điểm.)', '0,75'],
  ['2', 'Ở ruột non thức ăn đã được biến đổi hoàn toàn thành chất đơn giản; phần lớn chất dinh dưỡng được hấp thụ tại đây.', '0,25'],
  ['', 'Đặc điểm: ruột non rất dài; niêm mạc có nhiều nếp gấp, lông ruột và lông cực nhỏ → diện tích bề mặt hấp thụ rất lớn; mạng mao mạch máu và mạch bạch huyết dày đặc; lớp tế bào lót mỏng.', '0,5'],
  ['3', 'a) E = 80 × 4,3 + 25 × 4,1 + 15 × 9,3 = 344 + 102,5 + 139,5 = 586 kcal.', '0,25'],
  ['', 'b) 586 : 2 300 × 100% ≈ 25,5%.', '0,25'],
  ['', 'c) Đáp ứng đủ nhu cầu năng lượng và chất dinh dưỡng; cân đối các nhóm chất (carbohydrate, protein, lipid, vitamin, chất khoáng, nước); phù hợp lứa tuổi, giới tính, trạng thái sinh lí, mức độ hoạt động; đa dạng thực phẩm.', '0,25'],
  ['4', 'a) 150 mmHg: huyết áp tối đa (lúc tim co); 95 mmHg: huyết áp tối thiểu (lúc tim giãn).', '0,25'],
  ['', 'b) 150 ≥ 140 và 95 ≥ 90 → ông bị tăng huyết áp (cao huyết áp).', '0,25'],
  ['', 'c) Ăn nhạt, hạn chế mỡ động vật, đồ ngọt; không hút thuốc, hạn chế rượu bia; tập thể dục vừa sức đều đặn; đo huyết áp thường xuyên, khám và dùng thuốc theo chỉ định của bác sĩ. (Nêu đúng 3 ý.)', '0,25'],
];
add(table([['Câu', 'Lời giải – đáp án', 'Điểm'], ...tl], [800, W - 1800, 1000], { left: [1] }));

H('PHẦN IV. Bài tập thực tiễn – song ngữ – thí nghiệm (2,0 điểm – mỗi bài 1,0 điểm)', 120);
const tt = [
  ['1', 'a) Hạn sử dụng đến ngày 31/10/2026.', '0,25'],
  ['', 'b) Không nên ăn. Dù còn hạn nhưng sữa chua để ở nhiệt độ cao qua đêm, nắp phồng là dấu hiệu vi sinh vật phát triển mạnh, sinh khí → thực phẩm đã hỏng, có nguy cơ gây ngộ độc.', '0,5'],
  ['', 'c) VD: bảo quản lạnh thực phẩm dễ hỏng; để riêng thực phẩm sống và chín, dùng thớt, dao riêng; nấu chín kĩ; rửa tay trước khi chế biến và ăn; đọc kĩ nhãn, hạn sử dụng; không dùng thực phẩm ôi thiu, mốc. (Nêu đúng 3 ý.)', '0,25'],
  ['2', 'a) plasma: huyết tương; red blood cells: hồng cầu; white blood cells: bạch cầu; platelets: tiểu cầu; blood group: nhóm máu.', '0,25'],
  ['', 'b) Hồng cầu nhóm O không có kháng nguyên A và B nên không bị kháng thể trong huyết tương người nhận làm ngưng kết → về nguyên tắc có thể truyền cho các nhóm máu khác (truyền ít và chậm; thực tế ưu tiên truyền cùng nhóm).', '0,5'],
  ['', 'c) Platelets.', '0,25'],
];
add(table([['Bài', 'Lời giải – đáp án', 'Điểm'], ...tt], [800, W - 1800, 1000], { left: [1] }));
add(P('*Ghi chú: Học sinh trả lời theo cách khác đúng, lập luận chặt chẽ vẫn cho điểm tối đa. Nội dung bám theo yêu cầu cần đạt Bài 30, 32, 33 trong tài liệu ôn tập KHTN 8 (phần Vật sống).*', { p: { spacing: { before: 100 } } }));

