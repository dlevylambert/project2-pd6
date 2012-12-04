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
        data = [password, []]
        users[name] = data
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

    if name in users and users[name][0]==password:
        del d[name]
        return True
    else:
        return False
    
def clear_users():
    for name in users:
        print name
        print users[name]
        print name[0]
        delete_user(name, name[0], False)

if __name__ == '__main__':

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
