from App.database import db

class Review (db.Model):
    reviewID = db.Column (db.Integer, primary_key=True)
    experience = db.Column (db.String(400), nullable=False)
    upvotes = db.Column (db.Integer, default=0, nullable=False)
    downvotes = db.Column (db.Integer, default=0, nullable=False)
    studentID= db.Column(db.Integer, db.ForeignKey('student.studentID'), nullable=False)
    staffID= db.Column(db.Integer, db.ForeignKey('staff.staffID'), nullable=False)

    def toDict (self):
        return{
            "reviewID": self.reviewID,
            "experience":self.experience,
            "upvotes":self.upvotes,
            "downvotes":self.downvotes,
            "studentID":self.studentID,
            "staffID":self.staffID
        }



