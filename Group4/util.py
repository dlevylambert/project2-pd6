import urllib
import json
import sys
from pymongo import Connection
from twilio.rest import TwilioRestClient


Conn = Connection('ds041367.mongolab.com',41367)
db = Conn['stuycs_sideprojects']
res = db.authenticate('stuycs','stuycs')
coll = db.Project2

account = 'ACd118dcbff7f480ecd7ba59b8c217e87f'
token = '3acfc74ebcc11a59f4332bea592e7a1e'
client = TwilioRestClient(account,token)   


def getTextLog():
    for message in client.sms.messages.list():
        print message.body
        #lines = message.body.split('\n')
        #print lines[0]

