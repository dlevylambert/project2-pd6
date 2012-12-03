#!/usr/bin/python
import shelve

users = shelve.open("users.db")


def signup(name, id):
    #Will not allow for multiple users of the same name
    if name in users:
        return False
    else:
        #Note these passwords are unencrypted
        users[name][0] = id
        users[name][1] = [0]
        print users[name]
        return True

def save_search(name, search):
    user = users[name]
    user[1].append( search )

def get_search(name):
    return users[name][1]

def authenticate(name, id):
    if name in users and users[name]==id:
        return True
    else:
        return False

def delete_user(name, id):
    if name in users and users[name]==id:
        del d[name]
        return True
    else:
        return False
    
if __name__ == '__main__':

    for name in users:
        delete_user(name, users[name][0])
    
    signup('name', 8454)
    save_search('name', ['hello'])
    
    if 'name' in users:
        print 'name is a key'
        print users['name']
    else:
        print "ain't there"
    
    if (signup('name', 12345)):
        print 'need to fix this'
    else:
        print "works as it should"
    
    users.close()
