
H('PHẦN II. TRẮC NGHIỆM ĐÚNG/SAI (2 câu)');
add(P('*Trong mỗi ý a), b), c), d) ở mỗi câu, học sinh chọn Đúng (Đ) hoặc Sai (S).*'));
const DS = [
  ['Mendel cho lai hai giống đậu Hà Lan thuần chủng hoa tím và hoa trắng, F₁ thu được 100% hoa tím; cho F₁ tự thụ phấn, F₂ thu được 705 cây hoa tím và 224 cây hoa trắng.', [
    ['Hoa tím là tính trạng trội, hoa trắng là tính trạng lặn.', 'Đ', 'F₁ chỉ biểu hiện hoa tím.'],
    ['Trong số các cây hoa tím ở F₂, cây thuần chủng chiếm tỉ lệ 1/3.', 'Đ', 'Hoa tím F₂ gồm 1 AA : 2 Aa → AA chiếm 1/3.'],
    ['Cho cây hoa tím F₁ lai phân tích thì đời con có tỉ lệ 3 hoa tím : 1 hoa trắng.', 'S', 'Aa × aa → 1 hoa tím : 1 hoa trắng.'],
    ['Kết quả thí nghiệm chứng tỏ các nhân tố di truyền hòa trộn vào nhau.', 'S', 'Hoa trắng xuất hiện lại ở F₂ → nhân tố di truyền không hòa trộn.']]],
  ['Một đoạn phân tử DNA có 2 400 nucleotide, trong đó nucleotide loại A chiếm 20%.', [
    ['Số nucleotide loại T của đoạn DNA là 480.', 'Đ', 'A = T = 20% × 2 400 = 480.'],
    ['Số nucleotide loại G của đoạn DNA là 960.', 'S', 'G = (2 400 – 2 × 480) : 2 = 720.'],
    ['Đoạn DNA tái bản 2 lần tạo ra 4 đoạn DNA con, trong đó mỗi đoạn đều gồm hai mạch hoàn toàn mới.', 'S', 'Theo nguyên tắc bán bảo toàn, mỗi DNA con có 1 mạch của DNA mẹ (ở lần tái bản đầu) – có 2 DNA con còn chứa mạch cũ.'],
    ['Khi phiên mã, nucleotide loại A trên mạch khuôn liên kết với nucleotide loại U của môi trường.', 'Đ', 'Nguyên tắc bổ sung trong phiên mã: A – U.']]],
];
DS.forEach(([q, it], i) => { Q(`Câu ${i + 1}.`, q); it.forEach((x, j) => L(`${'abcd'[j]}) ${x[0]}`)); });

H('PHẦN III. TỰ LUẬN – TRẢ LỜI NGẮN (4 câu)');
Q('Câu 1.', 'Lấy ví dụ ở cây đậu Hà Lan để làm rõ các thuật ngữ: tính trạng, cặp tính trạng tương phản, allele, kiểu gene, kiểu hình, cơ thể thuần chủng.');
Q('Câu 2.', 'Ở đậu Hà Lan, allele A quy định thân cao trội hoàn toàn so với allele a quy định thân thấp. Cho cây thân cao thuần chủng lai với cây thân thấp được F₁; F₁ tự thụ phấn được F₂.');
L('a) Viết sơ đồ lai từ P đến F₂. Xác định tỉ lệ kiểu gene, kiểu hình ở F₂.');
L('b) Làm thế nào để biết một cây thân cao ở F₂ có thuần chủng hay không? Nêu cách đọc kết quả.');
Q('Câu 3.', 'Một gene có 3 000 nucleotide, trong đó có 900 nucleotide loại G.');
L('a) Tính số nucleotide mỗi loại của gene.');
L('b) Tính chiều dài của gene (nm) và số liên kết hydrogen của gene.');
Q('Câu 4.', 'Một đoạn mạch khuôn của gene có trình tự: 3′– TAC GCA TTG ACC –5′.');
L('a) Viết trình tự đoạn mRNA được phiên mã từ đoạn mạch khuôn trên.');
L('b) Viết trình tự đoạn mạch bổ sung của gene. So sánh trình tự đoạn mRNA với đoạn mạch bổ sung này.');

H('PHẦN IV. BÀI TẬP THỰC TIỄN – SONG NGỮ – THÍ NGHIỆM (2 bài)');
Q('Bài 1 (Thực tiễn – Ứng dụng phân tích DNA).', 'Ở Việt Nam, kĩ thuật giám định DNA được dùng để xác định danh tính hài cốt liệt sĩ còn thiếu thông tin, xác định quan hệ huyết thống và hỗ trợ điều tra tội phạm.');
L('a) Dựa vào kiến thức về gene và hệ gene, giải thích vì sao có thể dùng DNA để xác định danh tính một người.');
L('b) Kể tên ít nhất 3 loại mẫu sinh học có thể dùng để tách chiết DNA.');
L('c) Để xác định hài cốt có phải là con của một gia đình liệt sĩ hay không, người ta thường so sánh DNA của hài cốt với DNA của ai? Vì sao?');
Q('Bài 2 (Song ngữ – Bilingual).', 'Read the text and answer the questions. *(Đọc đoạn văn và trả lời câu hỏi.)*');
add(P('*"DNA is a double helix made of two strands. Each strand is a chain of nucleotides. There are four types of nucleotides: A, T, G and C. The bases on the two strands pair up following the complementary base-pairing rule: A pairs with T, and G pairs with C. Before a cell divides, DNA is copied by replication. Each new DNA molecule keeps one old strand and has one new strand."*', { p: { indent: { left: IND, right: 200 }, spacing: { before: 40, after: 40, line: 264 } } }));
L('a) Translate into Vietnamese: *double helix, strand, nucleotide, complementary base-pairing rule, replication.*');
L('b) One strand has the sequence 5′– GCA TTA CGT –3′. Write the sequence of the complementary strand.');
L('c) One DNA molecule replicates 4 times. How many DNA molecules are produced? *(Một phân tử DNA tái bản 4 lần tạo ra bao nhiêu phân tử DNA?)*');
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
  ['1', 'Tính trạng: màu hoa, chiều cao thân… Cặp tính trạng tương phản: hoa tím – hoa trắng; thân cao – thân thấp. Allele: A (hoa tím), a (hoa trắng) là hai allele của cùng một gene. Kiểu gene: AA, Aa, aa. Kiểu hình: hoa tím, hoa trắng. Cơ thể thuần chủng: AA (hoa tím thuần chủng), aa (hoa trắng). (Mỗi 2 thuật ngữ đúng: 0,25 điểm.)', '0,75'],
  ['2', 'a) P: AA (cao) × aa (thấp) → G: A; a → F₁: 100% Aa (thân cao). F₁ × F₁: Aa × Aa → G: A, a; A, a → F₂: 1 AA : 2 Aa : 1 aa; kiểu hình 3 thân cao : 1 thân thấp.', '0,5'],
  ['', 'b) Lai phân tích: cho cây thân cao F₂ lai với cây thân thấp (aa). Đời con 100% thân cao → cây đem lai thuần chủng (AA); đời con 1 cao : 1 thấp → không thuần chủng (Aa).', '0,25'],
  ['3', 'a) G = C = 900; A = T = (3 000 – 2 × 900) : 2 = 600.', '0,25'],
  ['', 'b) L = (3 000 : 2) × 0,34 = 510 nm. H = 2A + 3G = 2 × 600 + 3 × 900 = 3 900 liên kết.', '0,5'],
  ['4', 'a) mRNA: 5′– AUG CGU AAC UGG –3′.', '0,25'],
  ['', 'b) Mạch bổ sung: 5′– ATG CGT AAC TGG –3′. Trình tự mRNA giống mạch bổ sung, chỉ khác T được thay bằng U (cùng chiều 5′ → 3′).', '0,5'],
];
add(table([['Câu', 'Lời giải – đáp án', 'Điểm'], ...tl], [800, W - 1800, 1000], { left: [1] }));

H('PHẦN IV. Bài tập thực tiễn – song ngữ – thí nghiệm (2,0 điểm – mỗi bài 1,0 điểm)', 120);
const tt = [
  ['1', 'a) Mỗi cá thể có hệ gene (trình tự nucleotide) đặc trưng, gần như không trùng với người khác (trừ sinh đôi cùng trứng); con nhận một nửa vật chất di truyền từ bố, một nửa từ mẹ → so sánh DNA cho phép xác định danh tính và quan hệ huyết thống.', '0,5'],
  ['', 'b) Máu, tóc có chân tóc, niêm mạc miệng (nước bọt), da, móng, xương, răng… (nêu đúng 3 loại).', '0,25'],
  ['', 'c) So sánh với DNA của người thân cùng huyết thống trực hệ (mẹ, bố, anh chị em ruột…) vì họ có nhiều đoạn DNA giống với liệt sĩ; thường ưu tiên mẫu của mẹ hoặc người cùng dòng mẹ.', '0,25'],
  ['2', 'a) double helix: xoắn kép; strand: mạch (đơn); nucleotide: nucleotide; complementary base-pairing rule: nguyên tắc bổ sung; replication: tái bản (nhân đôi).', '0,25'],
  ['', 'b) 3′– CGT AAT GCA –5′ (hoặc viết 5′– TGC ATT ACG –3′).', '0,5'],
  ['', 'c) 2⁴ = 16 DNA molecules.', '0,25'],
];
add(table([['Bài', 'Lời giải – đáp án', 'Điểm'], ...tt], [800, W - 1800, 1000], { left: [1] }));
add(P('*Ghi chú: Học sinh trả lời theo cách khác đúng, lập luận chặt chẽ vẫn cho điểm tối đa. Nội dung bám theo yêu cầu cần đạt Bài 36 – 39 trong tài liệu ôn tập KHTN 9 (phần Vật sống).*', { p: { spacing: { before: 100 } } }));

