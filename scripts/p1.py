P = dict(fact_top=False, num=1, subject='MỞ ĐẦU', icon='🔬', title='Dụng cụ, hóa chất – Báo cáo và thuyết trình khoa học', en='Lab Skills – Scientific Reports and Presentations',
 theme=dict(c='#4338ca', cbg='#eef0fd', csoft='#cdd2f7', grad='linear-gradient(120deg,#1e1b4b 0%,#4338ca 50%,#7c3aed 100%)', shades=['#4338ca', '#5146d6', '#6d4fe0']),
 theory=[
  ('tree', 'BÁO CÁO VÀ THUYẾT TRÌNH KHOA HỌC', '🎤', [
     ('Cấu trúc báo cáo', ['Tên đề tài, người thực hiện.', 'Mục tiêu (câu hỏi nghiên cứu) và <b>giả thuyết khoa học</b>.', 'Dụng cụ, <b>phương pháp thực hiện</b>.', '<b>Kết quả và thảo luận</b> (bảng số liệu, đồ thị).', '<b>Kết luận</b> (và kiến nghị); tài liệu tham khảo.']),
     ('Cấu trúc bài thuyết trình', ['<b>Mở đầu</b>: giới thiệu vấn đề, lí do, mục tiêu.', '<b>Nội dung</b>: các ý chính kèm dẫn chứng, hình ảnh, số liệu.', '<b>Kết luận</b>: tóm tắt, nêu <b>đề xuất, kiến nghị</b>; cảm ơn, trả lời câu hỏi.']),
     ('Kĩ năng trình bày', ['Tìm hiểu kĩ nội dung, dùng nguồn tin cậy và ghi rõ nguồn.', 'Slide ít chữ, nhiều hình ảnh, sơ đồ; chữ đủ to.', 'Nói rõ ràng, giao tiếp bằng mắt, đúng thời gian; lắng nghe và trả lời câu hỏi.'])]),
  ('tree', 'DỤNG CỤ – HÓA CHẤT – AN TOÀN', '🧪', [
     ('Dụng cụ thường dùng', ['Vật lí: ampe kế, vôn kế, đồng hồ đo điện đa năng, biến áp nguồn, giá quang học, thấu kính, lăng kính.', 'Hóa học: ống nghiệm, cốc thủy tinh, bình tam giác, ống đong, đèn cồn, kẹp ống nghiệm.']),
     ('Sử dụng hóa chất', ['Đọc kĩ nhãn và <b>kí hiệu cảnh báo</b> (dễ cháy, ăn mòn, độc…).', 'Lấy lượng nhỏ theo hướng dẫn; không nếm, không ngửi trực tiếp.', 'Không đổ hóa chất thừa trở lại lọ đựng.']),
     ('An toàn phòng thí nghiệm', ['Mặc áo, đeo kính và găng tay bảo hộ khi cần.', 'Pha loãng acid đặc: <b>rót từ từ acid vào nước</b>, không làm ngược lại.', 'Báo ngay cho giáo viên khi có sự cố.'])]),
  ('warn', 'Lỗi hay gặp khi làm báo cáo, thuyết trình', ['Thay đổi nhiều yếu tố cùng lúc nên không biết yếu tố nào gây ra kết quả.', 'Chỉ làm thí nghiệm một lần; số liệu thiếu đơn vị.',
         'Sửa số liệu cho "khớp" giả thuyết – vi phạm trung thực khoa học.', 'Đọc nguyên văn slide, quá thời gian, không trả lời được câu hỏi.'])],
 levels=[3, 3, 2],
 mc=[
  dict(dc=3, q='Trong bài thuyết trình khoa học, phần nào là nơi trình bày các đề xuất hoặc kiến nghị?', o=['Phương pháp thực hiện.', 'Nội dung.', '*Kết luận.', 'Mở đầu.'], e='Đề xuất, kiến nghị được nêu ở phần kết luận, sau khi đã tổng hợp kết quả.'),
  dict(q='Phần nêu câu hỏi, vấn đề mà nghiên cứu cần giải quyết là', o=['kết luận.', '*mục tiêu nghiên cứu.', 'kết quả và thảo luận.', 'tài liệu tham khảo.'], e='Mục tiêu (câu hỏi nghiên cứu) nêu điều cần tìm hiểu.'),
  dict(q='Kí hiệu cảnh báo hình ngọn lửa trên nhãn lọ hóa chất cho biết đó là chất', o=['*dễ cháy.', 'ăn mòn.', 'gây độc.', 'phóng xạ.'], e='Hình ngọn lửa: chất dễ cháy.'),
  dict(dc=9, q='Khi tiến hành báo cáo khoa học, phần nào đóng vai trò quan trọng nhất trong việc bảo đảm kết quả thí nghiệm có giá trị?', o=['Mục tiêu nghiên cứu.', 'Kết quả và thảo luận.', '*Phương pháp thực hiện.', 'Giả thuyết khoa học.'], e='Phương pháp đúng, rõ ràng, lặp lại được thì số liệu mới đáng tin cậy.'),
  dict(q='Khi pha loãng dung dịch sulfuric acid đặc, cần', o=['*rót từ từ acid vào nước và khuấy đều.', 'rót nhanh nước vào acid.', 'rót từ từ nước vào acid.', 'đun nóng acid rồi thêm nước.'], e='Pha loãng acid đặc tỏa nhiều nhiệt; rót nước vào acid có thể làm acid sôi, bắn ra gây bỏng.'),
  dict(q='Slide của một bài thuyết trình hiệu quả nên', o=['*ít chữ, có hình ảnh, sơ đồ minh họa.', 'chép nguyên văn toàn bộ bài nói.', 'dùng thật nhiều màu và hiệu ứng.', 'chữ nhỏ để chứa nhiều nội dung.'], e='Slide chỉ hỗ trợ người nói, cần dễ đọc, trực quan.'),
  dict(q='Trước khi làm thí nghiệm "Ảnh hưởng của nhiệt độ nước đến tốc độ hòa tan của đường", bạn Lan dự đoán: "Nước càng nóng thì đường tan càng nhanh". Dự đoán này thuộc phần nào của báo cáo?', o=['*Giả thuyết khoa học.', 'Kết luận.', 'Phương pháp thực hiện.', 'Tên đề tài.'], e='Dự đoán đưa ra trước khi kiểm chứng là giả thuyết khoa học.'),
  dict(q='Để kết quả thí nghiệm ở câu 7 đáng tin cậy, bạn Lan nên', o=['làm thí nghiệm một lần là đủ.', '*chỉ thay đổi nhiệt độ, giữ nguyên các yếu tố khác và lặp lại nhiều lần.', 'thay đổi cùng lúc nhiệt độ và lượng đường.', 'chỉ ghi lại kết quả phù hợp với dự đoán.'], e='Chỉ thay đổi một yếu tố (biến độc lập), giữ nguyên yếu tố khác, lặp lại để lấy trung bình.')],
 ds=[
  dict(q='Về báo cáo và thuyết trình khoa học:', it=[('Phần kết luận có thể nêu các đề xuất, kiến nghị.', 'Đ', 'đúng cấu trúc'),
       ('Khi thuyết trình, nên đọc nguyên văn nội dung trên slide.', 'S', 'slide chỉ hỗ trợ, người nói cần diễn giải'),
       ('Số liệu nên trình bày bằng bảng, đồ thị để dễ so sánh.', 'Đ', 'trực quan, dễ phân tích'),
       ('Khi kết quả thí nghiệm khác giả thuyết, cần sửa số liệu cho phù hợp.', 'S', 'phải trung thực; giả thuyết có thể bị bác bỏ')])],
 sa=[],
 tl=[
  dict(lvl='cb', q='Lập dàn ý (3 phần) cho bài thuyết trình khoảng 3 phút với chủ đề: "Vì sao không nên dùng thùng sắt để pha thuốc Bordeaux (chứa CuSO₄)?"', lines=5,
       a='Mở đầu: giới thiệu thuốc Bordeaux và vấn đề dụng cụ pha. Nội dung: Fe đứng trước Cu trong dãy hoạt động hóa học → Fe + CuSO₄ → FeSO₄ + Cu; hậu quả: thùng bị ăn mòn, thuốc giảm tác dụng; minh họa bằng ảnh/thí nghiệm đinh sắt trong CuSO₄. Kết luận: dùng thùng nhựa; kiến nghị tuyên truyền cho bà con.'),
  dict(lvl='nc', q='Bạn Minh viết báo cáo: "Đề tài: Quả bóng nào nảy tốt hơn? Em thả quả bóng rổ từ độ cao 1 m và quả bóng tennis từ độ cao 2 m, mỗi quả thả 1 lần. Kết quả: bóng rổ nảy 60, bóng tennis nảy 110. Kết luận: bóng tennis nảy tốt hơn." Chỉ ra ít nhất 3 điểm chưa hợp lí và đề xuất cách sửa.', lines=5,
       a='(1) Thay đổi cùng lúc 2 yếu tố (loại bóng và độ cao thả) → phải thả hai quả từ cùng độ cao. (2) Chỉ thả 1 lần → lặp lại 3 – 5 lần, lấy trung bình. (3) Số liệu thiếu đơn vị (cm). (4) Thiếu giả thuyết, dụng cụ – phương pháp, bảng số liệu. (Gợi ý nâng cao: so sánh tỉ lệ độ cao nảy/độ cao thả, liên hệ phần cơ năng chuyển hóa thành nhiệt năng.)')],
 tt=[dict(t='🚗 Ngày hội STEM.', q='Em sắp thuyết trình 3 phút trước lớp về sản phẩm STEM "Xe chạy bằng năng lượng Mặt Trời". Nêu 3 việc em sẽ chuẩn bị để bài thuyết trình hấp dẫn, thuyết phục.', lines=3,
          a='Gợi ý: chuẩn bị sản phẩm thật để trình diễn; slide ít chữ với ảnh, sơ đồ nguyên lí (quang năng → điện năng → cơ năng) và số liệu đo được; tập nói đúng 3 phút, dự kiến câu hỏi và câu trả lời.')],
 fact='Trước khi được đăng, một bài báo khoa học thường phải qua bình duyệt (peer review): các nhà khoa học khác kiểm tra phương pháp và số liệu. Nhờ vậy, kết quả khoa học đáng tin cậy hơn.',
 job='nhà nghiên cứu khoa học, nhà báo khoa học, giáo viên, kĩ thuật viên phòng thí nghiệm.')
