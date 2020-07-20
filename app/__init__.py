# encoding=utf-8
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
import logging

logging.basicConfig()
logging.getLogger('apscheduler').setLevel(logging.DEBUG)

import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

os.environ.get("SENTRY_URI")

sentry_sdk.init(
    dsn=os.environ.get("SENTRY_URI"),
    integrations=[FlaskIntegration()]
)

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.models import *
from app.api import *
from app.views import *
from app.utils import error_handlers
from app.jobs.lectureHistory import generate_lecture_history
from app.jobs.studentPayment import generate_payments

scheduler = BackgroundScheduler(
    jobstores={'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')})
scheduler.start()
scheduler.add_job(generate_lecture_history, id="generate_lecture_history", replace_existing=True, trigger="interval",
                  minutes=5)
scheduler.add_job(generate_payments, id="generate_payments", replace_existing=True, trigger="interval", minutes=1)

if __name__ == "__main__":
    app.run(debug=True)


@app.route('/debug-sentry')
def trigger_error():
    division_by_zero = 1 / 0
