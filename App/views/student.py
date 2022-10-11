from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required


from App.controllers import (
    create_student, 
    get_all_students,
    get_all_students_JSON
)

student_views = Blueprint('student_views', __name__, template_folder='../templates')


@user_views.route('/students', methods=['GET'])
def get_student_page():
    students = get_all_students()
    return render_template('users.html', students=students)

@user_views.route('/api/students')
def client_app():
    students = get_all_students_json()
    return jsonify(students)

@user_views.route('/static/students')
def static_student_page():
  return send_from_directory('static', 'static-student.html')