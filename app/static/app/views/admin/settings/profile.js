$(document).ready(function() {
  $(".dropify").dropify();
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
