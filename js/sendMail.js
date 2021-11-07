$(function () {

    $('#send').on('click', function () {
        var username = $("#username").val();
        var email = $("#useremail").val();
        var message = $("#mail").val();
        if (validateMail(email)) {
            if (message != "") {
                $.post({
                    url: "http://127.0.0.1:5000/sendEmail",
                    datatype: "json",
                    data: { username: username, email: email, message: message },
                    success: checkMessageResponse,
                    error: function () {
                        printErrorMessage("AJAX Request Error")
                    }
                });
            } else printErrorMessage("Message could not be empty");
        } else printErrorMessage("Your mail is not valid");
    });
});

function checkMessageResponse(json) {
    if (json.errMsg) {
        printErrorMessage(json.errMsg);
    }
    else {
        printSuccessMessage("Message successfully sent");
        $("#mail").val('');
        var username = $("#username").val('');
        var email = $("#useremail").val('');
    }
}

function validateMail(email) {
    const re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return email.match(re);
}