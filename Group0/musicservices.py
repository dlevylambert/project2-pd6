import urllib
import json
from pymongo import Connection
from urllib2 import Request, urlopen
global connection, db, res, collection

#api_key = "ZPNZ4NM30OA84ZR2"
api_url = 'http://api.discogs.com'
def beg():
    global connection, db, res, collection
    connection = Connection('mongo.stuycs.org')
    db = connection.admin
    res = db.authenticate ('ml7', 'ml7')
    db = connection['z-pd6']
    collection = db['musicservices']

def getAlbuminfo(artist_name):
    headers = {"Accept" : "application/json"}
    request = Request("http://api.discogs.com/artist/" + artist_name)
    response_body = urlopen(request).read()
    result = json.loads(response_body)
    return result
#class Artist(APIBase):
    #def __init__(self, name, anv=None):
        #self._id = name
        #self._aliases = []
        #self._namevariations = []
        #self._releases = []
        #self._anv = anv or None
        #APIBase.__init__(self)
   

   # @property
    #def aliases(self):
        #if not self._aliases:
           # for alias in self.data.get('aliases', []):
              #  self._aliases.append(Artist(alias))
        #return self._aliases


#will work on more later
#url of site is http://freemusicarchive.org/api
