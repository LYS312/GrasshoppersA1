from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required


from App.controllers import (
    create_review, 
    update_review,
    delete_review,
    get_all_reviews,
    get_all_reviews_JSON
    upvote,
    downvote,
    remove_downvote,
    remove_upvote
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

@review_views.route('/api/newreview/<studentid>/<staffid>/<experience>/<rating>', methods=['GET'])
def new_review(studentid, staffid, experience, rating):
    create_review(studentid, staffid, experience, rating)
    return jsonify({"message":"Review Created"})

@review_views.route('/api/updatereview/<reviewid>/<experience>/<rating>', methods=['UPDATE'])
def update_review_info(reviewid, experience, rating):
    update_review(reviewid, experience, rating)
    return jsonify({"message":"Review Updated"})

@review_views.route('/api/deletereview/<reviewid>', methods=['GET'])
def delete_review_info(reviewid):
    delete = delete_review(reviewid)
    if delete:
        return jsonify({"message":"Review Deleted"})
    else:
        return jsonify({"message":"Review not found"})

@review_views.route('/api/upvotereview/<reviewid>', methods=['UPDATE'])
def upvote_review(reviewid):
    upvote(reviewid)
    return jsonify({"message":"Review Upvoted"})

@review_views.route('/api/downvotereview/<reviewid>', methods=['UPDATE'])
def downvote_review(reviewid):
    downvote(reviewid)
    return jsonify({"message":"Review Downvoted"})

@review_views.route('/api/removeupvote/<reviewid>', methods=['UPDATE'])
def remove_upvote_view(reviewid):
    remove_upvote(reviewid)
    return jsonify({"message":"Upvote Removed"})

@review_views.route('/api/removedownvote/<reviewid>', methods=['UPDATE'])
def remove_downvote_view(reviewid):
    remove_downvote(reviewid)
    return jsonify({"message":"Downvote Removed"})
