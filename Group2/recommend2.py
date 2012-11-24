import json
import urllib
import sys
from urllib2 import Request, urlopen

API_KEY = "450062599145d021e7243a767de7c7d0"
ID = 52591

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
    print result['results'][0]['id']
    return result

if __name__ == "__main__":     
    get_movie("uptown_girls",ID)
