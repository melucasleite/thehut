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
    monthly_payment = db.Column(db.DECIMAL(10,2))
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

    def __init__(self, name, email, cellphone, photo, classes_per_week, weeks, level_id, monthly_payment):
        self.name = name
        self.email = email
        self.cellphone = cellphone
        self.photo = photo
        self.classes_per_week = classes_per_week
        self.weeks = weeks
        self.level_id = level_id
        self.monthly_payment = monthly_payment
        self.message = ""
        self.deleted = False
        self.created_at = datetime.now()

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "cellphone": self.cellphone,
            "photo": self.photo,
            "classes_per_week": self.classes_per_week,
            "weeks": self.weeks,
            "level_id": self.level_id,
            "monthly_payment": float(self.monthly_payment),
            "message": self.message,
            "created_at": self.created_at.isoformat(),
        }

    def to_dict_full(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "cellphone": self.cellphone,
            "photo": self.photo,
            "classes_per_week": self.classes_per_week,
            "weeks": self.weeks,
            "level": self.level.name,
            "monthly_payment": float(self.monthly_payment),
            "message": self.message,
            "created_at": self.created_at.isoformat(),
            "lectures": map(lambda x: x.to_dict(), self.lectures)
        }
