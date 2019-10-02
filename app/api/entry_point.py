# encoding: utf-8
from app import app, db, User
from flask import abort, render_template
from flask_login import current_user
import json
from app.models import LectureHistoryStudent


@app.route("/api/entryPoint.js")
def api_entry_point():
    if not current_user.is_authenticated:
        abort(404)
    user = {
        "name": current_user.name,
        "email": current_user.email,
        "cellphone": current_user.cellphone,
        "roles": current_user.roles,
        "photo": current_user.photo,
        "created_at": current_user.created_at.isoformat(),
    }
    pending_review = db.session.query(LectureHistoryStudent) \
        .filter(LectureHistoryStudent.present == None) \
        .count()
    state = {
        "user": user,
        "pending_review": pending_review
    }
    return render_template("entryPoint.js", state=state)
