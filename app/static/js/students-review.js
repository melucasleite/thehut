$(".check-lecture").on("click", function(e) {
  console.log($(this).data("id"));
  $("#modalLectureReview").modal("toggle");
});

function next1() {
  $("#step1").hide();
  $("#step2").show();
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
