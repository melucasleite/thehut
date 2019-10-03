var payments = [];

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
  console.log(payments);
  payments = payments.sort(function(a, b) {
    return moment(a.due_date) - moment(b.due_date);
  });
  $template = $("#payment-template")
    .render(
      payments.map(function(payment) {
        student = payment.student;
        return {
          photo: student.photo,
          name: student.name,
          classes_per_week: student.classes_per_week,
          weeks: student.weeks,
          due_date: moment(payment.due_date).format("DD/MM/YYYY"),
          amount: payment.amount,
          status: payment.status
        };
      })
    )
    .appendTo("#payments");
  $(".student-Pending").on("click", function() {
    $("#modalPay").modal("toggle");
  });
  $(".student-Paid").on("click", function() {
    $("#modalPaid").modal("toggle");
  });
}
