from myblog import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __str__(self) -> str:
        return 'user'
# posts = db.relationship('Post', backref='author')