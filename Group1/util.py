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
    
def findBiggestSchool():
    ans = 100
    school = ''
    for i in p.keys():
        if p[i][3] > ans:
            ans = p[i][3]
            school = i
    print ans
    print school
def findSmallestSchool():
    ans = 1047
    school = ''
    for i in p.keys():
        if p[i][3] < ans and p[i][3] != 0:
            ans = p[i][3]
            school = i
    print ans
    print school    
    
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
        
def limitByBorough(borough):
    temp = p
    for i in p.keys():
        if temp[i][4] != borough:
            del(temp[i])
    return temp

def readingRank(borough):
    ans = []
    rvd = []
    ranked = limitByBorough(borough)
    for key,value in sorted(ranked.items(), key = lambda e: e[1][0]):
        ans.append((key,value))
    for i in reversed(ans):
        rvd.append(i)
    return rvd    

def mathRank(borough):
    ans = []
    rvd = []
    ranked = limitByBorough(borough)
    for key,value in sorted(ranked.items(), key = lambda e: e[1][1]):
        ans.append((key,value))
    for i in reversed(ans):
        rvd.append(i)
    return rvd

def writingRank(borough):
    ans = []
    rvd = []
    ranked = limitByBorough(borough)
    for key,value in sorted(ranked.items(), key = lambda e: e[1][2]):
        ans.append((key,value))
    for i in reversed(ans):
        rvd.append(i)
    return rvd
    
#size is user's ideal size, school is what we're checking against
#returns the percent match where 100 indicates that the school is the ideal size
def sizeMatch(school, size):
    one = 1047 - size
    two = size - 7
    larger = 0
    if one > two:
        larger = one
    else:
        larger = two
    comp = getClassSizeByName(school)
    comp = abs(comp - size)
    ans = float(comp* 100)
    ans = float(ans/larger)
    return 100 - ans

def findBestSizeMatch(dic, size):
    ans = 0
    school = ''
    for i in dic.keys():
        check = sizeMatch(i,size)
        if check > ans:
            ans = check
            school = i
    return {school: str(ans) + "%"}
        
    
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

def getSchoolMatches(priorityarr, size, borough, numres):
    rreading = []
    rmath = []
    rwriting = []
    rreading = readingRank(borough)
    rmath = mathRank(borough)
    rwriting = writingRank(borough)
    

if __name__ == "__main__":
    stackShelve()
    cleanShelve()
    print p['STUYVESANT HIGH SCHOOL ']
    #dbn = p['STUYVESANT HIGH SCHOOL '][4]
    #print dbn
    #for i in p.keys():
    #    print p[i]
    #print getReadingByName('STUYVESANT HIGH SCHOOL ')
    #print getMathByName('STUYVESANT HIGH SCHOOL ')
    #print getWritingByName('STUYVESANT HIGH SCHOOL ')
    #print getClassSizeByName('STUYVESANT HIGH SCHOOL ')
    #getSchools()
    #testing()
    #findWorstSchool()
    #findBestSchool()
    #print getTotalScoreByName('STUYVESANT HIGH SCHOOL ')
    #findBiggestSchool()
    #findSmallestSchool()
    print sizeMatch("FRANCIS LEWIS HIGH SCHOOL ", 804)
    #q = limitByBorough("Bronx")
    #print findBestSizeMatch(q, 804)
    #print limitByBorough("Manhattan")
    #print readingRank("Manhattan")
    #print mathRank("Manhattan")
    #print writingRank("Manhattan")
