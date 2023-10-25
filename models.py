from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()
class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    create_use = db.Column(db.DateTime, default=datetime.utcnow)
    rut_student = db.Column(db.String(12), unique=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(15), nullable=False)
    birthday = db.Column(db.DateTime)
    address = db.Column(db.String(250), nullable=False)
    email_student = db.Column(db.String(60), unique=True, nullable=False)
    health_system = db.Column(db.String(25), nullable=False)
    observation = db.Column(db.String(250), nullable=True)
    url_img = db.Column(db.String(750), nullable=True)
    roll = db.Column(db.Integer, nullable=False)
    course_name = db.Column(db.String(10), nullable=True)
    # Foreign Key
    status_id = db.Column(db.Integer, db.ForeignKey('status.id'))
    # Relationship
    financial = db.relationship('Apfinancial')
    academic = db.relationship('Apacademic')
    grades = db.relationship('Grade')
    courses = db.relationship('Course', secondary='studentcourse', back_populates='students')
    status = db.relationship('Status', back_populates='students')
    
    def serialize(self):
        return {
            "id": self.id,
            "rut": self.rut_student,
            "name": self.name,
            "last_name": self.last_name,
            "gender": self.gender,
            "birthday": self.birthday,
            "address": self.address,
            "email": self.email_student,
            "health_system": self.health_system,
            "observation": self.observation,
            "img": self.url_img,
            "roll": self.roll,
            "course_name": self.course_name,
        } 
class Apfinancial(db.Model):
    __tablename__ = 'apfinancial'
    id = db.Column(db.Integer, primary_key=True)
    rut_financial = db.Column(db.String(12), unique=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    contact_number = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    # Foreign Key
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    def serialize(self):
        return {
            "id": self.id,
            "rut_financial": self.rut_financial,
            "name": self.name,
            "last_name": self.last_name,
            "contact_number": self.contact_number,
            "address": self.address,
            "email": self.email
        }
class Apacademic(db.Model):
    __tablename__ = 'apacademic'
    id = db.Column(db.Integer, primary_key=True)
    rut_academic = db.Column(db.String(12), unique=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    contact_number = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
     # Foreign Key
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    def serialize(self):
        return {
            "id": self.id,
            "rut_academic": self.rut_academic,
            "name": self.name,
            "last_name": self.last_name,
            "contact_number": self.contact_number,
            "address": self.address,
            "email": self.email
        }
class Administrator(db.Model):
    __tablename__ = 'administrator'
    id = db.Column(db.Integer, primary_key=True)
    rut = db.Column(db.String(12), unique=True, nullable=False)
    password = db.Column(db.String(16), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    roll = db.Column(db.Integer, nullable=False)
    # Foreign Key
    status_id = db.Column(db.Integer, db.ForeignKey('status.id'))
    # Relationship
    status = db.relationship('Status', back_populates='administrator')
    def serialize(self):
        return {
            "id": self.id,
            "rut": self.rut,
            "name": self.name,
            "last_name": self.last_name,
            "email": self.email,
            "roll": self.roll
        }
class Grade(db.Model):
    __tablename__ = 'grade'
    id = db.Column(db.Integer, primary_key=True)
    grade = db.Column(db.String(20), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    # Foreign Key
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))

    def serialize(self):
        return {
            "id": self.id,
            "grade": self.grade,
            "date": self.date
        }
class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(20), nullable=False)
    # Relationship
    students = db.relationship('Student', secondary='studentcourse', back_populates='courses')
    def serialize(self):
        return {
            "id": self.id,
            "course": self.course_name
        }
class Status(db.Model):
    __tablename__ = 'status'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Integer, nullable=False)
    # Relationship
    students = db.relationship('Student', back_populates='status')
    administrator = db.relationship('Administrator', back_populates='status')
    def serialize(self):
        return {
            "id": self.id,
            "status": self.status
        }
class StudentCourse(db.Model):
    __tablename__ = 'studentcourse'
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), primary_key=True)