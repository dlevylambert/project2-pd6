import xml.etree.ElementTree as ET

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

getCategories()

def search(inputstring):
    searchresults = []
    strlist = inputstring.split(' ')
    for s in strlist:
        for item in root[0]:
            boolean = 0
            for line in item:
                if line.text != None:
                    if line.text.split(s, 1)[0].__len__() == line.text.__len__():
                        boolean = 1
                for i in searchresults:
                    if i[0].text == item[0].text:
                        boolean = 0
                if boolean == 1:
                    searchresults.append(item)
    return searchresults
    

