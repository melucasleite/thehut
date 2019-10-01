from app.models import Student, LectureStudent
from app import db
import names


def create_students():
    name = names.get_full_name()
    email = "_".join(name.split(" ")).lower() + "@gmail.com"
    student = Student(name, email, "111", "", 2, 20, 1, 100)
    db.session.add(student)
    db.session.commit()
    db.session.add(LectureStudent(student.id, 2))
    db.session.add(LectureStudent(student.id, 5))
    db.session.add(LectureStudent(student.id, 6))
    db.session.commit()

    name = names.get_full_name()
    email = "_".join(name.split(" ")).lower() + "@gmail.com"
    student = Student(name, email, "111", "", 2, 20, 1, 100)
    db.session.add(student)
    db.session.commit()
    db.session.add(LectureStudent(student.id, 2))
    db.session.add(LectureStudent(student.id, 5))
    db.session.add(LectureStudent(student.id, 6))
    db.session.commit()

    name = names.get_full_name()
    email = "_".join(name.split(" ")).lower() + "@gmail.com"
    student = Student(name, email, "111", "", 2, 20, 1, 100)
    db.session.add(student)
    db.session.commit()
    db.session.add(LectureStudent(student.id, 2))
    db.session.add(LectureStudent(student.id, 5))
    db.session.add(LectureStudent(student.id, 6))
    db.session.commit()
