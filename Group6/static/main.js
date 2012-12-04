function get_tweets(input) {
    val = $(input).val()
    $(input).val("")
    $("#data").text("");
    $.getJSON("/get_data?name=" + val, function(data) {
        var items = [];

	$.each(data, function(key, val) {
	    items.push('<td>' + key + '</td>' + '<td>' + val + '</td>');
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
			  
