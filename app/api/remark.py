# encoding: utf-8
from flask import request, redirect, session, abort, jsonify
from flask_login import login_required, current_user
from app import app, db
import json
from app.utils import json_serial
from app.models.remark import Remark
from datetime import datetime


@app.route('/api/remark', methods=["GET"])
@login_required
def api_remark_get():
    remarks = Remark.query.filter_by(deleted=False).all()
    remarks = [x.to_dict() for x in remarks]
    response = {"remarks": remarks}
    return jsonify(response)


@app.route('/api/remark', methods=["DELETE"])
@login_required
def api_remark_delete():
    id = request.form.get("id")
    remarks = Remark.query.get(id)
    if not remarks:
        raise Exception("Remark not found.")
    remarks.deleted = True
    db.session.commit()
    response = {"message": "Remark deleted."}
    return jsonify(response)


@app.route('/api/remark', methods=["POST"])
@login_required
def api_remark_post():
    args = request.form
    name = args.get("name")
    if not (name):
        raise Exception("Missing fields.")
    remarks = Remark(name)
    db.session.add(remarks)
    db.session.commit()
    response = {"message": "Remark Created."}
    return jsonify(response)
