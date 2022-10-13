from App.models import Review
from App.database import db

def create_review (studentID, staffID, experience, rating):
    newReview= Review(studentID=studentID, staffID=staffID, experience=experience, rating=rating)
    db.session.add(newReview)
    db.session.commit()

def delete_review(reviewID):
    review= Review.query.filter_by(reviewID=reviewID).first()
    if review:
        db.session.delete(review)
        db.session.commit()
    return review

def get_review(reviewID):
    return Review.query.get(reviewID)

def get_all_reviews():
    return Review.query.all()

def get_all_reviews_JSON():
    reviews = Review.query.all()
    if not reviews:
        return []
    reviews = [review.toJSON() for review in reviews]
    return reviews 

def get_reviews_by_student_JSON(studentID):
    reviews = Review.query.filter(studentID=studentID)
    if not reviews:
        return []
    reviews = [review.toJSON() for review in reviews]
    return reviews 

def get_reviews_by_staff_JSON(staffID):
    reviews = Review.query.filter(staffID=staffID)
    if not reviews:
        return []
    reviews = [review.toJSON() for review in reviews]
    return reviews 

def update_review_exp(reviewID, experience):
    review= get_review(reviewID)
    if review:
        review.experience=experience
        db.session.add(review)
        db.session.commit()
    return review

def update_review_rate(reviewID, rating):
    review= get_review(reviewID)
    if review:
        review.rating=rating
        db.session.add(review)
        db.session.commit()
    return review

def upvote(reviewID):
    review=get_review(reviewID)
    review.upvotes= review.upvotes+1
    db.session.add(review)
    db.session.commit()

def remove_upvote(reviewID):
    review=get_review(reviewID)
    review.upvotes= review.upvotes-1
    db.session.add(review)
    db.session.commit()

def downvote(reviewID):
    review=get_review(reviewID)
    review.downvotes= review.downvotes +1
    db.session.add(review)
    db.session.commit()

def remove_downvote(reviewID):
    review=get_review(reviewID)
    review.downvotes= review.downvotes -1
    db.session.add(review)
    db.session.commit()



