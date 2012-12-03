$(document).ready(function() {
    $('td').bind('click',function() {
	alert($(this).val());
	window.location = window.location+"/"+$(this).val();
    });
});

