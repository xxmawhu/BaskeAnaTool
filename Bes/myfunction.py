import os
import sys
import boss
#------the function to select the files whose type is txt
def findtype(files,type='.txt'):
    txt=[]
    for i in files:
        tp=os.path.splitext(i)[1]
        if(tp==type):
            txt.append(i)
    return txt
#-----find .c .cxx in files list
#--------end of function-------------------------------#
mypath=os.getcwd()
path=os.listdir('.')
#-----find all file in path 'p'
def findfiler(p):
    file=[]
    if os.path.isfile(p):
        file.append(os.path.abspath(p))
    else:
        path=[]
        for i in os.listdir(p):
            if i[-1]=='/':
                path.append(p+i)
            else:
                path.append(p+'/'+i)
        for i in path:
            file.extend(findfiler(i))
    return file
#-----end-------#
#-----find only file in current dir:p
def findfile(p):
    file=[]
    if p[-1] !="/":
        p += '/'
    if os.path.isfile(p):
        file.append(os.path.abspath(p))
    else:
        for i in os.listdir(p):
            if '/' in i :
                file.append(p+i)
            elif p=='.':
                file.append(p+i)
            else:
                file.append(p+i)
    return file
#-------end-----------#
