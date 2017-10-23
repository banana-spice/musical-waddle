$(document).ready(function(){
    $("p").append("Some appended text.");



  });
  
  function getText(){
    alert($('#second').text());
  }

  function stripe(){
    $("#second").toggleClass("striped");
  }
