function fillEventsBefore(Borough,Month,Day,Year){
    var stuff ={}
    stuff.Month=Month
    stuff.Day=Day
    stuff.Year=Year
    stuff.Borough=Borough
    $.getJSON("/get_e_before",stuff,function(data){
	var l=$("#events");
	var event=$("<p>Events")
	$(l).append(event);
	for (var i in data){
	    //console.log(i);
	    var name="<h2>"+data[i][8]+"</h2>";
	    var d="<p>Description: "+data[i][10];
	    var dte="<p>Date: "+data[i][12];
	    var loc="<p>Location: "+data[i][18];
	    event=$("<li></li>");
	    event.append(name);
	    event.append(d);
	    event.append(dte);
	    event.append(loc);
	    $(event).css('color','gray');
	    $(l).append(event);
	}
    });
};

function fillEventsOn(Borough,Month,Day,Year){
    var stuff ={}
    stuff.Month=Month
    stuff.Day=Day
    stuff.Year=Year
    stuff.Borough=Borough
    $.getJSON("/get_e_on",stuff,function(data){
	//console.log("here");
	var l=$("#events");
	l.empty();
	var event=$("<p>Events")
	$(l).append(event);
	for (var i in data){
	    //console.log(i);
	    var name="<h2>"+data[i][8]+"</h2>";
	    var d="<p>Description: "+data[i][10];
	    var dte="<p>Date: "+data[i][12];
	    var loc="<p>Location: "+data[i][18];
	    event=$("<li></li>");
	    event.append(name);
	    event.append(d);
	    event.append(dte);
	    event.append(loc);
	    $(event).css('color','red');
	    $(l).append(event);
	}
    });
    fillEventsAfter(Borough,Month,Day,Year);
};

function fillEventsAfter(Borough,Month,Day,Year){
    var stuff ={}
    stuff.Month=Month
    stuff.Day=Day
    stuff.Year=Year
    stuff.Borough=Borough
    $.getJSON("/get_e_after",stuff,function(data){
	var l=$("#events");
	var event=$("<p>Events")
	$(l).append(event);
	for (var i in data){
	    var name="<h2>"+data[i][8]+"</h2>";
	    var d="<p>Description: "+data[i][10];
	    var dte="<p>Date: "+data[i][12];
	    var loc="<p>Location: "+data[i][18];
	    event=$("<li></li>");
	    event.append(name);
	    event.append(d);
	    event.append(dte);
	    event.append(loc);
	    $(event).css('color','blue');
	    $(l).append(event);
	}
    });
    fillEventsBefore(Borough,Month,Day,Year);
};
function varyB(data){
    var borough="";
    borough=$(this).val();
    var month=$("select[name='Month']").val();
    var day=$("select[name='Day']").val();
    var year=$("select[name='Year']").val();
    fillEventsOn(borough,month,day,year);
}
function varyM(data){
    var month="";
    month =$(this).val();
    var borough=$("#Borough").val();
    var day=$("select[name='Day']").val();
    var year=$("select[name='Year']").val();
    fillEventsOn(borough,month,day,year);
}
function varyD(data){
    var day="";
    day=$(this).val();
    var month=$("select[name='Month']").val();
    var borough=$("#Borough").val();
    var year=$("select[name='Year']").val();
    fillEventsOn(borough,month,day,year);
}
function varyY(data){
    var year="";
    year=$(this).val();
    var month=$("select[name='Month']").val();
    var day=$("select[name='Day']").val();
    var borough=$("#Borough").val();
    fillEventsOn(borough,month,day,year);
}
function loadEvents(){
    $("#Borough").change(varyB);
}
function DateTime(){
    $("select[name='Month']").change(varyM);
    $("select[name='Day']").change(varyD);
    $("select[name='Year']").change(varyY);
}
$(document).ready(function(){
    loadEvents();
    DateTime();
});

/*
function colorize(data){
    if (date.substring(6,8)>year){
	event.attr("class","blue");
    }
    else if (date.substring(6,8)==year){
	if (date.substring(0,2)>month){
	    event.attr("class","blue");
	}
	else if (date.substring(0,2)==month){
	    if (date.substring(3,5)==day){
		event.attr("class","red");
	    }
	    else if (date.substring(3,5)>day){
		event.attr("class","blue");
	    }
	};
    }
    else 
    {
	event.attr("class","gray");
    }
}
*/


/*
  function showWithDates(){
  var borough=$("#Borough").val();
    var month=$("select[name='Month']").val();
    var day=$("select[name='Day']").val();
    var year=$("select[name='Year']").val();
    displayAfter(month,day,year);
    //displayOn(month,day,year,borough);
    }

    /*
      $.getJSON("/get_e_after",{Borough:Borough,Month:Month,Day:Day,Year:Year},function(data){
      $("blue").empty();
      var l=$("#events"); //not sure what the id for where events will go is
	console.log(l)
	for (var i in l){
	for (var d in data){
	if (i==d){
	$(data[d]).attr("class","");
	$(data[d]).attr("class","blue");
	};
	};
	};
	});
    */
/*
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
*/
