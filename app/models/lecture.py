# encoding: utf-8
from datetime import datetime

from app import db, app


class Lecture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    day_of_week = db.Column(db.String(180))
    start = db.Column(db.Datetime)
    end = db.Column(db.Datetime)
    student_capacity = db.Column(db.Integer)
    name = db.Column(db.String(180))
    accent_color = db.Column(db.String(180))
    # relationships
    students = db.relationship(
        'LectureStudent', backref='lecture', lazy='dynamic')
    skills = db.relationship('SkillStudent', backref='lecture', lazy='dynamic')
    remarks = db.relationship(
        'RemarkStudent', backref='lecture', lazy='dynamic')
    lecture_history = db.relationship(
        'StudentLectureHistory', backref='lecture', lazy='dynamic')
    # control
    created_at = db.Column(db.Datetime)
    deleted = db.Column(db.Boolean, default=False)

    def __init__(self, day_of_week, start, end, student_capacity, name, accent_color):
        self.day_of_week = day_of_week
        self.start = start
        self.end = end
        self.student_capacity = student_capacity
        self.name = name
        self.accent_color = accent_color
        self.created_at = datetime.now()
        self.deleted = False
