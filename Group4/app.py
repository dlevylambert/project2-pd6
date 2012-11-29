from flask import Flask,render_template,request,url_for,redirect,session
import util
from twilio import twiml
import time
from threading import Timer
import os

app = Flask(__name__)
app.secret_key = 'superduperkeyofsecretness'
currentreminder = 0
reminderlist = []

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
    return render_template('calendar.html',first=int(util.getFirstDay(month,year)),counter=0, RTh = util.getTimeWeb(session['user'])[0], RTm = util.getTimeWeb(session['user'])[1], RTampm = util.getTimeWeb(session['user'])[2])

@app.route('/update',methods=['GET','POST'])
def update():
    if request.method=='POST':
        num = request.form['From']
        data = request.form['Body']
        requestType = util.processEvent(num,data)
        if requestType == 0:
            util.sendResponse(num)
    return redirect(url_for('menu'))

def remindersHandler(initial):
    if (not initial):
        pass
    global reminderlist
    os.environ['TZ'] = "US/Eastern"
    time.tzset()
    timenow = time.strftime("%H:%M:%S",time.localtime())
    times = reminderlist.keys()
    timeinsecsnow = 0
    timeinsecsnext = 0
    nextTime = 0
    tmp = timenow.split(":")
    hournow = int(tmp[0])
    minutenow = int(tmp[1])
    secnow = int(tmp[2])
    for item in times:
        itemhour = int(item.split(":")[0])
        itemminute = int(item.split(":")[1])
        if hournow > itemhour and minutenow > itemminute:
            break
        else:
            timeinsecsnext = itemminute*60 + itemhour*3600
    timeinsecsnow = minutenow*60 + hournow*3600 + secnow
    nextTime = timeinsecsnext - timeinsecsnow
    if nextTime < 0:
        nextTime = (timeinsecsnext+86400) - timeinsecsnow
    print timenow
    print "now: "+str(timeinsecsnow) + "  next: " + str(timeinsecsnext) 
    print nextTime
    reminder = Timer(nextTime,remindersHandler(False))

if __name__ == "__main__":
    reminderlist = util.getReminderTimes()
    remindersHandler(True)
    app.debug = True 
    app.run(host='0.0.0.0', port=6004)
