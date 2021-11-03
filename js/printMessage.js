function printErrorMessage(string){
    var message = $("#message");
    message.css("background-color", "firebrick");
    message.text(string);
    message.addClass("show");
    setTimeout(function(){
        message.removeClass("show");
        message.text("")}, 3000);
}

function printSuccessMessage(string){
    var message = $("#message");
    message.css("background-color", "forestGreen");
    message.text(string);
    message.addClass("show");
    setTimeout(function(){
        message.removeClass("show");
        message.text("")}, 3000);
}