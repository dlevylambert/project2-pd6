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
    number = number.strip([' ','-','+','_'])
    newuser = {"user" : user, "pass" : tmp, "number" : number, "calinfo" : []}
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
            tmp.append(data)
            mongo.update({'number':num},{'$set':{"calinfo":tmp}})
            print "Event added"
        print num + '  ' + number

def sendResponse(number):
    message = client.sms.messages.create(to=number, from_="+16468074041",body="Event added to your Calendar")

if __name__ == "__main__":
    #getMostRecent()
    #sendReminder('biggs0125','Test')
    pass
