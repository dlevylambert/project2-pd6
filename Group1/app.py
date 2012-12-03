from flask import Flask
from flask import render_template
from flask import url_for,redirect, flash
from flask import session, escape
from flask import request

from flask.ext.login import (LoginManager, logout_user, login_required, login_user,
                             UserMixin, AnonymousUser)

import util
import users

class User(UserMixin):
    def __init__(self, name, id, active=True):
        self.name = name
        self.id = id
        self.active = active
    
    def is_active(self):
        return self.active


app = Flask(__name__)

login_manager = LoginManager()
login_manager.setup_app(app)


user = AnonymousUser()

app.secret_key = 'secret key'

#Login work starts here
#
@login_manager.user_loader
def load_user(userid):
    pass
#return User.get(userid)

@app.route("/login")
def login():
    pass

@app.route("/logout")
#@login_required
def logout():
    #logout_user()
    del session['username']
    return redirect(url_for("index"))


#
#Login work ends here

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method=="GET":
        return render_template("default.html", )
    if request.method=="POST":
        pass
        

@app.route("/index", methods=["GET", "POST"])
def index():
    if request.method=="GET":
        if 'username' in session:
            return render_template("index.html", username = session['username'])
        else:
            return render_template("index.html")
    if request.method=="POST":
        button = request.form['submit']
        
        if button == "Logout":
            return redirect(url_for('logout'))
        
        if button == "Login":
            email = request.form['email']
            password = request.form['password']
            if (users.authenticate(email, password)):
                user = User(email, password, True)
                login_user(user, remember=False, force=False)
                flash("Logged in successfuly.")
                session['username'] = email
            return render_template("index.html", username = session['username'])
            
    
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        flash( email )
        #users.signup(email, password)
        #return users.check_unicode(email)
    
        if users.signup(email, password):
            user = User(email, password, True)
            login_user(user, remember=False, force=False)
            flash("Logged in successfuly.")
            id = user.get_id()
            session['username'] = email
            if (user.is_anonymous()):
                return "<p>The User is anonymous</p>"
            else:
                return redirect(url_for("index"))
            
        else:
            return "I'm sorry, but that username is already taken please try again with another username"


@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method=="GET":
        return render_template("search.html", questions = util.listOfQuestions())
    if request.method=="POST":
        #This can change depending on how we make the search process work,
        #but I thought I'd just put something up to work with.
        #The options are either:
        # 1. A whole new page (more html work)
        # 2. Keep the same page and change it using javascript
        return redirect(url_for("result", variousinformation='information passed on from search.html'))
     
@app.route("/mySearches")
#@login_required
def mySearches():
    return redirect(url_for("under_construction"))

@app.route("/underConstruction", methods=["GET", "POST"])
def under_construction():
    if request.method=="GET":
        return render_template("underconstruction.html")
    if request.method=="POST":
        return redirect(url_for("home"))

@app.route("/search/result", methods=["GET", "POST"])
def result():
    if request.method=="GET":
        #result_db = shelve.open('temp_results.db')
        result = util.getSchoolMatches([1,2,3,4], 800, 'Manhattan', 5)
        return render_template("result.html", resultList=result )
    if request.method=="POST":
        return redirect(url_for('under_construction'))

@app.route("/test")
def test():
    if (user.is_anonymous()):
        return 'The User is anonymous'
    else:
        return 'The User is logged in'

if __name__ == "__main__":
    app.debug = True
    app.run();
