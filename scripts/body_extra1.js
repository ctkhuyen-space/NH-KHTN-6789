add(P('Phạm vi: Bài 30. Khái quát về cơ thể người – Bài 32. Dinh dưỡng và tiêu hóa ở người –', { run: { bold: true }, p: { alignment: AlignmentType.CENTER, spacing: { before: 160, after: 0 } } }));
add(P('Bài 33. Máu và hệ tuần hoàn của cơ thể người', { run: { bold: true }, p: { alignment: AlignmentType.CENTER } }));
add(P('Mức độ: Khá – Giỏi · Gồm 20 câu/bài: 12 trắc nghiệm nhiều lựa chọn, 2 Đúng/Sai, 4 tự luận – trả lời ngắn, 2 bài thực tiễn/song ngữ/thí nghiệm', { run: { italics: true }, p: { alignment: AlignmentType.CENTER, spacing: { after: 80 } } }));

// ===== A. KIẾN THỨC =====
H('A. KIẾN THỨC TRỌNG TÂM', 80);
const kt = [
  ['Bài', 'Kiến thức cần nhớ'],
  ['30. Khái quát về cơ thể người', 'Cơ thể người gồm đầu, cổ, thân, hai tay, hai chân và các hệ cơ quan: vận động (nâng đỡ, bảo vệ, vận động), tiêu hóa (biến đổi thức ăn, hấp thụ chất dinh dưỡng), tuần hoàn (vận chuyển các chất), hô hấp (trao đổi khí), bài tiết (thải chất thải), thần kinh (tiếp nhận, xử lí thông tin, điều khiển), nội tiết (tiết hormone điều hòa), sinh dục (sinh sản). Các hệ cơ quan phối hợp nhịp nhàng → cơ thể là một khối thống nhất.'],
  ['32. Dinh dưỡng và tiêu hóa', 'Dinh dưỡng: quá trình cơ thể tiếp nhận, biến đổi, sử dụng chất dinh dưỡng từ thức ăn. Nhóm sinh năng lượng: carbohydrate, protein, lipid; không sinh năng lượng: vitamin, chất khoáng, nước. Ống tiêu hóa: khoang miệng → hầu → thực quản → dạ dày → ruột non → ruột già → hậu môn; tuyến tiêu hóa: tuyến nước bọt, tuyến vị, gan, tụy, tuyến ruột. Miệng: amylase biến đổi một phần tinh bột chín → maltose; dạ dày: pepsin biến đổi một phần protein; ruột non: tiêu hóa hoàn toàn nhờ dịch tụy, dịch mật, dịch ruột và hấp thụ chủ yếu; ruột già: hấp thụ nước, tạo phân. Khẩu phần: đủ năng lượng, cân đối các chất, phù hợp lứa tuổi, giới tính, hoạt động. An toàn thực phẩm: ăn chín uống sôi, bảo quản đúng cách, đọc kĩ nhãn, hạn sử dụng.'],
  ['33. Máu và hệ tuần hoàn', 'Máu: huyết tương (≈ 55%) và tế bào máu (≈ 45%): hồng cầu vận chuyển O₂, CO₂; bạch cầu bảo vệ cơ thể; tiểu cầu tham gia đông máu. Nhóm máu ABO: A (kháng nguyên A, kháng thể β), B (B, α), AB (A và B, không có kháng thể), O (không có kháng nguyên, có α và β). Nguyên tắc truyền máu: kháng thể trong huyết tương người nhận không làm ngưng kết hồng cầu người cho; xét nghiệm kĩ trước khi truyền. Hệ tuần hoàn: tim (4 ngăn) và hệ mạch (động mạch, tĩnh mạch, mao mạch); vòng tuần hoàn nhỏ: tâm thất phải → động mạch phổi → mao mạch phổi → tĩnh mạch phổi → tâm nhĩ trái; vòng tuần hoàn lớn: tâm thất trái → động mạch chủ → mao mạch các cơ quan → tĩnh mạch chủ → tâm nhĩ phải. Miễn dịch: khả năng chống lại mầm bệnh; kháng nguyên kích thích cơ thể tạo kháng thể; vaccine giúp cơ thể chủ động tạo miễn dịch.'],
];
add(table(kt, [2300, W - 2300], { left: [1] }));

// ===== B. CÂU HỎI =====
H('B. CÂU HỎI ÔN TẬP');
H('PHẦN I. TRẮC NGHIỆM NHIỀU LỰA CHỌN (12 câu)', 60);
add(P('*Mỗi câu hỏi có 4 phương án, chỉ có 1 phương án đúng.*'));
const MC0 = [
  ['Hệ cơ quan có chức năng vận chuyển chất dinh dưỡng, oxygen đến các tế bào và vận chuyển chất thải đến các cơ quan bài tiết là', ['*hệ tuần hoàn.', 'hệ tiêu hóa.', 'hệ hô hấp.', 'hệ bài tiết.'], 'Hệ tuần hoàn vận chuyển các chất trong cơ thể.'],
  ['Khi chạy nhanh, tim đập nhanh hơn, thở gấp hơn và ra nhiều mồ hôi. Hiện tượng này chứng tỏ', ['*các hệ cơ quan phối hợp hoạt động, cơ thể là một khối thống nhất.', 'chỉ hệ vận động hoạt động khi chạy.', 'hệ tuần hoàn hoạt động độc lập với hệ hô hấp.', 'hệ bài tiết điều khiển các hệ cơ quan khác.'], 'Vận động tăng → cần nhiều O₂, chất dinh dưỡng, thải nhiều nhiệt → tuần hoàn, hô hấp, bài tiết cùng tăng cường (dưới sự điều khiển của hệ thần kinh).'],
  ['Nhóm chất dinh dưỡng nào sau đây <b>không</b> cung cấp năng lượng cho cơ thể?', ['*Vitamin, chất khoáng, nước.', 'Protein, lipid, carbohydrate.', 'Protein, vitamin, nước.', 'Lipid, chất khoáng, carbohydrate.'], 'Vitamin, chất khoáng, nước không sinh năng lượng nhưng cần cho hoạt động sống.'],
  ['Enzyme amylase trong nước bọt có tác dụng', ['*biến đổi một phần tinh bột chín thành đường maltose.', 'biến đổi protein thành amino acid.', 'biến đổi lipid thành glycerol và acid béo.', 'biến đổi protein thành chuỗi peptide ngắn.'], 'Tiêu hóa hóa học ở khoang miệng.'],
  ['Các chất dinh dưỡng được hấp thụ chủ yếu ở', ['*ruột non.', 'dạ dày.', 'ruột già.', 'thực quản.'], 'Ruột non dài, có nhiều nếp gấp, lông ruột, mạng mao mạch dày đặc.'],
  ['Dịch mật do gan tiết ra có vai trò chủ yếu là', ['*biến lipid thành các giọt nhỏ (nhũ tương hóa), giúp enzyme tiêu hóa lipid dễ dàng hơn.', 'biến đổi protein thành amino acid.', 'biến đổi tinh bột thành glucose.', 'tiêu diệt toàn bộ vi khuẩn trong thức ăn.'], 'Mật không chứa enzyme tiêu hóa nhưng hỗ trợ tiêu hóa lipid.'],
  ['Biện pháp nào sau đây giúp phòng tránh ngộ độc thực phẩm?', ['*Ăn chín, uống sôi; bảo quản thực phẩm đúng cách.', 'Dùng thực phẩm đã quá hạn sử dụng nếu chưa có mùi lạ.', 'Để thức ăn đã nấu chín ở nhiệt độ phòng qua đêm.', 'Dùng chung thớt cho thực phẩm sống và chín.'], 'Các phương án còn lại tạo điều kiện cho vi sinh vật phát triển hoặc lây nhiễm chéo.'],
  ['Thành phần nào của máu tham gia vào quá trình đông máu?', ['*Tiểu cầu.', 'Hồng cầu.', 'Bạch cầu.', 'Nước trong huyết tương.'], 'Tiểu cầu tham gia hình thành cục máu đông, chống mất máu.'],
  ['Trong huyết tương của người có nhóm máu A có loại kháng thể nào?', ['*Kháng thể β.', 'Kháng thể α.', 'Cả kháng thể α và β.', 'Không có kháng thể α và β.'], 'Nhóm A: hồng cầu có kháng nguyên A, huyết tương có kháng thể β.'],
  ['Một người có nhóm máu B cần được truyền máu. Theo nguyên tắc truyền máu, người này có thể nhận máu của người có nhóm máu', ['*B và O.', 'A và O.', 'AB và B.', 'A, B, AB và O.'], 'Huyết tương nhóm B có kháng thể α → không nhận được hồng cầu có kháng nguyên A (nhóm A, AB).'],
  ['Trong vòng tuần hoàn nhỏ, máu đi từ tâm thất phải theo đường nào để về tâm nhĩ trái?', ['*Động mạch phổi → mao mạch phổi → tĩnh mạch phổi.', 'Động mạch chủ → mao mạch các cơ quan → tĩnh mạch chủ.', 'Tĩnh mạch phổi → mao mạch phổi → động mạch phổi.', 'Tĩnh mạch chủ → mao mạch các cơ quan → động mạch chủ.'], 'Vòng tuần hoàn nhỏ đưa máu lên phổi trao đổi khí rồi về tim.'],
  ['Tiêm vaccine giúp phòng bệnh truyền nhiễm vì', ['*vaccine chứa kháng nguyên (mầm bệnh đã chết hoặc làm yếu), kích thích cơ thể tạo kháng thể và tế bào nhớ.', 'vaccine chứa sẵn kháng sinh tiêu diệt mầm bệnh.', 'vaccine làm tăng số lượng hồng cầu trong máu.', 'vaccine tiêu diệt ngay mọi vi khuẩn trong cơ thể.'], 'Cơ thể chủ động tạo miễn dịch, đáp ứng nhanh khi gặp lại mầm bệnh.'],
];
const TARGET = 'BDACCADBDBAC';
