//This may or may not be a really inefficient way of doing things :/

function displayMap(){
    $("#map").show();
}

function displayDateSelect(){
    displayMap();
    $("#dateSelect").show();
    $("#Go").click(displayEventStuff());
}

function displayEventStuff(){
    $("#eventStuff").show();
}

$(document).ready(function(){
    $("#dateSelect").hide();
    $("eventStuff").hide();
    displayMap();
    $("#Select").click(displayDateSelect());
});