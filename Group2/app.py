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

booleanGenre = False
booleanLatest = False
booleanPlaying = False
booleanSearch = False
booleanUpcoming = False
booleanPopular = False

@app.route("/", methods=["GET", "POST"])
def home():
    global result
    if request.method=="GET":
        return render_template("moviechooser.html", genres = recommend2.get_genres())
    else:
        button = request.form["button"]
        if button == "Search_Movie": #WORKS
            search.append(request.form["searchdata"].replace(" ", "_"))
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
            booleanSearch = True
            return render_template("searchresults.html", headerThing= "These are the results for your search for the word " + wordSelected)
        if len(genre)>0:
            genreSelected = genre.pop(0)
            booleanGenre = True
            return render_template("searchresults.html", headerThing= "These are the results for your search for the genre " + genreSelected)
        if len(latest)>0:
            global d
            d = latest.pop(0)
            booleanLatest = True
            return render_template("searchresults.html", headerThing= "This is the result for your search of the latest movie")
        if len(playing)>0:
            global f
            f = playing.pop(0)
            booleanPlaying = True
            return render_template("searchresults.html", headerThing= "These are the results for your search for movies playing in theaters")
        if len(upcoming)>0:
            global g
            g = upcoming.pop(0)
            booleanUpcoming = True
            return render_template("searchresults.html", headerThing= "These are the results for your search of upcoming movies")
        if len(popular)>0:
            global h
            h = popular.pop(0)
            booleanPopular = True
            return render_template("searchresults.html", headerThing= "These are the results of your search of popular movies")
    else:
        button = request.form["button"]
        if button == "back":
            return redirect(url_for('home'))
        #if button == "See these movies' information":
            #return redirect(url_for('home'))
        else:
            pass
          
@app.route("/get_info")
def get_info():
    movie_id=request.args.get('movie_id','') 
    return json.dumps(recommend2.get_info(movie_id))

@app.route("/get_dropdown")
def get_dropdown():
    global booleanGenre, booleanSearch, booleanLatest, booleanPlaying, booleanUpcoming, booleanPopular, result
    if booleanGenre:
        result = recommend2.genre_info(genreSelected)
        booleanGenre = False
    elif booleanSearch:
        result = recommend2.movie_info(wordSelected)
        booleanSearch = False
    elif booleanLatest:
        result = recommend2.latest_info()
        booleanLatest = False
    elif booleanPlaying:
        result = recommend2.now_playing_info()
        booleanPlaying = False
    elif booleanUpcoming:
        result = recommend2.upcoming_info()
        booleanUpcoming = False
    elif booleanPopular:
        result = recommend2.popular_info()
        booleanPopular = False
    return json.dumps(result)

@app.route("/get_similar")
def get_similar():
    booleanSearch = True
    movie_id=request.args.get('movie_id','')
    wordSelected = recommend2.get_info(movie_id)['title']
    return json.dumps(recommend2.movie_info(wordSelected))

if __name__ == "__main__":
    app.run(debug = True)
