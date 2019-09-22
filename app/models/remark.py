# encoding: utf-8
from datetime import datetime
from app import db, app


class Remark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(180))
    kind = db.Column(db.String(180))
    # management
    deleted = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime)
    # relationships
    remarkStudents = db.relationship(
        'RemarkStudent', backref='remark', lazy='dynamic')

    def __init__(self, name, kind):
        self.name = name
        self.kind = kind
        self.deleted = False
        self.created_at = datetime.now()
