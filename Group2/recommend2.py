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
    global API_KEY
    headers = {"Accept": "application/json"}
    request = Request("http://api.themoviedb.org/3/movie/" + str(movie_id) + "/similar_movies" + "?api_key=" + API_KEY, headers=headers)
    response_body = urlopen(request).read()
    result = json.loads(response_body)
    return result

def get_movie(movie_name):
    global API_KEY
    headers = {"Accept": "application/json"}
    request = Request("http://api.themoviedb.org/3/search/movie?api_key=" + API_KEY + "&query=" + movie_name, headers=headers)
    response_body = urlopen(request).read()
    result = json.loads(response_body)
    return result

def movie_info(movie_name):
    list_of_movies = get_movie(movie_name)
    counter = 0
    ids = []
    titles = []
    dates = []
    ratings = []
    trailer_ids = []
    cast= []
    summary = []
    for movie in list_of_movies['results']:
        ids.append(list_of_movies['results'][counter]['id'])
        titles.append(str(list_of_movies['results'][counter]['title']))
        dates.append(str(list_of_movies['results'][counter]['release_date']))
        ratings.append(list_of_movies['results'][counter]['vote_average'])
        if get_trailer_youtube(list_of_movies['results'][counter]['id']):
            trailer_ids.append(get_trailer_youtube(list_of_movies['results'][counter]['id']))
        else:
            trailer_ids.append("no trailer")
        cast.append(movie_cast(list_of_movies['results'][counter]['id'])['cast'][0]['name'] + ", " + movie_cast(list_of_movies['results'][counter]['id'])['cast'][1]['name'] + ", " + movie_cast(list_of_movies['results'][counter]['id'])['cast'][2]['name'] + ", and " + movie_cast(list_of_movies['results'][counter]['id'])['cast'][3]['name'])
        counter = counter + 1
    info = {}
    info['ids'] = ids
    info['titles'] = titles
    info['dates'] = dates
    info['ratings'] = ratings
    info['trailer_ids'] = trailer_ids
    info['cast'] = cast
    info['summary'] = summary
    return info

def get_trailer_youtube(movie_id):
    global API_KEY
    headers = {"Accept": "application/json"}
    request = Request("http://api.themoviedb.org/3/movie/" + str(movie_id) + "/trailers?api_key=" + API_KEY, headers=headers)
    response_body = urlopen(request).read()
    result = json.loads(response_body)
    return result['youtube'][0]['source']

    
def movie_cast(movie_id):
    global API_KEY
    headers = {"Accept": "application/json"}
    request = Request("http://api.themoviedb.org/3/movie/" + str(movie_id) + "/casts?api_key=" + API_KEY, headers=headers)
    response_body = urlopen(request).read()
    result = json.loads(response_body)
    return result

def movie_image(movie_id):
    global API_KEY
    headers = {"Accept": "application/json"}
    request = Request("http://api.themoviedb.org/3/movie/" + str(movie_id) + "/images?api_key=" + API_KEY, headers=headers)
    response_body = urlopen(request).read()
    result = json.loads(response_body)
    return result

def upcoming_movies():
    global API_KEY
    headers = {"Accept": "application/json"}
    request = Request("http://api.themoviedb.org/3/movie/upcoming?api_key=" + API_KEY, headers=headers)
    response_body = urlopen(request).read()
    result = json.loads(response_body)
    return result

def latest_movies():
    global API_KEY
    headers = {"Accept": "application/json"}
    request = Request("http://api.themoviedb.org/3/movie/latest?api_key=" + API_KEY, headers=headers)
    response_body = urlopen(request).read()
    result = json.loads(response_body)
    return result

def now_playing_movies():
    global API_KEY
    headers = {"Accept": "application/json"}
    request = Request("http://api.themoviedb.org/3/movie/now_playing?api_key=" + API_KEY, headers=headers)
    response_body = urlopen(request).read()
    result = json.loads(response_body)
    return result


def popular_movies():
    global API_KEY
    headers = {"Accept": "application/json"}
    request = Request("http://api.themoviedb.org/3/movie/popular?api_key=" + API_KEY, headers=headers)
    response_body = urlopen(request).read()
    result = json.loads(response_body)
    return result


def top_rated_movies():
    global API_KEY
    headers = {"Accept": "application/json"}
    request = Request("http://api.themoviedb.org/3/movie/top_rated?api_key=" + API_KEY, headers=headers)
    response_body = urlopen(request).read()
    result = json.loads(response_body)
    return result


def get_genres():
    global API_KEY
    headers = {"Accept": "application/json"}
    request = Request("http://api.themoviedb.org/3/genre/list?api_key=" + API_KEY, headers=headers)
    response_body = urlopen(request).read()
    result = json.loads(response_body)
    return result


def get_movies_by_genre(genre_id):
    global API_KEY
    headers = {"Accept": "application/json"}
    request = Request("http://api.themoviedb.org/3/genre/" + str(genre_id) + "/movies?api_key=" + API_KEY, headers=headers)
    response_body = urlopen(request).read()
    result = json.loads(response_body)
    return result

def genre_info(genre_name):
    global genre
    global temp
    global result
    result = {}
    for genre in get_genres()['genres']:
        if genre['name'] == genre_name:
            temp = get_movies_by_genre(genre['id'])
            break
    ids = []
    titles = []
    dates = []
    counter = 0
    for thing in temp['results']:
        ids.append(thing['id'])
        titles.append(thing['title'])
        dates.append(thing['release_date'])
        counter = counter + 1
    result['ids'] = ids
    result['titles'] = titles
    result['dates'] = dates
    return result

def add_movie_database(movie_name, movie_id):
    auth()
    col.insert({'title': movie_name, 'id': movie_id})
    

if __name__ == "__main__":     
    print movie_info("Uptown_Girls")
