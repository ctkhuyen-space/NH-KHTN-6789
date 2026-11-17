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
├── sources/              # Tài liệu gốc (.docx, .pdf, .doc)
│
└── de-thi-khtn/          # Đề thi chính thức theo năm học
    ├── <năm học>/                 # VD: 2026-2027
    │   └── <kỳ thi>/              # giua-ky-1, cuoi-ky-1, giua-ky-2, cuoi-ky-2
    │       └── khoi-<lớp>/        # khoi-6, khoi-7, khoi-8, khoi-9
    │           ├── de-goc/        # Đề gốc (chưa trộn mã)
    │           ├── ma-de/         # Các mã đề đã trộn
    │           ├── ma-tran/       # Ma trận đề thi (nếu có)
    │           └── dap-an/        # Đáp án / file chấm
    │
    └── cong-cu/           # Công cụ soạn đề độc lập, không thuộc một kỳ thi cụ thể
```

### Quy ước đặt tên

- Tên thư mục/file không dấu, dùng gạch ngang `-` để nối từ (VD: `giua-ky-1`, `khoi-8`, `de-goc`).
- Mỗi kỳ thi có đủ 4 thư mục con: `de-goc`, `ma-de`, `ma-tran`, `dap-an` (bỏ qua thư mục nào chưa có file).
- Tên file gốc giữ nguyên để tra cứu, không đổi nội dung khi di chuyển.

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

## Cấu trúc đề thi theo mẫu 2025 (dùng cho `de-thi-khtn/`)

- **Phần I. Trắc nghiệm** (4 điểm) — 16 câu, mỗi câu 0,25 điểm (4 Lý, 4 Hóa, 8 Sinh).
- **Phần II. Đúng/Sai** (3 điểm) — 3 câu (1 Lý, 1 Hóa, 1 Sinh), mỗi câu 1 điểm với 4 ý Đúng/Sai: đúng 1 ý được 0,1 điểm, 2 ý được 0,25 điểm, 3 ý được 0,5 điểm, 4 ý được 1 điểm.
- **Phần III. Trả lời ngắn** (3 điểm) — mỗi câu 0,5 điểm.

## Công cụ web

### Soạn đề KHTN (`web/soan-de.html`)
Dành riêng cho giáo viên. Duyệt, lọc ngân hàng câu hỏi. Bốc đề ngẫu nhiên theo cấu trúc tùy chỉnh. Tạo nhiều mã đề (xáo trộn thứ tự câu và phương án). Xuất Word (.doc) và HTML (in PDF) kèm đáp án.

### Kho học liệu (`web/kho-hoc-lieu.html`)
Dành cho cả GV và HS. GV quản lý ngân hàng, soạn đề. HS luyện tập, tự chấm điểm.

---

**Tác giả:** Công Thị Khánh Huyền — Giáo viên KHTN, Trường THCS Thiên Lộc, Hà Nội
