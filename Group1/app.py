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

#Login work starts here
#
@login_manager.user_loader
def load_user(userid):
    return User.get(userid)



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
        email = request.form['email']
        password = request.form['password']
        
        #return 'EMAIL: ' + email+ '<p>Password: ' + password
    
@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method=="GET":
        return render_template("search.html")
    if request.method=="POST":
        #This can change depending on how we make the search process work,
        #but I thought I'd just put something up to work with.
        #The options are either:
        # 1. A whole new page (more html work)
        # 2. Keep the same page and change it using javascript
        return render_template("madeSearch.html", variousinformation='information passed on from search.html')
    
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
