import json
import urllib2

#GiantBomb (requires API key)
url = "http://api.giantbomb.com/character/248/?api_key=9b2526fdab907c6deae7ad3d7c79483cb0358728&format=xml"

#The Games DB (might require API key)
url2 = "http://thegamesdb.net/api/GetGamesList.php?name=halo"

request=urllib2.urlopen(url2).read()

print request
