from sqlalchemy import Column, Integer, String, Date, ForeignKey
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    rut = db.Column(db.Integer, unique=True, nullable=False)
    password = db.Column(db.String(16))
    name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(15), nullable=False)
    birthday = db.Column(db.Date, nullable=False)
    address = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    health_system = db.Column(db.String(25), nullable=False)
    observation = db.Column(db.String(250), nullable=True)
    ap_financial_id = db.Column(db.Integer, db.ForeignKey('ap_financial.id'), unique=True, nullable=True)
    ap_financial = db.relationship('Ap_Financial', back_populates='student')
    ap_academic_id = db.Column(db.Integer, db.ForeignKey('ap_academic.id', unique=True, nullable=True))
    ap_academic = db.relationship('Ap_Academic', back_populates='student')
    roll_id = db.Column(db.Integer, db.ForeignKey(roll.id), unique=True, nullable=True)
    roll = db.relationship('Roll', back_populates='student')

    def serialize(self):
        return {
            "id": self.id,
            "rut": self.rut,
            "name": self.name,
            "last_name": self.last_name,
            "gender": self.gender,
            "birthdaadrress": self.birthdaadrress,
            "adrress": self.adrress,
            "email": self.email,
            "health_system": self.health_system,
            "observation": self.observation,
            "ap_financial": self.ap_financial.serialize() if self.ap_financial else None,
            "ap_academic": self.ap_academic.serialize() if self.ap_academic else None,
            "roll": self.roll.serialize() if self.roll else None
        }

class Ap_Financial(db.Model):
    __tablename__ = 'ap_financial'
    id = db.Column(db.Integer, primary_key=True)
    rut = db.Column(db.Integer, unique=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    contact_number = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    students = db.relationship('Student', back_populates='ap_financial')

    def serialize(self):
        return {
            "id": self.id,
            "runame": self.runame,
            "name": self.name,
            "last_name": self.last_name,
            "contact_number": self.contact_number,
            "address": self.address,
            "email": self.email
        }

class Ap_Academic(db.Model):
    __tablename__ = 'ap_academic'
    id = db.Column(db.Integer, primary_key=True)
    rut = db.Column(db.Integer, unique=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    contact_number = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    student = db.relationship('Student', back_populates='ap_academic')

    def serialize(self):
        return {
            "id": self.id,
            "runame": self.runame,
            "name": self.name,
            "last_name": self.last_name,
            "contact_number": self.contact_number,
            "address": self.address,
            "email": self.email
        }

class Administrator(db.Model):
    __tablename__ = 'administrator'
    id = db.Column(db.Integer, primary_key=True)
    rut = db.Column(db.Integer, unique=True, nullable=False)
    password = db.Column(db.String(16), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "rut": self.rut,
            "password": self.password,
            "name": self.name,
            "last_name": self.last_name,
            "email": self.email
        }

class Grade(db.Model):
    __tablename__ = 'grade'
    id = db.Column(db.Integer, primary_key=True)
    grade = db.Column(db.String(20), nullable=False)
    date = db.Column(db.Date, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "grade": self.grade,
            "date": self.date
        }

class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True)
    course = db.Column(db.String, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "course": self.course
        }
    
class Status(db.Model):
    __tablename__= 'status'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Integer, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "status": self.status
        }
    
class Roll(db.Model):
    __tablename__= 'roll'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Integer, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "roll": self.roll
        }
