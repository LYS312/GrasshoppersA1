from App.database import db

class Student (db.Model):
    studentID= db.Column (db.Integer, primary_key=True)
    name = db.Column (db.String(120), nullable=False)
    reviews= db.relationship('Review', backref='student', lazy=True, cascade="all, delete-orphan")

    def toJSON(self):
        return{
            'studentID':self.studentID,
            'name':self.name,
            'reviews':self.reviews,
            'karma_score':self.getScore()
        }
    
    def getScore (self):
        score=100
        for review in self.reviews:
            if (review.rating>5):
                score= score + review.rating + (review.rating-5)*review.upvotes - review.downvotes
            elif (review.rating<5):
                score= score - (10 - review.rating) - (5-review.rating)*review.upvotes + review.downvotes
            else (review==5):
                score=score + review.rating + review.upvotes - review.downvotes
        return score
            



