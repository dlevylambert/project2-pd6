import urllib2
import json
from operator import  itemgetter

def utils(url):
    return json.loads(urllib2.urlopen(url).read()) 

def currentYear(item,year,dInd):
    """
    item: Event data
    year: last 2 digits of year (i.e. "12" or "13")
    dInd: index of the time criteria to parse through (i.e. 12 = 'StartEventTime') for an event)
    returns true if event occurs in the same year as input
    standardizes date format: MM/DD/YY
    standardizes time format: 00:00 AM or 00:00 PM
    """ 
    boolean = False
    me=item[dInd]
    if me[1:2]=="/" and (me[4:6]==year or me[5:7]==year):
        if me[3:4]=="/":
            if me[4:6]==year:
                me=str(me[:2])+"0"+str(me[2:])
                boolean = True
        else:
            if me[5:7]==year:
                boolean = True
        me="0"+str(me)
    else:
        if me[4:5]=="/" and me[5:7]==year:
            me=str(me[:3])+"0"+str(me[3:])
            boolean=True
        elif me[6:8]==year:
            boolean=True
    me=str(me)
    if boolean and me[10:11]==":":
        me= me[:9]+"0"+me[9:]
    item[dInd]=me
    return boolean

def sortB(l,b):
    """
    l: list to sort through
    b: borough to look for
    """
    boro=[]
    for i in l:
        if i[19]==b:
            boro.append(i)
    return boro

def sortT(l):
    """
    returns the input, list, sorted by time
    according to the start time of the event (index 12)
    from most recent to least recent
    """
    return sorted(l,key=itemgetter(12), reverse=True)

def getE():
    url ="https://data.cityofnewyork.us/api/views/xenu-5qjw/rows.json"
    events=[]
    events2013=[]
    for i in utils(url)['data']:
        if currentYear(i,"12",12):
            events.append(i) #every event that occured in 2012
        elif currentYear(i,"13", 12):
            events2013.append(i)
    events=sortT(makeString(events))
    events2013=sortT(makeString(events2013))
    events = events2013+events
    return events

def makeString(l):
    temp = l
    for i in temp:
        n=0
        while n<len(i):
            i[n]=str(i[n])
            n=n+1
    l = temp
    return l

#print events

def getB(b):
    events=getE()
    return sortB(events,b)

for i in getB("Manhattan"):
    print i[12]
#need to add the events in 2013 to the boroughs...
