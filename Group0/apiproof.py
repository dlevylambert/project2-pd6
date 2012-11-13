#!/usr/bin/python

import urllib
import json

url = "http://data.cityofnewyork.us/api/views/xenu-5qjw/rows.json"
#example- not the api for project
def getinfo(url):
    request= urllib.urlopen(url).read()
    return request

if __name__ == "__main__":
    url = "http://data.cityofnewyork.us/api/views/xenu-5qjw/rows.json"
    print getinfo(url)

    
