list = ["Grammar", "Vocabulary", "Listening", "Reading", "Writing"];
var skills, remarks;
$(document).ready(function() {
  loadSkills();
  loadRemarks();
});

function loadSkills() {
  $.ajax({
    url: apiUrl + "skill",
    success: function(data) {
      skills = data.skills;
      skills.length > 0 ? $("#noSkills").hide() : $("#noSkills").show();
      $("#skills").html("");
      $("#skill_template")
        .render(skills)
        .appendTo("#skills");
    }
  });
}

function loadRemarks() {
  $.ajax({
    url: apiUrl + "remark",
    success: function(data) {
      remarks = data.remarks;
      remarks.length > 0 ? $("#noRemarks").hide() : $("#noRemarks").show();
      $("#remarks").html("");
      $("#remark_template")
        .render(remarks)
        .appendTo("#remarks");
    }
  });
}

function addSkill(event, form) {
  event.preventDefault();
  var data = $(form).values();
  $.ajax({
    url: apiUrl + "skill",
    method: "POST",
    data: data,
    success: function(data) {
      defaultSuccess(data, function() {
        loadSkills();
        $(form).trigger("reset");
      });
    },
    error: errorHandler
  });
}

function addRemark(event, form) {
  event.preventDefault();
  var data = $(form).values();
  $.ajax({
    url: apiUrl + "remark",
    method: "POST",
    data: data,
    success: function(data) {
      defaultSuccess(data, function() {
        loadRemarks();
        $(form).trigger("reset");
      });
    },
    error: errorHandler
  });
}

function deleteSkill(id) {
  defaultConfirm(function() {
    $.ajax({
      url: apiUrl + "skill",
      method: "DELETE",
      data: { id: id },
      error: errorHandler,
      success: function(data) {
        defaultSuccess(data, function() {
          loadSkills();
        });
      }
    });
  });
}

function deleteRemark(id) {
  defaultConfirm(function() {
    $.ajax({
      url: apiUrl + "remark",
      method: "DELETE",
      data: { id: id },
      error: errorHandler,
      success: function(data) {
        defaultSuccess(data, function() {
          loadRemarks();
        });
      }
    });
  });
}
