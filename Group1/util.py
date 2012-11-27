#!/usr/bin/python

import urllib2
import urllib
import json

def getThing(url):
    d = urllib2.urlopen(url).read()
    return d

if __name__ == "__main__":
    one = "http://data.cityofnewyork.us/api/views/zt9s-n5aj/rows.json"
    print getThing(one)
