#!/usr/bin/python
import shelve

users = shelve.open("users.db")

def check_unicode(unicode_name):
    name = unicode_name.encode('utf-8')
    return name + unicode_name

def signup(unicode_name, password, uni = True):
    #Will not allow for multiple users of the same name
    if uni == True:
        name = unicode_name.encode('utf-8')
    else:
        name = unicode_name
    
    if name in users:
        return False
    else:
        #Note these passwords are unencrypted
        users[name] = [2]
        users[name].append( password )
        users[name].append( [] )
        print users[name]
        return True

def save_search(unicode_name, search, uni=True):
    if uni == True:
        name = unicode_name.encode('utf-8')
    else:
        name = unicode_name
    user = users[name]
    user[1].append( search )

def get_search(unicode_name, uni=True):
    if uni == True:
        name = unicode_name.encode('utf-8')
    else:
        name = unicode_name
    return users[name][1]

def authenticate(unicode_name, password, uni=True):
    if uni == True:
        name = unicode_name.encode('utf-8')
    else:
        name = unicode_name
    if name in users and users[name]==password:
        return True
    else:
        return False

def delete_user(unicode_name, password, uni=True):
    if uni == True:
        name = unicode_name.encode('utf-8')
    else:
        name = unicode_name

    if name in users and users[name]==password:
        del d[name]
        return True
    else:
        return False
    

if __name__ == '__main__':

    for name in users:
        delete_user(name, users[name][0], False)
        
    signup('name', 8454, False)
    save_search('name', ['hello'], False)
    
    if 'name' in users:
        print 'name is a key'
        print users['name']
    else:
        print "ain't there"
    
    if (signup('name', 12345, False)):
        print 'need to fix this'
    else:
        print "works as it should"
    
    users.close()
