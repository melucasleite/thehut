from app.models import Lecture, LectureStudent, LectureHistoryStudent
from app import db, app
from datetime import datetime

weekdays = ["Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"]


def generate_lecture_history():
    with app.app_context():
        count = 0
        # Get today weekday
        # Get all lectures of the same weekday
        # Conditions:
        # End passed actual time.
        # Has lastLectureHistory not today.
        # For each leacture
        # All Students from this Lecture
        # Conditions:
        # Student has no lastLectureHistory for this lecture_id, create_at today
        # Generate lectureHistoryStudent for each student
        db.session.flush()
        now = datetime.now()
        now_time = now.replace(year=1900, month=1, day=1)
        now_date = now.replace(hour=0, minute=0, second=0, microsecond=0)
        weekday = weekdays[now.weekday()]
        lectures = db.session.query(Lecture) \
            .filter(now_time >= Lecture.end) \
            .filter(Lecture.day_of_week == weekday) \
            .all()
        for lecture in lectures:
            for lecture_student in lecture.students:
                student = lecture_student.student
                lecture_history_exists = db.session.query(LectureHistoryStudent) \
                    .filter(LectureHistoryStudent.student_id == student.id) \
                    .filter(LectureHistoryStudent.lecture_id == lecture.id) \
                    .filter(LectureHistoryStudent.date == now_date) \
                    .first()
                if lecture_history_exists:
                    continue
                db.session.add(LectureHistoryStudent(
                    student.id, now_date, lecture.id))
                count += 1
                db.session.commit()
        print("Created {} LectureHistoryStudent.".format(count))
        return count
