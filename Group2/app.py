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
genre = []
search= []
latest = []
playing = []
upcoming = []
popular = []

@app.route("/", methods=["GET", "POST"])
def home():
    global result
    if request.method=="GET":
        return render_template("moviechooser.html", genres = recommend2.get_genres())
    else:
        button = request.form["button"]
        if button == "Search_Movie": #WORKS
            result = recommend2.movie_info(request.form["searchdata"])
            search.append(request.form["searchdata"]
            return redirect(url_for('searchResults'))
        if button == "Genre_Selection": #WORKS
            res = request.form["genre_selection"]
            genre.append(res)
            result = recommend2.genre_info(res)
            return redirect(url_for('searchResults'))
        if button == "Latest_Selection": #not done
            result = recommend2.latest_info()
            latest.append("the latest movie")
            return redirect(url_for('searchResults'))
        if button == "Now_Playing_Selection": #I THINK IT WORKS
            result = recommend2.now_playing_info()
            playing.append("now playing")
            return redirect(url_for('searchResults'))
        if button == "Upcoming_Selection": #I THINK IT WORKS
            result = recommend2.upcoming_movies()
            upcoming.append("upcoming movies")
            return redirect(url_for('searchResults'))
        if button == "Popular_Selection": #not done
            result = popular_movies()
            popular.append("popular movies")
            return redirect(url_for('searchResults'))

@app.route("/searchResults/", methods=["GET", "POST"])
def searchResults():
    global result
    if request.method=="GET":
        if search[0]:
            global a
            a = search.pop(0)
            return render_template("searchresults.html", searchResult = result, searchWord = a)
        if genre[0]:
            global a
            a = genre.pop(0)
            return render_template("searchresults.html", searchResult = result, searchGenre = a)
        if latest[0]:
            global a
            a = latest.pop(0)
            return render_template("searchresults.html", searchResult = result, searchLatest = a)
        if playing[0]:
            global a
            a = playing.pop(0)
            return render_template("searchresults.html", searchResult = result, searchPlaying = a)
        if upcoming[0]:
            global a
            a = upcoming.pop(0)
            return render_template("searchresults.html", searchResult = result, searchPlaying = a)
        if popular[0]:
            global a
            a = popular.pop(0)
            return render_template("searchresults.html", searchResult = result, searchPlaying = a)
    else:
        pass
    


if __name__ == "__main__":
    app.run(debug = True)
