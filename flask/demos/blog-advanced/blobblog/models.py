from . import db


class Base(db.Model):
    """Base model for all entities"""

    __abstract__ = True

    id = db.Model(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
