from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required

from App.controllers import (
    create_review, 
    update_review_exp,
    update_review_rate,
    delete_review,
    get_all_reviews,
    get_all_reviews_JSON
)

review_views = Blueprint('review_views', __name__, template_folder='../templates')


@review_views.route('/reviews', methods=['GET'])
def get_review_page():
    reviews = get_all_reviews()
    return render_template('reviews.html', reviews=reviews)

@review_views.route('/api/reviews', methods=['GET'])
def client_app():
    reviews = get_all_reviews_JSON()
    return jsonify(reviews)

@review_views.route('/static/reviews')
def static_reviews_page():
  return send_from_directory('static', 'static-review.html')


@review_views.route('/review', methods=['POST'])
def new_review():
    data=request.get_json()
    create_review(data["studentID"], data["staffID"], data["experience"], data["rating"])
    return jsonify({"message":"Review Created"})

@review_views.route('/updatereview/experience/<reviewid>', methods=['PUT'])
def update_review_experience(reviewid):
    data=request.get_json()
    review=update_review_exp(reviewid, data["experience"])
    if review:
        return jsonify({"message":"Review Updated"})
    else:
        return jsonify({"message":"Review not found"})

@review_views.route('/updatereview/rating/<reviewid>', methods=['PUT'])
def update_review_rating(reviewid):
    data=request.get_json()
    review=update_review_rate(reviewid, data["rating"])
    if review:
        return jsonify({"message":"Review Updated"})
    else:
        return jsonify({"message":"Review not found"})

@review_views.route('/deletereview/<reviewid>', methods=['DELETE'])
def delete_review_info(reviewid):
    delete = delete_review(reviewid)
    if delete:
        return jsonify({"message":"Review Deleted"})
    else:
        return jsonify({"message":"Review not found"})