#!/usr/bin/python

import urllib
import json

import urllib2



#returns stuff nearby the given latitude and longtitute

url="http://api.nytimes.com/svc/semantic/v2/geocodes/query.xml?nearby=38.920833,-94.622222_&feature_class=P&api-key=your-API-key (no space after comma between lat/lon)"



request=urllib.urlopen(url)
result=json.loads(request.read())

print result
