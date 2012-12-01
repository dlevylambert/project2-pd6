function fillEvents(Borough){
    $.getJSON("/get_events",{Borough:Borough},function(data){
	var l=$("#events") //not sure what the id for where events will go is
	var event=$("<p>Events")
	$(l).append(event);
	for (var i in data){
	    var name=$("<p>"+data[i][8]);
	    var d=$("<p>"+data[i][10]);
	    var date=$("<p>"+data[i][12]);
	    var loc=$("<p>"+data[i][18]);
	    event=$("<li></li>");
	    event.append(name);
	    event.append(d);
	    event.append(date);
	    event.append(loc);
	    event.attr("class","gray")
	    l.append(event)
	}
    });
};

function displayAfter(Month,Day,Year,Borough){
    $.getJSON("/get_e_after",{Borough:Borough,Month:Month,Day:Day,Year:Year},function(data){
	$("blue").empty();
	var l=$("#events"); //not sure what the id for where events will go is
	for (var i in l){
	    for (var d in data){
		if (i==d){
		    $(data[d]).attr("class","");
		    $(data[d]).attr("class","blue");
		};
	    };
	};
    });
}

function displayOn(Month,Day,Year,Borough){
    $.getJSON("/get_e_on",{Borough:Borough,Month:Month,Day:Day,Year:Year},function(data){
	$("red").empty();
	var l=$("#events"); //not sure what the id for where events will go is
	for (var i in l){
	    for (var d in data){
		if (i==d){
		    $(data[d]).attr("class","");
		    $(data[d]).attr("class","red");
		};
	    };
	};
    });
}

function showEvents(){
    var borough=$("#Borough").val();
    fillEvents(borough);
}

function showWithDates(){
    var borough=$("#Borough").val();
    var month=$("select[name='Month']").val();
    var day=$("select[name='Day']").val();
    var year=$("select[name='Year']").val();
    displayAfter(month,day,year,borough);
    displayOn(month,day,year,borough);
}

$(document).ready(function(){
    $("#Go").click(showEvents())
    $("#Update").click(showWithDates()) //not sure what name of button to customize date is