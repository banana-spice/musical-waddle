
   var daysOfWeek = ["Sunday", "Monday", "Tues", "Wednesday", "Thursday", "Friday", "Saturday"];
   var opponents = ["Lightening", "Combines", "Combines", "Combines", "Lightening", "Lightening", "Lightening", "Lightening", "Barn Raisers", "Barn Raisers", "Barn Raisers", "Sodbusters", "Sodbusters", "Sodbusters", "Sodbusters", "(off)",
                   "River Riders", "River Riders", "River Riders", "Big Dippers", "Big Dippers", "Big Dippers", "(off)", "Sodbusters", "Sodbusters", "Sodbusters", "Combines", "Combines", "Combines", "(off)", "(off)"];
  var gameLocation = ["away", "away","away", "away", "home", "home","home", "home","home", "home", "home", "away","away", "away","away", "", "away", "away","away","away",
                     "away","away", "", "home",
                     "home", "home","home", "home", "home", "",""];

function addColumnHeaders(){
  var i = 0;
  while (i < 7){
    document.getElementsByTagName("th")[i].innerHTML = daysOfWeek[i];
    i++;
  }
}

function addCalendarDates(){
  var i = 1;
  var paragraphs = "";
  do {
    var tableCell = document.getElementById("08-" + i);
    paragraphs = tableCell.getElementsByTagName("p");
    paragraphs[0].innerHTML = i;
    i++;
  } while (i <= 31);
}

function addGameInfo(){
  var paragraphs="";
  for (var i = 0; i < 31; i++){

      var date = i + 1;
      var tableCell = document.getElementById("08-" + date);
      paragraphs = tableCell.getElementsByTagName("p");

      // if (gameLocation[i] === "away"){
      //   paragraphs[1].innerHTML = "@ ";
      // } else{
      //   paragraphs[1].innerHTML += "vs ";
      //
      // }// end if

      switch (gameLocation[i]){
        case "away":
            paragraphs[1].innerHTML = "@ ";
          break;
        case "home":
            paragraphs[1].innerHTML = "vs ";
          break;


      }



      paragraphs[1].innerHTML += opponents[i];
  }// end for
}// end function addGameInfo()

function setUpPage(){
  addColumnHeaders();
  addCalendarDates();
  addGameInfo();
}
window.addEventListener("load", setUpPage, false);
