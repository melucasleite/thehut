var lecture_history_student;
var lectures, selected_lecture, selected_student;
$(document).ready(function() {
  $.ajax({
    url: apiUrl + "lecture_history_student",
    success: function(data) {
      lecture_history_student = data.lectures_history_student;
      renderLectures(lecture_history_student);
    }
  });
});

function groupLectures(lecture_history_students) {
  lectures = [];
  lecture_history_students.map(function(lecture_history_student) {
    found_lecture = lectures.find(function(lecture) {
      return (
        lecture_history_student.lecture.id == lecture.id &&
        lecture.date == lecture_history_student.date
      );
    });
    if (found_lecture) {
      found_lecture.students.push(lecture_history_student.student);
    } else {
      lectures.push({
        id: lecture_history_student.lecture.id,
        date: lecture_history_student.date,
        lecture: lecture_history_student.lecture,
        students: [lecture_history_student.student]
      });
    }
  });
  return lectures;
}

function renderLectures(lecture_history_student) {
  $template = $("#lecture-template");
  $("#lectures").html("");
  lectures = groupLectures(lecture_history_student);
  lectures.map(function(lecture) {
    lecture.lecture_name = "[{0}] [{1} - {2}] {3}".format(
      lecture.lecture.day_of_week,
      moment(lecture.lecture.start).format("HH:mm"),
      moment(lecture.lecture.end).format("HH:mm"),
      lecture.lecture.name
    );
    lecture.date_str = moment(lecture.date).format("DD/MM");
  });
  $template.render(lectures).appendTo("#lectures");
}

function openModalLectureReview(id) {
  selected_lecture = lectures.find(function(lecture) {
    return lecture.id == id;
  });
  selected_student = selected_lecture.students[0];
  $(".student-name").html(selected_student.name);
  $(".student-photo").attr("src", selected_student.photo);
  $(".lecture-name").html(selected_lecture.lecture.name);
  $(".lecture-date").html(moment(selected_lecture.date).format("DD/MM"));
  $(".lecture-time").html(
    "{0} - {1}".format(
      moment(selected_lecture.lecture.start).format("HH:mm"),
      moment(selected_lecture.lecture.end).format("HH:mm")
    )
  );
  $("#modalLectureReview").modal("show");
}

function next1(present) {
  $.ajax({
    url: apiUrl + "review",
    data: {
      present: present,
      student_id: selected_student.id,
      lecture_history_student_id: selected_lecture.id
    },
    beforeSend: preloaderShow,
    complete: preloaderHide,
    success: function(data) {
      defaultSuccess(data);
      if (present) {
        $("#step1").hide();
        $("#step2").show();
      } else {
        nextStudent(student.id);
      }
    },
    error: errorHandler
  });
}

function nextStudent(current_student_id) {
  $("#modalLectureReview").modal("hide");
  students = students.filter(function(student) {
    return student.id != current_student_id;
  });
  console.log("Next Student");
  console.log(students);
}

function next2() {
  $("#step2").hide();
  $("#step3").show();
}

function next3() {
  $("#step3").hide();
  $("#step4").show();
}

function next4() {
  $("#step4").hide();

  $("#step1").show();
  $(".student-img").attr("src", "/static/assets/images/users/2.jpg");
  $(".student-name").html("Uriel Jabes");
}
