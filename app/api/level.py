# encoding: utf-8
from flask import request, redirect, session, abort, jsonify
from flask_login import login_required, current_user
from app import app, db
import json
from app.utils import json_serial
from app.models.level import Level
from datetime import datetime


@app.route('/api/level', methods=["GET"])
@login_required
def api_level_get():
    levels = Level.query.filter_by(deleted=False).all()
    levels = [x.to_dict() for x in levels]
    response = {"levels": levels}
    return jsonify(response)


@app.route('/api/level', methods=["DELETE"])
@login_required
def api_level_delete():
    id = request.form.get("id")
    level = Level.query.get(id)
    if not level:
        raise Exception("Level not found.")
    level.deleted = True
    db.session.commit()
    response = {"message": "Level deleted."}
    return jsonify(response)


@app.route('/api/level', methods=["POST"])
@login_required
def api_level_post():
    args = request.form
    name = args.get("name")
    if not (name):
        raise Exception("Missing fields.")
    level = Level(name)
    db.session.add(level)
    db.session.commit()
    response = {"message": "Level Created."}
    return jsonify(response)
