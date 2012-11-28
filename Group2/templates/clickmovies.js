$(document).ready(function(){
    $("#movielist").click(summary);
});

function summary(e){
    {{get_movie}}
    {{movie_info}}
}