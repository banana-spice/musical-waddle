var myName = "<h2>Vicky</h2>";
var stitchImage = "stitchMad.png";
var theSwitch = 0;

function toggleImage(){
	var newSrc;
	if (theSwitch == 1){
		newSrc = "stitchSweet.png";
		theSwitch = 0;
	} else {
		newSrc = "stitchMad.png";
		theSwitch = 1;
	}
	document.getElementById('stitch').src = newSrc;
}

function changeImage(){
	document.getElementById('stitch').src = stitchImage;
}

function changeImageMad(stitchImg){
	document.getElementById('stitch').src = stitchImg;
}