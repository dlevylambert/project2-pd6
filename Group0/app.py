from flask import Flask
from flask import url_for,redirect, flash
from flask import session, escape
from flask import request
from flask import render_template
import utils

app = Flask(__name__)
global current_user

@app.route("/", methods = ["GET", "POST"])
def homepage():
	global current_user
	if request.method == "GET":
		return render_template("musicboxhome.html");
        else:
		button = request.form["button"]
		if button == "create-new-user":
			current_user = request.form.get("new-user")
			utils.add_user(current_user)
			songs = utils.get_songs(current_user)
			return redirect("/"+current_user)
		
		
@app.route("/aboutus.html",methods=["GET"])
def aboutus():
	return render_template("aboutus.html")

@app.route("/login.html",methods=["GET","POST"])
def login():
	global current_user
	utils.connect()
	if request.method == "GET":
		user = current_user
		songs = utils.get_songs(user)
		return render_template("login.html")

	

#will add search later

if __name__ == "__main__":
    app.debug = True
    app.run();
