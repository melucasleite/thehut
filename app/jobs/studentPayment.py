from app.models import StudentPaymentHistory, Student
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
            due_date = now.replace(day=student.payment_date.day)
            amount = student.monthly_payment
            db.session.add(
                StudentPaymentHistory(student.id, due_date, amount))
            count += 1
            db.session.commit()
        print "Created {} StudentPaymentHistory.".format(count)
        return count
