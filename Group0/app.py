from flask import Flask, render_template
from flask import url_for,redirect, flash
from flask import session, escape
from flask import request
import utils

app = Flask(__name__)
global current_user

@app.route("/", methods=["GET", "POST"])
def homepage():
	utils.connect()
	if request.method == "GET":
		utils.search_artist("coldplay")
		return render_template("musicboxhome.html");
        else:
		global current_user
		button = str(request.form["button"])
		if button == "Login":
			user = request.form.get("login-or-register")
			current_user = utils.add_or_view_user(user)
			songs = utils.get_songs(current_user)
			print current_user
			return redirect("/"+current_user)
		if button == "Go":
			return render_template("search.html")
		
@app.route("/about.html",methods=["GET"])
def aboutus():
	return render_template("about.html")

@app.route("/"+"<username>",methods=["GET","POST"])
def login(username):
	global current_user
	utils.connect()
	if request.method == "GET":
		user = current_user
		songs = utils.get_songs(user)
		return render_template("login.html",user=user,songs=songs)
	else:
		button = str(request.form["button"])
		if button == "Close account":
			utils.remove_user(current_user)
			return redirect("/")
		elif button == "Back":
			return redirect("/")


if __name__ == "__main__":
    app.debug = True
    app.run()
