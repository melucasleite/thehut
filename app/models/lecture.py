# encoding: utf-8
from datetime import datetime

from app import db, app
import json
from app.utils.json_serial import json_serial


class Lecture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    day_of_week = db.Column(db.String(180))
    start = db.Column(db.DateTime)
    end = db.Column(db.DateTime)
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
        'LectureHistoryStudent', backref='lecture', lazy='dynamic')
    # control
    created_at = db.Column(db.DateTime)
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

    def to_dict(self):
        return {
            "id": self.id,
            "day_of_week": self.day_of_week,
            "start": self.start.isoformat(),
            "end": self.end.isoformat(),
            "students": len(self.students.all()),
            "student_capacity": self.student_capacity,
            "name": self.name,
            "accent_color": self.accent_color,
            "created_at": self.created_at.isoformat(),
        }

    def to_dict_full(self):
        return {
            "id": self.id,
            "day_of_week": self.day_of_week,
            "start": self.start.isoformat(),
            "end": self.end.isoformat(),
            "students": [student.to_dict() for student in self.students.all()],
            "student_capacity": self.student_capacity,
            "name": self.name,
            "accent_color": self.accent_color,
            "created_at": self.created_at.isoformat(),
        }
