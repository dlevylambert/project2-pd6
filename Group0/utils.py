from pymongo import Connection

conn = Connection("mongo.stuycs.org")
def connect():
    db = conn.admin
    res = db.authenticate("ml7","ml7")

def add_user(username):
    db = conn["musicbox"]
    users = db.first_collection
    entry = {"name": username, "songs": []}
    users.insert(entry)
    info = [line for line in users.find()]
    print info

def get_songs(username):
    db = conn["musicbox"]
    users = db.first_colletion
    for line in users.find():
        if line["name"] == username:
            return line["songs"]
