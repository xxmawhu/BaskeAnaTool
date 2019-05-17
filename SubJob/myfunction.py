#!/afs/ihep.ac.cn/soft/common/python27_sl65/bin/python
# -*- coding: utf-8 -*-
import os
import sys
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
            path.append(p+'/'+i)
        for i in path:
            file.extend(findfiler(i))
        file.sort()
    return file
#-----end-------#
#-----find only file in current dir:p
def findfile(p):
    file=[]
    if os.path.isfile(p):
        file.append(os.getcwd()+'/'+p)
    else:
        for i in os.listdir(p):
            if '/' in p :
                file.append(os.getcwd()+'/'+p+i)
            elif p=='.':
                file.append(os.getcwd()+'/'+i)
            else:
                file.append(os.getcwd()+'/'+p+'/'+i)
        file.sort()
    return file
#-------end-----------#
