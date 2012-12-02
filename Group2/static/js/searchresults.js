
function getDropdown(){
    $.getJSON("/get_dropdown", function(data) {
        $("#mlist").empty();
        for (var i = 0; i < data['ids'].length; i++){
            var item=$('<option value="'+data['ids'][i]+'">'+data['titles'][i]+'</option>');
            $("#mlist").append(item);
        }
	$("#mlist").change(loadInfo);
	      });
}

function loadInfo(data) {
    var moviestuff = $(this).attr('value')
    getInfo(moviestuff)

}

function getInfo(movie_id){
    var counter;
    counter = 0;
    $.getJSON("/get_info", {movie_id: movie_id}, function (data) {
	$('#results').empty();
	$('#similar').empty();
	      $('#ytapiplayer').empty();
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
	    else if (d != "trailer_id" && d != "id" )
		$('#results').append('<p><b>' + d + '</b>' + '  ' + data[d]  + '<\p>');
        }
	movie_trailer_id = data['trailer_id'];
	      	console.log(movie_trailer_id);
	console.log("change movie trailer");
	var params = { allowScriptAccess: "always" };
	
	var atts = { id: "myytplayer" };
	      $("#myytplayer").attr('data', "http://www.youtube.com/v/" +
movie_trailer_id + "?enablejsapi=1&playerapiid=ytplayer&version=3");
swfobject.embedSWF("http://www.youtube.com/v/" + movie_trailer_id +
	      "?enablejsapi=1&playerapiid=ytplayer&version=3","ytapiplayer",
	      "425", "356", "8", null, null, params, atts);

    });
}

$(document).ready(function(){
    var movie_trailer_id;
    getDropdown();
});
