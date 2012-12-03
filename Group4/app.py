from flask import Flask,render_template,request,url_for,redirect,session
import util
from twilio import twiml
import time
import threading 
import os

app = Flask(__name__)
app.secret_key = 'superduperkeyofsecretness'
currentreminder = 0
reminderlist = []
minutelist = []

for num in range(60):
    minutelist.append("0"+str(num))


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
                    return redirect(url_for('calendar',year=int(util.thisYear()),month=util.thisMonth()))
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
    if request.method=='GET':
        return render_template('calendar.html',first=int(util.getFirstDay(month,year)),counter=0,minutelist=minutelist,calbuilder=1,month=month,trcounter=1,foundfirst=0,year=int(year))
    else:
        if request.form.has_key('Next'):
            nextmonth = util.nextMonth(month)
            if nextmonth == 'January':
                yearnext = str(int(year) + 1)
            else:
                yearnext = year
            return redirect(url_for('calendar',year=yearnext,month=nextmonth))
        if request.form.has_key('Previous'):
            prevmonth = util.prevMonth(month)
            if prevmonth == 'December':
                yearprev = str(int(year) - 1)
            else:
                yearprev = year
            return redirect(url_for('calendar',year=yearprev,month=prevmonth))

@app.route('/update',methods=['GET','POST'])
def update():
    if request.method=='POST':
        num = request.form['From']
        data = request.form['Body']
        requestType = util.processEvent(num,data)
        if requestType == 0:
            util.sendResponse(num)
        if requestType == 1:
            reminderlist = util.getReminderTimes()
            print reminderlist
            threading.enumerate()[1].cancel()
            remindersHandler(True,0)
    return redirect(url_for('menu'))

def remindersHandler(initial,waitTime):
    #threading.Event().wait(waitTime)
    global reminderlist
    os.environ['TZ'] = 'US/Eastern'
    time.tzset()
    timenow = time.strftime("%H:%M:%S",time.localtime())
    tmp = timenow.split(":")
    if (not initial):
        for user in reminderlist[str(tmp[0])+":"+str(tmp[1])]:
            if util.remindersEnabled(user):
                message = util.eventsToMessage(util.getEventsToday(user))
                if message != "":
                    util.sendSomething(util.getUserNumber(user),message)
    times = reminderlist.keys()
    timeinsecsnow = 0
    timeinsecsnext = 0
    timeinsecsprev = 0
    nextTime = 0
    hournow = int(tmp[0])
    minutenow = int(tmp[1])
    secnow = int(tmp[2])
    found = False
    timeinsecsnextperm = 86000
    timeinsecsleast = 86000
    timeinsecsnow = hournow*3600 + minutenow*60 + secnow
    for item in times:
        itemhour = int(item.split(":")[0])
        itemminute = int(item.split(":")[1])
        timeinsecsnext = itemminute*60 + itemhour*3600
        if timeinsecsnext < timeinsecsleast:
            timeinsecsleast = timeinsecsnext
        if timeinsecsnow < timeinsecsnext:
            if timeinsecsnextperm > timeinsecsnext:
                found = True
                timeinsecsnextperm = timeinsecsnext
    if not found:
        timeinsecsnextperm = timeinsecsleast
    nextTime = timeinsecsnextperm - timeinsecsnow
    if nextTime < 0:
        nextTime = (timeinsecsnextperm+86400) - timeinsecsnow
    print nextTime
    arguments = (False,nextTime)
    reminder = threading.Timer(nextTime,remindersHandler,args=arguments)
    reminder.setDaemon(True)
    reminder.start()

if __name__ == "__main__":
    reminderlist = util.getReminderTimes()
    remindersHandler(True,0)
    app.debug = True 
    app.run(host='0.0.0.0', port=6004,use_reloader=False)
    
