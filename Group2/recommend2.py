import json
import urllib
import sys
from urllib2 import Request, urlopen

API_KEY = "450062599145d021e7243a767de7c7d0"
ID = 52591

def authenticate_token(id):
    global API_KEY
    headers = {"Accept": "application/json"}
    request = urllib.urlopen("http://api.themoviedb.org/3/authentication/token/new?api_key=" + API_KEY)
    result = json.loads(request.read())
    print result
#doesn't work when I put headers in, but when I don't, it prints: {u'status_code': 19, u'status_message': u'Invalid accept header'}. Helen: canyou see what's wrong with that??? like how to add in the headers. also this method goes first, b/c then you need the "token" to authenticate the session I think.


def authenticate_session(id):
    global API_KEY
#this is after you get a token. but the site says this is for "write" access, idk if we need "write" access, or just pull stuff from it    


####NOT SURE WE NEED AUTHENTICATE METHODS FOR WHAT WE DO. ALSO LOOK I MADE THE FIND MOVIE THING WORK SO NOW WE CAN GET THE JSON FROM IT
    
def get_similar_movies(id):
    global API_KEY
    headers = {"Accept": "application/json"}
    request = Request("http://api.themoviedb.org/3/movie/550?api_key=" + API_KEY + "&append_to_response=releases", headers=headers)
    response_body = urlopen(request).read()
    print response_body


# + "&append_to_response=" + str(id) + "/similar_movies"

def get_movie(movie_name, id):
    global API_KEY
    headers = {"Accept": "application/json"}
    request = Request("http://api.themoviedb.org/3/search/movie?api_key=" + API_KEY + "&query=" + movie_name, headers=headers)
    response_body = urlopen(request).read()
    result = json.loads(response_body)
    print result
    return result

if __name__ == "__main__":     
    get_movie("uptown_girls",ID)
