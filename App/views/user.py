from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required


from App.controllers import (
    create_user, 
    update_user,
    get_all_users,
    get_all_users_json,
)

user_views = Blueprint('user_views', __name__, template_folder='../templates')


@user_views.route('/users', methods=['GET'])
def get_user_page():
    users = get_all_users()
    return render_template('users.html', users=users)

@user_views.route('/api/users')
def client_app():
    users = get_all_users_json()
    return jsonify(users)

@user_views.route('/static/users')
def static_user_page():
  return send_from_directory('static', 'static-user.html')

@user_views.route('/api/newuser/<username>/<password>/<faculty>/<department>', methods=['GET'])
def new_user(username, password, faculty, department):
    create_user(username, password, faculty, department)
    return jsonify({"message":"User Created"})

@user_views.route('/api/updateuser/<id>/<username>/<faculty>/<department>', methods=['UPDATE'])
def update_user_info(id, username, faculty, department):
    update_user(id, username, faculty, department)
    return jsonify({"message":"User Updated"})