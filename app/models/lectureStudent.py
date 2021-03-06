# encoding: utf-8
from datetime import datetime, timedelta

from app import db


class LectureStudent(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    lecture_id = db.Column(db.Integer, db.ForeignKey('lecture.id'))
    # control
    created_at = db.Column(db.DateTime)
    deleted = db.Column(db.Boolean, default=False)

    def __init__(self, student_id, lecture_id):
        self.student_id = student_id
        self.lecture_id = lecture_id
        self.created_at = datetime.now()
        self.deleted = False

    def to_dict(self):
        return {
            "name": self.lecture.name,
            "accent_color": self.lecture.accent_color,
            "day_of_week": self.lecture.day_of_week,
            "start": self.lecture.start.isoformat(),
            "end": self.lecture.end.isoformat(),
            "student_capacity": self.lecture.student_capacity,
            "student_id": self.student_id,
            "student_name": self.student.name,
            "student_cellphone": self.student.cellphone,
            "student_photo": self.student.photo,
            "lecture_id": self.lecture_id,
        }