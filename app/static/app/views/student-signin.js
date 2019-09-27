var $lectureRange = $("#lectureRange");
var $lectureCount = $(".lectureCount");
var $weekRange = $("#weekRange");
var $weekCount = $("#weekCount");
var $monthCost = $("#monthCost");
var $weekCost = $("#weekCost");
var $lectureCost = $("#lectureCost");
var $totalCost = $("#totalCost");
var weeks, lecturesPerWeek, monthCost, weekCost, totalCost, lectureCost;
var lectures = [];
$selectedLectures = $(".lecture-td.active");
$selectedCount = $(".selectedCount");
var selectedLectures;

var $next2 = $("#next2");
var student = {
  name: "",
  cellphone: "",
  photo: "",
  classes_per_week: "",
  weeks: "",
  level: "",
  monthly_payment: "",
  lectures: []
};

$(function() {
  refresh();
  loadLectures();
});

function refresh() {
  weeks = $weekRange.val();
  lecturesPerWeek = $lectureRange.val();
  $lectureCount.html(lecturesPerWeek);
  $weekCount.html(weeks);

  totalCost = priceWeekBase[weeks] + 20 * (lecturesPerWeek - 3) * weeks;
  weekCost = totalCost / weeks;
  monthCost = weeks > 3 ? weekCost * 4 : totalCost;
  lectureCost = weekCost / lecturesPerWeek;

  $weekCost.text(Math.round(weekCost));
  $monthCost.text(Math.round(monthCost));
  $totalCost.text(Math.round(totalCost));
  $lectureCost.text(Math.round(lectureCost));

  selectedLectures = $(".lecture-td.active").length;
  $selectedCount.text(selectedLectures);
  if (selectedLectures < lecturesPerWeek) {
    $next2.attr("disabled", true);
    $selectedCount.addClass("text-info");
  } else if (selectedLectures > lecturesPerWeek) {
    $next2.attr("disabled", true);
    $selectedCount.addClass("text-danger");
  } else {
    $next2.attr("disabled", false);
    $selectedCount.removeClass("text-info");
    $selectedCount.removeClass("text-danger");
  }
}

$lectureRange.on("input", function() {
  refresh();
});

$weekRange.on("input", function() {
  refresh();
});

var priceWeekBase = {
  "1": 90,
  "2": 175,
  "3": 260,
  "4": 340,
  "5": 420,
  "6": 495,
  "7": 565,
  "8": 640,
  "9": 710,
  "10": 775,
  "11": 840,
  "12": 905,
  "13": 965,
  "14": 1025,
  "15": 1085,
  "16": 1140,
  "17": 1190,
  "18": 1245,
  "19": 1300,
  "20": 1345,
  "21": 1390,
  "22": 1435,
  "23": 1480,
  "24": 1525
};

// $("#step1").hide();
// $("#step2").hide();
// $("#step3").hide();
// $("#step4").hide();
// $("#step5").hide();
// $("#step6").hide();
// $("#step8").hide();

function next1() {
  student.monthly_payment = $("#monthCost").html();
  student.weeks = $("#weekCount").html();
  student.classes_per_week = lecturesPerWeek;
  $("#step1").fadeOut(function() {
    $("#step2").fadeIn();
  });
}

function next2() {
  student.lectures = $(".lecture-td.active")
    .map(function() {
      return $(this).data("id");
    })
    .get();
  $("#step2").fadeOut(function() {
    $("#step3").fadeIn();
    $("#name").focus();
  });
}
function next3() {
  student.name = $("#name").val();
  $("#step3").fadeOut(function() {
    $("#step4").fadeIn();
    $("#email").focus();
  });
}
function next4() {
  student.email = $("#email").val();
  $("#step4").fadeOut(function() {
    $("#step5").fadeIn();
    $("#cellphone").focus();
  });
}
function next5() {
  student.cellphone = $("#cellphone").val();
  $("#step5").fadeOut(function() {
    $("#step6").fadeIn();
  });
}
function next6() {
  student.photo = $("#photo").val();
  $("#step6").fadeOut(function() {
    $("#step7").fadeIn();
  });
}
function next7() {
  createStudent(student);
}

function back1() {
  $("#step2").fadeOut(function() {
    $("#step1").fadeIn();
  });
}

$(".lecture-td").on("click", lectureOnClick);

function lectureOnClick(el) {
  if (selectedLectures < lecturesPerWeek) {
    $(el).toggleClass("active");
  } else {
    $(el).removeClass("active");
  }
  refresh();
}

$(document).ready(function() {
  // Basic
  $(".dropify").dropify();
});

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
      $("#photo").val(response.url);
    }
  });
}

function createStudent(student) {
  var data = JSON.parse(JSON.stringify(student));
  data.lectures = JSON.stringify(data.lectures);
  $.ajax({
    url: apiUrl + "student",
    data: data,
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
        $("#main-wrapper").fadeOut(function() {
          $("#step8").fadeIn();
        });
      });
    }
  });
}

function loadLectures() {
  $.ajax({
    url: apiUrl + "lecture",
    method: "GET",
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

function renderLectures(lectures) {
  $lectureTemplate = $("#template_lecture");
  $rowTemplate = $("#template_row");
  var groups = groupLectures(lectures);
  var emptyLecture = {
    name: "Vazio",
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
