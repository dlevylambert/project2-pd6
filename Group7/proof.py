import urllib2
import json
from operator import  itemgetter

def proof(url):
    return json.loads(urllib2.urlopen(url).read()) 

url ="https://data.cityofnewyork.us/api/views/xenu-5qjw/rows.json"
events=[]
for i in proof(url)['data']:
    events.append(i)

print events
