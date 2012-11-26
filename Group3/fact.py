from factual import *

KEY = "WaCvw1FbqneYWbpLP0hatFJOhwxDyy3dQUDeQjpF"
SECRET = "p6tAvjCwVrkqH5EU3FtlGyzfgrnmfvmH7KkuoMf9"

#see https://github.com/Factual/factual-python-driver/blob/master/example.py

def getData():
    fact = Factual(KEY,SECRET)
    
    table = fact.table("restaurants-us").filters({
            "locality":"new york"})
    res = table.data()[0]
    #return len(table.data())
    return [ res['name'] , res["cuisine"] , res['latitude'] , res['longitude']
             , res['address'] ]

if __name__ == "__main__":
    print getData()
