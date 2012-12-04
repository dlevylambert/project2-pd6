function get_tweets(input) {
    val = $(input).val()
    $(input).val("")
    $("#data").text("");
    $.getJSON("/get_data?name=" + val, function(data) {
        var items = [];

	$.each(data, function(key, val) {
	    items.push('<td id"' + key + '">' + val + '</li>');
	});

	$('<tr/>', {
	    'class': 'data',
	    html: items.join('')
	}).appendTo('table');
    });
}

$(document).ready(function() {
    $("#twiturl").keypress(function(e) {
        if (e.which == 13){
            get_tweets(this);
        }
    });
    $("#go").click(get_tweets(this));
});
			  
