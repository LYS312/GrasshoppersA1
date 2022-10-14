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
    newuser=create_user(data["username"], data["password"], data["faculty"], data["department"])
    if newuser:
        return jsonify({"message":"User Created"})
    else:
        return jsonify({"message":"User " + data["username"] + " already exists"})

@user_views.route('/updateuser/<id>', methods=['PUT'])
@jwt_required()
def update_user_info(id):
    data=request.get_json()
    user=update_user(id, data["faculty"], data["department"])
    if user:
        return jsonify({"message":"User Updated"})
    else:
        return jsonify({"message":"User not found"})

@user_views.route('/deleteuser/<id>')
@jwt_required()
def delete_user_info(id):
    user=delete_user(id)
    if user:
        return jsonify({"message":"User Deleted"})
    else:
        return jsonify({"message":"User not found"})