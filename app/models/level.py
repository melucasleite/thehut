# encoding: utf-8
from datetime import datetime
from app import db, app


class Level(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(180))
    # management
    deleted = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime)
    # relationships
    students = db.relationship('Student', backref='level', lazy='dynamic')

    def __init__(self, name):
        self.name = name
        self.deleted = False
        self.created_at = datetime.now()

    def to_dict(self):
        return {
            "name": self.name,
            "id": self.id
        }