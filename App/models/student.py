from App.database import db

class Student (db.Model):
    studentID= db.Column (db.Integer, primary_key=True)
    name = db.Column (db.String(120), nullable=False)
    reviews= db.relationship('Review', backref='student', lazy=True, cascade="all, delete-orphan")

    def toJSON(self):
        return{
            'studentID':self.studentID,
            'name':self.name,
            'reviews':self.reviews
        }
    
    def getScore (self):
        score=100
        for review in self.reviews:
            score= score + review.upvotes - review.downvotes
        return score
            



