#!/bin/bash

# Khởi động backend
echo "Khởi động backend..."
cd /workspace/testopenhall
python backend/app_sqlite.py > backend.log 2>&1 &
BACKEND_PID=$!

# Đợi backend khởi động
sleep 5

# Khởi động frontend
echo "Khởi động frontend..."
cd /workspace/testopenhall/frontend
npm start > frontend.log 2>&1 &
FRONTEND_PID=$!

echo "Ứng dụng đã khởi động!"
echo "Backend PID: $BACKEND_PID"
echo "Frontend PID: $FRONTEND_PID"
echo "Backend URL: http://localhost:12000"
echo "Frontend URL: http://localhost:12001"

# Đợi người dùng nhấn Ctrl+C
echo "Nhấn Ctrl+C để dừng ứng dụng..."
wait
