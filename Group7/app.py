import utils
import urllib2,json
from flask import Flask, request, render_template, url_for, redirect

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def home():
    """
    Bk=getB("Brooklyn")
    Bx=getB("Bronx")
    SI=getB("Staten Island")
    M=getB("Manhattan")
    Q=getB("Queens")
    
    if request.method=='GET':
        return render_template("events.html")
    else:
        button=request.form['button']
        if button=='Go':
            borough=request.form["Borough"]
            events=utils.getB(borough)
            return render_template("events.html",Borough=borough,events=events)
    render_template("events.html")    
    """
    return render_template("events.html")

@app.route("/get_events")
def get_events():
    borough=request.args.get('Borough','')
    events=utils.getB(borough)
    return json.dumps(events)

@app.route("/get_e_after")
def get_e_after():
    month=request.args.get('Month','')
    day=request.args.get('Day','')
    year=request.args.get('Year','')
    borough=request.args.get('Borough','')
    events=utils.geteAfter(month,day,year,borough)
    return json.dumps(events)

@app.route("/get_e_on")
def get_e_on():
    month=request.args.get('Month','')
    day=request.args.get('Day','')
    year=request.args.get('Year','')
    borough=request.args.get('Borough','')
    events=utils.geteOn(month,day,year,borough)
    return json.dumps(events)

@app.route("/get_e_before")
def get_e_before():
    month=request.args.get('Month','')
    day=request.args.get('Day','')
    year=request.args.get('Year','')
    borough=request.args.get('Borough','')
    events=utils.geteBefore(month,day,year,borough)
    return json.dumps(events)

if __name__=="__main__":
    app.debug=True
    app.run(port=6207)
