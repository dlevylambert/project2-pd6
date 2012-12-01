function fillEvents(Borough,month,day,year){
    $.getJSON("/get_events",{Borough:Borough},function(data){
	var l=$("#events") //not sure what the id for where events will go is
	var event=$("<p>Events")
	$(l).append(event);

	for (var i in data){
	    var name="<p>"+data[i][8];
	    var d="<p>"+data[i][10];
	    var dte="<p>"+data[i][12];
	    var loc="<p>"+data[i][18];
	    event=$("<ul></ul>");
	    event.append(name);
	    event.append(d);
	    event.append(dte);
	    event.append(loc);
	    event.attr("class","");
	    var date = data[i][12]+"";
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
	    l.append(event);
	}
    });
    
};

function displayAfter(Month,Day,Year){
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
    var l=$("#events ul")
    console.log($(l))
}
function showEvents(){
    var borough=$("#Borough").val();
    var month=$("select[name='Month']").val();
    console.log(month);
    var day=$("select[name='Day']").val();
    var year=$("select[name='Year']").val();
    console.log(borough);
    fillEvents(borough,month,day,year);
    //doesn't adjust for the different days...
    //$("#Update").click(showWithDates());
}
$(document).ready(function(){
    $("#Go").bind("click", showEvents())
});



/*
  function showWithDates(){
  var borough=$("#Borough").val();
    var month=$("select[name='Month']").val();
    var day=$("select[name='Day']").val();
    var year=$("select[name='Year']").val();
    displayAfter(month,day,year);
    //displayOn(month,day,year,borough);
    }
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