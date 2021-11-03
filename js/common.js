let arrow;
$(function() {

    var navbar = $("#navbar");
    var sticky = navbar.offset();

    $(window).scroll(function(){
      scrollFunction();
      if ($(window).scrollTop() >= sticky.top) {
        navbar.addClass("stick")
      } else {
        navbar.removeClass("stick");
      }
    });

  arrow=$("<span id='arrow'><img src="+"../resources/img/fi-rr-angle-up.svg"+" alt='Top'></span>");
  $('footer').before(arrow);

  const barContainer= Array.from($("#barContainer .bar"));
  const body=$("body")
  let modal=null;

  $("#barContainer").on('click', function(){
    hamburger(barContainer,null,null,true);
    if(modal === null){
      modal=$("<div id ='modal'><div id='menuMobile'><a href='./index.php'><span>Home</span></a><a href='./install.php'><span>Install</span></a><a href='./documentation.php'><span>Documentation</span></a><a href='./learn.php'><span>Learn</span></a><a href='./contribute.php'><span>Contribute</span></a></div></div>");
      $('#separator').after(modal);
      body.css("overflow","hidden");
    }else{
      $(modal).remove();
      modal=null;
      body.css("overflow","auto");
    }
  });

  window.onclick = function(event) {
    if(modal !== null){
        if (event.target === modal[0]) {
          $(modal).remove();
          modal=null;
          body.css("overflow","auto");
          hamburger(barContainer,null,null,true);
        }
    }
  };

  $("#barContainer").mouseover(function(){
    hamburger(barContainer,"background-color","#0071b8",false);
   });

   $("#barContainer").mouseout(function(){
     hamburger(barContainer,"background-color","#02588e",false);
   });

  arrow.click(function(){
    $('html, body').animate({
      scrollTop: $(".header").offset().top
    },500);
  })

});

function hamburger(barContainer,property,value,toggle){
  if(toggle){ 
    barContainer.forEach(bar => {
      $(bar).toggleClass("open");
    });
  }else if(property !== null && value !==null){
    barContainer.forEach(bar => {
      $(bar).css(property,value);
    });
  }
}

function scrollFunction() {
if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
  arrow.css("display","block");
} else{
  arrow.css("display","none");
}
}
