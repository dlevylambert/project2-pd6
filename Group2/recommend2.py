import json
import urllib
import sys
from urllib2 import Request, urlopen

API_KEY = "450062599145d021e7243a767de7c7d0"
    
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
    global temp
    temp = get_movie(movie_name)
    global result
    global info
    counter = 0
    info = {}
    info['ids'] = []
    info['titles'] = []
    info['dates'] = []
    info['ratings'] = []
    info['trailer_ids'] = []
    info['cast'] = []
    info['summary'] = []
    for thing in temp['results']:
        if counter < 6:
            info['ids'].append(thing['id'])
            info['titles'].append(thing['title'])
            info['dates'].append(thing['release_date'])
            info['ratings'].append(thing['vote_average'])
            if get_trailer_youtube(thing['id']):
                info['trailer_ids'].append(get_trailer_youtube(thing['id']))
            else:
                info['trailer_ids'].append("no trailer")
            global leng
            leng = len(movie_cast(thing['id'])['cast'])
            if leng > 2 :        
                info['cast'].append(movie_cast(thing['id'])['cast'][0]['name'] + ", " + movie_cast(thing['id'])['cast'][1]['name'] + ", " + movie_cast(thing['id'])['cast'][2]['name'])
            elif leng > 1 :
                info['cast'].append(movie_cast(thing['id'])['cast'][0]['name'] + ", " + movie_cast(thing['id'])['cast'][1]['name'])
            elif leng > 0 :
                info['cast'].append(movie_cast(thing['id'])['cast'][0]['name'])
            else:
                info['cast'].append("No cast found")
            counter = counter + 1
        else:
            break
    return info

def get_trailer_youtube(movie_id):
    global API_KEY
    headers = {"Accept": "application/json"}
    request = Request("http://api.themoviedb.org/3/movie/" + str(movie_id) + "/trailers?api_key=" + API_KEY, headers=headers)
    response_body = urlopen(request).read()
    result = json.loads(response_body)
    if len(result['youtube']) > 0:
        return result['youtube'][0]['source']
    else:
        return
    
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

def latest_info():
    global temp
    global info
    temp = latest_movies()
    info = {}
    info['ids'] = temp['id']
    info['titles'] = temp['title']
    info['dates'] = temp['release_date']
    info['ratings'] = "Not available yet"
    info['trailer_ids'] = get_trailer_youtube(temp['id'])
    #info['cast']
    info['summary'] = temp['overview']
    return info

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

def popular_info():
    global temp
    temp = popular_movies()
    global result
    global info
    counter = 0
    info = {}
    info['ids'] = []
    info['titles'] = []
    info['dates'] = []
    info['ratings'] = []
    info['trailer_ids'] = []
    info['cast'] = []
    info['summary'] = []
    for thing in temp['results']:
        if counter < 6:
            info['ids'].append(thing['id'])
            info['titles'].append(thing['title'])
            info['dates'].append(thing['release_date'])
            info['ratings'].append(thing['vote_average'])
            if get_trailer_youtube(thing['id']):
                info['trailer_ids'].append(get_trailer_youtube(thing['id']))
            else:
                info['trailer_ids'].append("no trailer")
            global leng
            leng = len(movie_cast(thing['id'])['cast'])
            if leng > 2 :        
                info['cast'].append(movie_cast(thing['id'])['cast'][0]['name'] + ", " + movie_cast(thing['id'])['cast'][1]['name'] + ", " + movie_cast(thing['id'])['cast'][2]['name'])
            elif leng > 1 :
                info['cast'].append(movie_cast(thing['id'])['cast'][0]['name'] + ", " + movie_cast(thing['id'])['cast'][1]['name'])
            elif leng > 0 :
                info['cast'].append(movie_cast(thing['id'])['cast'][0]['name'])
            else:
                info['cast'].append("No cast found")
            counter = counter + 1
        else:
            break
    return info


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

def now_playing_info():
    global temp
    temp = now_playing_movies()
    global result
    global info
    counter = 0
    info = {}
    info['ids'] = []
    info['titles'] = []
    info['dates'] = []
    info['ratings'] = []
    info['trailer_ids'] = []
    info['cast'] = []
    info['summary'] = []
    for thing in temp['results']:
        if counter < 6:
            info['ids'].append(thing['id'])
            info['titles'].append(thing['title'])
            info['dates'].append(thing['release_date'])
            info['ratings'].append(thing['vote_average'])
            if get_trailer_youtube(thing['id']):
                info['trailer_ids'].append(get_trailer_youtube(thing['id']))
            else:
                info['trailer_ids'].append("no trailer")
            global leng
            leng = len(movie_cast(thing['id'])['cast'])
            if leng > 2 :        
                info['cast'].append(movie_cast(thing['id'])['cast'][0]['name'] + ", " + movie_cast(thing['id'])['cast'][1]['name'] + ", " + movie_cast(thing['id'])['cast'][2]['name'])
            elif leng > 1 :
                info['cast'].append(movie_cast(thing['id'])['cast'][0]['name'] + ", " + movie_cast(thing['id'])['cast'][1]['name'])
            elif leng > 0 :
                info['cast'].append(movie_cast(thing['id'])['cast'][0]['name'])
            else:
                info['cast'].append("No cast found")
            counter = counter + 1
        else:
            break
    return info



def upcoming_info():
    global temp
    temp = upcoming_movies()
    global result
    global info
    counter = 0
    info = {}
    info['ids'] = []
    info['titles'] = []
    info['dates'] = []
    info['ratings'] = []
    info['trailer_ids'] = []
    info['cast'] = []
    info['summary'] = []
    for thing in temp['results']:
        if counter < 6:
            info['ids'].append(thing['id'])
            info['titles'].append(thing['title'])
            info['dates'].append(thing['release_date'])
            info['ratings'].append(thing['vote_average'])
            if get_trailer_youtube(thing['id']):
                info['trailer_ids'].append(get_trailer_youtube(thing['id']))
            else:
                info['trailer_ids'].append("no trailer")
            global leng
            leng = len(movie_cast(thing['id'])['cast'])
            if leng > 2 :        
                info['cast'].append(movie_cast(thing['id'])['cast'][0]['name'] + ", " + movie_cast(thing['id'])['cast'][1]['name'] + ", " + movie_cast(thing['id'])['cast'][2]['name'])
            elif leng > 1 :
                info['cast'].append(movie_cast(thing['id'])['cast'][0]['name'] + ", " + movie_cast(thing['id'])['cast'][1]['name'])
            elif leng > 0 :
                info['cast'].append(movie_cast(thing['id'])['cast'][0]['name'])
            else:
                info['cast'].append("No cast found")
            counter = counter + 1
        else:
            break
    return info

def genre_info(genre_name):
    global genre
    info = {}
    for genre in get_genres()['genres']:
        if genre['name'] == genre_name:
            temp = get_movies_by_genre(genre['id'])
            break
    global result
    global info
    counter = 0
    info['ids'] = []
    info['titles'] = []
    info['dates'] = []
    info['ratings'] = []
    info['trailer_ids'] = []
    info['cast'] = []
    info['summary'] = []
    for thing in temp['results']:
        if counter < 6:
            info['ids'].append(thing['id'])
            info['titles'].append(thing['title'])
            info['dates'].append(thing['release_date'])
            info['ratings'].append(thing['vote_average'])
            if get_trailer_youtube(thing['id']):
                info['trailer_ids'].append(get_trailer_youtube(thing['id']))
            else:
                info['trailer_ids'].append("no trailer")
            global leng
            leng = len(movie_cast(thing['id'])['cast'])
            if leng > 2 :        
                info['cast'].append(movie_cast(thing['id'])['cast'][0]['name'] + ", " + movie_cast(thing['id'])['cast'][1]['name'] + ", " + movie_cast(thing['id'])['cast'][2]['name'])
            elif leng > 1 :
                info['cast'].append(movie_cast(thing['id'])['cast'][0]['name'] + ", " + movie_cast(thing['id'])['cast'][1]['name'])
            elif leng > 0 :
                info['cast'].append(movie_cast(thing['id'])['cast'][0]['name'])
            else:
                info['cast'].append("No cast found")
            counter = counter + 1
        else:
            break
    return info

if __name__ == "__main__":     
    print popular_info()