import urllib2

def proof(url):
    return urllib2.urlopen(url).read()

if __name__ == "__main__":
    one = "https://data.cityofnewyork.us/api/views/ens7-ac7e?"
    two = "https://data.cityofnewyork.us/api/views/zt9s-n5aj"
    print proof(one)
    print proof(two)
