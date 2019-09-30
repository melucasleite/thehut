# encoding: utf-8
from datetime import datetime, timedelta
from app import db


class RemarkStudent(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    lecture_id = db.Column(db.Integer, db.ForeignKey('lecture.id'))
    remark_id = db.Column(db.Integer, db.ForeignKey('remark.id'))
    lecture_history_student_id = db.Column(db.Integer, db.ForeignKey('lecture_history_student.id'))
    positive = db.Column(db.Boolean)
    # control
    created_at = db.Column(db.DateTime)
    deleted = db.Column(db.Boolean, default=False)

    def __init__(self, student_id, lecture_id, remark_id, lecture_history_student_id, positive):
        self.student_id = student_id
        self.lecture_id = lecture_id
        self.remark_id = remark_id
        self.lecture_history_student_id = lecture_history_student_id
        self.positive = positive
        self.created_at = datetime.now()
        self.deleted = False
