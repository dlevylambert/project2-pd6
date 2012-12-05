$(document).ready(function readyfunc(){
    $('li').mouseenter(function showx() {
	var current = $(this).text();
	$('input[value=current]').show();
    })
    $('li').mouseleave(function hidex() {
	var current = $(this).text();
	$('input[value=current]').hide();
	alert(current);
    })
})