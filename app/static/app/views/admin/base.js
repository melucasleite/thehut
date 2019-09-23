$(document).ready(function() {
  $(".user-name").html(AppState.user.name);
  $(".user-name").val(AppState.user.name);
  $(".user-email").html(AppState.user.email);
  $(".user-email").val(AppState.user.email);
  $(".user-cellphone").html(AppState.user.cellphone);
  $(".user-cellphone").val(AppState.user.cellphone);
});
