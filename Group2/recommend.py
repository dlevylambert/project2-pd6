from urllib2 import Request, urlopen

id = 52591

def get_similar_movies(id):
    headers = {"Accept": "application/json"}
    request = Request("http://themoviedb.apiary.io/3/movie/" + id + "/similar_movies", headers=headers)
    response_body = urlopen(request).read()
    print response_body

get_similar_movies(id)
