import urllib2

def proof(url):
    return urllib2.urlopen(url).read() 

url ="https://data.cityofnewyork.us/api/views/xenu-5qjw/rows.json"
request = proof(url)


if __name__ == "__main__":
    print request
        
