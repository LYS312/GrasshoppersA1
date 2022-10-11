from App.database import db
from datetime import datetime

class Review (db.Model):
    reviewID = db.Column (db.Integer, primary_key=True)
    experience = db.Column (db.String(400), nullable=False)
    rating = db.Column (db.Integer, nullable=False)
    upvotes = db.Column (db.Integer, default=0, nullable=False)
    downvotes = db.Column (db.Integer, default=0, nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.utcnow, nullable=False)
    studentID = db.Column(db.Integer, db.ForeignKey('student.studentID'), nullable=False)
    staffID= db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, experience, rating, studentID, staffID):
        self.experience = experience
        self.rating = rating
        self.studentID = studentID
        self.staffID = staffID


    def toJSON (self):
        return{
            'reviewID': self.reviewID,
            'experience':self.experience,
            'rating':self.rating,
            'upvotes':self.upvotes,
            'downvotes':self.downvotes,
            'created_on':self.created_on,
            'studentID':self.studentID,
            'staffID':self.staffID
        }



