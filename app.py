from flask import Flask, render_template
app = Flask(__name__)


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


@app.route("/lectures")
def lectures():
    return render_template("admin/lectures.html")


@app.route("/settings/lectures")
def settings_lectures():
    return render_template("admin/settings/lectures.html")


@app.route("/settings/student-evaluation")
def settings_student_evaluation():
    return render_template("admin/settings/student-evaluation.html")


if __name__ == "__main__":
    app.run(debug=True)
