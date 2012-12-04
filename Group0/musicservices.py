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

###to later build data on an artist###
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
    except KeyError: #not all artists are bands, eg Lionel Richie
        pass         #has no key "members"
def getID(artist): return artist["resp"]["artist"]["id"]
def getArtist(artistID): return getArtistInfoByID(artistID)["name"]

###to later build data on a song###
def getTitle(release):
    try: return str(release["title"])
    except KeyError: pass
def getYear(release):
    try: return str(release["year"])
    except KeyError: pass
def getLabel(release):
    try: return str(release["label"])
    except KeyError: pass
def getPic(release):
    try: return str(release["thumb"])
    except KeyError: pass

def getReleaseByTitle(title,artistID):
    releases = getReleasesByID(artistID)
    for release in releases["releases"]:
        if release["title"] == title:
            return release

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
