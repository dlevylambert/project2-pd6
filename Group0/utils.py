from pymongo import Connection
import musicservices

conn = Connection("mongo.stuycs.org")

def drop():
    db = conn["musicbox"]
    users = db.first_collection
    users.drop()

def connect():
    db = conn.admin
    res = db.authenticate("ml7","ml7")

def add_or_view_user(username):
    db = conn["musicbox"]
    users = db.first_collection
    for entry in users.find():
        if entry["name"] == username:
            info = [line for line in users.find()]
            print info
            return username #if it's there, do nothing
    entry = {"name": username, "songs": []}
    users.insert(entry) #otherwise, create a blank entry for the user
    return username

def get_songs(username):
    db = conn["musicbox"]
    users = db.first_colletion
    for line in users.find():
        if line["name"] == username:
            return line["songs"]

def build_artist(artist):
    return [
        musicservices.getName(artist)
        ,musicservices.getProfile(artist)
        ,musicservices.getMembers(artist)
        ,musicservices.getID(artist)
]

def remove_user(username):
    db = conn["musicbox"]
    users = db.first_collection
    users.remove( {"name": username}, True)

