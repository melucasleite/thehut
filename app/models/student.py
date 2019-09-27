# encoding: utf-8
from datetime import datetime

from app import db, app


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(180))
    email = db.Column(db.String(180), unique=True)
    cellphone = db.Column(db.String(180))
    photo = db.Column(db.String(180))
    # billing
    classes_per_week = db.Column(db.Integer)
    weeks = db.Column(db.Integer)
    monthly_payment = db.Column(db.Integer)
    message = db.Column(db.String(6000))
    # management
    deleted = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime)
    # relationships
    level_id = db.Column(db.Integer, db.ForeignKey('level.id'))
    lectures = db.relationship(
        'LectureStudent', backref='student', lazy='dynamic')
    skills = db.relationship('SkillStudent', backref='student', lazy='dynamic')
    remarks = db.relationship(
        'RemarkStudent', backref='student', lazy='dynamic')
    lecture_history = db.relationship(
        'StudentLectureHistory', backref='student', lazy='dynamic')
    payment_history = db.relationship(
        'StudentPaymentHistory', backref='student', lazy='dynamic')

    def __init__(self, name, email, cellphone, photo, classes_per_week, weeks, level, monthly_payment):
        self.name = name
        self.email = email
        self.cellphone = cellphone
        self.photo = photo
        self.classes_per_week = classes_per_week
        self.weeks = weeks
        self.level = level
        self.monthly_payment = monthly_payment
        self.message = ""
        self.deleted = False
        self.created_at = datetime.now()
