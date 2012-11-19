import xml.etree.ElementTree as ET
import re
import random


categories = []
tree = ET.parse("DPR_Eateries.xml")
root = tree.getroot()


def getCategories():
    for item in root[0]:
        s = item[11].text
        boolean = 0
        for i in categories:
            if i == s:
                boolean = 1
        if boolean != 1:
            categories.append(s)
    return s


def search(inputstring):
    inputstring = inputstring.lower()
    searchresults = []
    strcounter = []
    strlist = inputstring.split(' ')
    for s in strlist:
        strcounter.append(0)
    for item in root[0]:
        for line in item:
            i = 0
            for s in strlist:
                if line.text != None:
                    if re.search(s, line.text.lower()) != None:
                        strcounter[i] += 1
                i += 1
        product = 1
        for num in strcounter:
            product *= num
        if product > 0:
            b = 0
            for line in searchresults:
                if item[0].text.lower() == line[0].text.lower():
                    b = 1
            if b == 0:
                searchresults.append(item)
    return searchresults


def randomSearch(inputstring):
    l = search(inputstring)
    return l[random.randint(0,l.__len__() - 1)]

 
def randomRestaurant():
    return root[0][random.randint(0,root[0].__len__() - 1)]
