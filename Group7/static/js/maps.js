function display(borough){
    $("#image").attr("src", $(borough).attr("src"));
}

$(document).ready(function(){
    if ($("#Borough").val() == "Manhattan"){
	display("#manhattan");
    }
    if ($("#Borough").val() == "Brooklyn"){
	display("#brooklyn");
    }
    if ($("#Borough").val() == "Queens"){
	display("#brooklyn");
    }
    if ($("#Borough").val() == "Bronx"){
	display("#brooklyn");
    }
    if ($("#Borough").val() == "Staten Island"){
	display("#staten");
    }
});