$(function() {

    var navbar = $("#navbar");
    var sticky = navbar.offset();

  $(window).scroll(function(){
    if ($(window).scrollTop() >= sticky.top) {
      navbar.addClass("sticky")
    } else {
      navbar.removeClass("sticky");
    }
  })

});