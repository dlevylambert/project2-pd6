import urllib
import json
from pymongo import Connection
from urllib2 import Request, urlopen
global connection, db, res, collection

api_key = "ZPNZ4NM30OA84ZR2"

def beg():
    global connection, db, res, collection
    connection = Connection('mongo.stuycs.org')
    db = connection.admin
    res = db.authenticate ('ml7', 'ml7')
    db = connection['z-pd6']
    collection = db['musicservices']

def getAlbuminfo(album_title):
    headers = {"Accept" : "application/json"}
    request = Request("http://freemusicarchive.org/api/get/albums.json?api_key=ZPNZ4NM30OA84ZR2&album_title=" + str(album_title))
    response_body = urlopen(request).read()
    result = json.loads(response_body)
    return result

#will work on more later
#url of site is http://freemusicarchive.org/api
