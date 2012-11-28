from flask import Flask,render_template,request,url_for,redirect,session
import util
from twilio import twiml

app = Flask(__name__)
app.secret_key = 'superduperkeyofsecretness'

@app.route('/')
def start():
    return redirect(url_for('login'))

@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('login1.html')
    else:
        if request.form.has_key('login'):
            user = str(request.form['user'])
            password = str(request.form['pass'])
            if user in util.getUsernames():
                if password == util.checkPassword(user):
                    session['user'] = user
                    return redirect(url_for('calendar',year=util.thisYear(),month=util.thisMonth()))
            return render_template('login2.html')
        if request.form.has_key('newuser'):
            return redirect(url_for('newuser'))

@app.route('/newuser/',methods=['GET','POST'])
def newuser():
    if request.method=='GET':
        return render_template('newuser.html',notmatching=False,taken=False)
    else: 
        if request.form.has_key('submit'):
            user = request.form['user']
            password1 = request.form['pass1']
            password2 = request.form['pass2']
            number = request.form['num']
            if user in util.getUsernames():
                return render_template('newuser.html',notmatching=False,taken=True)
            if password1 != password2:
                return render_template('newuser.html',notmatching=True,taken=False)
            util.createNewUser(user,password1,number)
            return redirect(url_for('login'))
        
@app.route('/calendar/<year>/<month>',methods=['GET','POST'])
def calendar(month,year):
    return render_template('calendar.html',first=int(util.getFirstDay(month,year)),counter=0)

@app.route('/update',methods=['GET','POST'])
def update():
    if request.method=='POST':
        num = request.form['From']
        data = request.form['Body']
        requestType = util.processEvent(num,data)
        if requestType == 0:
            util.sendResponse(num)
    return redirect(url_for('menu'))

if __name__ == "__main__":
    app.debug = True 
    app.run(host='0.0.0.0', port=6004)
    
