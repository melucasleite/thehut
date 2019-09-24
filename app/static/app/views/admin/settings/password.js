function updatePassword(event, form) {
  event.preventDefault();
  var data = $(form).serializeArray();
  var button = $(form)
    .closest("form")
    .find(":submit");
  $.ajax({
    url: apiUrl + "user/password",
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
        window.location = "/settings/password";
      });
    }
  });
}
