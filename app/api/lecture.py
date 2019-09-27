# encoding: utf-8
from flask import request, redirect, session, abort, jsonify
from flask_login import login_required, current_user
from app import app, db
import json
from app.utils import json_serial
from app.models.lecture import Lecture
from datetime import datetime


@app.route('/api/lecture', methods=["GET"])
@login_required
def api_lecture_get():
    lectures = Lecture.query.filter_by(deleted=False).all()
    lectures = map(lambda x: x.to_dict(), lectures)
    response = {"lectures": lectures}
    return jsonify(response)


@app.route('/api/lecture', methods=["DELETE"])
@login_required
def api_lecture_delete():
    id = request.form.get("id")
    lecture = Lecture.query.filter_by(id=id).first()
    if not lecture:
        raise Exception("Lecture not found.")
    lecture.deleted = True
    db.session.commit()
    response = {"message": "Lecture deleted."}
    return jsonify(response)


@app.route('/api/lecture', methods=["POST"])
@login_required
def api_lecture_post():
    args = request.form
    day_of_week = args.get("day_of_week")
    name = args.get("lecture_name")
    student_capacity = args.get("student_capacity")
    start = args.get("start")
    end = args.get("end")
    start = datetime.strptime(start, '%H:%M')
    end = datetime.strptime(end, '%H:%M')
    accent_color = args.get("accent_color")
    if not (day_of_week and name and student_capacity and start and end and accent_color):
        raise Exception("Missing fields.")
    lecture = Lecture(day_of_week, start, end,
                      student_capacity, name, accent_color)
    db.session.add(lecture)
    db.session.commit()
    response = {"message": "Lecture Created."}
    return jsonify(response)


@app.route('/api/lecture', methods=["PUT"])
@login_required
def api_lecture_put():
    args = request.form
    id = args.get("id")
    lecture = Lecture.query.get(id)
    if not lecture:
        raise Exception("Lecture not found.")
    day_of_week = args.get("day_of_week")
    name = args.get("name")
    student_capacity = args.get("student_capacity")
    start = args.get("start")
    end = args.get("end")
    start = datetime.strptime(start, '%H:%M')
    end = datetime.strptime(end, '%H:%M')
    accent_color = args.get("accent_color")
    if not (day_of_week and name and student_capacity and start and end and accent_color):
        raise Exception("Missing fields.")
    lecture.day_of_week = day_of_week
    lecture.name = name
    lecture.student_capacity = student_capacity
    lecture.start = start
    lecture.end = end
    lecture.accent_color = accent_color
    db.session.commit()
    response = {"message": "Lecture Updated."}
    return jsonify(response)
