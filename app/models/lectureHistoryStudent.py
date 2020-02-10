# encoding: utf-8
from datetime import datetime, timedelta

from app import db


class LectureHistoryStudent(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    date = db.Column(db.DateTime)
    present = db.Column(db.Boolean)
    lecture_id = db.Column(db.Integer, db.ForeignKey('lecture.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    skills = db.relationship(
        'SkillStudent', backref='lecture_history', lazy='dynamic')
    remarks = db.relationship(
        'RemarkStudent', backref='lecture_history', lazy='dynamic')
    message = db.Column(db.String(6000))
    # control
    created_at = db.Column(db.DateTime)
    deleted = db.Column(db.Boolean, default=False)

    def __init__(self, student_id, date, lecture_id, user_id=None):
        self.student_id = student_id
        self.date = date
        self.lecture_id = lecture_id
        self.user_id = user_id
        self.created_at = datetime.now()
        self.present = None
        self.deleted = False

    def to_dict_full(self, student=True, lecture=True, skills=True, remarks=True):
        return {
            "date": self.date.isoformat(),
            "message": self.message,
            "lecture": self.lecture.to_dict() if lecture else self.lecture_id,
            "student": self.student.to_dict() if student else self.student_id,
            "skills": [x.to_dict() for x in self.skills] if skills else None,
            "remarks": [x.to_dict() for x in self.remarks] if remarks else None,
            "present": self.present,
            "id": self.id
        }
