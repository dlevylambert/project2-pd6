from flask import request,Flask,render_template, url_for,redirect,request
import urllib2,json
import recommend2

app = Flask(__name__)
global result, genre, search, latest, playing, upcoming, popular, wordSelected, booleanGenre, booleanSearch, booleanLatest, booleanPlaying, booleanUpcoming, booleanPopular, genreSelected
result = {}
genre = []
search= []
latest = []
playing = []
upcoming = []
popular = []
wordSelected = ""
genreSelected = ""

booleanGenre = false
booleanLatest = false
booleanPlaying = false
booleanSearch = false
booleanUpcoming = false
booleanPopular = false

@app.route("/", methods=["GET", "POST"])
def home():
    global result
    if request.method=="GET":
        return render_template("moviechooser.html", genres = recommend2.get_genres())
    else:
        button = request.form["button"]
        if button == "Search_Movie": #WORKS
            search.append(request.form["searchdata"])
            return redirect(url_for('searchResults'))
        if button == "Genre_Selection": #WORKS
            res = request.form["genre_selection"]
            genre.append(res)
            return redirect(url_for('searchResults'))
        if button == "Latest_Selection": #WORKS
            latest.append("the latest movie")
            return redirect(url_for('searchResults'))
        if button == "Now_Playing_Selection": #I THINK IT WORKS
            playing.append("now playing")
            return redirect(url_for('searchResults'))
        if button == "Upcoming_Selection": #I THINK IT WORKS
            upcoming.append("upcoming movies")
            return redirect(url_for('searchResults'))
        if button == "Popular_Selection": #WORKS
            popular.append("popular movies")
            return redirect(url_for('searchResults'))

@app.route("/searchResults/", methods=["GET", "POST"])
def searchResults():
    global result, wordSelected, genreSelected, booleanGenre, booleanSearch, booleanLatest, booleanPlaying, booleanUpcoming, booleanPopular 
    if request.method=="GET":
        if len(search)>0:
            wordSelected = search.pop(0)
            booleanSearch = true
            return render_template("searchresults.html", searchWord = wordSelected)
        if len(genre)>0:
            genreSelected = genre.pop(0)
            booleanGenre = true
            return render_template("searchresults.html", searchGenre = genreSelected)
        if len(latest)>0:
            global d
            d = latest.pop(0)
            booleanLatest = true
            return render_template("searchresults.html", searchLatest = d)
        if len(playing)>0:
            global f
            f = playing.pop(0)
            booleanPlaying = true
            return render_template("searchresults.html", searchPlaying = f)
        if len(upcoming)>0:
            global g
            g = upcoming.pop(0)
            booleanUpcoming = true
            return render_template("searchresults.html", searchUpcoming = g)
        if len(popular)>0:
            global h
            h = popular.pop(0)
            booleanPopular = true
            return render_template("searchresults.html", searchPopular = h)
    else:
        button = request.form["button"]
        if button == "back":
            return redirect(url_for('home'))
          
@app.route("/get_info")
def get_info():
    movie_id=request.args.get('movie_id','') 
    return json.dumps(recommend2.get_info(movie_id))

@app.route("/get_dropdown")
def get_dropdown():
    global booleanGenre, booleanSearch, booleanLatest, booleanPlaying, booleanUpcoming, booleanPopular, result
    if booleanGenre:
        result = recommend2.genre_info(genreSelected)
        booleanGenre = false
    elif booleanSearch:
        result = recommend2.movie_info(wordSelected)
        booleanSearch = false
    elif booleanLatest:
        result = recommend2.latest_info()
        booleanLatest = false
    elif booleanPlaying:
        result = recommend2.now_playing_info()
        booleanPlaying = false
    elif booleanUpcoming:
        result = recommend2.upcoming_info()
        booleanUpcoming = false
    elif booleanPopular:
        result = recommend2.popular_info()
        booleanPopular = false
    return json.dumps(result)

if __name__ == "__main__":
    app.run(debug = True)
