#!/usr/bin/python
import shelve

userlist = shelve.open("users.db")

def check_unicode(unicode_name):
    name = unicode_name.encode('utf-8')
    return name + unicode_name

def signup(unicode_name, uni_password, uni = True):
    #Will not allow for multiple users of the same name
    if uni == True:
        name = unicode_name.encode('utf-8')
        password = uni_password.encode('utf-8')
    else:
        name = unicode_name
        password = uni_password
    
    if name in userlist:
        return False
    else:
        #Note these passwords are unencrypted
        data = [password, []]
        userlist[name] = data
        print userlist[name]
        return True

def save_search(unicode_name, search, uni=True):
    if uni == True:
        name = unicode_name.encode('utf-8')
    else:
        name = unicode_name
    user = userlist[name]
    user[1].append( search )

def get_search(unicode_name, uni=True):
    if uni == True:
        name = unicode_name.encode('utf-8')
    else:
        name = unicode_name
    return user[name][1]

def authenticate(unicode_name, uni_password, uni=True):
    if uni == True:
        name = unicode_name.encode('utf-8')
        password = uni_password.encode('utf-8')
    else:
        name = unicode_name
        password = uni_password
        
    if name in userlist:
        print "name exists"
        print userlist[name][0]
        if userlist[name][0]==password:
            print "passcheck"
            return True
    else:
        return False

def delete_user(unicode_name, password, uni=True):
    if uni == True:
        name = unicode_name.encode('utf-8')
    else:
        name = unicode_name

    if name in userlist:
        del userlist[name]
        return True
    else:
        return False
    
def clear_users():
    for name in userlist:
        #print name
        #print userlist[name]
        #print name[0]
        delete_user(name, name[0], False)

if __name__ == '__main__':
    userlist = shelve.open("users.db")
    
    signup('name', 8454, False)
    save_search('name', ['hello'], False)
    
    if 'name' in userlist:
        print 'name is a key'
        print userlist['name']
    else:
        print "ain't there"
    
    if (signup('name', 12345, False)):
        print 'need to fix this'
    else:
        print "works as it should"
    
    
    print userlist
    clear_users()
    print userlist
    
    userlist.close()
