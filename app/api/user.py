# encoding: utf-8
from flask import request, redirect, session, abort, jsonify
from flask_login import login_required, current_user
from app import app, db
import json
from app.utils import json_serial


@app.route('/api/user/profile', methods=["PUT"])
@login_required
def api_user_profile_update():
    args = request.form
    name = args["name"].strip()
    cellphone = args["cellphone"].strip()
    cellphone = ''.join(filter(lambda x: x.isdigit(), cellphone))
    try:
        if (len(name) < 10 or len(cellphone) < 10):
            raise Exception("Name or cellphone needs to be at least 10 chars.")
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    current_user.name = name
    current_user.cellphone = cellphone
    db.session.commit()
    response = {"message": "Profile updated."}
    return jsonify(response)


@app.route('/api/user/password', methods=["PUT"])
@login_required
def api_user_password_update():
    args = request.form
    password = args["password"].strip()
    new_password = args["new_password"].strip()
    new_password_confirm = args["new_password_confirm"].strip()
    try:
        if password != current_user.password:
            raise Exception("Wrong password.")
        if new_password != new_password_confirm:
            raise Exception("Wrong password confirmation.")
        if (len(new_password) < 6):
            raise Exception("Password must be at least 6 characters long.")
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    current_user.password = new_password
    db.session.commit()
    response = {"message": "Password updated."}
    return jsonify(response)
