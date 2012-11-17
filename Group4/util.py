import urllib
import json
import sys
import time
import base64
from pymongo import Connection
from twilio.rest import TwilioRestClient


Conn = Connection('ds041367.mongolab.com',41367)
db = Conn['stuycs_sideprojects']
res = db.authenticate('stuycs','stuycs')
mongo = db.Project2

account = 'ACd118dcbff7f480ecd7ba59b8c217e87f'
token = '3acfc74ebcc11a59f4332bea592e7a1e'
client = TwilioRestClient(account,token)   

def createNewUser(user,password):
    tmp = base64.b64encode(password)
    newuser = {"user" : user, "pass" : tmp, "calinfo" : []}
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

def getTextLog():
    for message in client.sms.messages.list():
        print message.body
        #lines = message.body.split('\n')
        #print lines[0]

def getMostRecent():
    updates = client.sms.messages.list()
    recent = updates[0].body
    print recent

if __name__ == "__main__":
    getMostRecent()
