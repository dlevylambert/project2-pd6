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
#also an 'image' key with the game image
#and a description

def search(query, offset):
    everything = simplejson.load((urllib2.urlopen(baseurl + "/search/?api_key=%s&resources=game&query=%s&field_list=name,id,description,image&offset=%s&format=json" % (key, urllib2.quote(query), offset))))
    
    results = everything["results"]
    names = []
    id = []
    images = []
    descriptions = []
    for i in range(0, len(results)):
        names += [results[i]["name"]]
        id += [results[i]["id"]]
        images += [results[i]["image"]]
        descriptions += [results[i]["description"]]
    answer = {}
    answer['names'] = names
    answer['id'] = id
    answer['images'] = images
    answer['descriptions'] = descriptions

    return answer



#IMPORTANT: NEEDS THE ID ----- NOT THE NAME
#now take a deep breath - here's what happens:
#it returns a dictionary with keys (duh I guess)
#now the important keys can be read right there next to where it says _list
#for example, you have id, name, image, etc
#use these for whatever you want

def getGame(id):
    game = simplejson.load(urllib2.urlopen(baseurl + "/game/%s/?api_key=%s&field_list=id,name,image,genres,original_release_date,platforms&format=json" % (key,id)))
    return game['results']


#supposed to return the rating - I don't know how it works
def getRating(id):
    rating = simplejson.load(urllib2.urlopen(baseurl + "/game_rating/%s/?api_key=%s&field_list=name,rating_board&format=json" % (key,id)))
    print rating

print search('mario', 0)['names']
#getGame(410)
#getRating(410)
