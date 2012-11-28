import utils
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
    """
    if request.method=='GET':
        return render_template("events.html")
    else:
        button=request.form['button']
        if button=='Go':
            borough=request.form["Borough"]
            events=utils.getB(borough)
            return render_template("events.html",Borough=borough,events=events)
    render_template("events.html")    

if __name__=="__main__":
    app.debug=True
    app.run()
