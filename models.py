from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db=SQLAlchemy()

class Post(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    author= db.Column(db.String(100),nullable=False)
    title= db.Column(db.String(100),nullable=False)
    content= db.Column(db.Text,nullable=False)
    date_posted=db.Column(db.DateTime,nullable=False , default=datetime.utcnow)

    def serialize(self):
        return{
            'id':self.id,
            'author':self.author,
            'title':self.title,
            'content':self.content,
            'date_posted':self.date_posted.strftime('%Y-%m-%d %H:%M:%S')
        }