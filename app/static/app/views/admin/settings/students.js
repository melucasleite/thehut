var students, student, history;
var lectures, lecture_id;
$(document).ready(function() {
  var student_id = localStorage.getItem("student_id");
  var active_tab = localStorage.getItem("students_active_tab");
  active_tab ? $(active_tab).tab("show") : $("#settings").tab("show");
  getstudents(function() {
    if (!student_id) {
      student_id = students[0].id;
    }
    getStudent(student_id);
    getStudentHistory(student_id);
    students.map(function(student) {
      student.text = student.name;
    });
    $("#selectStudent")
      .select2({
        data: students
      })
      .on("select2:select", function(event) {
        var student_id = event.params.data.id;
        getStudent(student_id);
        getStudentHistory(student_id);
      });
  });
  getLectures(function() {
    lectures.map(function(lecture) {
      lecture.text = "[{0}] {3} [{1} - {2}]".format(
        lecture.day_of_week,
        moment(lecture.start).format("HH:mm"),
        moment(lecture.end).format("HH:mm"),
        lecture.name
      );
    });
    $("#selectLecture")
      .select2({
        data: lectures
      })
      .on("select2:select", function(event) {
        lecture_id = event.params.data.id;
      });
  });
});

function getstudents(callback) {
  $.ajax({
    url: apiUrl + "students",
    method: "GET",
    beforeSend: function() {
      preloaderShow();
    },
    complete: function() {
      preloaderHide();
    },
    error: errorHandler,
    success: function(response) {
      students = response.students;
      callback();
    }
  });
}

function getStudentHistory(student_id, callback) {
  $.ajax({
    url: apiUrl + "student/review",
    method: "GET",
    data: { student_id: student_id },
    error: errorHandler,
    success: function(response) {
      history = response.history;
      renderHistory(response.history);
      if (callback) callback();
    }
  });
}

function getLectures(callback) {
  $.ajax({
    url: apiUrl + "lecture",
    method: "GET",
    error: errorHandler,
    success: function(response) {
      lectures = response.lectures;
      callback();
    }
  });
}

function getStudent(id) {
  $.ajax({
    url: apiUrl + "student",
    method: "GET",
    data: { id: id },
    beforeSend: function() {
      preloaderShow();
    },
    complete: function() {
      preloaderHide();
    },
    error: errorHandler,
    success: function(response) {
      student = response.student;
      renderStudent(student);
    }
  });
}

function updateStudent(event, form) {
  event.preventDefault();
  var data = $(form).serializeArray();
  localStorage.setItem("students_active_tab", "#settings");
  $.ajax({
    url: apiUrl + "student",
    method: "PUT",
    data: data,
    beforeSend: preloaderShow,
    complete: preloaderHide,
    error: errorHandler,
    success: function(response) {
      defaultSuccess(response, function() {
        window.location = "/students";
      });
    }
  });
}

function renderStudent(student) {
  localStorage.setItem("student_id", student.id);
  $form = $("#studentForm");
  $form.values(student);
  $form.find("textarea").val(student.message);
  $("#studentLectureStr").html(
    "{0} Lectures selected of {1} Lectures per Week.".format(
      student.lectures.length,
      student.classes_per_week
    )
  );
  $("#studentPhoto").attr(
    "src",
    student.photo
      ? student.photo
      : "https://www.r-users.com/wp-content/plugins/all-in-one-seo-pack/images/default-user-image.png"
  );
  $("#studetName").html(student.name);
  $("#studentLectures").html(
    student.classes_per_week > 1
      ? student.classes_per_week + " Lectures / Week"
      : student.classes_per_week + " Lecture / Week"
  );
  $("#StudentWeeks").html(
    student.weeks > 1 ? student.weeks + " Weeks" : student.weeks + " Week"
  );
  $("#studentCreatedAt").html(
    "Started at " + moment(student.created_at).format("LL")
  );
  $("#studentCard").fadeIn();
  $lectureTemplate = $("#lecture_template");
  $("#lectures").html("");
  student.lectures.map(function(lecture) {
    lecture.timestamp =
      moment(lecture.start).format("HH:mm") +
      " - " +
      moment(lecture.end).format("HH:mm");
  });
  $lectureTemplate.render(student.lectures).appendTo("#lectures");
}

function deleteLecture(lecture_id) {
  localStorage.setItem("students_active_tab", "#home");
  defaultConfirm(function() {
    $.ajax({
      url: apiUrl + "student/lecture",
      data: { student_id: student.id, lecture_id: lecture_id },
      method: "DELETE",
      beforeSend: function() {
        preloaderShow();
      },
      complete: function() {
        preloaderHide();
      },
      error: errorHandler,
      success: function(response) {
        defaultSuccess(response, function() {
          window.location = "/students";
        });
      }
    });
  });
}

function addLecture(event, form) {
  event.preventDefault();
  localStorage.setItem("students_active_tab", "#home");
  $.ajax({
    url: apiUrl + "student/lecture",
    data: { student_id: student.id, lecture_id: lecture_id },
    method: "POST",
    beforeSend: function() {
      preloaderShow();
    },
    complete: function() {
      preloaderHide();
    },
    error: errorHandler,
    success: function(response) {
      defaultSuccess(response, function() {
        window.location = "/students";
      });
    }
  });
}

function renderHistory(student_history) {
  $template = $("#history-template");
  $("#history").html("");
  student_history.length > 0
    ? $("#no-history").hide()
    : $("#no-history").show();
  var history = student_history.map(function(history) {
    return {
      date: moment(history.lecture.date).format("L"),
      name: "{0} - {1} {2} - {3}".format(
        history.lecture.name,
        history.lecture.day_of_week,
        moment(history.lecture.start).format("HH:mm"),
        moment(history.lecture.end).format("HH:mm")
      ),
      present: history.present ? "Present" : "Missed",
      skills: history.skills
        .map(function(skill) {
          return "{0}: {1}".format(skill.name, skill.grade);
        })
        .join(", "),
      remarks: history.remarks
        .map(function(remark) {
          if (remark.positive) {
            return "<span class='badge badge-outline-info'>{0}</span>".format(
              remark.name
            );
          } else {
            return "<span class='badge badge-outline-danger'>{0}</span>".format(
              remark.name
            );
          }
        })
        .join("")
    };
  });
  $template.render(history).appendTo("#history");
}
