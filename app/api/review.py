# encoding: utf-8
from flask import request, redirect, session, abort, jsonify
from flask_login import login_required, current_user
from app import app, db
import json
from app.utils import json_serial
from app.models import Lecture, LectureHistoryStudent, SkillStudent, RemarkStudent, Student
from datetime import datetime


@app.route('/api/student/review', methods=["POST"])
@login_required
def api_student_review_post():
    args = request.form
    present = args["present"] == "true"
    comment = args["comment"]
    id = args["lecture_history_student_id"]
    lecture_history_student = LectureHistoryStudent.query.get(id)
    lecture_history_student.present = present
    lecture_history_student.message = comment
    lecture_history_student.user_id = current_user.id
    skills = json.loads(args["skills"])
    for skill in skills:
        db.session.add(SkillStudent(
            lecture_history_student.student_id,
            lecture_history_student.lecture_id,
            skill["skill_id"],
            lecture_history_student.id,
            skill["value"]
        ))
    remarks = json.loads(args["remarks"])
    for remark in remarks:
        db.session.add(RemarkStudent(
            lecture_history_student.student_id,
            lecture_history_student.lecture_id,
            remark["remark_id"],
            lecture_history_student.id,
            remark["positive"]
        ))
    db.session.commit()
    return jsonify({"message": "Lecture History updated."}), 200


@app.route('/api/student/review', methods=["GET"])
@login_required
def api_student_review_get():
    args = request.args
    student_id = args["student_id"]
    student = Student.query.get(student_id)
    if not student:
        raise Exception("Student not found.")
    history = student.lecture_history.all()
    response = [x.to_dict_full() for x in history]
    return jsonify({"history": response}), 200
