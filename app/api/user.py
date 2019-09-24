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
    response = {"message": "Profile updated.", "redirect":"#"}
    return jsonify(response)
