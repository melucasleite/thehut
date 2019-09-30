# encoding: utf-8
from flask import request, redirect, session, abort, jsonify
from flask_login import login_required, current_user
from app import app, db
import json
from app.utils import json_serial
from app.models.skill import Skill
from datetime import datetime


@app.route('/api/skill', methods=["GET"])
@login_required
def api_skill_get():
    skills = Skill.query.filter_by(deleted=False).all()
    skills = map(lambda x: x.to_dict(), skills)
    response = {"skills": skills}
    return jsonify(response)


@app.route('/api/skill', methods=["DELETE"])
@login_required
def api_skill_delete():
    id = request.form.get("id")
    skills = Skill.query.get(id)
    if not skills:
        raise Exception("Skill not found.")
    skills.deleted = True
    db.session.commit()
    response = {"message": "Skill deleted."}
    return jsonify(response)


@app.route('/api/skill', methods=["POST"])
@login_required
def api_skill_post():
    args = request.form
    name = args.get("name")
    if not (name):
        raise Exception("Missing fields.")
    skills = Skill(name)
    db.session.add(skills)
    db.session.commit()
    response = {"message": "Skill Created."}
    return jsonify(response)
