add(P('Phạm vi: Bài 1 (phần dụng cụ, thiết bị điện) – Bài 13. Khối lượng riêng –', { run: { bold: true }, p: { alignment: AlignmentType.CENTER, spacing: { before: 160, after: 0 } } }));
add(P('Bài 14. Thực hành xác định khối lượng riêng – Bài 15. Áp suất trên một bề mặt –', { run: { bold: true }, p: { alignment: AlignmentType.CENTER } }));
add(P('Bài 16. Áp suất chất lỏng. Áp suất khí quyển – Bài 17. Lực đẩy Archimedes', { run: { bold: true }, p: { alignment: AlignmentType.CENTER } }));
add(P('Mức độ: Khá – Giỏi · Gồm 20 câu/bài: 12 trắc nghiệm nhiều lựa chọn, 2 Đúng/Sai, 4 tự luận – trả lời ngắn, 2 bài thực tiễn/song ngữ/thí nghiệm', { run: { italics: true }, p: { alignment: AlignmentType.CENTER, spacing: { after: 80 } } }));

// ===== A. KIẾN THỨC =====
H('A. KIẾN THỨC TRỌNG TÂM', 80);
const kt = [
  ['Nội dung', 'Kiến thức cần nhớ', 'Công thức – đơn vị'],
  ['Thiết bị điện (Bài 1)', 'Biến áp nguồn: đổi điện áp xoay chiều 220 V thành điện áp xoay chiều/một chiều nhỏ, an toàn. Joulemeter: đo dòng điện, điện áp, công suất, năng lượng điện. Ampe kế mắc nối tiếp, vôn kế mắc song song; LED chỉ sáng khi mắc đúng chiều.', '—'],
  ['Khối lượng riêng (Bài 13, 14)', 'Khối lượng của một đơn vị thể tích chất. Xác định D: đo m bằng cân, đo V bằng bình chia độ (vật rắn không thấm nước) rồi tính D; đối chiếu bảng khối lượng riêng để biết chất.', 'D = m / V (kg/m³; g/cm³)\n1 g/cm³ = 1 000 kg/m³\nTrọng lượng riêng d = 10·D (N/m³)'],
  ['Áp suất trên bề mặt (Bài 15)', 'Áp lực là lực ép vuông góc với mặt bị ép. Tăng áp suất: tăng áp lực hoặc giảm diện tích bị ép (và ngược lại).', 'p = F / S\n1 Pa = 1 N/m²'],
  ['Áp suất chất lỏng, khí quyển (Bài 16)', 'Chất lỏng gây áp suất theo mọi phương; càng sâu áp suất càng lớn; các điểm cùng độ sâu trong chất lỏng đứng yên có áp suất bằng nhau. Không khí gây áp suất khí quyển theo mọi phương; càng lên cao càng giảm.', '★ p = d·h (h: độ sâu tính từ mặt thoáng)\np₀ ≈ 76 cmHg ≈ 1,013·10⁵ Pa'],
  ['Lực đẩy Archimedes (Bài 17)', 'Vật nhúng trong chất lỏng bị đẩy thẳng đứng từ dưới lên, độ lớn bằng trọng lượng phần chất lỏng bị vật chiếm chỗ. P > F_A: vật chìm; P = F_A: lơ lửng/nổi cân bằng; P < F_A: vật nổi lên.', 'F_A = d·V (V: thể tích phần chất lỏng bị chiếm chỗ)\nF_A = P (ngoài không khí) – P (trong chất lỏng)'],
];
add(table(kt, [1900, W - 1900 - 3000, 3000], { left: [1, 2] }));

// ===== B. CÂU HỎI =====
H('B. CÂU HỎI ÔN TẬP');
H('PHẦN I. TRẮC NGHIỆM NHIỀU LỰA CHỌN (12 câu)', 60);
add(P('*Mỗi câu hỏi có 4 phương án, chỉ có 1 phương án đúng.*'));
const MC = [
  ['Trong phòng thí nghiệm, biến áp nguồn là thiết bị có chức năng', ['chuyển điện áp xoay chiều 220 V thành điện áp xoay chiều hoặc một chiều có giá trị nhỏ, an toàn khi làm thí nghiệm.', 'đo cường độ dòng điện và hiệu điện thế của mạch điện.', 'chuyển điện áp một chiều của pin thành điện áp xoay chiều 220 V.', 'tích trữ điện năng để dùng khi mất điện.']],
  ['Bạn An mắc mạch điện gồm pin, công tắc, dây nối và một điôt phát quang (LED). Khi đóng công tắc, LED không sáng dù pin còn tốt và dây nối không bị đứt. Nguyên nhân có thể là', ['công tắc đang ở trạng thái đóng.', 'dây nối quá ngắn.', 'LED bị mắc ngược chiều so với cực của nguồn.', 'LED chỉ sáng khi dùng nguồn điện xoay chiều.']],
  ['Đặt một khối sắt có thể tích 1 dm³ lên đĩa trái của một cân đĩa. Phải đặt lên đĩa phải bao nhiêu lít nước (đựng trong bình có khối lượng không đáng kể) để cân thăng bằng? Biết D_sắt = 7 800 kg/m³, D_nước = 1 000 kg/m³.', ['9,2 lít.', '8,7 lít.', '7,8 lít.', '6,5 lít.']],
  ['Cho hai khối kim loại sắt và chì, khối sắt có khối lượng gấp đôi khối chì. Biết D_sắt = 7 800 kg/m³, D_chì = 11 300 kg/m³. Tỉ số thể tích V_sắt : V_chì gần nhất với giá trị', ['0,69.', '2,9.', '1,38.', '3,2.']],
  ['Trong giờ thực hành, một nhóm cân được viên sỏi có khối lượng 39 g. Bình chia độ đang chứa 50 mL nước, thả chìm viên sỏi vào thì mực nước chỉ 65 mL. Khối lượng riêng của sỏi là', ['2 600 kg/m³.', '780 kg/m³.', '600 kg/m³.', '2,6 kg/m³.']],
  ['Đặt bao gạo 60 kg lên một chiếc ghế bốn chân có khối lượng 4 kg. Diện tích tiếp xúc với mặt đất của mỗi chân ghế là 8 cm². Áp suất mà gạo và ghế tác dụng lên mặt đất là', ['20 000 Pa.', '2 000 000 Pa.', '187 500 Pa.', '200 000 Pa.']],
  ['Một khối hình hộp chữ nhật kích thước 20 cm × 10 cm × 5 cm làm bằng chất có trọng lượng riêng 2·10⁴ N/m³, đặt trên mặt bàn nằm ngang. Áp suất lớn nhất và nhỏ nhất khối hộp có thể tác dụng lên mặt bàn lần lượt là', ['4 000 Pa và 2 000 Pa.', '4 000 Pa và 1 000 Pa.', '10 000 Pa và 2 000 Pa.', '2 000 Pa và 1 000 Pa.']],
  ['Một thùng cao 80 cm đựng đầy nước. Biết p = d·h, trọng lượng riêng của nước 10 000 N/m³. Áp suất của nước tại điểm A cách đáy thùng 20 cm là', ['8 000 Pa.', '2 000 Pa.', '1 000 Pa.', '6 000 Pa.']],
  ['Một bình thông nhau chứa thủy ngân. Đổ vào nhánh thứ nhất dung dịch acid (d₁ = 18 000 N/m³), nhánh thứ hai đổ nước (d₂ = 10 000 N/m³). Khi cột nước cao 64 cm thì mực thủy ngân ở hai nhánh ngang nhau. Chiều cao cột acid là', ['64 cm.', '42,5 cm.', '35,6 cm.', '115,2 cm.']],
  ['Hiện tượng nào sau đây <b>không</b> do áp suất khí quyển gây ra?', ['Hút nước từ cốc lên miệng bằng ống hút.', 'Giác mút ép chặt vào mặt kính rất khó kéo ra.', 'Nắp ấm trà có lỗ nhỏ giúp rót nước dễ hơn.', 'Quả bóng bàn bị bẹp thả vào nước nóng phồng lên như cũ.']],
  ['Một quả cầu bằng đồng treo vào lực kế, ngoài không khí lực kế chỉ 4,45 N. Nhúng chìm hoàn toàn quả cầu trong rượu thì lực kế chỉ bao nhiêu? Biết d_rượu = 8 000 N/m³, d_đồng = 89 000 N/m³.', ['4,05 N.', '4,45 N.', '0,40 N.', '4,85 N.']],
  ['Thả chìm hoàn toàn 1 kg nhôm và 1 kg chì vào nước. Nhận xét nào sau đây đúng?', ['Lực đẩy Archimedes lên hai khối bằng nhau vì chúng có cùng khối lượng.', 'Lực đẩy Archimedes lên khối nhôm lớn hơn vì khối nhôm có thể tích lớn hơn.', 'Lực đẩy Archimedes lên khối chì lớn hơn vì chì có khối lượng riêng lớn hơn.', 'Không so sánh được vì chưa biết độ sâu của mỗi khối.']],
];
const ANS = 'ACCBADBDCDAB';
MC.forEach(([q, o], i) => { Q(`Câu ${i + 1}.`, q.replace(/<\/?b>/g, '**')); opts(o); });

H('PHẦN II. TRẮC NGHIỆM ĐÚNG/SAI (2 câu)');
add(P('*Trong mỗi ý a), b), c), d) ở mỗi câu, học sinh chọn Đúng (Đ) hoặc Sai (S).*'));
const DS = [
  ['Trong giờ thực hành xác định khối lượng riêng của một viên đá, bạn Nam dùng cân điện tử và bình chia độ.', [
    ['Cần đo khối lượng và thể tích của viên đá, sau đó tính D = m : V.', 'Đ', 'Nguyên tắc xác định khối lượng riêng.'],
    ['Nếu đập viên đá làm đôi thì khối lượng riêng của mỗi nửa chỉ bằng một nửa khối lượng riêng ban đầu.', 'S', 'Khối lượng riêng là đặc trưng của chất, không phụ thuộc kích thước vật.'],
    ['Nếu viên đá thấm một ít nước thì thể tích đo được nhỏ hơn thực tế, nên khối lượng riêng tính được lớn hơn thực tế.', 'Đ', 'Nước thấm vào đá nên mực nước dâng ít hơn → V đo nhỏ → D = m : V lớn hơn.'],
    ['Nam đo được m = 52 g, V = 20 cm³, suy ra D = 260 kg/m³.', 'S', 'D = 52 : 20 = 2,6 g/cm³ = 2 600 kg/m³.']]],
  ['Một thợ lặn đang ở độ sâu 20 m dưới mặt biển. Trọng lượng riêng của nước biển là 10 300 N/m³ (coi thể tích người và bộ đồ lặn không đổi).', [
    ['Áp suất do nước biển gây ra tại độ sâu đó là 206 000 Pa.', 'Đ', 'p = d·h = 10 300 × 20 = 206 000 Pa.'],
    ['Khi lặn sâu hơn, áp suất nước biển tác dụng lên người thợ lặn giảm.', 'S', 'Càng sâu, áp suất chất lỏng càng lớn.'],
    ['Khi lặn sâu hơn (vẫn chìm hoàn toàn), lực đẩy Archimedes tác dụng lên thợ lặn không đổi.', 'Đ', 'F_A = d·V; d và V không đổi nên F_A không đổi, không phụ thuộc độ sâu.'],
    ['Nước biển chỉ gây áp suất lên người thợ lặn theo phương thẳng đứng.', 'S', 'Chất lỏng gây áp suất theo mọi phương.']]],
];
DS.forEach(([q, it], i) => { Q(`Câu ${i + 1}.`, q); it.forEach((x, j) => L(`${'abcd'[j]}) ${x[0]}`)); });

H('PHẦN III. TỰ LUẬN – TRẢ LỜI NGẮN (4 câu)');
Q('Câu 1.', 'Một khối đá hoa cương dạng hình hộp chữ nhật có kích thước 2,0 m × 3,0 m × 1,5 m. Khối lượng riêng của đá hoa cương là 2 750 kg/m³.');
L('a) Tính khối lượng và trọng lượng của khối đá.');
L('b) Một xe tải chở được tối đa 10 tấn mỗi chuyến. Nếu cắt nhỏ khối đá thì cần ít nhất mấy chuyến xe để chở hết?');
Q('Câu 2.', 'Một người có khối lượng 60 kg, diện tích tiếp xúc của mỗi bàn chân với mặt sàn là 150 cm².');
L('a) Tính áp suất người đó tác dụng lên mặt sàn khi đứng cả hai chân và khi đứng co một chân.');
L('b) Vì sao khi phải đi qua bãi bùn, người ta thường đặt một tấm ván rộng lên trên để đi?');
Q('Câu 3.', 'Áp kế gắn ở vỏ ngoài một tàu ngầm lúc đầu chỉ 1 030 000 Pa, một lúc sau chỉ 1 545 000 Pa. Trọng lượng riêng của nước biển là 10 300 N/m³ (chỉ xét áp suất do nước biển gây ra, p = d·h).');
L('a) Tàu ngầm đang nổi lên hay lặn xuống? Giải thích.');
L('b) Tính độ sâu của tàu ở hai thời điểm trên.');
Q('Câu 4.', 'Treo một vật vào lực kế, ngoài không khí lực kế chỉ 12 N; khi nhúng chìm hoàn toàn vật trong nước thì lực kế chỉ 7 N. Trọng lượng riêng của nước là 10 000 N/m³.');
L('a) Tính lực đẩy Archimedes tác dụng lên vật và thể tích của vật.');
L('b) Tính trọng lượng riêng và khối lượng riêng của chất làm vật.');
L('c) Nếu nhúng chìm vật trong dầu (d = 8 000 N/m³) thì lực kế chỉ bao nhiêu?');

H('PHẦN IV. BÀI TẬP THỰC TIỄN – SONG NGỮ – THÍ NGHIỆM (2 bài)');
Q('Bài 1 (Thí nghiệm – Bài 14).', 'Một nhóm học sinh xác định khối lượng riêng của một viên sỏi bằng cân điện tử và bình chia độ, thu được bảng số liệu:');
add(table([['Lần đo', 'm (g)', 'V₁ – nước (mL)', 'V₂ – nước và sỏi (mL)', 'V = V₂ – V₁ (cm³)'],
  ['1', '31,2', '40,0', '52,0', ''], ['2', '31,2', '40,0', '52,5', ''], ['3', '31,2', '45,0', '56,5', '']], [1300, 1500, 2200, 2700, W - 7700]));
L('a) Hoàn thành cột cuối của bảng và tính thể tích trung bình của viên sỏi.');
L('b) Tính khối lượng riêng của sỏi theo g/cm³ và kg/m³.');
L('c) Nêu hai nguyên nhân có thể gây sai số trong thí nghiệm và cách khắc phục.');
Q('Bài 2 (Song ngữ – Bilingual).', 'Read the text and answer the questions. *(Đọc đoạn văn và trả lời câu hỏi.)*');
add(P('*"A steel ship is much heavier than a small stone, yet the ship floats while the stone sinks. When an object is placed in water, the water pushes it upward with a buoyant force. According to Archimedes\' principle, the buoyant force is equal to the weight of the water displaced by the object. A ship is hollow, so it displaces a large volume of water."*', { p: { indent: { left: IND, right: 200 }, spacing: { before: 40, after: 40, line: 264 } } }));
L('a) Translate into Vietnamese: *buoyant force, displaced water, float, sink, hollow.*');
L('b) Explain in Vietnamese why the steel ship floats but the stone sinks. *(Giải thích vì sao tàu thép nổi còn hòn đá chìm.)*');
L('c) A ship floating on the sea displaces 2 000 m³ of seawater (d = 10 300 N/m³). Calculate the buoyant force and the mass of the ship. *(Tính lực đẩy Archimedes và khối lượng của tàu.)*');
add(P('— HẾT PHẦN CÂU HỎI —', { run: { bold: true }, p: { alignment: AlignmentType.CENTER, spacing: { before: 160 } } }));

// ===== C. ĐÁP ÁN =====
add(new Paragraph({ children: [new PageBreak()] }));
add(P('C. ĐÁP ÁN – LỜI GIẢI – HƯỚNG DẪN CHẤM', { run: { bold: true, size: 28 }, p: { alignment: AlignmentType.CENTER, spacing: { after: 60 } } }));
add(P('*Thang điểm tham khảo (10 điểm): Phần I – 3,0 điểm; Phần II – 2,0 điểm; Phần III – 3,0 điểm; Phần IV – 2,0 điểm.*', { p: { alignment: AlignmentType.CENTER, spacing: { after: 80 } } }));
H('PHẦN I. Trắc nghiệm nhiều lựa chọn (3,0 điểm – mỗi câu đúng 0,25 điểm)', 60);
const cw12 = [1300, ...Array(12).fill(Math.floor((W - 1300) / 12))];
add(table([['Câu', ...Array.from({ length: 12 }, (_, i) => String(i + 1))], ['Đáp án', ...ANS.split('')]], cw12, { firstCol: true }));
const EX = [
  'Biến áp nguồn hạ điện áp lưới 220 V xuống điện áp nhỏ (AC hoặc DC) để thí nghiệm an toàn.',
  'LED chỉ cho dòng điện đi qua theo một chiều; mắc ngược cực thì LED không sáng.',
  'm_sắt = D·V = 7 800 × 0,001 = 7,8 kg → cần 7,8 kg nước = 7,8 lít.',
  'V_sắt : V_chì = (2m : 7 800) : (m : 11 300) = 2 × 11 300 : 7 800 ≈ 2,9.',
  'V = 65 – 50 = 15 cm³; D = 39 : 15 = 2,6 g/cm³ = 2 600 kg/m³.',
  'F = (60 + 4) × 10 = 640 N; S = 4 × 8 = 32 cm² = 0,0032 m²; p = 640 : 0,0032 = 200 000 Pa. (187 500 Pa là kết quả khi quên khối lượng ghế.)',
  'p = F : S = d·V : S = d·h (h là chiều cao khối hộp theo phương thẳng đứng). Lớn nhất khi h = 0,2 m: 4 000 Pa; nhỏ nhất khi h = 0,05 m: 1 000 Pa.',
  'Độ sâu của A tính từ mặt thoáng: h = 80 – 20 = 60 cm = 0,6 m → p = 10 000 × 0,6 = 6 000 Pa.',
  'Mực thủy ngân ngang nhau → áp suất do hai cột chất lỏng bằng nhau: d₁h₁ = d₂h₂ → h₁ = 10 000 × 64 : 18 000 ≈ 35,6 cm.',
  'Quả bóng bàn phồng lên do không khí bên trong nóng lên, nở ra (sự nở vì nhiệt), không do áp suất khí quyển.',
  'V = 4,45 : 89 000 = 5·10⁻⁵ m³; F_A = 8 000 × 5·10⁻⁵ = 0,4 N; số chỉ lực kế = 4,45 – 0,4 = 4,05 N.',
  'Cùng khối lượng, nhôm có khối lượng riêng nhỏ hơn nên thể tích lớn hơn → F_A = d·V lớn hơn.',
];
EX.forEach((e, i) => add(P(`**Câu ${i + 1} (${ANS[i]}).** ${e}`, { p: { spacing: { line: 264 } } })));

H('PHẦN II. Trắc nghiệm Đúng/Sai (2,0 điểm – mỗi câu 1,0 điểm)', 120);
add(P('*Điểm mỗi câu: đúng 1 ý – 0,1 điểm; đúng 2 ý – 0,25 điểm; đúng 3 ý – 0,5 điểm; đúng cả 4 ý – 1,0 điểm.*'));
const dsRows = [['Câu', 'Ý', 'Đáp án', 'Giải thích']];
DS.forEach(([_, it], i) => it.forEach((x, j) => dsRows.push([j === 0 ? String(i + 1) : '', 'abcd'[j], x[1], x[2]])));
add(table(dsRows, [800, 700, 1100, W - 2600], { left: [3] }));

H('PHẦN III. Tự luận – trả lời ngắn (3,0 điểm – mỗi câu 0,75 điểm)', 120);
const tl = [
  ['1', 'a) V = 2,0 × 3,0 × 1,5 = 9 m³; m = D·V = 2 750 × 9 = 24 750 kg; P = 10·m = 247 500 N.', '0,5'],
  ['', 'b) 24 750 kg = 24,75 tấn; 24,75 : 10 = 2,475 → cần ít nhất 3 chuyến.', '0,25'],
  ['2', 'a) F = P = 600 N. Hai chân: S = 300 cm² = 0,03 m² → p = 600 : 0,03 = 20 000 Pa. Một chân: S = 0,015 m² → p = 40 000 Pa.', '0,5'],
  ['', 'b) Tấm ván rộng làm tăng diện tích bị ép, giữ nguyên áp lực → áp suất lên bùn giảm, người không bị lún.', '0,25'],
  ['3', 'a) Áp suất tăng → độ sâu tăng (p tỉ lệ với h) → tàu đang lặn xuống.', '0,25'],
  ['', 'b) h₁ = 1 030 000 : 10 300 = 100 m; h₂ = 1 545 000 : 10 300 = 150 m.', '0,5'],
  ['4', 'a) F_A = 12 – 7 = 5 N; V = F_A : d_nước = 5 : 10 000 = 5·10⁻⁴ m³ (500 cm³).', '0,25'],
  ['', 'b) d_vật = P : V = 12 : 5·10⁻⁴ = 24 000 N/m³; D = d : 10 = 2 400 kg/m³.', '0,25'],
  ['', 'c) F_A (dầu) = 8 000 × 5·10⁻⁴ = 4 N → lực kế chỉ 12 – 4 = 8 N.', '0,25'],
];
add(table([['Câu', 'Lời giải – đáp án', 'Điểm'], ...tl], [800, W - 1800, 1000], { left: [1] }));

H('PHẦN IV. Bài tập thực tiễn – song ngữ – thí nghiệm (2,0 điểm – mỗi bài 1,0 điểm)', 120);
const tt = [
  ['1', 'a) V lần lượt: 12,0 cm³; 12,5 cm³; 11,5 cm³ → V_tb = (12,0 + 12,5 + 11,5) : 3 = 12,0 cm³.', '0,25'],
  ['', 'b) D = 31,2 : 12,0 = 2,6 g/cm³ = 2 600 kg/m³.', '0,25'],
  ['', 'c) Gợi ý: đọc vạch chia sai (mắt không ngang mực nước) → đặt mắt ngang mặt thoáng; nước bám vào sỏi hoặc còn bọt khí → thả nhẹ, lắc nhẹ để đuổi bọt khí; sỏi thấm nước → ngâm sỏi trước; cân chưa về số 0 → hiệu chỉnh cân. (Nêu đúng 2 nguyên nhân kèm cách khắc phục.)', '0,5'],
  ['2', 'a) buoyant force: lực đẩy (Archimedes); displaced water: nước bị vật chiếm chỗ; float: nổi; sink: chìm; hollow: rỗng.', '0,25'],
  ['', 'b) Tàu rỗng nên chiếm chỗ một thể tích nước rất lớn → lực đẩy Archimedes đủ lớn bằng trọng lượng tàu → tàu nổi. Hòn đá đặc, thể tích nhỏ, trọng lượng lớn hơn lực đẩy Archimedes → chìm.', '0,25'],
  ['', 'c) F_A = d·V = 10 300 × 2 000 = 20 600 000 N. Tàu nổi cân bằng: P = F_A → m = P : 10 = 2 060 000 kg = 2 060 tấn.', '0,5'],
];
add(table([['Bài', 'Lời giải – đáp án', 'Điểm'], ...tt], [800, W - 1800, 1000], { left: [1] }));
add(P('*Ghi chú: Học sinh giải cách khác đúng, lập luận chặt chẽ vẫn cho điểm tối đa.*', { p: { spacing: { before: 100 } } }));

