import urllib2
import json
from operator import  itemgetter

def proof(url):
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
    me=i[dInd]
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
    i[dInd]=me
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
    """
    return sorted(l,key=itemgetter(12))

url ="https://data.cityofnewyork.us/api/views/xenu-5qjw/rows.json"
names=[]
events=[]
events2013=[]
for i in proof(url)['data']:
    if currentYear(i,"12",12):
        events.append(i) #every event that occured in 2012
    elif currentYear(i,"13", 12):
        events2013.append(i)
for i in events:
    n=0
    while n<len(i):
        i[n]=str(i[n])
        n=n+1
for i in events:
    names.append(i[8])
#print events


Bk = sortT(sortB(events,'Brooklyn'))
Q = sortT(sortB(events,'Queens'))
M = sortT(sortB(events,'Manhattan'))
Bx = sortT(sortB(events,'Bronx'))
SI = sortT(sortB(events,'Staten Island'))

#print M

#for i in M:
#    print i[19]

#need to add the events in 2013 to the boroughs...
