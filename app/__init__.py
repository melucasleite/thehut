from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from apscheduler.schedulers.background import BackgroundScheduler
scheduler = BackgroundScheduler()
scheduler.start()

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route("/")
def hello():
    return render_template("admin/index.html")


@app.route("/finances")
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
def settings_lectures():
    return render_template("admin/settings/lectures.html")

@app.route("/settings")
def settings():
    return render_template("admin/settings/settings.html")


@app.route("/settings/profile")
def settings_profile():
    return render_template("admin/settings/profile.html")

@app.route("/settings/password")
def settings_password():
    return render_template("admin/settings/password.html")


@app.route("/settings/student-evaluation")
def settings_student_evaluation():
    return render_template("admin/settings/student-evaluation.html")


@app.route("/settings/teachers")
def settings_teachers():
    return render_template("admin/settings/teachers.html")


@app.route("/student-signin")
def student_signin():
    return render_template("student-signin.html")


if __name__ == "__main__":
    app.run(debug=True)
