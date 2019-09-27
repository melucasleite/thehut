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


@app.route('/api/students', methods=["GET"])
@login_required
def api_students_get():
    students = Student.query.all()
    students = map(lambda x: x.to_dict(), students)
    response = {"students": students}
    return jsonify(response)


@app.route('/api/student', methods=["GET"])
@login_required
def api_student_get():
    print request.args
    student = Student.query.get(request.args.get("id"))
    if not student:
        raise Exception("Student not found.")
    response = {"student": student.to_dict_full()}
    return jsonify(response)


@app.route('/api/student', methods=["PUT"])
@login_required
def api_student_update():
    args = request.form
    id = args["id"]
    name = args["name"].strip()
    email = args["email"].strip()
    cellphone = args["cellphone"].strip()
    classes_per_week = args["classes_per_week"].strip()
    weeks = args["weeks"].strip()
    monthly_payment = args["monthly_payment"].strip()
    message = args["message"].strip()
    cellphone = ''.join(filter(lambda x: x.isdigit(), cellphone))
    student = Student.query.get(id)
    if not student:
        raise Exception("Student not found.")
    if not(name and email):
        raise Exception("Missing fields.")
    student.name = name
    student.email = email
    student.cellphone = cellphone
    student.classes_per_week = classes_per_week
    student.weeks = weeks
    student.monthly_payment = monthly_payment
    student.message = message
    student.cellphone = cellphone
    db.session.commit()
    return jsonify({"message": "Student updated."}), 200
