import json
import urllib
import sys
from urllib2 import Request, urlopen
from pymongo import Connection
global connection
global db
global res
global col

API_KEY = "450062599145d021e7243a767de7c7d0"
ID = 52591

####NOT SURE WE NEED AUTHENTICATE METHODS FOR WHAT WE DO. ALSO LOOK I MADE THE FIND MOVIE THING WORK SO NOW WE CAN GET THE JSON FROM IT

def auth():
    global connection
    global db
    global res
    global col
    connection = Connection('mongo.stuycs.org')
    db = connection.admin
    res = db.authenticate ('ml7', 'ml7')
    db = connection['z-pd6']
    col = db['movieRecommender']
    
def get_similar_movies(movie_id):
    auth()    
    global API_KEY
    headers = {"Accept": "application/json"}
    request = Request("http://api.themoviedb.org/3/movie/" + str(movie_id) + "/similar_movies" + "?api_key=" + API_KEY, headers=headers)
    response_body = urlopen(request).read()
    result = json.loads(response_body)
    return result

def get_movie(movie_name):
    auth()
    global API_KEY
    headers = {"Accept": "application/json"}
    request = Request("http://api.themoviedb.org/3/search/movie?api_key=" + API_KEY + "&query=" + movie_name, headers=headers)
    response_body = urlopen(request).read()
    result = json.loads(response_body)
    return result

def movie_info(movie_name):
    auth()
    list_of_movies = get_movie(movie_name)
    counter = 0
    ids = []
    titles = []
    dates = []
    for movie in list_of_movies['results']:
        ids.append(list_of_movies['results'][counter]['id'])
        titles.append(str(list_of_movies['results'][counter]['title']))
        dates.append(str(list_of_movies['results'][counter]['release_date']))
        counter = counter + 1
    info = {}
    info['ids'] = ids
    info['titles'] = titles
    info['dates'] = dates
    return info


def movie_cast(movie_id):
    auth()
    global API_KEY
    headers = {"Accept": "application/json"}
    request = Request("http://api.themoviedb.org/3/movie/" + str(movie_id) + "/casts?api_key=" + API_KEY, headers=headers)
    response_body = urlopen(request).read()
    result = json.loads(response_body)
    return result

def movie_image(movie_id):
    auth()
    global API_KEY
    headers = {"Accept": "application/json"}
    request = Request("http://api.themoviedb.org/3/movie/" + str(movie_id) + "/images?api_key=" + API_KEY, headers=headers)
    response_body = urlopen(request).read()
    result = json.loads(response_body)
    return result

def upcoming_movies():
    auth()
    global API_KEY
    headers = {"Accept": "application/json"}
    request = Request("http://api.themoviedb.org/3/movie/upcoming?api_key=" + API_KEY, headers=headers)
    response_body = urlopen(request).read()
    result = json.loads(response_body)
    return result

def latest_movies():
    auth()
    global API_KEY
    headers = {"Accept": "application/json"}
    request = Request("http://api.themoviedb.org/3/movie/latest?api_key=" + API_KEY, headers=headers)
    response_body = urlopen(request).read()
    result = json.loads(response_body)
    return result

def now_playing_movies():
    auth()
    global API_KEY
    headers = {"Accept": "application/json"}
    request = Request("http://api.themoviedb.org/3/movie/now_playing?api_key=" + API_KEY, headers=headers)
    response_body = urlopen(request).read()
    result = json.loads(response_body)
    return result


def popular_movies():
    auth()
    global API_KEY
    headers = {"Accept": "application/json"}
    request = Request("http://api.themoviedb.org/3/movie/popular?api_key=" + API_KEY, headers=headers)
    response_body = urlopen(request).read()
    result = json.loads(response_body)
    return result


def top_rated_movies():
    auth()
    global API_KEY
    headers = {"Accept": "application/json"}
    request = Request("http://api.themoviedb.org/3/movie/top_rated?api_key=" + API_KEY, headers=headers)
    response_body = urlopen(request).read()
    result = json.loads(response_body)
    return result


def get_genres():
    auth()
    global API_KEY
    headers = {"Accept": "application/json"}
    request = Request("http://api.themoviedb.org/3/genre/list?api_key=" + API_KEY, headers=headers)
    response_body = urlopen(request).read()
    result = json.loads(response_body)
    return result


def get_movies_by_genre(genre):
    auth()
    global API_KEY
    headers = {"Accept": "application/json"}
    request = Request("http://api.themoviedb.org/3/genre/" + str(genre) + "/movies?api_key=" + API_KEY, headers=headers)
    response_body = urlopen(request).read()
    result = json.loads(response_body)
    return result


def add_movie_database(movie_name, movie_id):
    auth()
    col.insert({'title': movie_name, 'id': movie_id})
    

if __name__ == "__main__":     
    stuff = movie_info("love")
    print stuff
    print

    for r in get_similar_movies(stuff["ids"][0])['results']:
        print r['title']
        print
    for genre in get_genres()['genres']:
        print genre['name']
