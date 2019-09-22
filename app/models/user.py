# encoding: utf-8
from datetime import datetime

from flask_login import UserMixin
from app import db, app


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(180))
    email = db.Column(db.String(180), unique=True)
    password = db.Column(db.String(180))
    cellphone = db.Column(db.String(180))
    photo = db.Column(db.String(180))
    # control
    deleted = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime)

    def __init__(self, name, email, password, cellphone, photo):
        self.name = name
        self.email = email
        self.password = password
        self.cellphone = cellphone
        self.photo = photo
        self.deleted = False
        self.created_at = datetime.now()
