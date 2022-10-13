from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required


from App.controllers import (
    create_user, 
    update_user,
    delete_user,
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

@user_views.route('/user', methods=['POST'])
def new_user():
    data=request.get_json()
    create_user(data["username"], data["password"], data["faculty"], data["department"])
    return jsonify({"message":"User Created"})

@user_views.route('/api/updateuser/<id>/<username>/<faculty>/<department>', methods=['UPDATE'])
def update_user_info(id, username, faculty, department):
    update_user(id, username, faculty, department)
    return jsonify({"message":"User Updated"})

@user_views.route('/api/deleteuser/<userid>')
def delete_user_info(userid):
    delete_user(userid)
    return jsonify({"message":"User Deleted"})