var $lectureRange = $("#lectureRange");
var $lectureCount = $(".lectureCount");
var $weekRange = $("#weekRange");
var $weekCount = $("#weekCount");
var $monthCost = $("#monthCost");
var $weekCost = $("#weekCost");
var $lectureCost = $("#lectureCost");
var $totalCost = $("#totalCost");
var weeks, lecturesPerWeek, monthCost, weekCost, totalCost, lectureCost;
var lectures = [],
  levels = [];
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
  loadLevels();
});

function refresh() {
  weeks = $weekRange.val();
  lecturesPerWeek = $lectureRange.val();
  $lectureCount.html(lecturesPerWeek);
  $weekCount.html(weeks);
  var costBase = priceWeekBase.intermediate;
  var plan = levels.find(function(level) {
    return level.id == student.level;
  });
  if (plan !== undefined) {
    costBase = priceWeekBase[plan.name.toLowerCase()];
  }
  totalCost = costBase[weeks] + 20 * (lecturesPerWeek - 3) * weeks;
  weekCost = totalCost / weeks;
  monthCost = weeks > 3 ? weekCost * 4.43 : totalCost;
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
  advanced: {
    "1": 73,
    "2": 144,
    "3": 213,
    "4": 280,
    "5": 345,
    "6": 408,
    "7": 469,
    "8": 528,
    "9": 586,
    "10": 642,
    "11": 696,
    "12": 749,
    "13": 800,
    "14": 849,
    "15": 897,
    "16": 943,
    "17": 987,
    "18": 1031,
    "19": 1073,
    "20": 1113,
    "21": 1152,
    "22": 1190,
    "23": 1226,
    "24": 1261,
    "25": 1295,
    "26": 1328
  },
  intermediate: {
    "1": 66,
    "2": 130,
    "3": 192,
    "4": 253,
    "5": 312,
    "6": 369,
    "7": 424,
    "8": 478,
    "9": 530,
    "10": 580,
    "11": 629,
    "12": 677,
    "13": 723,
    "14": 767,
    "15": 811,
    "16": 852,
    "17": 893,
    "18": 932,
    "19": 970,
    "20": 1006,
    "21": 1042,
    "22": 1076,
    "23": 1109,
    "24": 1140,
    "25": 1171,
    "26": 1201
  },
  fundamentals: {
    "1": 60,
    "2": 118,
    "3": 175,
    "4": 230,
    "5": 283,
    "6": 335,
    "7": 386,
    "8": 434,
    "9": 482,
    "10": 528,
    "11": 572,
    "12": 615,
    "13": 657,
    "14": 698,
    "15": 737,
    "16": 775,
    "17": 812,
    "18": 847,
    "19": 882,
    "20": 915,
    "21": 947,
    "22": 978,
    "23": 1008,
    "24": 1037,
    "25": 1065,
    "26": 1092
  }
};

// $("#step1").hide();
// $("#step2").hide();
// $("#step3").hide();
// $("#step4").hide();
// $("#step5").hide();
// $("#step6").hide();
// $("#step8").hide();

function next0(id) {
  student.level = id;
  refresh();
  $("#step0").fadeOut(function() {
    $("#step1").fadeIn();
  });
}

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
      "Tuesday",
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

function loadLevels() {
  $.ajax({
    url: apiUrl + "level",
    method: "GET",
    success: function(data) {
      levels = data.levels;
      renderLevels(data.levels);
    }
  });
}

function renderLevels(levels) {
  $template = $("#template_level");
  $template.render(levels).appendTo("#levels");
}
