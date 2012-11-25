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
            res = request.form["genre_selection"]
            result = recommend2.get_movies_by_genre(res)
            return render_template("searchresults.html", searchResult = result)
        if button == "Latest_Selection":
            result = recommend2.latest_movies()
            return render_template("searchresults.html", searchResult = result)
        if button == "Now_Playing_Selection":
            result = recommend2.now_playing_movies()
            return render_template("searchresults.html", searchResult = result)
        if button == "Upcoming_Selection":
            result = recommend2.upcoming_movies()
            return render_template("searchresults.html", searchResult = result)
        if button == "Popular_Selection":
            result = popular_movies()
            return render_template("searchresults.html", searchResult = result)
    
if __name__ == "__main__":
    app.run(debug = True)
