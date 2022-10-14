from App.database import db
from App.models.review import db, Review

class Student (db.Model):
    studentID= db.Column (db.Integer, primary_key=True)
    name = db.Column (db.String(120), nullable=False)
    reviews= db.relationship('Review', backref="student", lazy=True, cascade="all, delete-orphan")

    #reviews= db.relationship('Review', lazy=True, cascade="all, delete-orphan",back_populates="student")
    #reviews= db.relationship('Review')


    def __init__(self, studentID, name):
        self.studentID = studentID
        self.name = name
    

    def toJSON(self):
        reviews = [review.toJSON() for review in self.reviews]

        return{
            'studentID':self.studentID,
            'name':self.name,
            'reviews':reviews,
            'karma_score':self.getScore()
        }
    

    def getScore (self):
        score=100
        for review in self.reviews:
            if (review.rating>5):
                score= score + review.rating + (review.rating-5)*review.upvotes - review.downvotes
            elif (review.rating<5):
                score= score - (10 - review.rating) - (5-review.rating)*review.upvotes + review.downvotes
            elif (review.rating==5):
                score=score + review.rating + review.upvotes - review.downvotes
        return score
            



