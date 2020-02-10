from app.models import StudentPaymentHistory, Student
from calendar import monthrange
from app import db, app
from datetime import datetime
from sqlalchemy import extract


def generate_payments():
    with app.app_context():
        count = 0
        db.session.flush()
        now = datetime.now()
        students = db.session.query(Student).all()
        for student in students:
            payment_exists = db.session.query(StudentPaymentHistory) \
                .filter(StudentPaymentHistory.student_id == student.id) \
                .filter(extract("month", StudentPaymentHistory.due_date) == now.month) \
                .first()
            if payment_exists:
                continue
            last_day_of_month = monthrange(now.year, now.month)[1]
            if student.payment_date.day <= last_day_of_month:
                due_date = now.replace(day=student.payment_date.day)
            else:
                due_date = now.replace(day=last_day_of_month)
            amount = student.monthly_payment
            db.session.add(StudentPaymentHistory(student.id, due_date, amount))
            count += 1
            db.session.commit()
        print("Created {} StudentPaymentHistory.".format(count))
        return count
