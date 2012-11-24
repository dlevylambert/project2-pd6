from flask import Flask
from flask import url_for,redirect,flash
from flask import session, escape
from flask import request
from flask import render_template
from pymongo import connection
import recommend2
from random import randrange

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method=="GET":
        return render_template("moviechooser.html")
    
if __name__ == "__main__":
    app.run(debug = True)
