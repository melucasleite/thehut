from app.jobs.lectureHistory import generate_lecture_history
from app.scripts.create_mocks import create_students

create_students()
generate_lecture_history()
print "Im done!"
