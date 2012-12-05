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
    #return redirect(url_for("under_construction"))

@app.route("/logout")
#@login_required
def logout():
    #logout_user()
    if 'username' in session:
        del session['username']
    return redirect(url_for("index"))

@app.route("/clear")
def clear():
    users.clear_users()
    return redirect(url_for("logout"))

#
#Login work ends here

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method=="GET":
        return redirect(url_for("index" ))
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
            else:
                return redirect(url_for("oops"))

@app.route("/oops", methods=["GET", "POST"])
def oops():
    if request.method=="GET":
        return render_template("sorry.html")
    if request.method=="POST":
        return redirect(url_for("index"))
    
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
        if 'results' in session:
            del session['results']
        return render_template("search.html", questions = util.listOfQuestions())
    if request.method=="POST":
        class_size = request.form['sizeofclass']#.encode('utf-8')
        class_size = class_size
        readingp = request.form['reading']
        mathp = request.form['math']
        writingp = request.form['writing']
        class_sizep = request.form['classsize']
        priority_array = [readingp, mathp, writingp, class_sizep]

        borough = request.form['borough']
        
        numres = int(request.form['numresults'])

        #results = util.getSchoolMatches(priority_array, class_size, borough, numres)
        
        #return class_size
        #session['results'] = results
        #return writingp
        return redirect(url_for("result"))
        #return redirect(url_for("result"))
     
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
        if 'results' in session:
            result = session['results']
        else:
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
    app.run(port=6001);
