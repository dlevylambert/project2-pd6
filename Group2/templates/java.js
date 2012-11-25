function genre() {
    searchResult = get_genres.result
}

function latest() {
    searchResult = latest_movies.result
}

function nowplaying() {
    searchResult = now_playing_movies.result
}

function upcoming() {
    searchResult = upcoming_movies.result
}

function popular() {
    searchResult = popular_movies.result
}

function searching() {
}

$(document).ready(function(){
    $("#Genre_Selection").click(genre);
    $("#Latest_Selection").click(latest);
    $("#Now_Playing_Selection").click(nowplaying);
    $("#Upcoming_Selection").click(upcoming);
    $("#Popular_Selection").click(popular);
    $("#Search_Movie").click(searching);
});