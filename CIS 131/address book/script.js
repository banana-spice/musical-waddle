/*Author: Victoria Braden
Date: 10.30.2017
file: script.js
*/

$(document).ready(function(){
	$("#neb1").click(function(){
		$("#contact1").slideToggle("slow", function(){
			$("#pics").attr("src","images/dojo.png");
		});
	});
});

$(document).ready(function(){
	$("#neb2").click(function(){
		$("#contact2").slideToggle("slow", function(){
			$("#pics").attr("src","images/jacko.png");			
		});
	});
});

$(document).ready(function(){
	$("#neb3").click(function(){
		$("#contact3").slideToggle("slow", function(){
			$("#pics").attr("src","images/jermaine.png");	
		});
	});
});