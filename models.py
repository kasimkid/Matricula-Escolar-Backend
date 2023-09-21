from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Date, ForeignKey

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
    id_financial = db.relationship('Ap_Financial', uselist=False)
    id_academic = db.relationship('Ap_Academic')

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
            "observation": self.observation
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
    id_student = db.Column(db.Integer, db.ForeignKey('student.id'))

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
    __tablename__ = 'ap_academico'
    id = db.Column(db.Integer, primary_key=True)
    rut = db.Column(db.Integer, unique=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    contact_number = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    id_student = db.Column(db.Integer, db.ForeignKey('student.id'))

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
