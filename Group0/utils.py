from pymongo import Connection
import musicservices

conn = Connection("mongo.stuycs.org")

def drop():
    db = conn["musicbox"]
    users = db.first_collection
    users.drop()

def disp():
    db = conn["musicbox"]
    users = db.first_collection
    print [user for user in users.find()]

def connect():
    db = conn.admin
    res = db.authenticate("ml7","ml7")

def add_or_view_user(username):
    db = conn["musicbox"]
    users = db.first_collection
    for entry in users.find():
        if entry["name"] == username:
            return username #if it's there, do nothing
    entry = {"name": username, "songs": []}
    users.insert(entry) #otherwise, create a blank entry for the user
    return username

def add_song(username, title, artistID):
    db = conn["musicbox"]
    users = db.first_collection
    for entry in users.find():
        if entry["name"] == username:
            tmp = entry["songs"]
            if [title,artistID] not in tmp:
                tmp.append([title, artistID])
            users.update({"name":username}, {"name":username, "songs":tmp})

def get_songs(username):
    db = conn["musicbox"]
    users = db.first_collection
    for entry in users.find():
        if entry["name"] == username:
            return [build_release(song) for song in entry["songs"]]

def build_artist(artist):
    releases = musicservices.getReleasesByID(
        musicservices.getID(artist))["releases"]
    return [
        musicservices.getName(artist)
        ,musicservices.getProfile(artist)
        ,musicservices.getMembers(artist)
        ,musicservices.getID(artist)
        ,releases
]

def build_release(arr):
    release = musicservices.getReleaseByTitle(str(arr[0]),str(arr[1]))
    result = []
    if musicservices.getTitle(release) != None:
        result.append("<h4>"+musicservices.getTitle(release)+"</h4>")
    if musicservices.getArtist(arr[1]) != None:
        result.append("Artist: "+musicservices.getArtist(arr[1]))
    if musicservices.getYear(release) != None:
        result.append("Year: "+musicservices.getYear(release))
    if musicservices.getLabel(release) != None:
        result.append("Label: "+musicservices.getLabel(release))
    if musicservices.getPic(release) != None:
        url = musicservices.getPic(release)
        result.append("<img src='"+url+"' alt='something'></img>")
    return result

def remove_user(username):
    db = conn["musicbox"]
    users = db.first_collection
    users.remove( {"name": username}, True)

def curate(s): #to replace spaces with %20
    while s.find(" ") != -1:
        s = s[:s.find(" ")]+"%20"+s[s.find(" ")+1:]
    return s
