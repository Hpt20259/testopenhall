from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
import math

# Tải biến môi trường từ file .env
load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Cấu hình kết nối MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@{os.getenv('MYSQL_HOST')}:{os.getenv('MYSQL_PORT')}/{os.getenv('MYSQL_DB')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Định nghĩa model cho phương trình bậc 2
class QuadraticEquation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    a = db.Column(db.Float, nullable=False)
    b = db.Column(db.Float, nullable=False)
    c = db.Column(db.Float, nullable=False)
    result = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'a': self.a,
            'b': self.b,
            'c': self.c,
            'result': self.result
        }

# Hàm giải phương trình bậc 2
def solve_quadratic_equation(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return "Phương trình có vô số nghiệm"
            else:
                return "Phương trình vô nghiệm"
        else:
            x = -c / b
            return f"Phương trình có một nghiệm: x = {x}"
    else:
        delta = b**2 - 4*a*c
        if delta < 0:
            return "Phương trình vô nghiệm"
        elif delta == 0:
            x = -b / (2*a)
            return f"Phương trình có nghiệm kép: x = {x}"
        else:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            return f"Phương trình có hai nghiệm phân biệt: x1 = {x1}, x2 = {x2}"

# API endpoint để giải phương trình và lưu vào database
@app.route('/api/equations', methods=['POST'])
def add_equation():
    data = request.json
    a = float(data.get('a', 0))
    b = float(data.get('b', 0))
    c = float(data.get('c', 0))
    
    result = solve_quadratic_equation(a, b, c)
    
    equation = QuadraticEquation(a=a, b=b, c=c, result=result)
    db.session.add(equation)
    db.session.commit()
    
    return jsonify(equation.to_dict()), 201

# API endpoint để lấy tất cả phương trình
@app.route('/api/equations', methods=['GET'])
def get_equations():
    equations = QuadraticEquation.query.all()
    return jsonify([equation.to_dict() for equation in equations])

# API endpoint để lấy một phương trình cụ thể
@app.route('/api/equations/<int:id>', methods=['GET'])
def get_equation(id):
    equation = QuadraticEquation.query.get_or_404(id)
    return jsonify(equation.to_dict())

# API endpoint để cập nhật phương trình
@app.route('/api/equations/<int:id>', methods=['PUT'])
def update_equation(id):
    equation = QuadraticEquation.query.get_or_404(id)
    data = request.json
    
    a = float(data.get('a', equation.a))
    b = float(data.get('b', equation.b))
    c = float(data.get('c', equation.c))
    
    result = solve_quadratic_equation(a, b, c)
    
    equation.a = a
    equation.b = b
    equation.c = c
    equation.result = result
    
    db.session.commit()
    
    return jsonify(equation.to_dict())

# API endpoint để xóa phương trình
@app.route('/api/equations/<int:id>', methods=['DELETE'])
def delete_equation(id):
    equation = QuadraticEquation.query.get_or_404(id)
    db.session.delete(equation)
    db.session.commit()
    return jsonify({'message': 'Phương trình đã được xóa thành công'})

# Tạo bảng trong database nếu chưa tồn tại
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    port = int(os.getenv('FLASK_PORT', 12000))
    app.run(host='0.0.0.0', port=port, debug=True)