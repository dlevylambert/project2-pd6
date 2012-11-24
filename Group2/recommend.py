import urllib
import json
import sys

class Rester:
    def __init__(self,url):
        self.url = url

    def call(self,q):
        urlstring = "%s/%s"%(self.url,q)
        print urlstring
        
        request = urllib.urlopen(urlstring)
        #result = request.read();
        result = json.loads(request.read())
        return result


r = Rester("http://api.nytimes.com/svc/movies/v2/reviews")
qstring = "search.json?query=big&thousand-best=Y&opening-date=1930-01-01;2000-01-01&api-key=d392ca168b1be29a3360f09ecdf195c6:0:66271972"

result = r.call(qstring) # remember rester converts from json

for r in result['results']:
    print r['display_title']
    print
