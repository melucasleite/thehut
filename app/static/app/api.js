var apiUrl = "http://localhost:5000/api/";
var defaultApiError = "Occoreu um erro com sua solicitação.";
var applicationError = "Erro na aplicação. Entre em contato com o suporte.";
var connectionApiError =
  "Erro de conexão com o servidor. Verifique sua conexão de internet. Caso esteja on-line. Entre em contato com o suporte.";

function errorHandler(data) {
  if (data.readyState == 4) {
    try {
      message = data.responseJSON.message;
      Swal.fire("Error", message, "error");
    } catch {
      Swal.fire("Error", defaultApiError, "error");
    }
  } else if (data.readyState == 0) {
    Swal.fire("Error", connectionApiError, "error");
  } else {
    Swal.fire("Error", applicationError, "error");
  }
}

function loginRedirect(data) {
  window.location.href = "/"
}
