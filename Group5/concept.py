#!/usr/bin/python

import urllib
import json

import urllib2



#returns stuff nearby the given latitude and longtitute 
#This is the general information of the area

url="http://api.nytimes.com/svc/semantic/v2/geocodes/query.json?nearby=38.920833,-94.622222_&feature_class=P&api-key=d575055f9ce4d2f35e76d42c3ff476c2:18:66928926"



#returns census information - I still need to get a key for this
#gives the population of the current region (NYC)


urltwo="http://api.usatoday.com/open/census/pop?keypat=New York&keyname=placename&sumlevid=3&api_key=XXXXXX"

#google maps api

#not sure how this works yet


request=urllib2.urlopen(url).read()
#result=json.loads(request.read())
print request

request=urllib.urlopen(urltwo)
#result=json.loads(request.read())
#print result
