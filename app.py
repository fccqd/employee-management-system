# app.py
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from models import db, Employee
from flask_cors import CORS

# 在创建 Flask 应用实例后添加
app = Flask(__name__)
CORS(app)

# 允许所有域（不推荐在生产环境中使用）
app.config['CORS_HEADERS'] = 'Content-Type'

# 或者只允许特定的域
app.config['CORS_ORIGINS'] = ['http://localhost:8083']

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:wyhnb@localhost/employee_management'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/employees', methods=['GET', 'POST'])
def manage_employees():
    if request.method == 'POST':
        data = request.get_json()
        new_employee = Employee(**data)
        db.session.add(new_employee)
        db.session.commit()
        return jsonify(new_employee.to_dict()), 201
    else:
        employees = Employee.query.all()
        return jsonify([emp.to_dict() for emp in employees])

@app.route('/employees/<int:employee_id>', methods=['GET', 'PUT', 'DELETE'])
def employee(employee_id):
    employee = Employee.query.get_or_404(employee_id)
    if request.method == 'PUT':
        data = request.get_json()
        employee.name = data.get('name', employee.name)
        employee.age = data.get('age', employee.age)
        employee.gender = data.get('gender', employee.gender)
        employee.position = data.get('position', employee.position)
        db.session.commit()
        return jsonify(employee.to_dict())
    elif request.method == 'DELETE':
        db.session.delete(employee)
        db.session.commit()
        return '', 204

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=5000, debug=True)