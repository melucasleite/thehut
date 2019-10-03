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
    amount = db.Column(db.DECIMAL(10, 2))
    status = db.Column(db.String(180))
    payment_method = db.Column(db.String(180))
    # control
    created_at = db.Column(db.DateTime)
    deleted = db.Column(db.Boolean, default=False)

    def __init__(self, student_id, due_date, amount, payment_method=None, payment_date=None):
        self.student_id = student_id
        self.due_date = due_date
        self.payment_date = payment_date
        self.amount = amount
        self.payment_method = payment_method
        self.created_at = datetime.now()
        self.status = "Pending"
        self.deleted = False

    def to_dict(self, student=False):
        response = {
            "id": self.id,
            "student_id": self.student_id,
            "due_date": self.due_date.isoformat(),
            "payment_date": self.payment_date.isoformat() if self.payment_date else None,
            "amount": self.amount,
            "status": self.status,
            "payment_method": self.payment_method,
            "created_at": self.created_at.isoformat(),
        }
        if student:
            response["student"] = self.student.to_dict()
        return response
