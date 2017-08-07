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

    $("#tc").keyup(function(e) {
        var tcInput = this.value;
        console.log("testing",tcInput);

        e.preventDefault()
        $.ajax({
            url: '/search',
            method: 'GET',
            data: $(this).serialize(),
            success: function(serverResponse) {
                // console.log("Received this from server: ", serverResponse)
                $('.theSearch').html(serverResponse)
            }
        })

    })


});
