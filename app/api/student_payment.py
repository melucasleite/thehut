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
        .all()
    student_payment_history = [x.to_dict(student=True) for x in student_payment_history]
    response = {"student_payment_history": student_payment_history}
    return jsonify(response)


@app.route('/api/student_payment_history', methods=["POST"])
@login_required
def api_student_payment_history_post():
    args = request.form
    student_payment_history_id = args["id"]
    amount_paid = args["amount_paid"]
    payment_method = args["payment_method"]
    student_payment_history = StudentPaymentHistory.query.get(student_payment_history_id)
    if not student_payment_history:
        raise Exception("Student Payment History not found.")
    student_payment_history.status = "Paid"
    student_payment_history.amount = amount_paid
    student_payment_history.payment_method = payment_method
    student_payment_history.payment_date = datetime.now()
    db.session.commit()
    return jsonify({"message": "Payment updated."})


@app.route('/api/student_payment_history', methods=["DELETE"])
@login_required
def api_student_payment_history_delete():
    args = request.form
    student_payment_history_id = args["id"]
    student_payment_history = StudentPaymentHistory.query.get(student_payment_history_id)
    if not student_payment_history:
        raise Exception("Student Payment History not found.")
    student_payment_history.status = "Pending"
    student_payment_history.amount = None
    student_payment_history.payment_method = None
    student_payment_history.payment_date = None
    db.session.commit()
    return jsonify({"message": "Payment deleted."})
