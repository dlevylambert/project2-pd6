import urllib
import json
import xml.etree.ElementTree as ET

def getRes(url):
    req = urllib.urlopen(url)
    res = json.loads(req.read())
    return res

def xmlStuff():
    tree = ET.parse("DPR_Eateries.xml")
    root = tree.getroot()
    return root[0][0][0].tag + " : " + root[0][0][0].text
    

if __name__ == "__main__":

    # nyc opendata - street events listing
    url = "http://data.cityofnewyork.us/api/views/xenu-5qjw/rows.json"
    print getRes(url)['meta']['view']['name']

    print "----------------"

    url = "http://data.cityofnewyork.us/api/views/fiaa-wgtd/rows.json"
    print getRes(url)['meta']['view']['name']

    print "----------------"

    #from github: info on restaurants from food-tech hackathon
    print xmlStuff()

    # note: google places and map APIs have limits
    # after which, they charge you

    # heroku be there nyc 
    url = "http://betherenyc.com/api/search" #?date=2012-07-04"
    #print getRes(url) # the data should come in an array
    #print urllib.urlopen(url) # but instead returns a cursor-like object?

    # note: eventful (api.eventful.com) uses oAuth
    # and, as such, will not be tested yet
