# encoding: utf-8
from flask import request, redirect, session, abort, jsonify
from flask_login import login_required, current_user
from app import app, db
import json
from app.utils import json_serial
from app.models import Lecture, LectureHistoryStudent
from datetime import datetime


@app.route('/api/lecture_history_student', methods=["GET"])
@login_required
def api_lecture_history_student_get():
    lectures_history_student = db.session.query(LectureHistoryStudent) \
        .filter(LectureHistoryStudent.present == None) \
        .all()
    lectures_history_student = map(lambda x: x.to_dict_full(), lectures_history_student)
    response = {"lectures_history_student": lectures_history_student}
    return jsonify(response)
