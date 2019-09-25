# encoding: utf-8
from flask import request, redirect, session, abort, jsonify
from flask_login import login_required, current_user
from app import app, db
import json
from app.utils import json_serial
from app.models import Student


@app.route('/api/student', methods=["POST"])
@login_required
def api_student_post():
    args = request.form
    name = args["name"].strip()
    email = args["email"].strip()
    cellphone = args["cellphone"].strip()
    cellphone = ''.join(filter(lambda x: x.isdigit(), cellphone))
    photo = args["photo"].strip()
    classes_per_week = args["classes_per_week"].strip()
    weeks = args["weeks"].strip()
    level = args["level"].strip()
    monthly_payment = args["monthly_payment"].strip()
    student = Student(name, email, cellphone, photo,
                      classes_per_week, weeks, level, monthly_payment)
    db.session.add(student)
    db.session.commit()
    response = {"message": "Student Created."}
    return jsonify(response)
