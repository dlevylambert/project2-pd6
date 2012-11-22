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

def createNewUser(user,password,number):
    tmp = base64.b64encode(password)
    number = str(number).strip(' -+_')
    newuser = {"user" : user, "pass" : tmp, "number" : number, "calinfo" : {'2012':{'1':{},'2':{},'3':{},'4':{},'5':{},'6':{},'7':{},'8':{},'9':{},'10':{},'11':{},'12':{}}},"reminderTime":"8:00","remindersEnabled":True}
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

def sendReminder(user,data):
    tmp = mongo.find_one({'user':user})
    targetnum = str(tmp['number'])
    message = client.sms.messages.create(to=targetnum, from_="+16468074041",body=data)

def addEvent(number,data):
    for num in getPhoneNumbers():
        if num in number:
            tmp = mongo.find_one({'number':num})['calinfo']
            event = parseText(data)
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
            

def sendResponse(number):
    message = client.sms.messages.create(to=number, from_="+16468074041",body="Event added to your Calendar")

def sendMessageFailed(number):
    message = client.sms.create(to=number, from_="+16468074041",body="Failed to add event, check syntax")

def parseText(message):
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
if __name__ == "__main__":
    #getMostRecent()
    #sendReminder('biggs0125','Test')
    #print parseText("01/21/2012:hello")
    pass
