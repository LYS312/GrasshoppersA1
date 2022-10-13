from flask import Blueprint, redirect, render_template, request, send_from_directory

index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/home', methods=['GET'])
def index_page():
    return render_template('index.html')

@index_views.route('/<id>', methods=['GET'])
def get_student_reviews():
    return render_template('index.html')


