import json
import urllib
import sys
from urllib2 import Request, urlopen


id = 52591

class Rester:
    def __init__(self, url):
        self.url = url
    def call(self, q):
        urlstring = "%s?%s"%(self.url, q)
        print urlstring
        request = urllib.urlopen(urlstring)
        result = json.loads(request.read())
        return result
    def authentication(self):
        headers = {"Accept": "application/json"}
        self.call("/3/authentication/token/new")
    

test = Rester("http://themoviedb.apiary.io")
test.authentication()

#http://api.themoviedb.org/3/movie/550?api_key=450062599145d021e7243a767de7c7d0

#result = test.call(qstring)
#print result

#def get_similar_movies(id):
#    headers = {"Accept": "application/json"}
#    request = Request("http://themoviedb.apiary.io/3/movie/" + str(id) + "/similar_movies", headers=headers)
#    response_body = urlopen(request).read()
#    print response_body

#get_similar_movies(id)

