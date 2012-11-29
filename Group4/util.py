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
    newuser = {"user" : user, "pass" : tmp, "number" : number, "calinfo" : {'2012' : {'1':{},'2':{},'3':{},'4':{},'5':{},'6':{},'7':{},'8':{},'9':{},'10':{},'11':{},'12':{}}},"reminderTime":"8:00am","remindersEnabled":True}
    mongo.insert(newuser)

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
    print "01 "+str(month)+" "+str(year)
    date = time.strptime("01 "+str(month)+" "+str(year),"%d %B %Y")
    return time.strftime("%w",date)

def thisYear():
    return time.strftime("%Y",time.localtime())
def thisMonth():
    return time.strftime("%B",time.localtime())
def thisDay():
    return time.strftime("%d",time.localtime())

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

def getMostRecent():
    updates = client.sms.messages.list()
    recent = updates[0].body
    return recent

def getReminderTimes():
    tmp = mongo.find()
    times = {}
    for item in tmp:
        eachtime = str(item['reminderTime'])
        if "pm" in eachtime:
            eachtime = str(int(eachtime.split(":")[0])+12)+eachtime.split(":")[1]
        if "am" in eachtime and "12" in eachtime:
            eachtime = str(0)+":"+eachtime.split(":")[1]
        eachtime = eachtime[:-2]
        if times.has_key(eachtime):
            times[eachtime].append(item['user'])
        else:
            times[eachtime] = [item['user']]
    return times  
 
def getEvents(user, month, day, year):
    cal = mongo.find_one({'user':user})['calinfo']
    return cal[year][month][day]

def sendReminder(user,data):
    tmp = mongo.find_one({'user':user})
    targetnum = str(tmp['number'])
    message = client.sms.messages.create(to=targetnum, from_=phonenum,body=data)

def processEvent(number,data):
    #event is an array [message, month, day, year]
    for num in getPhoneNumbers():
        if num in number:
            tmp = mongo.find_one({'number':num})['calinfo']
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
            else:
                day = str(int(event[1]))
                month = str(int(event[0]))
                year = event[2]
                events = tmp[year][month][day]
                response = ''
                counter = 1
                for item in events:
                    if item == events[0]:
                        response = str(counter)+": "+item
                    else:
                        response = response+', '+str(counter)+": "+item
                    counter = counter + 1
                sendEvent(number,response)
                return response

def sendEvent(number,event):
    sendSomething(number,event)

def sendSomething(number, text):
    message = client.sms.messages.create(to=number, from_=phonenum, body=text)

def sendResponse(number):
    sendSomething(number,"Event added to your Calendar")

def sendMessageFailed(number):
    sendSomething(number,"Failed to add event, check syntax")

def changeStatus(number):
    rE = mongo.find_one({'number':number})['remindersEnabled']
    rE = not remindersEnabled
    text = "off"
    if rE:
        text = "on"
    sendSomething(number, text)


def setTime(number, time):
    rT = mongo.find_one({'number':number})['reminderTime']
    rT = time
    sendSomething(number, "Reminder time changed to " + rT)
    
def setTimeWeb(user, time):
    rT = mongo.find_one({'user':user})['reminderTime']
    rT = time
    sendSomething(number, "Reminder time changed to " + rT)

def getTimeWeb(user):
    rT = mongo.find_one({'user':user})['reminderTime']
    ampm = rT[-2:]
    b = rT[:-2]
    c = b.split(':')
    c.append(ampm)
    return c
def parseText(message):
    if ':' in message:
        x = message.find(':')
        message = message[:x].replace('-','/')+message[x:]
        date = message[:x].split('/')
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
        event.insert(0,message[(x+1):])
        return event
    else:
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

if __name__ == "__main__":
    #getMostRecent()
    #sendReminder('biggs0125','Test')
    #print parseText("01/21/2012:hello")
    #print thisYear()
    #print getFirstDay(11,thisYear())
    #print getReminderTimes()
    pass
