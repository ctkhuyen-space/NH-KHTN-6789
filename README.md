# Ngân hàng Khoa học Tự nhiên — Lớp 6, 7, 8, 9

Bộ công cụ soạn đề và quản lý ngân hàng câu hỏi môn Khoa học tự nhiên theo chương trình **Kết nối tri thức với cuộc sống** (KNTT), dùng cho giáo viên THCS.

## Cấu trúc thư mục

```
├── web/                  # Trang web (HTML artifacts)
│   ├── soan-de.html      # Công cụ soạn đề dành cho GV
│   ├── kho-hoc-lieu.html # Kho học liệu đầy đủ (GV + HS)
│   └── phieu_hs.html     # Phiếu bài tập cho HS
│
├── data/                 # Dữ liệu ngân hàng câu hỏi
│   ├── bank.json         # 989 câu hỏi (MC, Đ/S, TL, TT)
│   └── curriculum.json   # Chương trình KNTT lớp 6–9
│
├── scripts/              # Scripts tạo ngân hàng câu hỏi
│   ├── import_all.py     # Import tổng hợp từ nhiều nguồn
│   ├── common.py         # Hàm dùng chung
│   ├── gen*.py           # Sinh câu hỏi
│   ├── ch*.py            # Dữ liệu câu hỏi theo chương (Lớp 7)
│   ├── k*.py             # Dữ liệu câu hỏi (Lớp 8)
│   ├── n*.py             # Dữ liệu câu hỏi (Lớp 9)
│   ├── p*.py             # Phiếu bài tập
│   └── build*, body*, content*, make*  # Tiện ích build
│
└── sources/              # Tài liệu gốc (.docx, .pdf, .doc)
```

## Ngân hàng câu hỏi

Tổng: **989 câu** phân bố theo lớp và dạng:

| Lớp | MC | Đ/S | TL | TT | Tổng |
|-----|----:|-----:|----:|----:|-----:|
| 6   | 185 |  22  | 56  | 25  | 288  |
| 7   | 115 |  16  | 32  | 15  | 178  |
| 8   | 148 |  20  | 36  | 14  | 218  |
| 9   | 212 |  28  | 46  | 19  | 305  |

Các dạng câu hỏi:
- **MC** — Trắc nghiệm nhiều lựa chọn (4 phương án A–D)
- **Đ/S** — Đúng/Sai (4 ý, xác định Đúng hoặc Sai)
- **TL** — Tự luận
- **TT** — Thực tiễn / Song ngữ

## Cấu trúc đề kiểm tra mặc định

12 TN + 2 Đ/S (4 ý mỗi câu) + 4 TL + 2 TT = 20 câu

## Công cụ web

### Soạn đề KHTN (`web/soan-de.html`)
Dành riêng cho giáo viên. Duyệt, lọc ngân hàng câu hỏi. Bốc đề ngẫu nhiên theo cấu trúc tùy chỉnh. Tạo nhiều mã đề (xáo trộn thứ tự câu và phương án). Xuất Word (.doc) và HTML (in PDF) kèm đáp án.

### Kho học liệu (`web/kho-hoc-lieu.html`)
Dành cho cả GV và HS. GV quản lý ngân hàng, soạn đề. HS luyện tập, tự chấm điểm.

---

**Tác giả:** Công Thị Khánh Huyền — Giáo viên KHTN, Trường THCS Thiên Lộc, Hà Nội
