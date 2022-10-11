import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.database import create_db, get_migrate
from App.main import create_app
from App.controllers import ( 
    create_user, 
    get_all_users_json, 
    get_all_users, 
    update_user,
    create_student, 
    get_all_students,
    get_all_students_JSON,
    create_review, 
    get_all_reviews,
    get_all_reviews_JSON,
    )

# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def initialize():
    create_db(app)
    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>


user_cli = AppGroup('user', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
@click.argument("faculty", default="FST")
@click.argument("department", default="DCIT")
def create_user_command(username, password, faculty, department):
    create_user(username, password, faculty, department)
    print(f'{username} created!')

# this command will be : flask user create rob robpass FST DCIT


student_cli = AppGroup('student', help="Student object commands")

@student_cli.command("create", help="Create a student")
@click.argument("name", default="tom")
def create_student_command(name):
    create_student(name)
    print(f'{name} created!')



review_cli = AppGroup('review', help="Review object commands")

@review_cli.command("create", help="Create a review")
@click.argument("studentid", default="1")
@click.argument("staffid", default="1")
@click.argument("experience", default="100")
@click.argument("rating", default="5")
def create_review_command(studentid, staffid, experience, rating):
    create_review(studentid, staffid, experience, rating)
    print(f'review created!')



@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

@user_cli.command("update", help="Updates info on staff member")
@click.argument("id", default="1")
@click.argument("username", default="rob")
@click.argument("faculty", default="FSS")
@click.argument("department", default="DPS")
def update_user_command(id, username, faculty, department):
    update_user(id, username, faculty, department)
    print(f'{username} updated!')

app.cli.add_command(user_cli) # add the group to the cli
app.cli.add_command(student_cli)
app.cli.add_command(review_cli)





'''
Generic Commands
'''

@app.cli.command("init")
def initialize():
    create_db(app)
    print('database intialized')

'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)