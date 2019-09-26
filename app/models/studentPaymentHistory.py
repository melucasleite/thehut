# encoding: utf-8
from datetime import datetime, timedelta
import uuid

from sqlalchemy.dialects.mysql import JSON

from app import db


class StudentPaymentHistory(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    due_date = db.Column(db.DateTime)
    payment_date = db.Column(db.DateTime)
    amount = db.Column(db.Integer)
    payment_method = db.Column(db.String(180))
    # control
    created_at = db.Column(db.DateTime)
    deleted = db.Column(db.Boolean, default=False)

    def __init__(self, student_id, due_date, payment_date, amount, payment_method):
        self.student_id = student_id
        self.due_date = due_date
        self.payment_date = payment_date
        self.amount = amount
        self.payment_method = payment_method
        self.created_at = datetime.now()
        self.deleted = False
