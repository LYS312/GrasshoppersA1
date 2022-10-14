from App.models import Student
from App.database import db
import json

def create_student(studentID, name):
    student=Student.query.filter_by(studentID=studentID).first()
    if student:
        return None
    
    # if student has not already been added
    newStudent= Student(studentID, name=name)
    db.session.add(newStudent)
    db.session.commit()
    return newStudent

def delete_student(studentID):
    student=Student.query.get(studentID)
    if student:
        db.session.delete(student)
        db.session.commit()
    return student

def update_student(studentID, name):
    student=Student.query.filter_by(studentID=studentID).first()
    if student:
        student.name=name
        db.session.add(student)
        db.session.commit()
    return student

def get_student(studentID):
    return Student.query.filter_by(studentID=studentID).first()

def get_all_students():
    return Student.query.all()

def get_all_students_JSON():
    students=get_all_students()
    if not students:
        return []
    else:
        students = [student.toJSON() for student in students]
        return students






