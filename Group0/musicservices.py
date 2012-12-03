import urllib
import json
from pymongo import Connection
from urllib2 import Request, urlopen
import discogs_client as discogs

discogs.user_agent = 'musicbox'
conn = Connection("mongo.stuycs.org")

#api_key = "ZPNZ4NM30OA84ZR2"
api_url = 'http://api.discogs.com'

def beg():
    db = conn.admin
    res = db.authenticate ('ml7', 'ml7')
    db = connection["musicservices"]
    collection = db.first_collection    

def getArtistInfo(artist_name):
    headers = {"Accept" : "application/json"}
    request = Request("http://api.discogs.com/artist/" + artist_name, headers = headers)
    response_body = urlopen(request).read()
    result = json.loads(response_body)
    return result #Artistinfo gives ID as well so someone can search releases!
    # artist = discogs.Artist('artist_name').data
    #print artist

def getArtistInfoByID(artist_id):
    headers = {"Accept" : "application/json"}
    request = Request("http://api.discogs.com/artists/" + str(artist_id), headers = headers)
    response_body = urlopen(request).read()
    result = json.loads(response_body)
    return result

def getName(artist):
    try:
        return str(artist["resp"]["artist"]["name"])
    except KeyError:
        pass
def getProfile(artist):
    try: 
        return str(artist["resp"]["artist"]["profile"])
    except KeyError:
        pass
def getMembers(artist):
    try:
        return [str(line) for line in  artist["resp"]["artist"]["members"]]
    except KeyError:
        pass
def getID(artist): return artist["resp"]["artist"]["id"]


def getReleasesByID(artist_id):
    headers = {"Accept" : "application/json"}
    request = Request("http://api.discogs.com/artists/" + str(artist_id) +"/releases", headers = headers)
    response_body = urlopen(request).read()
    result = json.loads(response_body)
    return result

def getCertainRelease(release_id):
    headers = {"Accept" : "application/json"}
    request = Request("http://api.discogs.com/releases/" + str(release_id), headers = headers)
    response_body = urlopen(request).read()
    result = json.loads(response_body)
    return result # can get from artist' releases
    #release = discogs.Release(artist_id)
    #release.tracklist

#if __name__ == "__main__":
