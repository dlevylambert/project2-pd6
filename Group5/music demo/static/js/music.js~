var name = "";

$(document).ready(function(){
	fileSelect();
      $("#jquery_jplayer_1").jPlayer({
        ready: function () {
          $(this).jPlayer("setMedia", {
            mp3: name
          });
        },
        swfPath: "/js",
        supplied: "mp3"
      });
    });

function fileSelect(){

    var files = [
	"Donkey Kong Theme song",
	"Final Fantasy VII - Prelude [HQ]",
	"Megaman 2 - Dr. Wily Stage",
	"Super Mario Bros Official Theme Song",
	"zelda theme"
    ]
    var number = Math.floor(Math.random() * 5);
    var names = [
	"Donkey Kong Theme",
	"Final Fantasy VII - Prelude",
	"Megaman 2 - Dr. Wily Stage",
	"Super Mario Bros Official Theme Song",
	"The Legend of Zelda Theme"
    ]
    name = "audio/" + files[number] + ".mp3";
}