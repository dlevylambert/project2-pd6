import urllib2

def proof(url):
    return urllib2.urlopen(url).read()

if __name__ == "__main__":
    print proof("https://data.cityofnewyork.us/api/views/xenu-5qjw")
