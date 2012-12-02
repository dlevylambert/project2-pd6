from factual import *
import random

KEY = "WaCvw1FbqneYWbpLP0hatFJOhwxDyy3dQUDeQjpF"
SECRET = "p6tAvjCwVrkqH5EU3FtlGyzfgrnmfvmH7KkuoMf9"

fact = Factual(KEY,SECRET)

cuisine = ['American', 'Argentine', 'Asian', 'Bagels', 'Bakery', 'Barbecue', 'Bistro', 'Brazilian', 'Burgers', 'Cafe', 'Caribbean', 'Catering', 'Chicken', 'Chinese', 'Coffee', 'Contemporary', 'Continental', 'Crepes', 'Cuban', 'Deli', 'Diner', 'Dominican', 'Donuts', 'Eastern European', 'Eclectic', 'Ethiopian', 'Fast Food', 'French', 'German', 'Greek', 'Hawaiian', 'Healthy', 'Hot Dogs', 'Ice Cream', 'Indian', 'International', 'Irish', 'Italian', 'Japanese', 'Juices', 'Korean', 'Kosher', 'Latin American', 'Malaysian', 'Mediterranean', 'Mexican', 'Middle Eastern', 'Moroccan', 'Pan Asian', 'Persian', 'Pizza', 'Polish', 'Pub Food', 'Salad', 'Sandwiches', 'Seafood', 'Smoothies', 'Soup', 'South American', 'Southern', 'Southwestern', 'Spanish', 'Steak', 'Sushi', 'Tapas', 'Thai', 'Turkish', 'Vegetarian', 'Vietnamese']


#see https://github.com/Factual/factual-python-driver/blob/master/example.py
#and http://developer.factual.com/download/attachments/2392149/factual_cuisines.json?version=1&modificationDate=1323825420112

def getFirst():    
    table = fact.table("restaurants-us").filters({
            "locality":"new york"})
    res = table.data()[0]
    #return len(table.data())
    return [ res['name'] , res["cuisine"] , res['latitude'] , res['longitude']
             , res['address'] ]

def getCuisine(cuisine,limit=30):
    if not cuisine: return []
    table = fact.table("restaurants-us").filters({
            "locality":"new york" , "cuisine":cuisine}).limit(limit)
    res = []
    for place in table.data():
        subres = [ place['name'] , place['longitude'] , place['latitude'] , 
                   place['address'] ]
        res.append(subres)
        
    return res

def findRandomRestaurant(cuis = ""):
	res = []
	if cuis == "":
		while len(res) == 0:
			cuis2 = cuisine[random.randrange(0,len(cuisine) - 1)]
			res = getCuisine(cuis2)
		return [res[random.randrange(0, len(res))], cuis2]
	else:
		res = getCuisine(cuis)
	return [res[random.randrange(0, len(res))], cuis]

def findRestaurant(cuisine, restaurant):
    	if not cuisine: 
		return []
	cuises = getCuisine(cuisine)
	n = int(restaurant[len(restaurant) - 1])
	for r in cuises:
		if r[0] == restaurant[:len(restaurant) - 1]:
			if n == 0:
				return r
			else:
				n = n -1
	return []

if __name__ == "__main__":
    print getCuisine("Afghan")
