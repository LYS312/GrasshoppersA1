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

@student_views.route('/api/students', methods=['GET'])
def client_app():
    students = get_all_students_JSON()
    return jsonify(students)

@student_views.route('/static/students')
def static_student_page():
  return send_from_directory('static', 'static-student.html')


@student_views.route('/student', methods=['POST'])
def new_student():
    data=request.get_json()
    student=create_student(data["studentID"], data["name"])
    if student:
        return jsonify({"message":"Student Created"})
    else:
        return jsonify({"message":"This student id is already in use"})

@student_views.route('/updatestudent/<studentid>', methods=['PUT'])
def update_student_info(studentid):
    data=request.get_json()
    student=update_student(studentid, data["name"])
    if student:
        return jsonify({"message":"Student updated"})
    else:
        return jsonify({"message":"Student not found"})

@student_views.route('/deletestudent/<studentid>', methods=['DELETE'])
def delete_student_info(studentid):
    student=delete_student(studentid)
    if student:
        return jsonify({"message":"Student deleted"})
    else:
        return jsonify({"message":"Student not found"})

@student_views.route('/student/<studentid>')
def get_student_info(studentid):
    student = get_student(studentid)
    if student:
        student = student.toJSON()
        return student
    else:
        return jsonify({"message":"Student not found"})