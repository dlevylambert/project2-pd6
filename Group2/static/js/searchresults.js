//loads the dropdown with the movies

function getDropdown(){
    $.getJSON("/get_dropdown", function(data) {
        $("#mlist").empty();
        for (var i = -1; i < data['ids'].length; i++){
	    if (i == -1) {
		$("#mlist").append('<option value="'+000+'">' + "SELECT A MOVIE TO VIEW ITS INFO"  + '<\p>');
	    }
	    else {
            var item=$('<option value="'+data['ids'][i]+'">'+data['titles'][i]+'</option>');
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
	$('#results').empty();
	$('#similar').empty();
	$('#ytapiplayer').empty();
	$('#similar').append('<option value="'+000+'">' + "SELECT A MOVIE TO VIEW ITS INFO"  + '<\p>');
	$("#movieTitle").empty();
	$("#movieTitle").append("<b>" + data['title'] + "</b>");
        for (var d in data) {
	    if (d == "similar movies"){
		$('#results').append('<p><b>' + d + '</b></p>');
		var titles = [];
		var ids = [];
		var rtitles = data[d];
		for (var thing in rtitles){
		    id = rtitles[thing]['id'];
		    title = rtitles[thing]['title'];
		    $('#similar').append('<option value="'+id+'">' + title  + '<\p>');		    
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
	swfobject.embedSWF("http://www.youtube.com/v/" + movie_trailer_id + "?enablejsapi=1&playerapiid=ytplayer&version=3","ytapiplayer","425", "356", "8", null, null, params, atts);
	
    });
}

function changePage(data) {
    console.log("hi");
    var movieid = $(this).attr('value');
    getInfo(movieid);
}



//what's running
$(document).ready(function(){
    var movie_trailer_id;
    $("#mlist").append('<option value="'+000+'">' + "SELECT A MOVIE TO VIEW ITS INFO"  + '<\p>');
    $('#similar').append('<option value="'+000+'">' + "SELECT A SIMILAR MOVIE TO VIEW ITS INFO AFTER SELECTING A MOVIE ABOVE"  + '<\p>');
    getDropdown();
});
