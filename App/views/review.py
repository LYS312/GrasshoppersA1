from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required

from App.controllers import (
    create_review, 
    update_review_exp,
    update_review_rate,
    delete_review,
    get_all_reviews,
    get_all_reviews_JSON,
    upvote,
    remove_upvote,
    downvote,
    remove_downvote,
    get_student
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
@jwt_required()
def new_review():
    data=request.get_json()
    student=get_student(data["studentID"])
    if student:
        create_review(data["studentID"], data["staffID"], data["experience"], data["rating"])
        return jsonify({"message":"Review Created"})
    else:
        return jsonify({"message":"Student not found"})

@review_views.route('/updatereview/experience/<reviewid>', methods=['PUT'])
@jwt_required()
def update_review_experience(reviewid):
    data=request.get_json()
    review=update_review_exp(reviewid, data["experience"])
    if review:
        return jsonify({"message":"Review Updated"})
    else:
        return jsonify({"message":"Review not found"})

@review_views.route('/updatereview/rating/<reviewid>', methods=['PUT'])
@jwt_required()
def update_review_rating(reviewid):
    data=request.get_json()
    review=update_review_rate(reviewid, data["rating"])
    if review:
        return jsonify({"message":"Review Updated"})
    else:
        return jsonify({"message":"Review not found"})

@review_views.route('/deletereview/<reviewid>', methods=['DELETE'])
@jwt_required()
def delete_review_info(reviewid):
    delete = delete_review(reviewid)
    if delete:
        return jsonify({"message":"Review Deleted"})
    else:
        return jsonify({"message":"Review not found"})

@review_views.route('/upvote/<reviewid>', methods=['PUT'])
@jwt_required()
def upvote_review(reviewid):
    review=upvote(reviewid)
    if review:
        return jsonify({"message":"Review Upvoted"})
    else:
        return jsonify({"message":"Review not found"})

@review_views.route('/downvote/<reviewid>', methods=['PUT'])
@jwt_required()
def downvote_review(reviewid):
    review=downvote(reviewid)
    if review:
        return jsonify({"message":"Review Downvoted"})
    else:
        return jsonify({"message":"Review not found"})

@review_views.route('/removeupvote/<reviewid>', methods=['PUT'])
@jwt_required()
def remove_upvote_view(reviewid):
    review=remove_upvote(reviewid)
    if review:
        return jsonify({"message":"Upvote Removed"})
    else:
        return jsonify({"message":"Review not found"})

@review_views.route('/removedownvote/<reviewid>', methods=['PUT'])
@jwt_required()
def remove_downvote_view(reviewid):
    review=remove_downvote(reviewid)
    if review:
        return jsonify({"message":"Downvote Removed"})
    else:
        return jsonify({"message":"Review not found"})