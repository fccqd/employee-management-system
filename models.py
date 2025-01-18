# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Employee(db.Model):
    __tablename__ = 'employees'
    employee_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.department_id'), nullable=False)
    position = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            'employee_id': self.employee_id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'department_id': self.department_id,
            'position': self.position
        }

class Department(db.Model):
    __tablename__ = 'departments'
    department_id = db.Column(db.Integer, primary_key=True)
    department_name = db.Column(db.String(50), nullable=False)