import proof
from flask import Flask, request, render_template, url_for, redirect

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def home():
    Bk=getB("Brooklyn")
    Bx=getB("Bronx")
    SI=getB("Staten Island")
    M=getB("Manhattan")
    Q=getB("Queens")
    if request.method=='GET':
        return render_template("home.html")
    else:
        button=request.form['button']
        if button=="Before":
            
