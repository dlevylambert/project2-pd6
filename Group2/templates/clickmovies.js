$(document).ready(function(){
    $("#go").click(loadSummary());
});

function loadSummary(e){
    $.getJSON("/get_info/<int:movie_id>",function(data){
	$("#opmenu li").empty();
	for (var i in data) {
	    var item=$('<li>+data[i]+</li>');
	    $("#opmenu").append(item);
	}
}