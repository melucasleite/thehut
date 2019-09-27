$(document).ready(function() {
  getLevels();
});

function addLevel(event, form) {
  event.preventDefault();
  var data = $(form).serializeArray();
  var button = $(form)
    .closest("form")
    .find(":submit");
  $.ajax({
    url: apiUrl + "level",
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
        window.location = "/settings/level";
      });
    }
  });
}

function getLevels() {
  $.ajax({
    url: apiUrl + "level",
    method: "GET",
    beforeSend: function() {
      preloaderShow();
    },
    complete: function() {
      preloaderHide();
    },
    error: errorHandler,
    success: function(data) {
      levels = data.levels;
      renderLevels(levels);
    }
  });
}

function renderLevels(levels) {
  $template = $("#level_template");
  $template.render(levels).appendTo("#levels");
}

function deleteLevelConfirm(id) {
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
      deleteLevel(id);
    }
  });
}

function deleteLevel(id) {
  $.ajax({
    url: apiUrl + "level",
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
        window.location = "/settings/level";
      });
    }
  });
}
