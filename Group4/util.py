import urllib
import json
import sys
import time
import base64
from pymongo import Connection
from twilio.rest import TwilioRestClient
from twilio import twiml


Conn = Connection('ds041367.mongolab.com',41367)
db = Conn['stuycs_sideprojects']
res = db.authenticate('stuycs','stuycs')
mongo = db.Project2

account = 'ACd118dcbff7f480ecd7ba59b8c217e87f'
token = '3acfc74ebcc11a59f4332bea592e7a1e'
client = TwilioRestClient(account,token)

phonenum = '+16468074041'

def createNewUser(user,password,number):
    tmp = base64.b64encode(password)
    number = str(number).strip(' -+_()')
    if len(number) == 11:
        number = number[1:]
    if len(number) == 10:
        newuser = {"user" : user, "pass" : tmp, "number" : number, "calinfo" : {'2012' : {'1':{},'2':{},'3':{},'4':{},'5':{},'6':{},'7':{},'8':{},'9':{},'10':{},'11':{},'12':{}}},"reminderTime":"8:00am","remindersEnabled":True}
        mongo.insert(newuser)
        return True
    else:
        return False

def checkPassword(user):
    tmp = mongo.find_one({"user":user})
    password = base64.b64decode(tmp['pass'])
    return password

def getUsernames():
    tmp = mongo.find()
    users = []
    for line in tmp:
        users.append(str(line['user']))
    return users

def getFirstDay(month,year):
    date = time.strptime("01 "+str(month)+" "+str(year),"%d %B %Y")
    return time.strftime("%w",date)

def thisYear():
    return time.strftime("%Y",time.localtime())
def thisMonth():
    return time.strftime("%B",time.localtime())
def thisDay():
    return time.strftime("%d",time.localtime())
def thisMonthNum():
    return time.strftime("%m",time.localtime())
def nextMonth(month):
    forward = int(time.strftime("%m",time.strptime(month,"%B"))) + 1
    if forward == 13:
        forward = 1
    forwardstring = ""
    if forward < 10:
        forwardstring = "0"+ str(forward)
    else:
        forwardstring = str(forward)
    return time.strftime("%B",time.strptime(forwardstring,"%m"))
def prevMonth(month):
    back = int(time.strftime("%m",time.strptime(month,"%B"))) - 1
    if back == 0:
        back = 12
    backstring = ""
    if back < 10:
        backstring = "0"+ str(back)
    else:
        backstring = str(back)
    return time.strftime("%B",time.strptime(backstring,"%m"))

def getPhoneNumbers():
    tmp = mongo.find()
    users = []
    for line in tmp:
        users.append(str(line['number']))
    return users

def getTextLog():
    for message in client.sms.messages.list():
        print message.body
        #lines = message.body.split('\n')
        #print lines[0]

def getUserNumber(user):
    tmp = mongo.find_one({'user':user})
    return tmp['number']

def getMostRecent():
    updates = client.sms.messages.list()
    recent = updates[0].body
    return recent

def getReminderTimes():
    tmp = mongo.find()
    times = {}
    keylist = []
    for item in tmp:
        eachtime = str(item['reminderTime'])
        if "pm" in eachtime:
            eachtime = str(int(eachtime.split(":")[0])+12)+":"+eachtime.split(":")[1]
        if "am" in eachtime and "12" in eachtime:
            eachtime = str(0)+":"+eachtime.split(":")[1]
        eachtime = eachtime[:-2]
        if times.has_key(eachtime):
            times[eachtime].append(item['user'])
        else:
            times[eachtime] = [item['user']]
         
    return times  
 
def eventsToMessage(events):
    message = ""
    if len(events) > 0:
        counter = 1
        for event in events:
            if counter > 1:
                message = message+", " +str(counter)+"-"+event
            else:
                message = str(counter)+"-"+event
            counter = counter + 1
    return message

def remindersEnabled(user):
    tmp = mongo.find_one({'user':user})
    return tmp['remindersEnabled']

def getEventsToday(user):
    day = str(int(thisDay()))
    month = str(int(thisMonthNum()))
    year = thisYear()
    return getEvents(user,month,day,year)

def getEvents(user, month, day, year):
    cal = mongo.find_one({'user':user})['calinfo']
    month = str(int(month))
    if cal.has_key(year):
        if cal[year][month].has_key(day):
            if len(cal[year][month][day]) > 0:
                return cal[year][month][day]
    return []

def sendReminder(user,data):
    tmp = mongo.find_one({'user':user})
    targetnum = str(tmp['number'])
    message = client.sms.messages.create(to=targetnum, from_=phonenum,body=data)

def processEvent(number,data):
    #event is an array [message, month, day, year]
    for num in getPhoneNumbers():
        if num in number:
            tmpone = mongo.find_one({'number':num})
            tmp = tmpone['calinfo']
            user = tmpone['user']
            event = parseText(data)
            if len(event) == 4:
                year = event[3]
                month = str(int(event[1]))
                day = str(int(event[2]))
                message = event[0]
                if tmp.has_key(year):
                    if tmp[year][month].has_key(day):
                        tmp[year][month][day].append(message)
                    else:
                        tmp[year][month][day] = [message]
                else:
                    tmp[year] = {'1':{},'2':{},'3':{},'4':{},'5':{},'6':{},'7':{},'8':{},'9':{},'10':{},'11':{},'12':{}}
                    tmp[year][month][day] = [message]
                mongo.update({'number':num},{'$set':{"calinfo":tmp}})
                return 0
            if len(event) == 3:
                day = str(int(event[1]))
                month = str(int(event[0]))
                year = event[2]
                events = getEvents(user,month,day,year)
                response = ''
                counter = 1
                for item in events:
                    if item == events[0]:
                        response = str(counter)+": "+item
                    else:
                        response = response+', '+str(counter)+": "+item
                    counter = counter + 1
                if len(events) > 0:
                    sendSomething(number,response)
                else:
                    sendSomething(number,"No Events On This Day")
                return response
            if len(event) == 1:
                if event[0] == 'help':
                    response = 'helped'
                    sendHelp(number)
                    return response
                if event[0] == True:
                    if tmpone['remindersEnabled'] == False:
                        changeStatus(num)
                        response = "Reminders Enabled"
                        sendSomething(number,response)
                        return response
                    else:
                        response = "Already Enabled"
                        sendSomething(number,response)
                        return response
                if event[0] == False:
                    if tmpone['remindersEnabled'] == True:
                        changeStatus(num)
                        response = "Reminders Disabled"
                        sendSomething(number,response)
                        return response
                    else:
                        response = "Already Disabled"
                        sendSomething(number,response)
                        return response
            if len(event) == 2:
                if event[0] != '':
                    setTime(num,event[0])
                    response = "Reminder time changed to " + event[0]
                    sendSomething(number,response)
                    return 1
                else:
                    response = "Please resend with 'am' or 'pm' appended to time"
                    sendSomething(number,response)
                    return response

def sendSomething(number,text):
    message = client.sms.messages.create(to=number, from_=phonenum, body=text)

def sendResponse(number):
    sendSomething(number,"Event added to your Calendar")

def sendMessageFailed(number):
    sendSomething(number,"Failed to add event, check syntax")

def getStatus(user):
    return mongo.find_one({'user':user})['remindersEnabled']

def changeStatus(number):
    rE = mongo.find_one({'number':number})['remindersEnabled']
    rE = not rE
    mongo.update({'number':number},{'$set':{'remindersEnabled':rE}})
    
def addEvent(user,year,month,day,message):
    tmp = mongo.find_one({'user':user})['calinfo']
    if tmp.has_key(year):
        if tmp[year][month].has_key(day):
            tmp[year][month][day].append(message)
        else:
            tmp[year][month][day] = [message]
    else:
        tmp[year] = {'1':{},'2':{},'3':{},'4':{},'5':{},'6':{},'7':{},'8':{},'9':{},'10':{},'11':{},'12':{}}
        tmp[year][month][day] = [message]
    mongo.update({'user':user},{'$set':{"calinfo":tmp}})


def setTime(number, time):
    mongo.update({'number':number},{'$set':{'reminderTime':time}})

def getCurrentTime(user):
    return mongo.find_one({'user':user})['reminderTime']

def parseText(message):
    if ':' in message:
        loc = message.find(':')
        x = [message[:loc],message[loc+1:]]
        if 'set' in x[0].lower():
            timetoset = ''
            parsed = message.split('-')
            timetoset = parsed[1].replace(' ','')
            timetoset = timetoset.lower()
            if ('pm' in timetoset and not 'am' in timetoset) or ('am' in timetoset and not 'pm' in timetoset):
                return [timetoset,'']
            else:
                return ['','']
        message = x[0].replace('-','/')+x[1]
        date = x[0].split('/')
        month = date[0]
        day = date[1]
        year = ''        
        if len(date)== 3:
            if len(date[2]) == 2:
                year = '20'+date[2]
            else:
                year = date[2]
        else:
            year = time.strftime('%Y',time.localtime())
        event = [month,day,year]
        event.insert(0,x[1])
        return event
    else:
        if 'commands' in message.lower():
            return ['help']
        if 'disable' in message.lower():
            return [False]
        if 'enable' in message.lower():
            return [True]
        message = message.replace('-','/')
        date = message.split('/')
        month = date[0]
        day = date[1]
        year = ''
        if len(date)== 3:
            if len(date[2]) == 2:
                year = '20'+date[2]
            else:
                year = date[2]
        event = [month,day,year]
        return event    

def getEventsInMonth(user,month,year):
    tmpone = mongo.find_one({'user':user})['calinfo']
    monthevents = []
    if tmpone.has_key(year):
        month = str(int(time.strftime("%m",time.strptime(month,"%B"))))
        tmp = tmpone[year][month]
        for date in tmp:
            eventsonday=tmp[date]
            dateevents = [int(date),len(eventsonday)]
            monthevents.append(dateevents)
    return monthevents

def sendHelp(number):
    messageone = 'Month>mm/m; Day>dd/d; Year>yyyy/yy; Date Format>Month/Day/Year (No Year Defaults To This Year); Add Event>date:event;' 
    messagetwo = 'Get Events>date; Enable/Disable Reminders>"enable"/"disable"; Change Reminder Time>set - time; Time Format>hh:mm(am/pm)'    
    sendSomething(number,messageone)
    sendSomething(number,messagetwo)

def getUserNumber(user):
    tmp = mongo.find_one({'user':user})
    return tmp['number']

if __name__ == "__main__":
    #getMostRecent()
    #sendReminder('biggs0125','Test')
    #print parseText("01/21/2012:hello")
    #print thisYear()
    #print getFirstDay(11,thisYear())
    #print getReminderTimes()
    pass
