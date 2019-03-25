import os
import commands
import sys
import re
#Type match
def typeMatch(i, Type):
    if Type == "":
        return True
    if Type[0] != '.':
        Type = '.' +Type
    elif "." + i.split('.')[-1] == Type:
        #print "match:", Type, ">>", i
        return True

    #print "fail:", Type, ">>", i
    return False

def walkDir(Dir, Type=""):
    File = []
    for tup in os.walk(Dir):
        path = tup[0]
        files = tup[2]
        for f in files:
            if typeMatch(f, Type):
                File.append(os.path.abspath(os.path.join(path, f)))
    File.sort()
    return File

def findfile(p, Type="") :
    File = []
    # if p is a file
    if os.path.isfile(p) and typeMatch(p, Type):
        File.append(os.path.abspath(p))
        File.sort()
        return File
    # p is a director
    if os.path.isdir(p):
        for i in os.listdir(p):
            if os.path.isfile(i) and typeMatch(i, Type):
                File.append(os.path.join(os.path.abspath(p), i))
    File.sort()
    return File


def match(k, aim):
    key = k.replace("*", "[a-zA-Z0-9_.]*")
    pattern = re.compile(key)
    if pattern.match(aim):
        return True
    else:
        return False

#regular expression
def findRegular(expre, Type = "", r = ""):
    matchList = []
    File = []
    for i in os.listdir(".") :
        if match(expre, i) :
            matchList.append(i)
    for i in matchList:
        if os.path.isfile(i) and typeMatch(i, Type):
            File.append(os.path.abspath(i))
        elif os.path.isdir(i):
            File += findfiler(i, Type, r)
    File.sort()
    return File



#find file recursive
def findfiler(p, Type = "", r="-r"):
    File = []
    if os.path.isfile(p) and typeMatch(p, Type):
        File.append(os.path.abspath(p))
        return File

    if os.path.isdir(p):
        if r == "-r":
            return walkDir(p, Type)
        else:
            return findfile(p, Type)
    
    #may be regular expression
    return findRegular(p, Type, r)






