#!/bin/bash

# Tải biến môi trường từ file .env
export $(grep -v '^#' .env | xargs)

# Khởi tạo cơ sở dữ liệu MySQL
echo "Khởi tạo cơ sở dữ liệu MySQL..."
cd backend
python init_db.py

# Khởi động backend
echo "Khởi động backend Flask..."
cd /workspace/testopenhall/backend
python app.py &
BACKEND_PID=$!

# Đợi backend khởi động
sleep 5

# Khởi động frontend
echo "Khởi động frontend React..."
cd /workspace/testopenhall/frontend
npm start &
FRONTEND_PID=$!

# Xử lý khi nhận tín hiệu thoát
trap "kill $BACKEND_PID $FRONTEND_PID; exit" SIGINT SIGTERM

# Giữ script chạy
wait