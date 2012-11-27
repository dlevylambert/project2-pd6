import urllib
import json
import sys
import string

def call(q):
    urlstring = '%s/%s'%('http://api.nytimes.com/svc/movies/v2/reviews',q)
    print urlstring
    
    request = urllib.urlopen(urlstring)
    result = json.loads(request.read())
    return result

def getReviews(movie, date):
    #cleaning title for things like dash and colon, will probably have to add
    if string.find(movie, ':') > 0:
        movie = string.split(movie, ':')[1];
    if string.find(movie, ' - ') > 0:
        movie = string.split(movie, ' - ')[0];
    title = movie.replace(' ', '+')
    #requests data
    qstring = 'search.json?query=' + title + '&opening-date=' + date + '&api-key=d392ca168b1be29a3360f09ecdf195c6:0:66271972'
    result = call(qstring)
    for r in result['results']:
        if movie in r['display_title']:
            print r['display_title']
            link =  r['link']['url']
            print link
            print
            #check if empty here?
            return link 


getReviews('The Twilight Saga: Breaking Dawn - Part 2', '2012-11-16')
