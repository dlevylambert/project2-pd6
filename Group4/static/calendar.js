$(document).ready(function readyfunc() {
    $('.cell').click(function name() {
	if ($(this).text().indexOf("Eve") != -1){
	    var tmp = $(this).text();
	    var num = tmp.indexOf(" ") - 1;
	    tmp = tmp.substring(0,num);
	    window.location = window.location+"/"+tmp;
	}
	else {
	    if ($(this).text().valueOf() > 1) {
		window.location = window.location+"/"+$(this).text();
	    }
	}
    })})
   


