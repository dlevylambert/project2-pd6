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
    
def get_similar_movies(movie):
    auth()    
    global API_KEY
    headers = {"Accept": "application/json"}
    request = Request("http://api.themoviedb.org/3/movie/" + str(movie) + "?api_key=" + API_KEY + "&append_to_response=releases", headers=headers)
    response_body = urlopen(request).read()
    result = json.loads(response_body)
    return result

def get_movie(movie_name, id):
    auth()
    global API_KEY
    headers = {"Accept": "application/json"}
    request = Request("http://api.themoviedb.org/3/search/movie?api_key=" + API_KEY + "&query=" + movie_name, headers=headers)
    response_body = urlopen(request).read()
    result = json.loads(response_body)
    return result

def movie_info(movie_name, id):
    auth()
    list_of_movies = get_movie(movie_name, id)
    counter = 0
    ids = []
    titles = []
    dates = []
    for movie in list_of_movies['results']:
        ids.append(list_of_movies['results'][counter]['id'])
        titles.append(str(list_of_movies['results'][counter]['title']))
        dates.append(str(list_of_movies['results'][counter]['release_date']))
    info = []
    info.append(ids) #info[0] then refers to ids
    info.append(titles) #info[1] then refers to titles
    info.append(dates) #info[2] then refers to dates of release
    return info

def add_movie_database(movie_name, movie_id):
    auth()
    col.insert({'title': movie_name, 'id': movie_id})
    
if __name__ == "__main__":     
    info = movie_info("uptown_girls",ID)
    print info
    print get_similar_movies(info[0][0])
