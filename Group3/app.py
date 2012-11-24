from flask import Flask,render_template, url_for,redirect,request
import urllib2,json
import util

app=Flask(__name__)

@app.route("/")
@app.route("/index")
@app.route("/index.html")
@app.route("/home")
def index():
    res = util.randomRestaurant()
    resName = res[0].text
    resLoc = res[1].text
    resLat = res[7].text
    resLong = res[8].text
    #print resName,resLat,resLong,resLoc
    #return "<b>home</b>"
    return render_template("index.html",resName=resName,resLat=resLat,
                           resLong=resLong,resLoc=resLoc)

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
