$(document).ready(function(){
    $('select>option').click( function() {
	movie_id = $('#mlist option:selected').attr('id');
	loadSummary(movie_id);
    }); 
});

function loadSummary(movie_id){ 
    $.getJSON("/get_info", {movie_id: movie_id}, function (data) {
	console.log(data);
	for (var d in data) {
	    ('#results').append('<li><b>' + d + '</b>' + '  ' + data[d]  + '<\li>');
	}
    });
}