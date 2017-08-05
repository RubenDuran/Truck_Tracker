// $('.ui.checkbox')
//     .checkbox();
$(document).ready(function() {
    console.log("ready!");
    $(".regBtn").click(function() {
        console.log("reg clicked");
        // ui.basic.modal.
        $('#reg')
            .modal('show');
    });
    $("#cancel").click(function() {
        $('#reg')
            .modal('hide')
    });

    $(".loginBtn").click(function() {
        $('#login')
            .modal('show');
    });
    $("#cancelBtn").click(function() {
        $('#login')
            .modal('hide')
    });

    $(".cancelBtn").click(function() {
        $('#login')
            .modal('show')
    });
});
