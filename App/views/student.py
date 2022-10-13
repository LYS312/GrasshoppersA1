from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required

from App.controllers import (
    create_student, 
    update_student,
    delete_student,
    get_student,
    get_all_students,
    get_all_students_JSON
)

student_views = Blueprint('student_views', __name__, template_folder='../templates')


@student_views.route('/students', methods=['GET'])
def get_student_page():
    students = get_all_students()
    return render_template('users.html', students=students)

@student_views.route('/api/students')
def client_app():
    students = get_all_students_JSON()
    return jsonify(students)

@student_views.route('/static/students')
def static_student_page():
  return send_from_directory('static', 'static-student.html')

@student_views.route('/api/newstudent/<studentID>/<name>', methods=['GET'])
def new_student(studentID, name):
    create_student(studentID, name)
    return jsonify({"message":"Student Created"})

@student_views.route('/api/updatestudent/<studentid>/<name>', methods=['UPDATE'])
def update_student_info(studentid, name):
    update_student(studentid)
    return jsonify({"message":"Student Deleted"})

@student_views.route('/api/deletestudent/<studentid>', methods=['GET'])
def delete_student_info(studentid):
    delete_student(studentid)
    return jsonify({"message":"Student deleted"})

@student_views.route('/api/<studentid>')
def get_student_info(studentid):
    student = get_student(studentid)
    student = student.toJSON()
    return student