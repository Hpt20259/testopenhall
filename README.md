# Hệ thống giải phương trình bậc 2

Hệ thống web cho phép nhập a, b, c để giải phương trình bậc 2, lưu kết quả vào cơ sở dữ liệu và cho phép xem/sửa/xoá phương trình đã lưu.

## Công nghệ sử dụng

- **Frontend**: React, TypeScript, Material-UI
- **Backend**: Python, Flask
- **Cơ sở dữ liệu**: SQLite

## Cài đặt

### Yêu cầu

- Node.js (v14 trở lên)
- Python (v3.6 trở lên)
- pip (trình quản lý gói Python)
- npm (trình quản lý gói Node.js)

### Cài đặt thủ công

1. **Clone repository**

```bash
git clone https://github.com/Hpt20259/testopenhall.git
cd testopenhall
```

2. **Cài đặt backend**

```bash
pip install flask flask-cors python-dotenv
```

3. **Cài đặt frontend**

```bash
cd frontend
npm install
cd ..
```

## Chạy ứng dụng

Bạn có thể chạy ứng dụng bằng script tự động:

```bash
./start.sh
```

Hoặc chạy thủ công:

1. **Khởi động backend**

```bash
cd /path/to/testopenhall
python backend/app_sqlite.py
```

2. **Khởi động frontend (trong terminal khác)**

```bash
cd /path/to/testopenhall/frontend
npm start
```

## Sử dụng

- Frontend: http://localhost:12001
- Backend API: http://localhost:12000

### API Endpoints

- `GET /api/equations`: Lấy tất cả phương trình
- `GET /api/equations/:id`: Lấy phương trình theo ID
- `POST /api/equations`: Thêm phương trình mới
- `PUT /api/equations/:id`: Cập nhật phương trình
- `DELETE /api/equations/:id`: Xóa phương trình

## Cấu trúc dự án

```
testopenhall/
├── backend/
│   ├── app.py             # Flask API
│   └── app_sqlite.py      # Flask API với SQLite
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   ├── EquationForm.tsx
│   │   │   └── EquationList.tsx
│   │   ├── App.tsx
│   │   ├── index.tsx
│   │   └── ...
│   ├── package.json
│   └── ...
├── .env                   # Biến môi trường
├── equations.db           # Cơ sở dữ liệu SQLite
├── start.sh               # Script khởi động
└── README.md
```

## Chức năng

1. **Nhập phương trình**
   - Nhập hệ số a, b, c
   - Tính toán và hiển thị kết quả
   - Lưu vào cơ sở dữ liệu

2. **Quản lý phương trình**
   - Xem danh sách phương trình đã lưu
   - Sửa phương trình
   - Xóa phương trình

## Giao diện

Giao diện được thiết kế với Material-UI, bao gồm:
- Form nhập hệ số a, b, c
- Nút tính toán và nút thêm bố trí cạnh nhau
- Bảng hiển thị danh sách phương trình với các nút sửa, xóa
