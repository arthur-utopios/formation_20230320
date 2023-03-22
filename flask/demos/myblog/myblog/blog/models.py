from myblog import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)