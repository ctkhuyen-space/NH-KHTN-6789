add(P('Phạm vi: Bài 1. Giới thiệu về Khoa học tự nhiên – Bài 2. An toàn trong phòng thực hành –', { run: { bold: true }, p: { alignment: AlignmentType.CENTER, spacing: { before: 160, after: 0 } } }));
add(P('Bài 3. Sử dụng kính lúp – Bài 4. Sử dụng kính hiển vi quang học – Bài 18. Tế bào – đơn vị cơ bản', { run: { bold: true }, p: { alignment: AlignmentType.CENTER } }));
add(P('của sự sống – Bài 19. Cấu tạo và chức năng các thành phần của tế bào – Bài 20. Sự lớn lên và sinh sản của tế bào', { run: { bold: true }, p: { alignment: AlignmentType.CENTER } }));
add(P('Mức độ: Khá – Giỏi · Gồm 28 câu/bài: 20 trắc nghiệm nhiều lựa chọn, 2 Đúng/Sai, 4 tự luận – trả lời ngắn, 2 bài thực tiễn/song ngữ/thí nghiệm', { run: { italics: true }, p: { alignment: AlignmentType.CENTER, spacing: { after: 80 } } }));

// ===== A. KIẾN THỨC =====
H('A. KIẾN THỨC TRỌNG TÂM', 80);
const kt = [
  ['Bài', 'Kiến thức cần nhớ'],
  ['1. Giới thiệu về KHTN', 'KHTN nghiên cứu các sự vật, hiện tượng, quy luật tự nhiên và ảnh hưởng của chúng đến con người, môi trường. Các lĩnh vực chính: Vật lí, Hóa học, Sinh học, Khoa học Trái Đất, Thiên văn học. Vật sống có trao đổi chất, sinh trưởng, phát triển, cảm ứng, sinh sản; vật không sống thì không.'],
  ['2. An toàn trong phòng thực hành', 'Biển báo cấm: hình tròn, nền trắng, viền đỏ; biển cảnh báo nguy hiểm: tam giác đều, nền vàng, viền đen; biển bắt buộc thực hiện: hình tròn, nền xanh. Không nếm, ngửi trực tiếp hóa chất; dùng đồ bảo hộ; báo ngay cho giáo viên khi có sự cố.'],
  ['3. Kính lúp', 'Gồm tay cầm, khung và tấm kính lồi (thấu kính hội tụ); phóng to ảnh của vật khoảng 3 – 20 lần. Cách dùng: đặt kính gần vật, điều chỉnh khoảng cách đến khi nhìn rõ. Bảo quản: lau bằng khăn mềm, tránh làm xước mặt kính.'],
  ['4. Kính hiển vi quang học', 'Phóng to khoảng 40 – 3 000 lần. Gồm hệ thống phóng đại (thị kính, vật kính), hệ thống chiếu sáng (đèn/gương, màng chắn sáng), hệ thống điều chỉnh (ốc to, ốc nhỏ), hệ thống giá đỡ (chân, thân, bàn kính, kẹp). Độ phóng đại = độ phóng đại thị kính × độ phóng đại vật kính.'],
  ['18. Tế bào', 'Tế bào là đơn vị cấu trúc và chức năng của cơ thể sống. Hình dạng, kích thước đa dạng, phù hợp chức năng; phần lớn có kích thước 10 – 100 µm, phải dùng kính hiển vi; một số tế bào lớn nhìn được bằng mắt thường (trứng cá chép, trứng ếch…).'],
  ['19. Thành phần tế bào', 'Màng tế bào: bao bọc, kiểm soát các chất ra vào. Tế bào chất: nơi diễn ra hầu hết hoạt động sống. Nhân/vùng nhân: chứa vật chất di truyền, điều khiển hoạt động sống. Tế bào nhân sơ (vi khuẩn): chưa có màng nhân. Tế bào nhân thực: có nhân hoàn chỉnh. Tế bào thực vật có thành tế bào, lục lạp, không bào trung tâm.'],
  ['20. Lớn lên và sinh sản', 'Tế bào lớn lên nhờ trao đổi chất; đến kích thước nhất định thì phân chia: nhân phân chia trước, tế bào chất phân chia sau → 1 tế bào mẹ tạo 2 tế bào con. Sau n lần phân chia: 1 tế bào → 2ⁿ tế bào. Ý nghĩa: cơ thể lớn lên, thay thế tế bào già, chết, tổn thương.'],
];
add(table(kt, [2300, W - 2300], { left: [1] }));

// ===== B. CÂU HỎI =====
H('B. CÂU HỎI ÔN TẬP');
H('PHẦN I. TRẮC NGHIỆM NHIỀU LỰA CHỌN (20 câu)', 60);
add(P('*Mỗi câu hỏi có 4 phương án, chỉ có 1 phương án đúng.*'));
// đáp án đúng đánh dấu *, sẽ được xoay vòng để phân bố đều A, B, C, D
const MC0 = [
  ['Đối tượng nghiên cứu nào sau đây thuộc lĩnh vực Sinh học?', ['Sự chuyển động của các hành tinh.', 'Tính chất của kim loại.', '*Quá trình quang hợp ở cây xanh.', 'Sự hình thành mưa.'], 'Quang hợp là hoạt động sống của thực vật → Sinh học.'],
  ['Hoạt động nào sau đây <b>không</b> phải là hoạt động nghiên cứu khoa học tự nhiên?', ['Tìm hiểu vì sao lá cây chuyển vàng vào mùa thu.', 'Đo nhiệt độ sôi của nước ở các độ cao khác nhau.', 'Nghiên cứu chế tạo vaccine phòng bệnh.', '*Sáng tác một bài hát về mùa thu.'], 'Sáng tác âm nhạc là hoạt động nghệ thuật, không nghiên cứu sự vật, hiện tượng tự nhiên.'],
  ['Dấu hiệu nào sau đây giúp phân biệt vật sống với vật không sống?', ['Có khối lượng và kích thước.', '*Có trao đổi chất, sinh trưởng và sinh sản.', 'Có khả năng chuyển động.', 'Được cấu tạo từ các chất.'], 'Vật không sống cũng có khối lượng, có thể chuyển động (ô tô), được cấu tạo từ các chất; chỉ vật sống mới trao đổi chất, sinh trưởng, sinh sản.'],
  ['Biển báo có dạng hình tam giác đều, nền vàng, viền đen trong phòng thực hành là', ['biển báo cấm.', '*biển cảnh báo nguy hiểm.', 'biển bắt buộc thực hiện.', 'biển chỉ dẫn thoát hiểm.'], 'Biển cảnh báo nguy hiểm: tam giác đều, nền vàng, viền đen.'],
  ['Khi làm thí nghiệm, cồn trong đèn cồn bị đổ ra và bắt cháy trên mặt bàn. Việc làm đúng là', ['dội nước thật nhiều lên ngọn lửa.', '*dùng khăn ướt hoặc cát phủ lên ngọn lửa và báo ngay cho giáo viên.', 'dùng miệng thổi tắt ngọn lửa.', 'mở cửa sổ cho gió thổi tắt ngọn lửa.'], 'Khăn ướt/cát ngăn tiếp xúc với không khí làm tắt lửa; dội nước có thể làm cồn cháy loang rộng; gió làm lửa cháy mạnh hơn.'],
  ['Việc làm nào sau đây là đúng khi làm việc trong phòng thực hành?', ['Nếm thử hóa chất để nhận biết.', 'Ngửi trực tiếp miệng lọ hóa chất.', '*Đeo kính, găng tay khi làm thí nghiệm với hóa chất; rửa tay sau khi thực hành.', 'Đổ hóa chất thừa trở lại lọ đựng ban đầu.'], 'Quy tắc an toàn: dùng đồ bảo hộ, vệ sinh sau thực hành; không nếm, ngửi trực tiếp, không đổ hóa chất thừa vào lọ.'],
  ['Kính lúp có thể phóng to ảnh của vật khoảng', ['*3 – 20 lần.', '40 – 3 000 lần.', '100 – 1 000 lần.', '1 – 2 lần.'], 'Kính lúp: 3 – 20 lần; kính hiển vi quang học: 40 – 3 000 lần.'],
  ['Đối tượng nào sau đây thích hợp để quan sát bằng kính lúp?', ['Tế bào vi khuẩn.', 'Các bào quan bên trong tế bào lá.', '*Gân lá, nhụy hoa, cấu tạo ngoài của con kiến.', 'Tế bào hồng cầu người.'], 'Kính lúp chỉ phóng to 3 – 20 lần, phù hợp vật nhỏ nhưng vẫn thấy được bằng mắt thường; tế bào phải dùng kính hiển vi.'],
  ['Bộ phận nào của kính hiển vi quang học thuộc hệ thống phóng đại?', ['Ốc to, ốc nhỏ.', 'Đèn chiếu sáng, màng chắn sáng.', 'Bàn kính, kẹp giữ tiêu bản.', '*Thị kính, vật kính.'], 'Hệ thống phóng đại gồm thị kính và vật kính.'],
  ['Quan sát tiêu bản bằng kính hiển vi có thị kính ghi 10x và vật kính ghi 40x. Ảnh của mẫu vật được phóng to', ['50 lần.', '4 lần.', '*400 lần.', '4 000 lần.'], 'Độ phóng đại = 10 × 40 = 400 lần.'],
  ['Khi vặn ốc to để hạ vật kính xuống gần sát tiêu bản, mắt người quan sát phải', ['*nhìn từ bên ngoài, ngang bàn kính, để vật kính không chạm vào tiêu bản.', 'nhìn vào thị kính.', 'nhắm lại.', 'nhìn vào đèn chiếu sáng.'], 'Nhìn từ bên ngoài để tránh vật kính chạm làm vỡ tiêu bản và hỏng vật kính.'],
  ['Sau khi đã nhìn thấy mẫu vật qua thị kính, để ảnh rõ nét nhất ta cần vặn', ['ốc to.', '*ốc nhỏ (ốc điều chỉnh tinh).', 'đĩa quay gắn vật kính.', 'kẹp giữ tiêu bản.'], 'Ốc nhỏ dùng để điều chỉnh tinh, làm ảnh rõ nét.'],
  ['Phát biểu nào sau đây đúng về tế bào?', ['*Tế bào là đơn vị cấu trúc và chức năng của cơ thể sống.', 'Tế bào chỉ có ở cơ thể động vật.', 'Tế bào là đơn vị cấu tạo của mọi vật, kể cả vật không sống.', 'Mọi tế bào đều có hình dạng và kích thước giống nhau.'], 'Mọi cơ thể sống đều được cấu tạo từ tế bào; tế bào có hình dạng, kích thước đa dạng.'],
  ['Tế bào nào sau đây có thể quan sát được bằng mắt thường?', ['Tế bào vi khuẩn E. coli.', 'Tế bào hồng cầu người.', 'Tế bào biểu bì vảy hành.', '*Tế bào trứng cá chép.'], 'Trứng cá chép, trứng ếch là những tế bào lớn, nhìn được bằng mắt thường; các tế bào còn lại cần kính hiển vi.'],
  ['Thành phần nào của tế bào chứa vật chất di truyền và điều khiển hầu hết các hoạt động sống của tế bào?', ['Màng tế bào.', 'Tế bào chất.', '*Nhân tế bào.', 'Thành tế bào.'], 'Nhân (hoặc vùng nhân) chứa vật chất di truyền, là trung tâm điều khiển.'],
  ['Đặc điểm nào sau đây là của tế bào nhân sơ?', ['Có nhân hoàn chỉnh được bao bọc bởi màng nhân.', '*Chưa có màng nhân, vật chất di truyền nằm ở vùng nhân.', 'Có lục lạp để quang hợp.', 'Chỉ có ở tế bào thực vật.'], 'Tế bào nhân sơ (vi khuẩn) chưa có màng nhân.'],
  ['Bào quan nào sau đây có ở tế bào thực vật mà <b>không</b> có ở tế bào động vật?', ['Nhân tế bào.', 'Màng tế bào.', 'Tế bào chất.', '*Lục lạp.'], 'Lục lạp chứa diệp lục, giúp tế bào thực vật quang hợp; tế bào động vật không có.'],
  ['Khi một tế bào phân chia, thành phần nào phân chia trước?', ['*Nhân tế bào.', 'Tế bào chất.', 'Màng tế bào.', 'Thành tế bào.'], 'Nhân phân chia trước, sau đó tế bào chất phân chia, tạo hai tế bào con.'],
  ['Có 3 tế bào cùng thực hiện phân chia liên tiếp 3 lần. Tổng số tế bào con được tạo ra là', ['9.', '18.', '*24.', '27.'], 'Mỗi tế bào sau 3 lần tạo 2³ = 8 tế bào → 3 × 8 = 24.'],
  ['Ý nghĩa của sự lớn lên và sinh sản của tế bào đối với cơ thể là', ['làm cơ thể nhỏ lại.', '*giúp cơ thể lớn lên, thay thế các tế bào già, chết hoặc bị tổn thương.', 'chỉ giúp tạo ra cá thể mới.', 'làm giảm số lượng tế bào trong cơ thể.'], 'Tăng số lượng, kích thước tế bào → cơ thể lớn lên; thay thế tế bào già, chết, tổn thương.'],
];
// xoay vòng phương án để đáp án đúng phân bố đều 5A – 5B – 5C – 5D
const TARGET = 'BDACCADBABDCDBACCADB';
const MC = MC0.map(([q, o, e], i) => {
  const ci = o.findIndex(x => x.startsWith('*')); const clean = o.map(x => x.replace(/^\*/, ''));
  const t = 'ABCD'.indexOf(TARGET[i]); const s = (t - ci + 4) % 4;
  const rot = s ? [...clean.slice(4 - s), ...clean.slice(0, 4 - s)] : clean;
  return [q, rot, e];
});
const ANS = TARGET;
MC.forEach(([q, o], i) => { Q(`Câu ${i + 1}.`, q.replace(/<\/?b>/g, '**')); opts(o); });

H('PHẦN II. TRẮC NGHIỆM ĐÚNG/SAI (2 câu)');
add(P('*Trong mỗi ý a), b), c), d) ở mỗi câu, học sinh chọn Đúng (Đ) hoặc Sai (S).*'));
const DS = [
  ['Bạn Lan thực hành quan sát tế bào biểu bì vảy hành bằng kính hiển vi quang học.', [
    ['Khi di chuyển kính hiển vi, Lan dùng một tay cầm thân kính, tay kia đỡ chân kính.', 'Đ', 'Cách cầm, di chuyển kính đúng, tránh rơi vỡ.'],
    ['Với thị kính 10x và vật kính 40x, ảnh tế bào được phóng to 50 lần.', 'S', 'Độ phóng đại = 10 × 40 = 400 lần.'],
    ['Lan nên quan sát bằng vật kính có độ phóng đại nhỏ trước, sau đó mới chuyển sang vật kính có độ phóng đại lớn hơn.', 'Đ', 'Vật kính nhỏ có trường nhìn rộng, dễ tìm mẫu vật.'],
    ['Sau khi dùng, có thể lau vật kính bằng khăn giấy thô hoặc vạt áo.', 'S', 'Phải dùng giấy lau kính chuyên dụng, tránh xước thấu kính.']]],
  ['So sánh tế bào lá cây (tế bào thực vật) và tế bào niêm mạc miệng người (tế bào động vật):', [
    ['Cả hai loại tế bào đều có màng tế bào, tế bào chất và nhân.', 'Đ', 'Đều là tế bào nhân thực, có đủ ba thành phần chính.'],
    ['Tế bào lá cây có lục lạp nên có khả năng quang hợp.', 'Đ', 'Lục lạp chứa diệp lục.'],
    ['Tế bào niêm mạc miệng có thành tế bào bao bên ngoài màng tế bào.', 'S', 'Tế bào động vật không có thành tế bào.'],
    ['Cả hai đều là tế bào nhân sơ.', 'S', 'Cả hai là tế bào nhân thực (có màng nhân).']]],
];
DS.forEach(([q, it], i) => { Q(`Câu ${i + 1}.`, q); it.forEach((x, j) => L(`${'abcd'[j]}) ${x[0]}`)); });

H('PHẦN III. TỰ LUẬN – TRẢ LỜI NGẮN (4 câu)');
Q('Câu 1.', 'Cho các hoạt động nghiên cứu: (1) nghiên cứu vaccine phòng bệnh; (2) tìm hiểu nguyên nhân gây động đất; (3) nghiên cứu phản ứng giữa kim loại và acid; (4) nghiên cứu chuyển động của Mặt Trăng quanh Trái Đất; (5) lai tạo giống lúa chịu mặn; (6) đo tốc độ âm thanh trong không khí. Hãy xếp các hoạt động trên vào đúng lĩnh vực của Khoa học tự nhiên.');
Q('Câu 2.', 'Nêu các bước sử dụng kính hiển vi quang học để quan sát một tiêu bản. Giải thích vì sao khi hạ vật kính xuống gần tiêu bản, mắt phải nhìn từ bên ngoài mà không nhìn vào thị kính.');
Q('Câu 3.', 'Hoàn thành bảng so sánh (ghi "Có" hoặc "Không"):');
add(table([['Thành phần', 'Tế bào vi khuẩn', 'Tế bào lá cây', 'Tế bào cơ người'],
  ['Màng tế bào', '', '', ''], ['Tế bào chất', '', '', ''], ['Màng nhân (nhân hoàn chỉnh)', '', '', ''], ['Thành tế bào', '', '', ''], ['Lục lạp', '', '', '']], [3200, ...Array(3).fill(Math.floor((W - 3200) / 3))], { left: [0] }));
Q('Câu 4.', 'Trong điều kiện thuận lợi, vi khuẩn E. coli cứ khoảng 20 phút lại phân chia một lần.');
L('a) Từ 1 tế bào ban đầu, sau 2 giờ sẽ tạo ra bao nhiêu tế bào?');
L('b) Nếu ban đầu có 5 tế bào thì sau 1 giờ có bao nhiêu tế bào?');
L('c) Từ kết quả trên, giải thích vì sao thức ăn đã nấu chín để lâu ở nhiệt độ phòng nhanh bị ôi thiu.');

H('PHẦN IV. BÀI TẬP THỰC TIỄN – SONG NGỮ – THÍ NGHIỆM (2 bài)');
Q('Bài 1 (Thí nghiệm).', 'Nhóm em được giao làm tiêu bản và quan sát tế bào biểu bì vảy hành bằng kính hiển vi quang học.');
L('a) Nêu các bước làm tiêu bản tế bào biểu bì vảy hành.');
L('b) Vì sao phải lấy lớp biểu bì thật mỏng và khi đậy lamen cần đặt nghiêng một cạnh rồi hạ từ từ xuống?');
L('c) Dự đoán hình dạng tế bào quan sát được và nêu những thành phần của tế bào em có thể nhìn thấy.');
Q('Bài 2 (Song ngữ – Bilingual).', 'Read the text and answer the questions. *(Đọc đoạn văn và trả lời câu hỏi.)*');
add(P('*"The cell is the basic unit of life. All living things are made of one or more cells. Bacteria are single-celled organisms, and their cells have no nucleus. Plant cells have a cell wall and chloroplasts, which animal cells do not have. A cell grows bigger and then divides into two new cells."*', { p: { indent: { left: IND, right: 200 }, spacing: { before: 40, after: 40, line: 264 } } }));
L('a) Translate into Vietnamese: *cell, nucleus, cell wall, chloroplast, single-celled organism, divide.*');
L('b) True or False? (1) Bacterial cells have a nucleus. (2) Animal cells have chloroplasts. (3) A cell divides into two new cells.');
L('c) One cell divides 5 times in a row. How many cells are there? *(Một tế bào phân chia liên tiếp 5 lần tạo ra bao nhiêu tế bào?)*');
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
  ['1', 'Sinh học: (1), (5). Khoa học Trái Đất: (2). Hóa học: (3). Thiên văn học: (4). Vật lí: (6). (Đúng 4 – 5 hoạt động: 0,25 điểm; đúng cả 6: 0,5 điểm.)', '0,5'],
  ['2', 'Các bước: đặt kính nơi bằng phẳng, đủ sáng → điều chỉnh ánh sáng (bật đèn hoặc chỉnh gương) → đặt tiêu bản lên bàn kính, kẹp giữ → mắt nhìn từ bên ngoài, vặn ốc to hạ vật kính sát tiêu bản → mắt nhìn vào thị kính, vặn ốc to theo chiều ngược lại nâng vật kính lên đến khi thấy mẫu vật → vặn ốc nhỏ cho ảnh rõ nét.', '0,25'],
  ['', 'Giải thích: nếu nhìn vào thị kính sẽ không biết vật kính đã chạm tiêu bản chưa, dễ làm vỡ tiêu bản và hỏng vật kính.', '0,25'],
  ['3', 'Tế bào vi khuẩn: Có – Có – Không – Có – Không. Tế bào lá cây: Có – Có – Có – Có – Có. Tế bào cơ người: Có – Có – Có – Không – Không. (Đúng 2 cột: 0,25 điểm; đúng cả 3 cột: 0,5 điểm.)', '0,5'],
  ['4', 'a) 2 giờ = 120 phút → 6 lần phân chia → 2⁶ = 64 tế bào. b) 1 giờ → 3 lần → 5 × 2³ = 40 tế bào.', '0,25'],
  ['', 'c) Vi khuẩn sinh sản rất nhanh (số lượng tăng gấp đôi sau mỗi lần phân chia) ở nhiệt độ phòng, phân hủy thức ăn → thức ăn nhanh ôi thiu; cần bảo quản lạnh, đậy kín.', '0,25'],
];
add(table([['Câu', 'Lời giải – đáp án', 'Điểm'], ...tl], [800, W - 1800, 1000], { left: [1] }));
add(P('*Lưu ý câu 3: phần lớn vi khuẩn có thành tế bào bao ngoài màng tế bào (khác thành tế bào thực vật về thành phần).*', { p: { spacing: { before: 40 } } }));

H('PHẦN IV. Bài tập thực tiễn – song ngữ – thí nghiệm (2,0 điểm – mỗi bài 1,0 điểm)', 120);
const tt = [
  ['1', 'a) Nhỏ một giọt nước cất lên giữa lam kính → dùng kim mũi mác tách lớp biểu bì mỏng mặt trong vảy hành, đặt vào giọt nước, dàn phẳng → đậy lamen (có thể nhuộm bằng dung dịch xanh methylene hoặc iodine loãng) → thấm bớt nước thừa → quan sát bằng vật kính 10x rồi 40x.', '0,5'],
  ['', 'b) Lớp biểu bì mỏng để ánh sáng xuyên qua, các tế bào không chồng lên nhau nên nhìn rõ. Đặt lamen nghiêng rồi hạ từ từ để không tạo bọt khí che mẫu vật.', '0,25'],
  ['', 'c) Tế bào hình nhiều cạnh (gần hình chữ nhật), xếp sát nhau; quan sát được thành tế bào/màng tế bào, tế bào chất, nhân.', '0,25'],
  ['2', 'a) cell: tế bào; nucleus: nhân tế bào; cell wall: thành tế bào; chloroplast: lục lạp; single-celled organism: sinh vật đơn bào; divide: phân chia.', '0,5'],
  ['', 'b) (1) False; (2) False; (3) True.', '0,25'],
  ['', 'c) 2⁵ = 32 cells.', '0,25'],
];
add(table([['Bài', 'Lời giải – đáp án', 'Điểm'], ...tt], [800, W - 1800, 1000], { left: [1] }));
add(P('*Ghi chú: Học sinh trả lời theo cách khác đúng, lập luận chặt chẽ vẫn cho điểm tối đa.*', { p: { spacing: { before: 100 } } }));

