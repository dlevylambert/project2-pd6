function get_tweets(input) {
    var val = $(input).val()
    $(input).val("")
    $("#data").text("");
    $.getJSON("/get_data?name=" + val, function(data) {
        var items = [];
        $.each(data, function(key, val) {
            items.push('<tr><td>' + key + '</td>' + '<td>' + val + '</td></tr>');
        });

        console.log(items)
        $('<table/>', {
            'class': 'data',
            html: items.join('')
        }).appendTo('#data');
    });
}

$(document).ready(function() {
    $("#twiturl").keypress(function(e) {
        if (e.which == 13){
            get_tweets(this);
        }
    });
    $("#go").click(function() {
        get_tweets("#twiturl");
    })
//    $("#inputform").submit(function () {
//        get_tweets($(this).children("input:first"))
//    })
});
			  
