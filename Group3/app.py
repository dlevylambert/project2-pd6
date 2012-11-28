from flask import Flask,render_template, url_for,redirect,request
import urllib2,json
import util,fact

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
#@app.route("/index",methods=["GET","POST"])
#@app.route("/index.html",methods=["GET","POST"])
#@app.route("/home",methods=["GET","POST"])
def index():
    if request.method=="GET":
        return render_template("index.html",cuisineList=fact.cuisine)
    else:
       	button = request.form["button"]
       	if button == "Choose":
       		global cuisine
		cuisine = request.form["cuisine"] 
       		res = fact.getCuisine(cuisine)
		if len(res) > 0:
       			return render_template("index.html", restaurantList=res)
		else:
			return render_template("index.html", cuisineList=fact.cuisine, alert = 10)
             	#restaurantList is a list of lists (see fact.py)
	else:
		resName = request.form["restaurant"]
		restaurant = fact.findRestaurant(cuisine, resName)
		resLoc = restaurant[3]
		resLat = restaurant[2]
		resLong = restaurant[1]
		return render_template("index.html",resLoc = resLoc, resLat = resLat, resLong = resLong, resName = resName, restaurantList=fact.getCuisine(cuisine))

if __name__=="__main__":
    app.debug=True
    app.run()


#unused:
#button = request.form["button"]
        #foodtype = request.form["carttype"]
        #if foodtype == "Foodcart":
         #   res = util.randomRestaurant()
          #  resName = res[0].text
           # resLoc = res[1].text
         #   resLat = res[7].text
          #  resLong = res[8].text
           # return render_template("index.html",resName=resName,resLat=resLat,
               #                    resLong=resLong,resLoc=resLoc)
       # else: #if foodtype == "Restaurant":
        #    res = fact.getData()
         #   resName = res[0]
          #  resLoc = res[4]
           # resLat = res[2]
          #  resLong = res[3]
           # return render_template("index.html",resName=resName,resLat=resLat,
            #                       resLong=resLong,resLoc=resLoc)
        #temporary
        #button = request.form["button"]
        #foodtype = request.form["carttype"]
        #if foodtype == "Foodcart":
         #   res = util.randomRestaurant()
          #  resName = res[0].text
           # resLoc = res[1].text
         #   resLat = res[7].text
          #  resLong = res[8].text
           # return render_template("index.html",resName=resName,resLat=resLat,
               #                    resLong=resLong,resLoc=resLoc)
       # else: #if foodtype == "Restaurant":
        #    res = fact.getData()
         #   resName = res[0]
          #  resLoc = res[4]
           # resLat = res[2]
          #  resLong = res[3]
           # return render_template("index.html",resName=resName,resLat=resLat,
            #                       resLong=resLong,resLoc=resLoc)
        #temporary
       # return render_template("index.html",cuisineList=fact.cuisine)
