$(document).ready(function() {
  $(".dropify").dropify({
    defaultFile: AppState.user.photo
  });
});

function updateProfile(event, form) {
  event.preventDefault();
  var data = $(form).serializeArray();
  var button = $(form)
    .closest("form")
    .find(":submit");
  $.ajax({
    url: apiUrl + "user/profile",
    data: data,
    method: "PUT",
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
        window.location = "/settings/profile";
      });
    }
  });
}

function uploadFile(event, form) {
  event.preventDefault();
  $.ajax({
    type: "POST",
    url: apiUrl + "bucket",
    data: new FormData(form),
    dataType: "json",
    contentType: false,
    cache: false,
    processData: false,
    beforeSend: function() {
      preloaderShow();
    },
    complete: function() {
      preloaderHide();
    },
    success: function(response) {
      $("#image_url").val(response.url);
    }
  });
}
