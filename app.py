from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/finances")
def finances():
    return render_template("finances.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/students")
def students():
    return render_template("students.html")


@app.route("/lectures")
def lectures():
    return render_template("lectures.html")


if __name__ == "__main__":
    app.run(debug=True)
