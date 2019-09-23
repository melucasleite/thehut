console.log("Blessed be the name of the LORD From this time forth and forever.")
var state = {{ state|tojson }};
$(document).ready(function(){
    $(".user-name").html(state.user.name);
    $(".user-name").val(state.user.name);
    $(".user-email").html(state.user.email);
    $(".user-email").val(state.user.email);
    $(".user-cellphone").html(state.user.cellphone);
    $(".user-cellphone").val(state.user.cellphone);
})