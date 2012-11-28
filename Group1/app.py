from flask import Flask
from flask import render_template
from flask import url_for,redirect, flash
from flask import session, escape
from flask import request


app = Flask(__name__)

login_manager = LoginManager()

@login_manager.user_loader
def load_user(userid):
    return User.get(userid)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method=="GET":
        return render_template("index.html", username=username)
    if request.method=="POST":
        #need to discuss use of login

#Below are login related things

@app.route("savedsearches")
@login_required
def savedsearches():
    pass

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("/"))

