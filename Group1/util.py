#!/usr/bin/python

import urllib2
import urllib
import json

satScores = json.loads(urllib2.urlopen("http://data.cityofnewyork.us/api/views/zt9s-n5aj/rows.json").read())
data = satScores["data"]

def getSchools():
    i = 0
    for item  in data:
        print data[i][9]
        i = i + 1


def testing2():
    if int(data[0][11], base=10) == 391:
        print "testing2 works"

#gives an error saying int() can't convert non-string with explicit base?
def testing():
    i = 0
    for item in data:
        if int(data[i][11], base=10) > 600:
            print data[i][9]
        i = i + 1

if __name__ == "__main__":
    getSchools()
    testing2()
    testing()
