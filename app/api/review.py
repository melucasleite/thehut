# encoding: utf-8
from flask import request, redirect, session, abort, jsonify
from flask_login import login_required, current_user
from app import app, db
import json
from app.utils import json_serial
from app.models import Lecture, LectureHistoryStudent, SkillStudent, RemarkStudent
from datetime import datetime


@app.route('/api/student/review', methods=["POST"])
@login_required
def api_student_review():
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
        print skill
        db.session.add(SkillStudent(
            lecture_history_student.student_id,
            lecture_history_student.lecture_id,
            skill["skill_id"],
            lecture_history_student.id,
            skill["value"]
        ))
    remarks = json.loads(args["remarks"])
    for remark in remarks:
        print remark
        db.session.add(RemarkStudent(
            lecture_history_student.student_id,
            lecture_history_student.lecture_id,
            remark["remark_id"],
            lecture_history_student.id,
            remark["positive"]
        ))
    db.session.commit()
    return jsonify({"message": "Lecture History updated."}), 200
