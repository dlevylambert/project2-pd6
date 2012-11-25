from flask import Flask,render_template, url_for,redirect,request
import urllib2,json
import util

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
#@app.route("/index",methods=["GET","POST"])
#@app.route("/index.html",methods=["GET","POST"])
#@app.route("/home",methods=["GET","POST"])
def index():
    if request.method=="GET":
        return render_template("index.html")
    else:
        button = request.form["button"]
        foodtype = request.form["carttype"]
        if foodtype == "Foodcart":
            res = util.randomRestaurant()
            resName = res[0].text
            resLoc = res[1].text
            resLat = res[7].text
            resLong = res[8].text
            return render_template("index.html",resName=resName,resLat=resLat,
                                   resLong=resLong,resLoc=resLoc)
        else:
            #temporary
            return render_template("index.html")

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
