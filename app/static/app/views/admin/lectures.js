var lectures, students, student_id;
$(document).ready(function() {
  loadLectures();
  loadStudents(function() {
    students.map(function(student) {
      student.text = "{0} ({1})".format(student.name, student.email);
    });
    $("#selectStudents")
      .select2({
        data: students
      })
      .on("select2:select", function(event) {
        student_id = event.params.data.id;
      });
  });
});

function loadLectures() {
  $.ajax({
    url: apiUrl + "lecture",
    method: "GET",
    beforeSend: preloaderShow,
    complete: preloaderHide,
    success: function(data) {
      data.lectures.map(function(lecture) {
        lecture.created_at = moment(lecture.created_at);
        lecture.start = moment(lecture.start);
        lecture.end = moment(lecture.end);
      });
      lectures = data;
      renderLectures(data.lectures);
    }
  });
}

function loadStudents(callback) {
  $.ajax({
    url: apiUrl + "students",
    method: "GET",
    beforeSend: preloaderShow,
    complete: preloaderHide,
    success: function(data) {
      data.students.map(function(student) {
        student.created_at = moment(student.created_at);
      });
      students = data.students;
      callback();
    }
  });
}

function renderLectures(lectures) {
  $lectureTemplate = $("#template_lecture");
  $rowTemplate = $("#template_row");
  $("#lectures").html("");
  var groups = groupLectures(lectures);
  var emptyLecture = {
    name: "Empty",
    id: null,
    accent_color: ""
  };
  groups.map(function(group) {
    $rowTemplate.render(group).appendTo("#lectures");
    var weekDays = [
      "Monday",
      "Thuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
      "Sunday"
    ];
    weekDays.map(function(weekDay) {
      var foundLecture = group.lectures.find(function(lecture) {
        return lecture.day_of_week == weekDay;
      });
      if (foundLecture !== undefined) {
        $lectureTemplate.render(foundLecture).appendTo("#ts" + group.id);
      } else {
        $lectureTemplate.render(emptyLecture).appendTo("#ts" + group.id);
      }
    });
  });
}

function groupLectures(lectures) {
  time = lectures
    .sort((a, b) => a.start.valueOf() - b.start.valueOf())
    .map(function(lecture) {
      timestamp =
        lecture.start.format("HH:mm") + " - " + lecture.end.format("HH:mm");
      return timestamp;
    })
    .filter(function(value, index, self) {
      return self.indexOf(value) === index;
    });
  var groups = [];
  lectures.map(function(lecture) {
    var timestamp =
      lecture.start.format("HH:mm") + " - " + lecture.end.format("HH:mm");
    var foundGroup = groups.find(function(group) {
      return group.timestamp == timestamp;
    });
    if (foundGroup !== undefined) {
      foundGroup.lectures.push(lecture);
    } else {
      groups.push({
        timestamp: timestamp,
        lectures: [lecture],
        id: groups.length
      });
    }
  });
  return groups;
}

function lectureOnClick(id) {
  loadLecture(id, function() {
    lecture.timestamp =
      moment(lecture.start).format("HH:mm") +
      " - " +
      moment(lecture.end).format("HH:mm");
    lecture.capacity_str =
      lecture.students.length + "/" + lecture.student_capacity;
    $("#lectureName").html(lecture.name);
    $("#lectureTimestamp").html(lecture.timestamp);
    $("#lectureCapacityStr").html(lecture.capacity_str);
    $template = $("#template_student");
    $("#students").html("");
    lecture.students.map(function(student) {
      student.student_initials = student.student_name[0];
    });
    $template.render(lecture.students).appendTo("#students");
    $("#modalLectureStudents").modal("show");
  });
}

var lecture;
function loadLecture(id, callback) {
  $.ajax({
    url: apiUrl + "lecture",
    method: "GET",
    data: { lecture_id: id },
    beforeSend: preloaderShow,
    complete: preloaderHide,
    success: function(data) {
      lecture = data.lecture;
      callback();
    }
  });
}

function deleteStudent(student_id) {
  defaultConfirm(function() {
    $.ajax({
      url: apiUrl + "student/lecture",
      data: { student_id: student_id, lecture_id: lecture.id },
      method: "DELETE",
      beforeSend: function() {
        preloaderShow();
      },
      complete: function() {
        preloaderHide();
      },
      error: errorHandler,
      success: function(response) {
        lectureOnClick(lecture.id);
        loadLectures();
      }
    });
  });
}

function addStudent() {
  $.ajax({
    url: apiUrl + "student/lecture",
    data: { student_id: student_id, lecture_id: lecture.id },
    method: "POST",
    beforeSend: function() {
      preloaderShow();
    },
    complete: function() {
      preloaderHide();
    },
    error: errorHandler,
    success: function(response) {
      lectureOnClick(lecture.id);
      loadLectures();
    }
  });
}
