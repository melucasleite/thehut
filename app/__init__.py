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
from app.views import *
from app.utils import error_handlers

if __name__ == "__main__":
    app.run(debug=True)
