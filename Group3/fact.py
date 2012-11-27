from factual import *

KEY = "WaCvw1FbqneYWbpLP0hatFJOhwxDyy3dQUDeQjpF"
SECRET = "p6tAvjCwVrkqH5EU3FtlGyzfgrnmfvmH7KkuoMf9"

fact = Factual(KEY,SECRET)

cuisine = [ "Afghan", "American", "Argentine", "Asian", "Austrian", "Bagels",
            "Bakery", "Barbecue", "Belgian", "Bistro", "Brazilian", "British",
            "Buffet", "Burgers", "Cafe", "Cajun", "Californian", "Calzones",
            "Cambodian", "Caribbean", "Catering", "Cheesesteaks", "Chicken",
            "Chinese", "Chowder", "Coffee", "Colombian", "Contemporary", 
            "Continental", "Creole", "Crepes", "Cuban", "Czech", "Deli",
            "Dim Sum", "Diner", "Dominican", "Donuts", "Eastern European",
            "Eclectic", "English", "Ethiopian", "European", "Fast Food",
            "Filipino", "Fish and Chips", "Fondue", "French", "Frozen Yogurt",
            "Fusion", "Gastropub", "German", "Greek", "Grill", "Gyros",
            "Haitian", "Halal", "Hawaiian", "Healthy", "Hookah Bar", "Hot Dogs",
            "Ice Cream", "Indian", "Indonesian", "International", "Irish",
            "Israeli", "Italian", "Japanese", "Juices", "Korean", 
            "Korean Barbeque", "Kosher", "Latin", "Latin American", "Lebanese",
            "Malaysian", "Mediterranean", "Mexican", "Middle Eastern",
            "Mongolian", "Moroccan", "Nepalese", "Noodle Bar", "Norwegian",
            "Organic", "Oysters", "Pacific Rim", "Pakistani", "Pan Asian",
            "Pasta", "Pasteries", "Persian", "Peruvian", "Pho", "Pizza",
            "Polish", "Polynesian", "Portuguese", "Pub Food", "Puerto Rican",
            "Ribs", "Salad", "Salvadoran", "Sandwiches", "Seafood",
            "Singaporean", "Smoothies", "Soul Food", "Soup", "South American",
            "South Pacific", "Southern", "Southwestern", "Spanish", "Steak",
            "Subs", "Sushi", "Taiwanese", "Tapas", "Tea", "Tex Mex",
            "Thai", "Tibetan", "Traditional", "Turkish", "Ukrainian",
            "Vegan", "Vegetarian", "Venezuelan", "Venusian", "Vietnamese",
            "Wings", "Wraps" ]

#see https://github.com/Factual/factual-python-driver/blob/master/example.py
#and http://developer.factual.com/download/attachments/2392149/factual_cuisines.json?version=1&modificationDate=1323825420112

def getFirst():    
    table = fact.table("restaurants-us").filters({
            "locality":"new york"})
    res = table.data()[0]
    #return len(table.data())
    return [ res['name'] , res["cuisine"] , res['latitude'] , res['longitude']
             , res['address'] ]

def getCuisine(cuisine,limit=10):
    table = fact.table("restaurants-us").filters({
            "locality":"new york" , "cuisine":cuisine}).limit(limit)
    res = []
    for place in table.data():
        subres = [ place['name'] , place['longitude'] , place['latitude'] , 
                   place['address'] ]
        res.append(subres)
        
    return res
    

if __name__ == "__main__":
    print getCuisine("Tapas")[0]
