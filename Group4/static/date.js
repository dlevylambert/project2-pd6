$(document).ready(function readyfunc(){
    $('li').each(function hideall() {
	var current = $(this).text().replace(' ','_').replace(/[\d':+-;]/g,"");
	$("#"+current).hide();
    })
    $('li').mouseenter(function showx() {
	var current1 = $(this).text().replace(' ','_').replace(/[\d':+-;]/g,"");
	$("#"+current1).show();
    })
    $('li').mouseleave('slow',function hidex() {
	var current2 = $(this).text().replace(' ','_').replace(/[\d':+-;]/g,"");
	$("#"+current2).delay(1200).fadeOut('slow');
    })
})