#!/usr/bin/python

import urllib
import json as simplejson
import urllib2


key = "9b2526fdab907c6deae7ad3d7c79483cb0358728"
baseurl = 'http://api.giantbomb.com/'


# enter a string for the name of game to be searched
#enter the offset number - typically 0, but if the user wants to
#see more results, simply increment the number by 20
#returns an array with a list of the names of 20 games

def search(query, offset):
    everything = simplejson.load((urllib2.urlopen(baseurl + "/search/?api_key=%s&resources=game&query=%s&field_list=name&offset=%s&format=json" % (key, urllib2.quote(query), offset))))
    
    results = everything["results"]
    names = []
    for i in range(0, len(results)):
        names += [results[i]["name"]]

    return names
#print search('mario', 0)

