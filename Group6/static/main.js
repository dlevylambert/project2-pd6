function start(e) {
    $(".stats").hide();
    $("#go").click(function() {
	$(".stats").show();
    });
}

$(document).ready(function() {
    start();
});


