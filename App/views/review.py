from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required


from App.controllers import (
    create_review, 
    get_all_reviews,
    get_all_reviews_JSON
)

review_views = Blueprint('review_views', __name__, template_folder='../templates')


@review_views.route('/reviews', methods=['GET'])
def get_review_page():
    reviews = get_all_reviews()
    return render_template('reviews.html', reviews=reviews)

@review_views.route('/api/reviews')
def client_app():
    reviews = get_all_reviews_JSON()
    return jsonify(reviews)

@review_views.route('/static/reviews')
def static_reviews_page():
  return send_from_directory('static', 'static-review.html')