
H('PHẦN II. TRẮC NGHIỆM ĐÚNG/SAI (2 câu)');
add(P('*Trong mỗi ý a), b), c), d) ở mỗi câu, học sinh chọn Đúng (Đ) hoặc Sai (S).*'));
const DS = [
  ['Về quá trình quang hợp và các yếu tố ảnh hưởng đến quang hợp:', [
    ['Chỉ có lá cây mới có khả năng thực hiện quang hợp.', 'S', 'Các bộ phận có màu xanh (chứa diệp lục) như thân non cũng quang hợp được.'],
    ['Nước là nguyên liệu của quang hợp, được rễ cây hút từ đất và vận chuyển qua thân lên lá.', 'Đ', 'SBT 22.5.'],
    ['Trong một giới hạn nhất định, khi tăng hàm lượng khí carbon dioxide thì cường độ quang hợp tăng.', 'Đ', 'CO₂ là nguyên liệu; vượt quá giới hạn thì quang hợp không tăng nữa, thậm chí giảm.'],
    ['Cây ưa sáng có nhu cầu ánh sáng thấp hơn cây ưa bóng.', 'S', 'Cây ưa sáng cần nhiều ánh sáng mạnh.']]],
  ['Thí nghiệm: hai ống nghiệm đổ đầy nước, mỗi ống chứa một cành rong đuôi chó, úp ngược vào hai cốc nước. Cốc A để ngoài nắng, cốc B bọc kín bằng giấy đen. Sau khoảng 6 giờ:', [
    ['Ở ống nghiệm của cốc A có nhiều bọt khí thoát ra từ cành rong và tụ lại ở đáy ống nghiệm (phía trên).', 'Đ', 'Rong quang hợp mạnh dưới ánh sáng, giải phóng khí.'],
    ['Đưa que đóm còn tàn đỏ vào miệng ống nghiệm A, que đóm bùng cháy vì khí thu được là carbon dioxide.', 'S', 'Khí làm que đóm bùng cháy là oxygen (SBT 24.3).'],
    ['Ống nghiệm của cốc B hầu như không có khí vì thiếu ánh sáng, rong không quang hợp.', 'Đ', 'Ánh sáng là điều kiện bắt buộc của quang hợp.'],
    ['Thí nghiệm chứng minh quang hợp đã hấp thụ khí oxygen.', 'S', 'Thí nghiệm chứng minh quang hợp giải phóng khí oxygen.']]],
];
DS.forEach(([q, it], i) => { Q(`Câu ${i + 1}.`, q); it.forEach((x, j) => L(`${'abcd'[j]}) ${x[0]}`)); });

H('PHẦN III. TỰ LUẬN – TRẢ LỜI NGẮN (4 câu)');
Q('Câu 1.', 'Cho các yếu tố: thức ăn, oxygen, carbon dioxide, nhiệt năng, chất thải (phân, nước tiểu), chất hữu cơ, ATP. Hãy xác định những yếu tố mà cơ thể người lấy vào, thải ra và tích lũy trong cơ thể.');
Q('Câu 2.', 'Viết phương trình quang hợp dạng chữ. Giải thích vì sao người ta nói: "Không có quang hợp thì không có sự sống trên Trái Đất".');
Q('Câu 3.', 'Một nhóm học sinh đặt cành rong đuôi chó trong cốc nước và chiếu đèn ở các khoảng cách khác nhau, đếm số bọt khí thoát ra trong 1 phút *(số liệu giả định)*:');
add(table([['Khoảng cách từ đèn đến cành rong (cm)', '10', '20', '30', '40', '50'], ['Số bọt khí/phút', '40', '26', '15', '8', '5']], [3600, ...Array(5).fill(Math.floor((W - 3600) / 5))], { firstCol: true, left: [0] }));
L('a) Nhận xét sự thay đổi số bọt khí khi đèn càng xa cành rong.');
L('b) Giải thích kết quả. Từ đó cho biết ánh sáng ảnh hưởng thế nào đến quang hợp.');
L('c) Nêu một ứng dụng của kết quả này trong trồng trọt.');
Q('Câu 4.', 'Viết phương trình hô hấp tế bào dạng chữ. Lập bảng so sánh quang hợp và hô hấp tế bào theo các tiêu chí: nguyên liệu, sản phẩm, năng lượng, nơi diễn ra (bào quan), điều kiện ánh sáng.');

H('PHẦN IV. BÀI TẬP THỰC TIỄN – SONG NGỮ – THÍ NGHIỆM (2 bài)');
Q('Bài 1 (Thí nghiệm).', 'Cho các bước của thí nghiệm chứng minh tinh bột được tạo thành trong quang hợp (chưa theo thứ tự):');
L('(1) Ngắt lá, bỏ băng giấy đen, đun cách thủy lá trong cồn 90°, rửa sạch bằng nước ấm.');
L('(2) Để chậu cây khoai lang vào chỗ tối hai ngày.');
L('(3) Nhỏ vài giọt dung dịch iodine lên lá và quan sát.');
L('(4) Dùng băng giấy đen bịt kín một phần lá ở cả hai mặt, đặt chậu cây ra chỗ nắng (hoặc chiếu bóng điện) 4 – 6 giờ.');
L('a) Sắp xếp các bước theo đúng trình tự.');
L('b) Nếu bỏ qua bước (2), kết quả thí nghiệm sẽ thay đổi thế nào? Vì sao?');
L('c) Nêu kết quả quan sát được ở bước (3) và rút ra kết luận.');
Q('Bài 2 (Song ngữ – Bilingual).', 'Read the text and answer the questions. *(Đọc đoạn văn và trả lời câu hỏi.)*');
add(P('*"Green plants make their own food by photosynthesis. Chlorophyll in the leaves absorbs light energy. Plants take in water and carbon dioxide, and they produce glucose and release oxygen. All living cells, including plant cells, release energy from glucose by cellular respiration, which uses oxygen and gives out carbon dioxide and water."*', { p: { indent: { left: IND, right: 200 }, spacing: { before: 40, after: 40, line: 264 } } }));
L('a) Translate into Vietnamese: *photosynthesis, chlorophyll, light energy, glucose, cellular respiration.*');
L('b) Write the word equation of photosynthesis in English. *(Viết phương trình chữ của quang hợp bằng tiếng Anh.)*');
L('c) Which process happens in plant cells both during the day and at night: photosynthesis or cellular respiration? Explain briefly. *(Quá trình nào diễn ra cả ngày lẫn đêm? Giải thích ngắn gọn.)*');
add(P('— HẾT PHẦN CÂU HỎI —', { run: { bold: true }, p: { alignment: AlignmentType.CENTER, spacing: { before: 160 } } }));

// ===== C. ĐÁP ÁN =====
add(new Paragraph({ children: [new PageBreak()] }));
add(P('C. ĐÁP ÁN – LỜI GIẢI – HƯỚNG DẪN CHẤM', { run: { bold: true, size: 28 }, p: { alignment: AlignmentType.CENTER, spacing: { after: 60 } } }));
add(P('*Thang điểm tham khảo (10 điểm): Phần I – 4,0 điểm; Phần II – 2,0 điểm; Phần III – 2,0 điểm; Phần IV – 2,0 điểm.*', { p: { alignment: AlignmentType.CENTER, spacing: { after: 80 } } }));
H('PHẦN I. Trắc nghiệm nhiều lựa chọn (4,0 điểm – mỗi câu đúng 0,2 điểm)', 60);
const cw10 = [1300, ...Array(10).fill(Math.floor((W - 1300) / 10))];
add(table([['Câu', ...Array.from({ length: 10 }, (_, i) => String(i + 1))], ['Đáp án', ...ANS.slice(0, 10).split('')],
           ['Câu', ...Array.from({ length: 10 }, (_, i) => String(i + 11))], ['Đáp án', ...ANS.slice(10).split('')]], cw10, { firstCol: true }));
MC.forEach(([, , e], i) => add(P(`**Câu ${i + 1} (${ANS[i]}).** ${e}`, { p: { spacing: { line: 264 } } })));

H('PHẦN II. Trắc nghiệm Đúng/Sai (2,0 điểm – mỗi câu 1,0 điểm)', 120);
add(P('*Điểm mỗi câu: đúng 1 ý – 0,1 điểm; đúng 2 ý – 0,25 điểm; đúng 3 ý – 0,5 điểm; đúng cả 4 ý – 1,0 điểm.*'));
const dsRows = [['Câu', 'Ý', 'Đáp án', 'Giải thích']];
DS.forEach(([_, it], i) => it.forEach((x, j) => dsRows.push([j === 0 ? String(i + 1) : '', 'abcd'[j], x[1], x[2]])));
add(table(dsRows, [800, 700, 1100, W - 2600], { left: [3] }));

H('PHẦN III. Tự luận – trả lời ngắn (2,0 điểm – mỗi câu 0,5 điểm)', 120);
const tl = [
  ['1', 'Lấy vào: thức ăn, oxygen. Thải ra: carbon dioxide, nhiệt năng, chất thải. Tích lũy: chất hữu cơ, ATP (năng lượng). (Đúng 2 nhóm: 0,25 điểm; đúng cả 3 nhóm: 0,5 điểm.)', '0,5'],
  ['2', 'Nước + Carbon dioxide —(ánh sáng, diệp lục)→ Glucose + Oxygen.', '0,25'],
  ['', 'Quang hợp tạo ra chất hữu cơ – nguồn thức ăn, năng lượng cho thực vật và gián tiếp cho động vật, con người; giải phóng oxygen cho hô hấp của hầu hết sinh vật; hấp thụ CO₂, giữ cân bằng khí trong khí quyển.', '0,25'],
  ['3', 'a) Đèn càng xa (cường độ ánh sáng chiếu tới càng yếu) thì số bọt khí càng giảm (40 → 5 bọt/phút).', '0,15'],
  ['', 'b) Bọt khí là oxygen do quang hợp giải phóng; ánh sáng yếu → quang hợp yếu → ít oxygen. Kết luận: trong giới hạn nhất định, cường độ ánh sáng càng mạnh thì quang hợp càng mạnh.', '0,25'],
  ['', 'c) VD: chiếu sáng bổ sung trong nhà kính; trồng cây ưa sáng nơi quang đãng, trồng đúng mật độ để cây không che khuất nhau.', '0,1'],
  ['4', 'Glucose + Oxygen → Carbon dioxide + Nước + Năng lượng (ATP + nhiệt).', '0,1'],
  ['', 'Quang hợp – Hô hấp: Nguyên liệu: nước, CO₂ – glucose, O₂. Sản phẩm: glucose, O₂ – CO₂, nước. Năng lượng: tích lũy (quang năng → hóa năng) – giải phóng (ATP, nhiệt). Nơi diễn ra: lục lạp – ti thể. Ánh sáng: cần ánh sáng – diễn ra cả khi có và không có ánh sáng. (Mỗi tiêu chí đúng: 0,08 điểm.)', '0,4'],
];
add(table([['Câu', 'Lời giải – đáp án', 'Điểm'], ...tl], [800, W - 1800, 1000], { left: [1] }));

H('PHẦN IV. Bài tập thực tiễn – song ngữ – thí nghiệm (2,0 điểm – mỗi bài 1,0 điểm)', 120);
const tt = [
  ['1', 'a) Trình tự: (2) → (4) → (1) → (3).', '0,25'],
  ['', 'b) Nếu không để trong tối, lá vẫn còn tinh bột tạo ra từ trước nên cả phần bị bịt giấy đen cũng có màu xanh tím → không chứng minh được tinh bột chỉ tạo thành khi có ánh sáng (SBT 24.6).', '0,5'],
  ['', 'c) Phần lá được chiếu sáng có màu xanh tím (có tinh bột); phần bịt giấy đen không có màu xanh tím. Kết luận: lá cây chỉ tạo được tinh bột khi có ánh sáng.', '0,25'],
  ['2', 'a) photosynthesis: quang hợp; chlorophyll: diệp lục; light energy: năng lượng ánh sáng (quang năng); glucose: glucose; cellular respiration: hô hấp tế bào.', '0,25'],
  ['', 'b) water + carbon dioxide —(light, chlorophyll)→ glucose + oxygen.', '0,25'],
  ['', 'c) Cellular respiration. Respiration does not need light and all living cells need energy all the time; photosynthesis needs light, so it happens only when there is light. (Hô hấp tế bào diễn ra cả ngày lẫn đêm vì không cần ánh sáng, tế bào luôn cần năng lượng.)', '0,5'],
];
add(table([['Bài', 'Lời giải – đáp án', 'Điểm'], ...tt], [800, W - 1800, 1000], { left: [1] }));
add(P('*Ghi chú: Học sinh trả lời theo cách khác đúng, lập luận chặt chẽ vẫn cho điểm tối đa. Các câu ghi "SBT" được tham khảo, chỉnh sửa từ Sách bài tập KHTN 7.*', { p: { spacing: { before: 100 } } }));

