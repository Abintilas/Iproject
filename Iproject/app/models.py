
from app.database import db

class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(length=16))
    email = db.Column(db.String(length=32))
    password = db.Column(db.String(length=32))

    def __repr__(self):
        return str(self.username)
