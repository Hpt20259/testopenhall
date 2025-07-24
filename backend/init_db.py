import pymysql
import os
from dotenv import load_dotenv

# Tải biến môi trường từ file .env
load_dotenv()

# Lấy thông tin kết nối từ biến môi trường
host = os.getenv('MYSQL_HOST', 'localhost')
user = os.getenv('MYSQL_USER', 'root')
password = os.getenv('MYSQL_PASSWORD', 'password')
db_name = os.getenv('MYSQL_DB', 'quadratic_equation_db')

# Kết nối đến MySQL server (không chỉ định database)
connection = pymysql.connect(
    host=host,
    user=user,
    password=password,
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with connection.cursor() as cursor:
        # Tạo database nếu chưa tồn tại
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        print(f"Database '{db_name}' đã được tạo hoặc đã tồn tại.")
        
        # Sử dụng database
        cursor.execute(f"USE {db_name}")
        
        # Tạo bảng quadratic_equation nếu chưa tồn tại
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS quadratic_equation (
            id INT AUTO_INCREMENT PRIMARY KEY,
            a FLOAT NOT NULL,
            b FLOAT NOT NULL,
            c FLOAT NOT NULL,
            result VARCHAR(255) NOT NULL
        )
        """)
        print("Bảng 'quadratic_equation' đã được tạo hoặc đã tồn tại.")
    
    # Commit các thay đổi
    connection.commit()
    print("Khởi tạo cơ sở dữ liệu thành công!")

except Exception as e:
    print(f"Lỗi: {e}")

finally:
    connection.close()