from flask import Flask
from flask import url_for,redirect,flash
from flask import session, escape
from flask import request
from flask import render_template
from pymongo import connection
import recommend2
from random import randrange

app = Flask(__name__)
global result
result = {}

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method=="GET":
        return render_template("moviechooser.html", genres = recommend2.get_genres())
    else:
        button = request.form["button"]
        if button == "Search_Movie":
            result = recommend2.movie_info(request.form["searchdata"])
            return render_template("searchresults.html", searchResult = result)
        if button == "Genre_Selection":
            return render_template("searchresults.html", searchResult = result)
        if button == "Latest_Selection":
            return render_template("searchresults.html", searchResult = result)
        if button == "Now_Playing_Selection":
            return render_template("searchresults.html", searchResult = result)
        if button == "Upcoming_Selection":
            return render_template("searchresults.html", searchResult = result)
        if button == "Popular_Selection":
            return render_template("searchresults.html", searchResult = result)
    
if __name__ == "__main__":
    app.run(debug = True)
