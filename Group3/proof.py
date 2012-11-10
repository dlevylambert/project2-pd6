import urllib
import json

def getRes(url):
    req = urllib.urlopen(url)
    res = json.loads(req.read())
    return res

if __name__ == "__main__":

    # nyc opendata - street events listing
    url = "http://data.cityofnewyork.us/api/views/xenu-5qjw/rows.json"
    print getRes(url)['meta']['view']['description']

    # heroku be there nyc 
    url = "http://betherenyc.com/api/search" #?date=2012-07-04"
    #print getRes(url) # the data should come in an array
    #print urllib.urlopen(url) # but instead returns a cursor-like object?

    # note: eventful (api.eventful.com) uses oAuth
    # and, as such, will not be tested yet
