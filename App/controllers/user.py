from App.models import User
from App.database import db

#def create_user(username, password, faculty, department):
#    newuser = User(username=username, password=password, faculty=faculty, department=department)
#    db.session.add(newuser)
#    db.session.commit()
#    return newuser

def create_user(username, password, faculty, department):
    old_user = User.query.filter_by(username=username).first()
    if not old_user:
        newuser = User(username=username, password=password, faculty=faculty, department=department)
    db.session.add(newuser)
    db.session.commit()
    return newuser

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def get_user(id):
    return User.query.filter_by(id=id).first()

def get_all_users():
    return User.query.all()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.toJSON() for user in users]
    return users

def update_user(id, username, faculty, department):
    user = get_user(id)
    if user:
        user.username = username
        user.faculty=faculty
        user.department=department
        db.session.add(user)
        db.session.commit()

def delete_user(id):
    user= User.query.get(id)
    db.session.delete(user)
    db.session.commit()
