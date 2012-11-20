#!/usr/bin/python

import urllib
import json as simplejson
import urllib2


key = "9b2526fdab907c6deae7ad3d7c79483cb0358728"
baseurl = 'http://api.giantbomb.com/'


# enter a string for the name of game to be searched
#enter the offset number - typically 0, but if the user wants to
#see more results, simply increment the number by 20
#returns a dictionary with a 'name' key containing names and 'id' with id's

def search(query, offset):
    everything = simplejson.load((urllib2.urlopen(baseurl + "/search/?api_key=%s&resources=game&query=%s&field_list=name,id&offset=%s&format=json" % (key, urllib2.quote(query), offset))))
    
    results = everything["results"]
    names = []
    id = []
    for i in range(0, len(results)):
        names += [results[i]["name"]]
        id += [results[i]["id"]]
    answer = {}
    answer['names'] = names
    answer['id'] = id

    return answer



#IMPORTANT: NEEDS THE ID ----- NOT THE NAME
#now take a deep breath - here's what happens:
#it returns a dictionary with keys (duh I guess)
#now the important keys can be read right there next to where it says _list
#for example, you have id, name, image, etc
#use these for whatever you want

def getGame(id):
    game = simplejson.load(urllib2.urlopen(baseurl + "/game/%s/?api_key=%s&field_list=id,name,image,genres,original_release_date,platforms&format=json" % (id,key)))
     return game['results']


#print search('mario', 0)
#getGame(410)
