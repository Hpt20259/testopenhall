# Hệ thống giải phương trình bậc 2

Hệ thống web cho phép nhập hệ số a, b, c để giải phương trình bậc 2 và lưu kết quả vào MySQL. Hệ thống hỗ trợ đầy đủ các chức năng xem, sửa, xóa phương trình đã lưu.

## Công nghệ sử dụng

### Frontend
- React
- TypeScript
- Material-UI
- Axios

### Backend
- Python
- Flask
- Flask-SQLAlchemy
- Flask-CORS

### Database
- MySQL/MariaDB

## Cài đặt và chạy

### Yêu cầu
- Node.js (v14+)
- Python (v3.8+)
- MySQL/MariaDB

### Các bước cài đặt

1. Clone repository
```bash
git clone https://github.com/Hpt20259/testopenhall.git
cd testopenhall
```

2. Cài đặt dependencies cho backend
```bash
cd backend
pip install flask flask-cors flask-sqlalchemy pymysql python-dotenv
cd ..
```

3. Cài đặt dependencies cho frontend
```bash
cd frontend
npm install
cd ..
```

4. Cấu hình môi trường
- Tạo file `.env` trong thư mục gốc với nội dung:
```
# Cấu hình MySQL
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=password
MYSQL_DB=quadratic_equation_db
MYSQL_PORT=3306

# Cấu hình Flask
FLASK_APP=app.py
FLASK_ENV=development
FLASK_DEBUG=1
FLASK_PORT=12000

# Cấu hình Frontend
REACT_APP_API_URL=http://localhost:12000
FRONTEND_PORT=12001
```

5. Khởi động hệ thống
```bash
chmod +x start.sh
./start.sh
```

## Sử dụng
- Frontend: http://localhost:12001
- Backend API: http://localhost:12000

## Chức năng
- Nhập hệ số a, b, c và giải phương trình bậc 2
- Lưu kết quả vào cơ sở dữ liệu MySQL
- Xem danh sách các phương trình đã lưu
- Sửa hệ số của phương trình đã lưu
- Xóa phương trình đã lưu

## API Endpoints
- `GET /api/equations`: Lấy danh sách phương trình
- `GET /api/equations/:id`: Lấy thông tin một phương trình
- `POST /api/equations`: Thêm phương trình mới
- `PUT /api/equations/:id`: Cập nhật phương trình
- `DELETE /api/equations/:id`: Xóa phương trình
