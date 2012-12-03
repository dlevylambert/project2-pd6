//loads the dropdown with the movies

function getDropdown(){
    $.getJSON("/get_dropdown", function(data) {
        $("#mlist").empty();
        for (var i = -1; i < data['ids'].length; i++){
	    if (i == -1) {
		$("#mlist").append('<option value="'+000+'">' + "SELECT A MOVIE TO VIEW ITS INFO"  + '<\p>');
	    }
	    else {
		var item=$('<option value="'+data['ids'][i]+'">'+data['titles'][i]+"  "+data['dates'][i]+'</option>');
		$("#mlist").append(item);
	    }
        }
	$("#mlist").change(loadInfo);
    });
}
//loads the result stuff by calling getInfo
function loadInfo(data) {
    var moviestuff = $(this).attr('value')
    getInfo(moviestuff)
    
}
//fills the results div with the results
function getInfo(movie_id){
    var counter;
    counter = 0;
    $.getJSON("/get_info", {movie_id: movie_id}, function (data) {
	     //new_tab(data['review']);
	$('#results').empty();
	$('#ytapiplayer').empty();
	$("#movieTitle").empty();
	$("#movieTitle").append("<b>" + data['title'] + "</b>");
        for (var d in data) {
	    if (data[d] == null)
		$('#results').append('<p><b>' + d + '</b>' + " unavailable" + '</p>');
	    else if (d == "review"){
		if (data[d] == "no review available")
		    $('#results').append('<p><b>' + d + '</b>' + '  ' + data[d]  + '<\p>');
		else{
		    $('#results').append('<p><b>' + d + "  "  + '</b><a id="rlink" href="'+data[d]+'">' + data[d] + '</a><\p>');
		    $('#rlink').click(function() {
			$(this).attr('target', '_blank');
		    });
		}
	    }
	    else if (d == "similar movies"){
		$('#results').append('<p><b>' + d + '</b></p>');
		$('#results').append('<select id="similar">' + '</select>');
		$('#similar').append('<option value="'+000+'">' + "SELECT A MOVIE TO VIEW ITS INFO"  + '<\p>');
		var titles = [];
		var ids = [];
		var dates = [];
		var rtitles = data[d];
		for (var thing in rtitles){
		    id = rtitles[thing]['id'];
		    title = rtitles[thing]['title'];
		    date = rtitles[thing]['date'];
		    $('#similar').append('<option value="'+id+'">' + title + "  " + date  + '<\p>');    
		}
	    }
	    else if (d != "trailer_id" && d != "id" ) {
		$('#results').append('<p><b>' + d + '</b>' + '  ' + data[d]  + '<\p>');
	    }
        }
	$('#similar').change(changePage);

	//stuff with the youtube API. Works!
	movie_trailer_id = data['trailer_id'];
	var params = { allowScriptAccess: "always" };
	var atts = { id: "myytplayer" };
	$("#myytplayer").attr('data', "http://www.youtube.com/v/" + movie_trailer_id + "?enablejsapi=1&playerapiid=ytplayer&version=3");
	var url = "http://www.youtube.com/v/" + movie_trailer_id + "?enablejsapi=1&playerapiid=ytplayer&version=3";
	// making trailer not show when not available, not working
	//  if (checkUrl(url)) {
	swfobject.embedSWF(url,"ytapiplayer","425", "356", "8", null, null, params, atts);
	//  }
	//  else{
	//  $('#ytapiplayer').append('<p><b>' + "TRAILER UNAVAILABLE" + '<b><p><br><br>');
	//  }
	
    });
}

function new_tab(url)
{
    window.open(url, '_blank');
    window.focus();
}

function checkUrl(url) {
    var request = false;
    if (window.XMLHttpRequest) {
	request = new XMLHttpRequest();
    }
    else if (window.ActiveXObject) {
	request = new ActiveXObject("Microsoft.XMLHttp");
    }
    if (request) {
	request.onreadystatechange=function() {
	    request.open("GET", url);
	    if (request.status == 200){
		return true;
	    }
	}
    }
    return false;
}

function changePage(data) {
    console.log("hi");
    var movieid = $(this).attr('value');
    getInfo(movieid);
}

//what's running
$(document).ready(function(){
    getDropdown();
});