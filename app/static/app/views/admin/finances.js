var payments = [];
var selected_payment;

$(document).ready(function() {
  loadPaymentHistory();
});

function loadPaymentHistory() {
  $.ajax({
    url: apiUrl + "student_payment_history",
    success: function(data) {
      payments = data.student_payment_history;
      renderPayments();
    }
  });
}

function renderPayments() {
  payments = payments.sort(function(a, b) {
    return moment(a.due_date) - moment(b.due_date);
  });
  $("#payments").html("");
  $template = $("#payment-template")
    .render(
      payments.map(function(payment) {
        student = payment.student;
        var accent = "primary";
        payment.status == "Pending" ? (accent = "danger") : null;
        payment.status == "Paid" ? (accent = "info") : null;
        return {
          id: payment.id,
          photo: student.photo,
          name: student.name,
          classes_per_week: student.classes_per_week,
          weeks: student.weeks,
          due_date: moment(payment.due_date).format("DD/MM/YYYY"),
          amount: payment.amount,
          status: payment.status,
          accent: accent
        };
      })
    )
    .appendTo("#payments");

  $(".student-Pending").on("click", function() {
    var payment_id = $(this).data("id");
    renderModal(payment_id);
    $("#modalPay").modal("toggle");
  });

  $(".student-Paid").on("click", function() {
    var payment_id = $(this).data("id");
    renderModal(payment_id);
    $("#modalPaid").modal("toggle");
  });
}

function renderModal(payment_id) {
  var payment = payments.find(function(payment) {
    return payment.id == payment_id;
  });
  selected_payment = payment;
  var student = payment.student;
  $(".student-name").html(student.name);
  $(".student-phone").html(student.cellphone);
  $(".student-email").html(student.email);
  $(".student-started-at").html(moment(student.created_at).format("LL"));
  $(".student-monthly-payment").html("R$ " + student.monthly_payment);
  $(".student-lectures-per-week").html(student.classes_per_week);
  $(".student-payment-date").html(moment(student.payment_date).format("DD"));
  $(".payment-id").val(selected_payment.id);
  $(".payment-amount").html("R$ " + payment.amount);
  $(".payment-date").html(
    payment.payment_date ? moment(payment.payment_date).format("LL") : ""
  );
  $(".payment-method").html(payment.payment_method);
}

function addPayment(form, event) {
  event.preventDefault();
  $form = $(form);
  var data = $form.serializeArray();
  $.ajax({
    url: apiUrl + "student_payment_history",
    data: data,
    beforeSend: preloaderShow,
    complete: preloaderHide,
    method: "POST",
    success: function(data) {
      defaultSuccess(data, function() {
        $("#modalPay").modal("toggle");
        loadPaymentHistory();
      });
    },
    error: errorHandler
  });
}

function cancelPayment(form, event) {
  event.preventDefault();
  $form = $(form);
  var data = $form.serializeArray();
  $.ajax({
    url: apiUrl + "student_payment_history",
    data: data,
    beforeSend: preloaderShow,
    complete: preloaderHide,
    method: "DELETE",
    success: function(data) {
      defaultSuccess(data, function() {
        $("#modalPaid").modal("toggle");
        loadPaymentHistory();
      });
    },
    error: errorHandler
  });
}
