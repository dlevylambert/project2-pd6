import urllib
import json
from pymongo import Connection
from urllib2 import Request, urlopen
global connection, db, res, collection
#import discogs_client

discogs.user_agent = 'musicbox'
#api_key = "ZPNZ4NM30OA84ZR2"
api_url = 'http://api.discogs.com'
def beg():
    global connection, db, res, collection
    connection = Connection('mongo.stuycs.org')
    db = connection.admin
    res = db.authenticate ('ml7', 'ml7')
    db = connection['z-pd6']
    collection = db['musicservices']
    

def getArtistinfo(artist_name):
    headers = {"Accept" : "application/json"}
    request = Request("http://api.discogs.com/artist/" + artist_name, headers = headers)
    response_body = urlopen(request).read()
    result = json.loads(response_body)
    return result #Artistinfo gives ID as well so someone can search releases!
    # artist = discogs.Artist('artist_name').data
    #print artist
def getArtistinfoID(artist_id):
    headers = {"Accept" : "application/json"}
    request = Request("http://api.discogs.com/artists/" + (str)artist_id, headers = headers)
    response_body = urlopen(request).read()
    result = json.loads(response_body)
    return result

def getReleasesID(artist_id):
    headers = {"Accept" : "application/json"}
    request = Request("http://api.discogs.com/artists/" + (str)artist_id +"/releases", headers = headers)
    response_body = urlopen(request).read()
    result = json.loads(response_body)
    return result

def getcertainrelease(release_id):
    headers = {"Accept" : "application/json"}
    request = Request("http://api.discogs.com/releases/" + (str)release_id, headers = headers)
    response_body = urlopen(request).read()
    result = json.loads(response_body)
    return result # can get from artist' releases
    #release = discogs.Release(artist_id)
    #release.tracklist

#if __name__ == "__main__":
