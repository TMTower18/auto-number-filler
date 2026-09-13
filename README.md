# Auto Number Filler

Ứng dụng desktop Python đơn giản để tạo dãy số có prefix và số chữ số cố định. Ứng dụng chạy hoàn toàn offline, không cần cơ sở dữ liệu hoặc đăng nhập.

## Cấu trúc project

```text
AutoNumberFiller/
├── app.py
├── requirements.txt
└── README.md
```

## Chức năng từng file

- `app.py`: Chứa toàn bộ giao diện Tkinter và logic kiểm tra dữ liệu, tạo danh sách, sao chép, xóa dữ liệu.
- `requirements.txt`: Xác nhận không cần cài thêm thư viện bên ngoài.
- `README.md`: Hướng dẫn sử dụng và chạy ứng dụng.

## Cách chạy

1. Cài Python 3 nếu máy chưa có.
2. Mở Terminal hoặc Command Prompt tại thư mục project.
3. Chạy lệnh:

   ```bash
   python app.py
   ```

Trên một số máy Windows, dùng:

```bash
py app.py
```

Ví dụ nhập `Start = 1`, `End = 5`, `Prefix = ID-`, `Digits = 3`, sau đó bấm **Generate** để nhận `ID-001` đến `ID-005`. Nút **Copy** sao chép toàn bộ kết quả và **Clear** xóa form/kết quả.
