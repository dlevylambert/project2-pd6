import urllib2
import json

def proof(url):
    return json.loads(urllib2.urlopen(url).read()) 

def currentYear(item,year,dInd):
    """
    item: Event data
    year: last 2 digits of year (i.e. "12" or "11")
    dInd: index of the time criteria to parse through (i.e. 12 = 'StartEventTime') for an event)
    returns true if event occurs in the same year as input
    standardizes date format: MM/DD/YY
    """ 
    boolean = False
    me=i[dInd]
    if me[1:2]=="/":
        if me[3:4]=="/":
            if me[4:6]==year:
                me=str(me[:2])+"0"+str(me[2:])
                booblean = True
        else:
            if me[5:7]==year:
                boolean = True
        me="0"+str(me)
    else:
        if me[4:5]=="/":
            if me[5:7]==year:
                me=str(me[:3])+"0"+str(me[3:])
                boolean=True
        else:
            if me[6:8]==year:
                boolean=True
    me=str(me)
    i[dInd]=me
    return boolean

url ="https://data.cityofnewyork.us/api/views/xenu-5qjw/rows.json"
names=[]
dates=[]
events=[]
for i in proof(url)['data']:
    if currentYear(i,"12",12):
        events.append(i) #every event that occured in 2012
for i in events:
    n=0
    while n<len(i):
        i[n]=str(i[n])
        n=n+1
for i in events:
    names.append(i[8])
    dates.append(i[12])
print events
