# encoding: utf-8
from datetime import datetime, timedelta

from app import db


class LectureHistoryStudent(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    date = db.Column(db.DateTime)
    present = db.Column(db.Boolean)
    lecture_id = db.Column(db.Integer, db.ForeignKey('lecture.id'))
    skills = db.relationship('SkillStudent', backref='lecture_history', lazy='dynamic')
    remarks = db.relationship('RemarkStudent', backref='lecture_history', lazy='dynamic')
    # control
    created_at = db.Column(db.DateTime)
    deleted = db.Column(db.Boolean, default=False)

    def __init__(self, student_id, date, lecture_id):
        self.student_id = student_id
        self.date = date
        self.lecture_id = lecture_id
        self.created_at = datetime.now()
        self.present = None
        self.deleted = False

    def to_dict_full(self):
        return {
            "date": self.date.isoformat(),
            "lecture": self.lecture.to_dict(),
            "student": self.student.to_dict(),
            "present": self.present
        }
