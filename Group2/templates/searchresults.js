
function getDropdown(){
    $.getJSON("/get_dropdown", function(data) {
        $("#mlist").empty();
        for (var i = 0; i < data['ids'].length; i++){
            var item=$('<option value="'+data['ids'][i]+'">'+data['titles'][i]+'  '+data['dates'][i]+'</option>');
            $("#mlist").append(item);
        }
	$("#mlist").change(loadInfo);
	      });
}

function loadInfo(data) {
    var moviestuff = $(this).attr('value')
    getInfo(moviestuff)

}

function getInfo(movie_id){
    $.getJSON("/get_info", {movie_id: movie_id}, function (data) {
        console.log(data);
        for (var d in data) {
            $('#results ul').append('<li><b>' + d + '</b>' + '  ' + data[d]  + '<\li>');
        }
    });
}

$(document).ready(function(){
    getDropdown();
    $("#mlist").change(getInfo(console.log("change")));
});