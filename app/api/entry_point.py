# encoding: utf-8
from app import app, db, User
from app.utils import json_serial
from flask import render_template, abort
from flask_login import login_required, current_user
import json


@app.route("/api/entryPoint.js")
def api_entry_point():
    if not current_user.is_authenticated:
        abort(404)
    user = {
        "name": current_user.name,
        "email": current_user.email,
        "cellphone": current_user.cellphone,
        "roles": current_user.roles,
        "created_at": current_user.created_at,
    }
    state = {
        "user": user
    }
    return render_template("entryPoint.js", state=state)
