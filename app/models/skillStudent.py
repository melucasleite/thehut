# encoding: utf-8
from datetime import datetime, timedelta

from app import db


class SkillStudent(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    lecture_id = db.Column(db.Integer, db.ForeignKey('lecture.id'))
    skill_id = db.Column(db.Integer, db.ForeignKey('skill.id'))
    lecture_history_student_id = db.Column(db.Integer, db.ForeignKey('lecture_history_student.id'))
    grade = db.Column(db.Integer)
    # control
    created_at = db.Column(db.DateTime)
    deleted = db.Column(db.Boolean, default=False)

    def __init__(self, student_id, lecture_id, skill_id, lecture_history_student_id, grade):
        self.student_id = student_id
        self.lecture_id = lecture_id
        self.skill_id = skill_id
        self.lecture_history_student_id = lecture_history_student_id
        self.grade = grade
        self.created_at = datetime.now()
        self.deleted = False
