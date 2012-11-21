from flask import Flask,render_template, url_for,redirect,request
import urllib2,json

app=Flask(__name__)

@app.route("/")
def index():
    return "<b>home</b>"

if __name__=="__main__":
    app.debug=True
    app.run()
