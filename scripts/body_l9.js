add(P('Phạm vi: Bài 36. Khái quát về di truyền học – Bài 37. Các quy luật di truyền của Mendel –', { run: { bold: true }, p: { alignment: AlignmentType.CENTER, spacing: { before: 160, after: 0 } } }));
add(P('Bài 38. Nucleic acid và gene – Bài 39. Tái bản DNA và phiên mã tạo RNA', { run: { bold: true }, p: { alignment: AlignmentType.CENTER } }));
add(P('Mức độ: Khá – Giỏi · Gồm 20 câu/bài: 12 trắc nghiệm nhiều lựa chọn, 2 Đúng/Sai, 4 tự luận – trả lời ngắn, 2 bài thực tiễn/song ngữ/thí nghiệm', { run: { italics: true }, p: { alignment: AlignmentType.CENTER, spacing: { after: 80 } } }));

// ===== A. KIẾN THỨC =====
H('A. KIẾN THỨC TRỌNG TÂM', 80);
const kt = [
  ['Bài', 'Kiến thức cần nhớ'],
  ['36. Khái quát về di truyền học', 'Di truyền: truyền đặc điểm từ bố mẹ, tổ tiên cho con cháu. Biến dị: con sinh ra có đặc điểm khác nhau và khác bố mẹ. Gene quy định di truyền và biến dị → gene là trung tâm của di truyền học. Thí nghiệm của Mendel bác bỏ quan niệm di truyền hòa trộn: mỗi tính trạng do một cặp nhân tố di truyền (gene) quy định. Thuật ngữ: tính trạng, cặp tính trạng tương phản, tính trạng trội/lặn, kiểu gene, kiểu hình, allele, cơ thể thuần chủng, dòng thuần; kí hiệu P, G, F₁, F₂, ×.'],
  ['37. Các quy luật di truyền của Mendel', 'Quy luật phân li: mỗi tính trạng do một cặp allele quy định; khi phát sinh giao tử, các allele phân li đồng đều, mỗi giao tử chỉ chứa một allele. P thuần chủng khác nhau 1 cặp tính trạng → F₁ đồng tính trội → F₂: 3 trội : 1 lặn (1 AA : 2 Aa : 1 aa). Quy luật phân li độc lập: các cặp allele phân li độc lập khi phát sinh giao tử, tổ hợp tự do khi thụ tinh → F₂: 9 : 3 : 3 : 1; xuất hiện biến dị tổ hợp. Lai phân tích: cá thể trội × cá thể lặn để xác định kiểu gene (100% trội → AA; 1 : 1 → Aa).'],
  ['38. Nucleic acid và gene', 'Nucleic acid gồm DNA và RNA, cấu tạo theo nguyên tắc đa phân. DNA: xoắn kép, 2 mạch song song ngược chiều; 4 loại nucleotide A, T, G, C; liên kết theo nguyên tắc bổ sung A – T (2 liên kết hydrogen), G – C (3 liên kết hydrogen); mỗi chu kì xoắn 10 cặp nucleotide dài 3,4 nm. Chức năng: lưu giữ, bảo quản, truyền đạt thông tin di truyền. RNA: 1 mạch, 4 loại A, U, G, C; mRNA mang thông tin, tRNA vận chuyển amino acid, rRNA cấu tạo ribosome. Gene: đoạn DNA mang thông tin mã hóa RNA hoặc chuỗi polypeptide. Ứng dụng phân tích DNA: xác định huyết thống, truy tìm tội phạm, chẩn đoán bệnh.'],
  ['39. Tái bản DNA và phiên mã', 'Tái bản DNA: tháo xoắn, tách 2 mạch → nucleotide tự do liên kết với mỗi mạch khuôn theo nguyên tắc bổ sung (A – T, G – C) → 2 DNA con giống hệt DNA mẹ, mỗi DNA con có 1 mạch cũ, 1 mạch mới (bán bảo toàn). Sau n lần tái bản: 1 DNA → 2ⁿ DNA. Phiên mã: tổng hợp RNA dựa trên mạch khuôn của gene, nguyên tắc bổ sung A – U, T – A, G – C, C – G; mạch RNA được tổng hợp theo chiều 5′ → 3′.'],
];
add(table(kt, [2300, W - 2300], { left: [1] }));
add(P('• Công thức (DNA): N = A + T + G + C; A = T, G = C → A + G = N/2. Chiều dài L = (N/2) × 0,34 nm. Số liên kết hydrogen H = 2A + 3G.', { p: { spacing: { before: 60, line: 264 } } }));

// ===== B. CÂU HỎI =====
H('B. CÂU HỎI ÔN TẬP');
H('PHẦN I. TRẮC NGHIỆM NHIỀU LỰA CHỌN (12 câu)', 60);
add(P('*Mỗi câu hỏi có 4 phương án, chỉ có 1 phương án đúng.*'));
const MC0 = [
  ['Biến dị là hiện tượng', ['*thế hệ con sinh ra có những đặc điểm khác nhau và khác với thế hệ trước.', 'truyền đạt các đặc điểm của bố mẹ, tổ tiên cho con cháu.', 'con cái giống hệt bố mẹ về mọi đặc điểm.', 'các tính trạng của bố và mẹ hòa trộn vào nhau ở đời con.'], 'Khái niệm biến dị (phương án B là di truyền).'],
  ['Trong thí nghiệm của Mendel, F₁ toàn hoa tím nhưng hoa trắng lại xuất hiện ở F₂. Điều này chứng tỏ', ['tính trạng hoa trắng đã bị mất đi ở F₁.', 'nhân tố di truyền quy định hoa trắng bị biến đổi thành hoa tím.', 'các nhân tố di truyền hòa trộn vào nhau.', '*nhân tố di truyền quy định hoa trắng không mất đi mà chỉ bị lấn át bởi nhân tố trội ở F₁.'], 'Các nhân tố di truyền không hòa trộn; hoa trắng là tính trạng lặn.'],
  ['Cho cây hoa tím (tính trạng trội) chưa biết kiểu gene lai với cây hoa trắng. Đời con có tỉ lệ 1 hoa tím : 1 hoa trắng. Kiểu gene của cây hoa tím đem lai là', ['AA.', 'aa.', '*Aa.', 'AA hoặc Aa.'], 'Lai phân tích cho 1 : 1 → cá thể đem lai dị hợp (Aa).'],
  ['Phép lai AaBb × aabb (hai cặp gene phân li độc lập, trội hoàn toàn) cho đời con có tỉ lệ kiểu hình là', ['*1 : 1 : 1 : 1.', '9 : 3 : 3 : 1.', '3 : 1.', '3 : 3 : 1 : 1.'], 'AaBb tạo 4 loại giao tử tỉ lệ bằng nhau; aabb chỉ tạo ab → 1 : 1 : 1 : 1.'],
  ['P thuần chủng: hạt vàng, trơn × hạt xanh, nhăn. F₁ tự thụ phấn, F₂ thu được 1 600 hạt. Theo lí thuyết, số hạt vàng, nhăn ở F₂ là', ['100.', '*300.', '900.', '1 600.'], 'Vàng, nhăn chiếm 3/16 → 1 600 × 3/16 = 300 hạt.', 'fix'],
  ['Các loại nucleotide cấu tạo nên phân tử DNA là', ['A, U, G, C.', 'A, T, U, G.', '*A, T, G, C.', 'A, T, G, U, C.'], 'DNA có T, không có U; RNA có U thay cho T.'],
  ['Một đoạn mạch của phân tử DNA có trình tự: 5′– ATG CTA GGC –3′. Trình tự đoạn mạch bổ sung là', ['5′– TAC GAT CCG –3′.', '3′– AUG CUA GGC –5′.', '3′– ATG CTA GGC –5′.', '*3′– TAC GAT CCG –5′.'], 'Bổ sung A – T, G – C, hai mạch ngược chiều.'],
  ['Một phân tử DNA có 3 000 nucleotide, trong đó số nucleotide loại A là 600. Số nucleotide loại G là', ['600.', '*900.', '1 500.', '2 400.'], 'A + G = N/2 = 1 500 → G = 1 500 – 600 = 900.', 'fix'],
  ['Loại RNA có chức năng vận chuyển amino acid đến ribosome để tổng hợp chuỗi polypeptide là', ['*tRNA.', 'mRNA.', 'rRNA.', 'DNA.'], 'tRNA – RNA vận chuyển.'],
  ['Chỉ từ 4 loại nucleotide nhưng tạo nên vô số phân tử DNA khác nhau vì DNA', ['có cấu trúc xoắn kép.', 'có hai mạch song song, ngược chiều.', '*khác nhau về số lượng, thành phần và trình tự sắp xếp các nucleotide.', 'có các liên kết hydrogen giữa hai mạch.'], 'Tính đa dạng và đặc trưng của DNA.'],
  ['Một phân tử DNA tái bản liên tiếp 3 lần. Trong số các phân tử DNA con tạo ra, số phân tử còn chứa mạch của DNA mẹ ban đầu là', ['1.', '*2.', '4.', '8.'], 'Tạo 2³ = 8 DNA con; theo nguyên tắc bán bảo toàn, hai mạch của DNA mẹ nằm ở 2 DNA con.', 'fix'],
  ['Một đoạn mạch khuôn của gene có trình tự: 3′– TAC GGA TCA –5′. Đoạn mRNA được phiên mã từ đoạn mạch này có trình tự', ['5′– ATG CCT AGT –3′.', '3′– AUG CCU AGU –5′.', '5′– UAC GGA UCA –3′.', '*5′– AUG CCU AGU –3′.'], 'Phiên mã: A – U, T – A, G – C, C – G; mRNA ngược chiều mạch khuôn.'],
];
const TARGET = 'ADCABCDBACBD';
