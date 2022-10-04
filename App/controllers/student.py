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


