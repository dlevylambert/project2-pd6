function get_tweets(input) {
    var val = $(input).val()
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
	}).appendTo('#data table');
    });
}

$(document).ready(function() {
//$("#twiturl").keypress(function(e) {
//        if (e.which == 13){
//            get_tweets(this);
//        }
//    });
//    $("#go").click(get_tweets(this));
    $("#inputform").submit(function () {
        get_tweets($(this).children("input:first"))
    })
});
			  
