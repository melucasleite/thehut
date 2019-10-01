from app.models import Lecture, LectureStudent, LectureHistoryStudent
from app import db
from datetime import datetime

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def generate_lecture_history():
    # Get today weekday
    # Get all lectures of the same weekday
    # Conditions:
    # End passed actual time.
    # Has lastLectureHistory not today.
    now = datetime.now()
    now_time = now.replace(year=1900, month=1, day=1, hour=18)
    now_date = now.replace(hour=0, minute=0, second=0, microsecond=0)
    weekday = weekdays[now.weekday()-1]
    lectures = db.session.query(Lecture) \
        .filter(now_time >= Lecture.end) \
        .filter(Lecture.day_of_week == weekday) \
        .all()
    for lecture in lectures:
        print lecture
        for lecture_student in lecture.students:
            student = lecture_student.student
            print student
            lecture_history_exists = db.session.query(LectureHistoryStudent) \
                .filter(LectureHistoryStudent.student_id == student.id) \
                .filter(LectureHistoryStudent.lecture_id == lecture.id) \
                .filter(LectureHistoryStudent.date == now_date) \
                .first()
            if lecture_history_exists:
                print lecture_history_exists.to_dict_full()
                continue
            db.session.add(LectureHistoryStudent(student.id, now_date, lecture.id))
            db.session.commit()
            print "Registered"
    # For each leacture
    # All Students from this Lecture
    # Conditions:
    # Student has no lastLectureHistory for this lecture_id, create_at today
    # Generate lectureHistoryStudent for each student
    pass
