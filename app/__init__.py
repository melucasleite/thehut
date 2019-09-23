#encoding=utf-8
from flask import Flask, render_template, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import login_required
from apscheduler.schedulers.background import BackgroundScheduler
scheduler = BackgroundScheduler()
scheduler.start()

import logging
logging.basicConfig()

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.models import *
from app.api import *
from app.api.security import admin_permission

@app.route("/")
@login_required
def user_index():
    return render_template("admin/index.html")


@app.route("/finances")
@admin_permission.require(http_exception=403)
def finances():
    return render_template("admin/finances.html")


@app.route("/login")
def login():
    return render_template("admin/login.html")


@app.route("/register")
def register():
    return render_template("admin/register.html")


@app.route("/students")
def students():
    return render_template("admin/students.html")


@app.route("/students/review")
def students_review():
    return render_template("admin/students-review.html")


@app.route("/lectures")
def lectures():
    return render_template("admin/lectures.html")


@app.route("/settings/lectures")
@admin_permission.require(http_exception=403)
def settings_lectures():
    return render_template("admin/settings/lectures.html")

@app.route("/settings")
@admin_permission.require(http_exception=403)
def settings():
    return render_template("admin/settings/settings.html")


@app.route("/settings/profile")
@admin_permission.require(http_exception=403)
def settings_profile():
    return render_template("admin/settings/profile.html")

@app.route("/settings/password")
@admin_permission.require(http_exception=403)
def settings_password():
    return render_template("admin/settings/password.html")


@app.route("/settings/student-evaluation")
@admin_permission.require(http_exception=403)
def settings_student_evaluation():
    return render_template("admin/settings/student-evaluation.html")


@app.route("/settings/teachers")
@admin_permission.require(http_exception=403)
def settings_teachers():
    return render_template("admin/settings/teachers.html")


@app.route("/student-signin")
def student_signin():
    return render_template("student-signin.html")

@app.errorhandler(403)
def error_handler_forbidden(e):
    return redirect(url_for('login'))


@app.errorhandler(401)
def error_handler_api_unauthorized(e):
    return jsonify({"message":"Unauthorized."}), 401


if __name__ == "__main__":
    app.run(debug=True)
