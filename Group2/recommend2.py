import json
import urllib
import sys
from urllib2 import Request, urlopen

API_KEY = "450062599145d021e7243a767de7c7d0"
ID = 52591

def authenticate(id):
    global API_KEY
    headers = {"Accept": "application/json"}
    request = urllib.urlopen("http://api.themoviedb.org/3/authentication/token/new?api_key=" + API_KEY)
    result = json.loads(request.read())
    print result

def get_similar_movies(id):
    global API_KEY
    headers = {"Accept": "application/json"}
    request = Request("http://api.themoviedb.org/3/movie/550?api_key=" + API_KEY + "&append_to_response=releases", headers=headers)
    response_body = urlopen(request).read()
    print response_body


# + "&append_to_response=" + str(id) + "/similar_movies"


if __name__ == "__main__":     
    get_similar_movies(ID)
    authenticate(ID)
    
