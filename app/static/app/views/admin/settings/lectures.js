var lectures;

$(document).ready(function() {
  $(".dropify").dropify();
  $(".clockpicker")
    .clockpicker({
      donetext: "Done"
    })
    .find("input")
    .change(function() {});
  getLectures();
});

function createLecture(event, form) {
  event.preventDefault();
  var data = $(form).serializeArray();
  var button = $(form)
    .closest("form")
    .find(":submit");
  $.ajax({
    url: apiUrl + "lecture",
    data: data,
    method: "POST",
    beforeSend: function() {
      preloaderShow();
      buttonDisable(button);
    },
    complete: function() {
      preloaderHide();
      buttonEnable(button);
    },
    error: errorHandler,
    success: function(response) {
      defaultSuccess(response, function() {
        window.location = "/settings/lectures";
      });
    }
  });
}

function getLectures() {
  $.ajax({
    url: apiUrl + "lecture",
    method: "GET",
    beforeSend: function() {
      preloaderShow();
    },
    complete: function() {
      preloaderHide();
    },
    error: errorHandler,
    success: function(response) {
      lectures = response.lectures;
      renderLectures(response.lectures);
    }
  });
}

function renderLectures(lectures) {
  lectures.map(function(lecture) {
    lecture.start = new moment(lecture.start).format("HH:mm");
    lecture.end = new moment(lecture.end).format("HH:mm");
    lecture.created_at = new moment(lecture.created_at);
  });
  $("#template_lecture")
    .render(lectures)
    .appendTo("#lectures");
}

function deleteLectureConfirm(id) {
  Swal.fire({
    title: "Are you sure?",
    text: "You won't be able to revert this!",
    type: "warning",
    showCancelButton: true,
    confirmButtonColor: "#3085d6",
    cancelButtonColor: "#d33",
    confirmButtonText: "Yes, delete it!"
  }).then(result => {
    if (result.value) {
      deleteLecture(id);
    }
  });
}

function deleteLecture(id) {
  $.ajax({
    url: apiUrl + "lecture",
    data: { id: id },
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
        window.location = "/settings/lectures";
      });
    }
  });
}

function openModalUpdateLecture(id) {
  lecture = lectures.find(function(lecture) {
    return lecture.id == id;
  });
  $("#modalEditLecture").modal("toggle");
  $("#updateForm").values(lecture);
}

function updateLecture(event, form) {
  event.preventDefault();
  var data = $(form).serializeArray();
  var button = $(form)
    .closest("form")
    .find(":submit");
  $.ajax({
    url: apiUrl + "lecture",
    data: data,
    method: "PUT",
    beforeSend: function() {
      preloaderShow();
    },
    complete: function() {
      preloaderHide();
    },
    error: errorHandler,
    success: function(response) {
      defaultSuccess(response, function() {
        window.location = "/settings/lectures";
      });
    }
  });
}
