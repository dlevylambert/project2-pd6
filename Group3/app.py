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
       cuisine = request.form["cuisine"] 
       res = fact.getCuisine(cuisine)
       return render_template("index.html",restaurantList=res)
             #restaurantList is a list of lists (see fact.py)

@app.route("/locations")
def locations():
    res = util.randomRestaurant()
    resName = res[0].text
    resLoc = res[1].text
    resLat = res[7].text
    resLong = res[8].text
    #print resName,resLat,resLong,resLoc
    #return "<b>home</b>"
    return render_template("res.html",resName=resName,resLat=resLat,
                           resLong=resLong,resLoc=resLoc)

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
