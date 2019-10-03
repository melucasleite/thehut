# encoding: utf-8
from flask import request, redirect, session, abort, jsonify
from flask_login import login_required, current_user
from app import app, db
import json
from app.utils import json_serial
from app.models import Lecture, StudentPaymentHistory
from datetime import datetime


@app.route('/api/student_payment_history', methods=["GET"])
@login_required
def api_student_payment_history():
    student_payment_history = db.session.query(StudentPaymentHistory) \
        .filter(StudentPaymentHistory.payment_date == None) \
        .all()
    student_payment_history = map(lambda x: x.to_dict(student=True), student_payment_history)
    response = {"student_payment_history": student_payment_history}
    return jsonify(response)
