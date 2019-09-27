var students, student;
$(document).ready(function() {
  var student_id = localStorage.getItem("student_id");
  getstudents(function() {
    getStudent(student_id ? student_id : students[0].id);
    students.map(function(student) {
      student.text = student.name;
    });
    $("#select2")
      .select2({
        data: students
      })
      .on("select2:select", function(event) {
        var student_id = event.params.data.id;
        getStudent(student_id);
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
}
