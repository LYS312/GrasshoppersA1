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


