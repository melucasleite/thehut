var lectures;
$(document).ready(function() {
  loadLectures();
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

function lectureOnClick() {
  $("#modalLectureStudents").modal("toggle");
}
