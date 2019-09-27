# encoding: utf-8
from flask import request, redirect, session, abort, jsonify
from flask_login import login_required, current_user
from app import app, db
import json
from app.utils import json_serial
from app.models import Student, LectureStudent, Lecture


@app.route('/api/student', methods=["POST"])
@login_required
def api_student_post():
    args = request.form
    name = args["name"].strip()
    email = args["email"].strip()
    cellphone = args["cellphone"].strip()
    lectures = json.loads(args["lectures"])
    cellphone = ''.join(filter(lambda x: x.isdigit(), cellphone))
    photo = args["photo"].strip()
    classes_per_week = args["classes_per_week"].strip()
    weeks = args["weeks"].strip()
    level = args["level"].strip()
    monthly_payment = args["monthly_payment"].strip()
    student_exists = Student.query.filter_by(email=email).first()
    if student_exists:
        return jsonify({"message": "Já existe um estudante cadastrado com esse e-mail."}), 400
    student = Student(name, email, cellphone, photo,
                      classes_per_week, weeks, level, monthly_payment)
    db.session.add(student)
    db.session.commit()
    for lecture_id in lectures:
        lecture = Lecture.query.get(lecture_id)
        lecture_student = LectureStudent(student.id, lecture.id)
        db.session.add(lecture_student)
        db.session.commit()
    response = {"message": "Student Created."}
    return jsonify(response)
