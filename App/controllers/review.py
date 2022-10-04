from App.models import Review
from App.database import db

def create_review (studentID, staffID, experience, rating):
    newReview= Review(studentID=studentID, staffID=staffID, experience=experience, rating=rating)
    db.session.add(newReview)
    db.session.commit()

def delete_review(reviewID):
    review= Review.query.get(reviewID)
    db.session.delete(review)
    db.session.commit()

def get_all_reviews():
    return Review.query.all()

def get_all_reviews_JSON():
    reviews = Review.query.all()
    if not reviews:
        return []
    reviews = [review.toDict() for review in reviews]
    return reviews 

def get_reviews_by_student_JSON(studentID):
    reviews = Review.query.filter(studentID=studentID)
    if not reviews:
        return []
    reviews = [review.toDict() for review in reviews]
    return reviews 

def get_reviews_by_staff_JSON(staffID):
    reviews = Review.query.filter(studentID=studentID)
    if not reviews:
        return []
    reviews = [review.toDict() for review in reviews]
    return reviews 



