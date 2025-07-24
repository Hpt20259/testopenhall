from flask import Flask, request, jsonify
from flask_cors import CORS
import math
import sqlite3
import os
from dotenv import load_dotenv

# Tải biến môi trường từ file .env
load_dotenv()

app = Flask(__name__)
CORS(app)

# Kết nối đến SQLite
def get_db_connection():
    conn = sqlite3.connect('equations.db')
    conn.row_factory = sqlite3.Row
    return conn

# Khởi tạo cơ sở dữ liệu
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS equations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        a REAL NOT NULL,
        b REAL NOT NULL,
        c REAL NOT NULL,
        discriminant REAL NOT NULL,
        x1 TEXT,
        x2 TEXT,
        solution_type TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

# Hàm giải phương trình bậc 2
def solve_quadratic_equation(a, b, c):
    if a == 0:
        return {
            "error": "Không phải phương trình bậc 2 (a = 0)"
        }
    
    # Tính delta
    discriminant = b**2 - 4*a*c
    
    # Xác định loại nghiệm
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        solution_type = "Phương trình có hai nghiệm phân biệt"
        return {
            "discriminant": discriminant,
            "x1": x1,
            "x2": x2,
            "solution_type": solution_type
        }
    elif discriminant == 0:
        x = -b / (2*a)
        solution_type = "Phương trình có nghiệm kép"
        return {
            "discriminant": discriminant,
            "x1": x,
            "x2": x,
            "solution_type": solution_type
        }
    else:
        real_part = -b / (2*a)
        imag_part = math.sqrt(abs(discriminant)) / (2*a)
        solution_type = "Phương trình có hai nghiệm phức"
        x1 = f"{real_part} + {imag_part}i"
        x2 = f"{real_part} - {imag_part}i"
        return {
            "discriminant": discriminant,
            "x1": x1,
            "x2": x2,
            "solution_type": solution_type
        }

# API endpoint để lấy tất cả phương trình
@app.route('/api/equations', methods=['GET'])
def get_equations():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM equations')
    equations = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return jsonify(equations)

# API endpoint để lấy một phương trình cụ thể
@app.route('/api/equations/<int:id>', methods=['GET'])
def get_equation(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM equations WHERE id = ?', (id,))
    equation = cursor.fetchone()
    conn.close()
    
    if equation is None:
        return jsonify({"error": "Phương trình không tồn tại"}), 404
    
    return jsonify(dict(equation))

# API endpoint để thêm phương trình mới
@app.route('/api/equations', methods=['POST'])
def add_equation():
    data = request.get_json()
    
    if not data or 'a' not in data or 'b' not in data or 'c' not in data:
        return jsonify({"error": "Dữ liệu không hợp lệ"}), 400
    
    a = float(data['a'])
    b = float(data['b'])
    c = float(data['c'])
    
    # Giải phương trình
    result = solve_quadratic_equation(a, b, c)
    
    if "error" in result:
        return jsonify(result), 400
    
    # Lưu vào cơ sở dữ liệu
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO equations (a, b, c, discriminant, x1, x2, solution_type) VALUES (?, ?, ?, ?, ?, ?, ?)',
        (a, b, c, result['discriminant'], str(result['x1']), str(result['x2']), result['solution_type'])
    )
    conn.commit()
    
    # Lấy ID của phương trình vừa thêm
    equation_id = cursor.lastrowid
    conn.close()
    
    # Trả về phương trình đã thêm
    return jsonify({
        "id": equation_id,
        "a": a,
        "b": b,
        "c": c,
        "discriminant": result['discriminant'],
        "x1": result['x1'],
        "x2": result['x2'],
        "solution_type": result['solution_type']
    })

# API endpoint để cập nhật phương trình
@app.route('/api/equations/<int:id>', methods=['PUT'])
def update_equation(id):
    data = request.get_json()
    
    if not data or 'a' not in data or 'b' not in data or 'c' not in data:
        return jsonify({"error": "Dữ liệu không hợp lệ"}), 400
    
    a = float(data['a'])
    b = float(data['b'])
    c = float(data['c'])
    
    # Giải phương trình
    result = solve_quadratic_equation(a, b, c)
    
    if "error" in result:
        return jsonify(result), 400
    
    # Cập nhật vào cơ sở dữ liệu
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'UPDATE equations SET a = ?, b = ?, c = ?, discriminant = ?, x1 = ?, x2 = ?, solution_type = ? WHERE id = ?',
        (a, b, c, result['discriminant'], str(result['x1']), str(result['x2']), result['solution_type'], id)
    )
    conn.commit()
    
    # Kiểm tra xem phương trình có tồn tại không
    if cursor.rowcount == 0:
        conn.close()
        return jsonify({"error": "Phương trình không tồn tại"}), 404
    
    conn.close()
    
    # Trả về phương trình đã cập nhật
    return jsonify({
        "id": id,
        "a": a,
        "b": b,
        "c": c,
        "discriminant": result['discriminant'],
        "x1": result['x1'],
        "x2": result['x2'],
        "solution_type": result['solution_type']
    })

# API endpoint để xóa phương trình
@app.route('/api/equations/<int:id>', methods=['DELETE'])
def delete_equation(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM equations WHERE id = ?', (id,))
    conn.commit()
    
    # Kiểm tra xem phương trình có tồn tại không
    if cursor.rowcount == 0:
        conn.close()
        return jsonify({"error": "Phương trình không tồn tại"}), 404
    
    conn.close()
    
    return jsonify({"message": "Phương trình đã được xóa"})

if __name__ == '__main__':
    # Khởi tạo cơ sở dữ liệu
    init_db()
    
    # Lấy cổng từ biến môi trường hoặc sử dụng cổng mặc định
    port = int(os.environ.get('FLASK_PORT', 12000))
    
    # Chạy ứng dụng
    app.run(host='0.0.0.0', port=port, debug=True)
