function getDropdownActor(){
    $.getJSON("/get_dropdown_actor", function(data) {
        $("#alist").empty();
        console.log(data);
	$("#alist").append('<option value="'+000+'">' + "Select an actor or actress:" + '<\p>');
        for (var i = 0; i < data.length; i++) {
	    $("#alist").append('<option value="'+data[i]['id']+'">'+data[i]['name']+'</option>');
	    
	}
	$("#alist").change(loadstuff);
    });
}

function loadstuff(data) {
    var actorid = $(this).attr('value');
    loadMovies(actorid);
}

function loadMovies(actorid) {
    $.getJSON("/get_movies_actor", {actorid: actorid}, function(data) {
        $("#mlist").empty();
	console.log(data);
	});
}
    
    //what's running
$(document).ready(function(){
    getDropdownActor();
});