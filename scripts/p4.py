PUN = ('<div class="two">'
       '<div class="box fm"><h5>🧮 Bảng tổ hợp F₁ × F₁: Aa × Aa</h5><table class="pn"><tr><th>♀ \\ ♂</th><th>A</th><th>a</th></tr>'
       '<tr><th>A</th><td>AA</td><td>Aa</td></tr><tr><th>a</th><td>Aa</td><td>aa</td></tr></table>'
       '<div style="text-align:center">KG: 1 AA : 2 Aa : 1 aa &nbsp;→&nbsp; KH: 3 trội : 1 lặn</div></div>'
       '<div class="box fm"><h5>🫛 F₂ lai hai cặp tính trạng (AaBb × AaBb)</h5><table class="pn"><tr><th>Kiểu hình</th><th>Kiểu gene</th><th>Tỉ lệ</th></tr>'
       '<tr><td>Vàng, trơn</td><td>A_B_</td><td>9/16</td></tr><tr><td>Vàng, nhăn</td><td>A_bb</td><td>3/16</td></tr>'
       '<tr><td>Xanh, trơn</td><td>aaB_</td><td>3/16</td></tr><tr><td>Xanh, nhăn</td><td>aabb</td><td>1/16</td></tr></table></div></div>')

P = dict(fact_top=True, num=4, subject='SINH HỌC', icon='🧬', title='Di truyền học Mendel', en="Mendelian Genetics",
 theme=dict(c='#15803d', cbg='#eaf7ee', csoft='#bbe5c8', grad='linear-gradient(120deg,#14532d 0%,#16a34a 50%,#86efac 100%)', shades=['#15803d', '#1b9447', '#22a855']),
 theory=[
  ('tree', 'MỘT SỐ KHÁI NIỆM DI TRUYỀN HỌC', '🧬', [
     ('Tính trạng – nhân tố di truyền', ['<b>Tính trạng</b>: đặc điểm về hình thái, cấu tạo, sinh lí… của cơ thể (thân cao, hạt vàng…).', '<b>Cặp tính trạng tương phản</b>: hai trạng thái trái ngược của cùng một tính trạng (thân cao – thân thấp).', '<b>Nhân tố di truyền</b> (nay gọi là gene) quy định tính trạng.']),
     ('Gene – allele – kiểu gene', ['<b>Allele</b>: các trạng thái khác nhau của cùng một gene (A và a).', '<b>Kiểu gene</b>: tổ hợp các allele của cơ thể (AA, Aa, aa…).', '<b>Kiểu hình</b>: tổ hợp các tính trạng của cơ thể.']),
     ('Đồng hợp – dị hợp – kí hiệu', ['<b>Đồng hợp</b>: hai allele giống nhau (AA, aa); <b>dị hợp</b>: hai allele khác nhau (Aa).', '<b>Giống thuần chủng</b>: con cháu giống bố mẹ về tính trạng đang xét.', 'P: bố mẹ; G: giao tử; F₁, F₂: đời con; ×: phép lai; ♀ cái, ♂ đực.'])]),
  ('tree', 'CÁC QUY LUẬT DI TRUYỀN CỦA MENDEL', '🫛', [
     ('Phương pháp', ['<b>Phân tích các thế hệ lai</b>: lai bố mẹ thuần chủng khác nhau về một hoặc vài cặp tính trạng tương phản, theo dõi riêng từng cặp qua các thế hệ, dùng thống kê để phân tích.', 'Đối tượng: <b>đậu Hà Lan</b>.']),
     ('Lai một cặp – Quy luật phân li', ['P t/c: hạt vàng × hạt xanh → F₁: 100% vàng → F₂: <b>3 vàng : 1 xanh</b>.', 'Mỗi tính trạng do một cặp nhân tố di truyền quy định; khi hình thành giao tử, mỗi nhân tố trong cặp <b>phân li</b> về một giao tử và giữ nguyên bản chất.']),
     ('Lai hai cặp – Phân li độc lập', ['P t/c: vàng, trơn × xanh, nhăn → F₁: 100% vàng, trơn → F₂: <b>9 : 3 : 3 : 1</b>.', 'Các cặp nhân tố di truyền <b>phân li độc lập</b> khi hình thành giao tử.', 'Tỉ lệ mỗi kiểu hình ở F₂ bằng <b>tích</b> tỉ lệ các tính trạng hợp thành → xuất hiện <b>biến dị tổ hợp</b>.'])]),
  ('html', PUN),
  ('fm', 'Lai phân tích & mẹo tính nhanh', ['<b>Lai phân tích:</b> cá thể mang tính trạng trội (A_) × cá thể mang tính trạng lặn (aa)', '<b>Đời con 100% trội</b> → cá thể đem lai đồng hợp (AA)', '<b>Đời con 1 trội : 1 lặn</b> → cá thể đem lai dị hợp (Aa)',
         '<b>Giao tử:</b> mỗi giao tử mang 1 allele của mỗi cặp; AaBb → AB, Ab, aB, ab', '<b>Số loại giao tử</b> = 2ⁿ (n: số cặp gene dị hợp, phân li độc lập)', '<b>Tách riêng từng cặp</b> rồi nhân: Aa × Aa → ¾ trội; Aa × aa → ½ trội']),
  ('warn', 'Lỗi sai thường gặp', ['Không quy ước gene trước khi viết sơ đồ lai.', 'Viết giao tử mang cả hai allele của một cặp (sai: giao tử "Aa").',
         'Nhầm tỉ lệ kiểu gene (1 : 2 : 1) với tỉ lệ kiểu hình (3 : 1).', 'Cơ thể mang tính trạng trội chưa rõ kiểu gene → phải xét đủ trường hợp AA và Aa.'])],
 levels=[5, 6, 5],
 mc=[
  dict(dc=6, q='Theo Mendel, yếu tố được truyền nguyên vẹn từ bố mẹ sang con là', o=['kiểu gene.', 'allele.', '*nhân tố di truyền.', 'tính trạng.'], e='Mendel cho rằng nhân tố di truyền được truyền nguyên vẹn, không hòa trộn.'),
  dict(dc=4, q='Muốn xác định một cá thể mang tính trạng trội có kiểu gene đồng hợp hay dị hợp, người ta dùng phương pháp', o=['*lai phân tích.', 'lai với bố mẹ.', 'lai tương đương.', 'quan sát dưới kính hiển vi.'], e='Lai phân tích: lai với cá thể mang tính trạng lặn để đọc kiểu gene qua đời con.'),
  dict(q='Kiểu gene nào sau đây là đồng hợp?', o=['Aa.', 'Bb.', 'AaBb.', '*aa.'], e='aa gồm hai allele giống nhau.'),
  dict(q='Đối tượng chủ yếu Mendel dùng trong các thí nghiệm lai là', o=['*đậu Hà Lan.', 'ruồi giấm.', 'cà chua.', 'lúa nước.'], e='Mendel làm thí nghiệm trên đậu Hà Lan.'),
  dict(dc=28, fix=True, q='Cho các kiểu gene: (1) AaBB; (2) AaBb; (3) Aabb; (4) AABB. Các cá thể dị hợp là', o=['2, 3 và 4.', '2.', '*1, 2 và 3.', '1.'], e='(1), (2), (3) đều có ít nhất một cặp dị hợp (Aa); AABB đồng hợp cả hai cặp.'),
  dict(dc=2, q='Ở cà chua, A: thân đỏ thẫm, a: thân xanh lục. Phép lai thân đỏ thẫm × thân đỏ thẫm cho F₁ 100% thân đỏ thẫm. Kiểu gene của P có thể là', o=['Aa × Aa.', '*AA × AA.', 'Aa × aa.', 'aa × aa.'], e='Aa × Aa cho 3 : 1; Aa × aa cho 1 : 1; aa × aa cho 100% xanh lục → chọn AA × AA (P là AA × Aa cũng thỏa mãn nhưng không có trong các phương án).'),
  dict(dc=10, q='Ở chó, lông ngắn trội hoàn toàn so với lông dài. P: lông ngắn thuần chủng × lông dài. Kết quả ở F₁ là', o=['3 lông ngắn : 1 lông dài.', '1 lông ngắn : 1 lông dài.', 'toàn lông dài.', '*toàn lông ngắn.'], e='AA × aa → F₁ 100% Aa (lông ngắn).'),
  dict(dc=11, q='Quy luật phân li độc lập được Mendel rút ra từ', o=['phép lai phân tích.', 'quan sát tế bào dưới kính hiển vi.', '*thí nghiệm lai hai cặp tính trạng.', 'thí nghiệm lai một cặp tính trạng.'], e='Lai hai cặp tính trạng (vàng, trơn × xanh, nhăn) cho F₂ 9 : 3 : 3 : 1 = (3 : 1)(3 : 1) → hai cặp tính trạng di truyền độc lập.'),
  dict(dc=24, fix=True, q='Điền vào chỗ trống: "Khi lai hai bố mẹ khác nhau về (1)… cặp tính trạng thuần chủng tương phản (2)… với nhau thì F₂ có tỉ lệ mỗi kiểu hình bằng (3)… các tỉ lệ của các tính trạng hợp thành nó."', o=['*hai; di truyền độc lập; tích.', 'một; di truyền độc lập; tích.', 'hai; di truyền; tích.', 'hai; di truyền độc lập; tổng.'], e='Nội dung quy luật phân li độc lập.'),
  dict(q='Phép lai Aa × aa (A trội hoàn toàn) cho đời con có tỉ lệ kiểu hình là', o=['3 trội : 1 lặn.', '*1 trội : 1 lặn.', '1 : 2 : 1.', '100% trội.'], e='Aa × aa → 1 Aa : 1 aa.'),
  dict(q='Cơ thể có kiểu gene AaBb (hai cặp gene phân li độc lập) tạo ra số loại giao tử là', o=['2.', '*4.', '8.', '1.'], e='AB, Ab, aB, ab (2² = 4).'),
  dict(dc=29, q='Tỉ lệ phân li kiểu hình của phép lai P: AaBb × aabb (trội hoàn toàn, phân li độc lập) là', o=['9 : 3 : 3 : 1.', '3 : 3 : 1 : 1.', '*1 : 1 : 1 : 1.', '1 : 2 : 1 : 2 : 1.'], e='(1 : 1)(1 : 1) = 1 : 1 : 1 : 1.'),
  dict(dc=30, q='Thực hiện phép lai P: AABB × aabb, F₁ tự thụ phấn. Các kiểu gene thuần chủng xuất hiện ở F₂ là', o=['*AABB, AAbb, aaBB và aabb.', 'AABB và AAbb.', 'AABB, AAbb và aaBB.', 'AABB và aaBB.'], e='F₁ AaBb tự thụ → F₂ có 4 kiểu gene đồng hợp cả hai cặp.'),
  dict(dc=26, q='A: thân cao trội hoàn toàn so với a: thân thấp; B: quả đỏ trội hoàn toàn so với b: quả vàng. Phép lai AaBb × aaBb cho đời con có kiểu hình thân cao, quả đỏ chiếm tỉ lệ', o=['56,25%.', '18,75%.', '*37,5%.', '12,5%.'], e='Aa × aa → ½ cao; Bb × Bb → ¾ đỏ; ½ × ¾ = 3/8 = 37,5%.'),
  dict(q='Lai đậu Hà Lan hạt vàng thuần chủng với hạt xanh, F₁ toàn hạt vàng. Cho F₁ tự thụ phấn, F₂ thu được 1 200 cây. Theo lí thuyết, số cây hạt xanh ở F₂ là', o=['*300.', '400.', '600.', '900.'], e='F₂: 3 vàng : 1 xanh → 1 200 × ¼ = 300.'),
  dict(q='Phép lai AaBb × AaBb (phân li độc lập) cho tỉ lệ con có kiểu gene aabb là', o=['*6,25%.', '25%.', '12,5%.', '56,25%.'], e='¼ aa × ¼ bb = 1/16 = 6,25%.')],
 ds=[
  dict(dc='3.1', q='Về thí nghiệm lai hai cặp tính trạng của Mendel (P thuần chủng: hạt vàng, trơn × hạt xanh, nhăn):', it=[('F₂ có tỉ lệ phân li kiểu hình 9 : 3 : 3 : 2.', 'S', 'tỉ lệ đúng là 9 : 3 : 3 : 1'),
       ('F₁ đồng tính, toàn hạt vàng, trơn.', 'Đ', 'P thuần chủng tương phản → F₁ đồng tính trội'),
       ('Ở F₂ xuất hiện các biến dị tổ hợp: vàng, nhăn và xanh, trơn.', 'Đ', 'kiểu hình khác P do tổ hợp lại tính trạng'),
       ('Quy luật di truyền của Mendel chỉ đúng với cây đậu Hà Lan.', 'S', 'đúng với nhiều loài sinh vật')]),
  dict(dc='3.2', q='Về phép lai phân tích:', it=[('Phép lai phân tích giúp xác định kiểu gene của cá thể mang tính trạng trội.', 'Đ', 'đúng mục đích'),
       ('Phép lai phân tích chỉ áp dụng cho các tính trạng lặn.', 'S', 'dùng để kiểm tra cá thể mang tính trạng trội'),
       ('Nếu đời con của phép lai phân tích đồng tính trội thì cá thể đem lai có kiểu gene đồng hợp trội.', 'Đ', 'AA × aa → 100% Aa'),
       ('Phép lai phân tích luôn cho đời con đồng tính.', 'S', 'nếu cá thể đem lai dị hợp, đời con phân li 1 : 1')]),
  dict(q='Về các khái niệm di truyền học:', it=[('Allele là các trạng thái khác nhau của cùng một gene.', 'Đ', 'định nghĩa'),
       ('Hai cơ thể dị hợp (Aa) giao phấn với nhau luôn cho đời con 100% thuần chủng.', 'S', 'Aa × Aa → có ½ Aa không thuần chủng'),
       ('Kiểu hình là tổ hợp các tính trạng của cơ thể.', 'Đ', 'định nghĩa'),
       ('Khi trội hoàn toàn, tính trạng lặn chỉ biểu hiện ở cơ thể đồng hợp lặn (aa).', 'Đ', 'Aa biểu hiện tính trạng trội')])],
 sa=[
  dict(dc=13, q='Một gene quy định một tính trạng, trội hoàn toàn, các gene phân li độc lập. Cơ thể dị hợp 2 cặp gene tự thụ phấn, F₁ thu được 240 hạt. Theo lí thuyết, số hạt dị hợp 2 cặp gene ở F₁ là bao nhiêu?', box=[('Đáp số:', 'hạt')],
       a='AaBb × AaBb: P(AaBb) = ½ × ½ = ¼ → 240 × ¼ = <b>60 hạt</b>.'),
  dict(q='Cơ thể có kiểu gene AaBbDd (các cặp gene phân li độc lập) tạo ra tối đa bao nhiêu loại giao tử?', box=[('Đáp số:', 'loại')], a='2³ = <b>8 loại</b>.'),
  dict(q='P thuần chủng: hạt vàng, trơn × hạt xanh, nhăn → F₁ tự thụ phấn, F₂ thu được 1 600 hạt. Theo lí thuyết, số hạt xanh, trơn ở F₂ là bao nhiêu?', box=[('Đáp số:', 'hạt')], a='Xanh, trơn = 3/16 → 1 600 × 3/16 = <b>300 hạt</b>.'),
  dict(q='Phép lai Aa × Aa cho đời con có kiểu gene dị hợp chiếm bao nhiêu phần trăm?', box=[('Đáp số:', '%')], a='1 AA : 2 Aa : 1 aa → Aa = <b>50%</b>.')],
 tl=[
  dict(lvl='cb', dc=14, q='Ở lúa, hạt gạo đục trội hoàn toàn so với hạt gạo trong. Cho cây lúa hạt gạo đục thuần chủng thụ phấn với cây lúa hạt gạo trong. Viết sơ đồ lai, xác định kết quả ở F₁ và F₂.', lines=4,
       a='Quy ước A: đục, a: trong. P: AA × aa → G: A, a → F₁: 100% Aa (đục). F₁ × F₁: Aa × Aa → F₂: KG 1 AA : 2 Aa : 1 aa; KH 3 đục : 1 trong.'),
  dict(lvl='cb', dc=15, q='Ở cà chua, quả đỏ trội hoàn toàn so với quả vàng. Xác định kiểu gene, kiểu hình của F₁ trong các trường hợp: a) P: quả đỏ × quả đỏ; b) P: quả đỏ × quả vàng; c) P: quả vàng × quả vàng.', lines=5,
       a='A: đỏ, a: vàng. a) AA × AA → 100% AA (đỏ); AA × Aa → 1 AA : 1 Aa (100% đỏ); Aa × Aa → 1 AA : 2 Aa : 1 aa (3 đỏ : 1 vàng). b) AA × aa → 100% Aa (đỏ); Aa × aa → 1 Aa : 1 aa (1 đỏ : 1 vàng). c) aa × aa → 100% aa (vàng).'),
  dict(lvl='nc', dc=16, q='Ở đậu Hà Lan, thân cao (A) và hạt vàng (B) trội hoàn toàn so với thân thấp (a) và hạt xanh (b); hai cặp tính trạng di truyền độc lập. Lập sơ đồ lai (xét đủ các trường hợp):', sub=['a) Cây thân cao, hạt xanh × cây thân thấp, hạt vàng.', 'b) Cây thân cao, hạt vàng × cây thân thấp, hạt xanh.'], lines=6,
       a='a) A_bb × aaB_: AAbb × aaBB → 100% cao, vàng; AAbb × aaBb → 1 cao, vàng : 1 cao, xanh; Aabb × aaBB → 1 cao, vàng : 1 thấp, vàng; Aabb × aaBb → 1 cao, vàng : 1 cao, xanh : 1 thấp, vàng : 1 thấp, xanh. b) A_B_ × aabb: AABB → 100% cao, vàng; AABb → 1 cao, vàng : 1 cao, xanh; AaBB → 1 cao, vàng : 1 thấp, vàng; AaBb → 1 : 1 : 1 : 1 (cao vàng : cao xanh : thấp vàng : thấp xanh).')],
 tt=[dict(t='🌾 Kiểm tra giống lúa.', q='Một người nông dân mua giống lúa hạt gạo đục (trội) nhưng không biết giống đó có thuần chủng không. Em hãy đề xuất cách kiểm tra và cho biết cách đọc kết quả.', lines=3,
          a='Dùng lai phân tích: lai cây hạt đục với cây hạt trong (aa). Nếu đời con 100% hạt đục → giống thuần chủng (AA); nếu đời con có cả hạt đục và hạt trong (≈ 1 : 1) → giống không thuần chủng (Aa).')],
 fact='Mendel công bố kết quả nghiên cứu năm 1866 nhưng gần như bị lãng quên suốt khoảng 35 năm; đến năm 1900 các nhà khoa học mới "tái phát hiện" và ông được coi là cha đẻ của di truyền học.',
 job='kĩ sư chọn tạo giống cây trồng, nhà di truyền học, chuyên viên tư vấn di truyền, kĩ sư công nghệ sinh học.')
