#!/usr/bin/python
import shelve
import urllib2
import urllib
import json

satScores = json.loads(urllib2.urlopen("http://data.cityofnewyork.us/api/views/zt9s-n5aj/rows.json").read())
data = satScores["data"]
p = shelve.open("storage")

def stackShelve():
    school=''
    info=[]
    temp = []
    for item in data:
        info = []
        school=str(item[9])
        if item[11] != None:
            temp = int(item[11])
        else:
            temp = item[11]
        info.append(temp)
        if item[12] != None:
            temp = int(item[12])
        else:
            temp = item[12]
        info.append(temp)
        if item[13] != None:
            temp = int(item[13])
        else:
            temp = item[13]
        info.append(temp)
        if item[10] != None:
            temp = int(item[10])
        else:
            temp = item[10]
        info.append(temp)
        temp = str(item[8])[2]
        if temp == "M":
            temp = "Manhattan"
        elif temp == "K":
            temp = "Brooklyn"
        elif temp == "X":
            temp = "Bronx"
        elif temp == "Q":
            temp = "Queens"
        else:
            temp = "Staten Island"
        info.append(temp)
        p[school] = info

def cleanShelve():
    for i in p.keys():
        if p[i][0] == None:
            del(p[i])
            
def findBestSchool():
    ans = 1000
    for i in p.keys():
        comp = 0
        if p[i][0] != None:
            comp+=p[i][0]
        else:
            comp+=0
        if p[i][1] != None:
            comp+=p[i][1]
        else:
            comp+=0
        if p[i][2] != None:
            comp+=p[i][2]
        else:
            comp+=0
        if comp > ans and comp != 0:
            ans = comp
            school = i
    print school
    print ans

def findWorstSchool():
    ans = 1000
    for i in p.keys():
        comp = 0
        if p[i][0] != None:
            comp+=p[i][0]
        else:
            comp+=0
        if p[i][1] != None:
            comp+=p[i][1]
        else:
            comp+=0
        if p[i][2] != None:
            comp+=p[i][2]
        else:
            comp+=0
        if comp < ans and comp != 0:
            ans = comp
            school = i
    print school
    print ans

def getReadingByName(school):
    return p[school][0]
def getMathByName(school):
    return p[school][1]
def getWritingByName(school):
    return p[school][2]
def getClassSizeByName(school):
    return p[school][3]
def getTotalScoreByName(school):
    comp = 0
    if p[school][0] != None:
        comp+=p[school][0]
    else:
        comp+=0
    if p[school][1] != None:
        comp+=p[school][1]
    else:
        comp+=0
    if p[school][2] != None:
        comp+=p[school][2]
    else:
        comp+=0
    return comp
def getSchools():
    for item  in data:
        print item[9]



def testing2():
    if int(data[0][11]) == 391:
        print "testing2 works"

#gives an error saying int() can't convert non-string with explicit base?
def testing():
    i = 0
    for item in data:
        print item
        print item[9]  #prints school name
        if item[11] != None:  #prints critical reading score if it exists
            print int(item[11])
        else:
            print item[11]
        #this doesnt work
        #if int(data[i][11]) > 600:
        #    print data[i][9]
        #i = i + 1

if __name__ == "__main__":
    stackShelve()
    cleanShelve()
    print p['STUYVESANT HIGH SCHOOL ']
    #dbn = p['STUYVESANT HIGH SCHOOL '][4]
    #print dbn
    for i in p.keys():
        print p[i]
    #print getReadingByName('STUYVESANT HIGH SCHOOL ')
    #print getMathByName('STUYVESANT HIGH SCHOOL ')
    #print getWritingByName('STUYVESANT HIGH SCHOOL ')
    #print getClassSizeByName('STUYVESANT HIGH SCHOOL ')
    #getSchools()
    #testing2()
    #testing()
    #findWorstSchool()
    #findBestSchool()
    #print getTotalScoreByName('STUYVESANT HIGH SCHOOL ')
