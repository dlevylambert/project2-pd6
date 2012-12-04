from flask import Flask, render_template
from flask import url_for,redirect, flash
from flask import session, escape
from flask import request
import utils, musicservices

app = Flask(__name__)
global current_user
global current_artist
global current_artistID

@app.route("/", methods=["GET", "POST"])
def homepage():
	utils.connect()
	if request.method == "GET":
		return render_template("musicboxhome.html");
        else:
		global current_user
		button = str(request.form["button"])
		if button == "Login":
			user = request.form.get("login-or-register")
			current_user = utils.add_or_view_user(user)
			songs = utils.get_songs(current_user)
			return redirect("/"+current_user)
		if button == "Go":
			return render_template("search.html")
		
@app.route("/about.html",methods=["GET"])
def aboutus():
	return render_template("about.html")

@app.route("/"+"<username>",methods=["GET","POST"])
def login(username):
	global current_user
	global current_artist
	global current_artistID
	utils.connect()
	if request.method == "GET":
		songs = utils.get_songs(current_user)		
		return render_template("login.html",user=current_user,songs=songs)
	else:
		button = str(request.form["button"])
		if button == "Close account":
			utils.remove_user(current_user)
			return redirect("/")
		elif button == "Search":
			current_artist = request.form.get("search")
			current_artistID = str(musicservices.getID(
					musicservices.getArtistInfo(
						utils.curate(current_artist))))
			return redirect("/"+current_user+"/"+current_artistID)

@app.route("/"+"<username>"+"/"+"<artistID>",methods=["GET","POST"])
def artist(username,artistID):
	global current_user, current_artist, current_artistID
	if request.method=="GET":
		info = utils.build_artist(
			musicservices.getArtistInfo(
				utils.curate(current_artist)))
		info[4] = list(set([line["title"] for line in info[4]]))
		#list(set(some_list)) removes duplicates
		return render_template("artist.html", artist=info[0]
				       ,profile=info[1],members=info[2]
				       ,aID=info[3],releases=info[4])
	else:
		button = str(request.form["button"])
		if button == "Back to profile":
			return redirect("/"+current_user)
		else:
			utils.add_song(current_user,button
				       ,current_artistID)
			return redirect("/"+current_user)
	
if __name__ == "__main__":
    app.debug = True
    app.run()
