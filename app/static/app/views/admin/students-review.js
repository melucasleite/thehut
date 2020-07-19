var lecture_history_student,
    review = {};
var lectures, selected_lecture, selected_student, selected_students;
var skills, remarks;
$(document).ready(function () {
    $.ajax({
        url: apiUrl + "lecture_history_student",
        success: function (data) {
            lecture_history_student = data.lectures_history_student;
            renderLectures(lecture_history_student);
        },
        error: errorHandler
    });
    $.ajax({
        url: apiUrl + "skill",
        success: function (data) {
            skills = data.skills;
            renderSkills(skills);
        },
        error: errorHandler
    });
    $.ajax({
        url: apiUrl + "remark",
        success: function (data) {
            remarks = data.remarks;
            renderRemarks(remarks);
        },
        error: errorHandler
    });
});

function groupLectures(lecture_history_students) {
    lectures = [];
    lecture_history_students = lecture_history_students.sort(function (a, b) {
        return moment(a.lecture.start) - moment(b.lecture.start);
    });
    lecture_history_students.map(function (lecture_history_student) {
        found_lecture = lectures.find(function (lecture) {
            return (
                lecture_history_student.lecture.id == lecture.id &&
                lecture.date == lecture_history_student.date
            );
        });
        lecture_history_student.student.lecture_history_student_id =
            lecture_history_student.id;
        if (found_lecture) {
            found_lecture.students.push(lecture_history_student.student);
        } else {
            lectures.push({
                id: lecture_history_student.lecture.id,
                date: lecture_history_student.date,
                lecture: lecture_history_student.lecture,
                students: [lecture_history_student.student]
            });
        }
    });
    return lectures;
}

function renderLectures(lecture_history_student) {
    if (lecture_history_student.length == 0) {
        $("#no-review-card").show();
        $("#review-card").hide();
    } else {
        $("#no-review-card").hide();
        $("#review-card").show();
    }
    $template = $("#lecture-template");
    $("#lectures").html("");
    lectures = groupLectures(lecture_history_student);
    lectures.map(function (lecture, index) {
        lecture.lecture_name = "[{0}] [{1} - {2}] {3}".format(
            lecture.lecture.day_of_week,
            moment(lecture.lecture.start).format("HH:mm"),
            moment(lecture.lecture.end).format("HH:mm"),
            lecture.lecture.name
        );
        lecture.index = index;
        lecture.date_str = moment(lecture.date).format("DD/MM");
    });
    $template.render(lectures).appendTo("#lectures");
}

function openModalLectureReview(index) {
    selected_lecture = lectures[index];
    selected_students = selected_lecture.students;
    selected_student = selected_students[0];
    renderStudent();
    $("step1").show();
    $("step2").hide();
    $("step3").hide();
    $("step4").hide();
    $("#modalLectureReview").modal("show");
}

function renderStudent() {
    $(".student-name").html(selected_student.name);
    $(".student-photo").attr("src", selected_student.photo);
    $(".lecture-name").html(selected_lecture.lecture.name);
    $(".lecture-date").html(moment(selected_lecture.date).format("DD/MM"));
    $(".lecture-time").html(
        "{0} - {1}".format(
            moment(selected_lecture.lecture.start).format("HH:mm"),
            moment(selected_lecture.lecture.end).format("HH:mm")
        )
    );
}

function next1(present) {
    review = {skills: [], remarks: [], comment: ""};
    review.present = present;
    review.lecture_history_student_id =
        selected_student.lecture_history_student_id;
    console.log(review);
    if (!present) {
        next4();
    } else {
        $("#step1").hide();
        $("#step2").show();
    }
}

function next2() {
    $selectedStars = $(".skill-star.selected");
    var rated_skills = $selectedStars
        .map(function () {
            $star = $(this);
            return {
                skill_id: $star.data("skillid"),
                value: $star.data("value")
            };
        })
        .get();
    if (skills.length > rated_skills.length) {
        Swal.fire({
            title: "Error",
            text: "You have to rate all the skills.",
            timer: 2000,
            type: "error"
        });
        return;
    }
    review.skills = rated_skills;
    $("#step2").hide();
    $("#step3").show();
}

function next3() {
    var toImprove = $(".to-improve:checked")
        .map(function () {
            $checkbox = $(this);
            return {
                remark_id: $checkbox.data("id"),
                positive: false
            };
        })
        .get();
    var strenght = $(".strenght:checked")
        .map(function () {
            $checkbox = $(this);
            return {
                remark_id: $checkbox.data("id"),
                positive: true
            };
        })
        .get();
    review.remarks = toImprove.concat(strenght);
    $("#step3").hide();
    $("#step4").show();
}

function next4() {
    review.comment = $("#comment").val();
    $.ajax({
        url: apiUrl + "student/review",
        method: "POST",
        data: {
            present: review.present,
            lecture_history_student_id: review.lecture_history_student_id,
            skills: JSON.stringify(review.skills),
            remarks: JSON.stringify(review.remarks),
            comment: review.comment
        },
        beforeSend: preloaderShow,
        complete: preloaderHide,
        success: function (data) {
            defaultSuccess(data, function () {
                nextStudent();
                $("#step4").hide();
                $("#step1").show();
            });
        },
        error: errorHandler
    });
}

function nextStudent() {
    selected_students = selected_students.filter(function (selected_student) {
        return (
            selected_student.lecture_history_student_id !=
            review.lecture_history_student_id
        );
    });

    if (selected_students.length > 0) {
        selected_student = selected_students[0];
    } else {
        window.location = "/students/review";
    }
    selected_lecture.students = selected_students;
    renderStudent();
    $(".skill-star")
        .removeClass("selected fas")
        .addClass("far");
    renderRemarks(remarks);
    $("#comment").val("");
}

function renderSkills(skills) {
    $("#skills").html("");
    $template = $("#skill-template")
        .render(skills)
        .appendTo("#skills");
}

function skillClick(e) {
    var $clickedStar = $(e);
    var value = $clickedStar.data("value");
    var skillId = $clickedStar.data("skillid");
    var $allStars = $('*[data-skillid="' + skillId + '"]');
    $allStars.removeClass("fas selected");
    $clickedStar.addClass("selected");
    $allStars.addClass("far");
    $allStars
        .filter(function () {
            return $(this).data("value") <= value;
        })
        .removeClass("far")
        .addClass("fas");
}

function renderRemarks(remarks) {
    $("#remarks").html("");
    $template = $("#remark-template")
        .render(remarks)
        .appendTo("#remarks");
}
