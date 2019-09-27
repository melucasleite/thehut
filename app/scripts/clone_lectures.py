# replicate all_lectures to a weekdays list
from app import db
from app.models import Lecture

def clone_lectures():
    all_lectures = Lecture.query.all()
    week_days = [
        #"Monday",
        "Thuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]
    for week_day in week_days:
        for lecture in all_lectures:
            new_lecture = Lecture(week_day, lecture.start, lecture.end, lecture.student_capacity, lecture.name, lecture.accent_color)
            db.session.add(new_lecture)
            db.session.commit()
