from flask import Flask
from flask import render_template
from flask import url_for,redirect, flash
from flask import session, escape
from flask import request

from flask.ext.login import LoginManager, logout_user, login_required

app = Flask(__name__)

login_manager = LoginManager()
login_manager.setup_app(app)

app.secret_key = 'secret key'

@login_manager.user_loader
def load_user(userid):
    return User.get(userid)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method=="GET":
        return render_template("default.html", )
    if request.method=="POST":
        #need to discuss use of login
        pass

@app.route("/index", methods=["GET", "POST"])
def index():
    if request.method=="GET":
        pass
    if request.method=="POST":
        pass
    
@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method=="GET":
        pass
    if request.method=="POST":
        pass
    
@app.route("/mySearches")
@login_required
def mySearches():
    pass

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("/"))


if __name__ == "__main__":
    app.debug = True
    app.run();
