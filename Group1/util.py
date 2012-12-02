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


#I have no idea why the following tells me that 391 > 700 and that 391 < 700
def testing():
    print "data[0][11] is: "+data[0][11]
    if 391 < 700:
        print "391 < 700"
    if data[0][11] > 700:
        print "data[0][11] > 700"

#it's the same reason why this doesn't work
def testing2():
    i = 0
    for item in data:
        if data[i][11] > 600:
            print data[i][9]
        i = i + 1

if __name__ == "__main__":
    getSchools()
    testing2()
    testing()
