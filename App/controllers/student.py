from App.models import Student
from App.database import db

def create_student(name):
    newStudent= Student(student=student)
    db.session.add(student)
    db.session.commit()

def delete_student(studentID):
    student=Student.query.get(studentID)
    db.session.delete(student)
    db.session.commit()

def update_student(studentID, name):
    student=Student.query.get(studentID)
    student.name=name
    db.session.add(student)
    db.session.commit()

def get_student(studentID):
    return Student.query.get(studentID)

def get_all_students():
    return Student.query.all()

def get_all_students_JSON():
    students=get_all_students()
    if not students:
        return []
    students = [student.toJSON() for student in students]
    return students






