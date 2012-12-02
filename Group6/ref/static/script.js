function get_tweets(input) {
    val = $(input).val()
    $(input).val("")
    $("#data").text("");
    $.getJSON("/get_data?name=" + val, function(data) {
        for (var i in data["tweets"]){
            $("#data").append("<p>" + data["tweets"][i] + "</p>");
        }
    });
}

$(document).ready(function() {
    $("#twiturl").keypress(function(e) {
        if (e.which == 13){
            get_tweets(this)
        }
    })
})

