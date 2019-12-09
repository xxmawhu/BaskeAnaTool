# useful function
import string, sys, os
from Bes.commands import getoutput as do
from SubJob import hep
def name(dsts,m):
    name=[]
    N=len(dsts)
    for i in range(0,N):
        s=dsts[i].split('/')
        name.append('')
        name[i] =s[-1]
        for j in range(2,m+1):
            name[i] =name[i]+'_'+s[-j]
    return name
def getname(dsts):
    i=1
    while 1:
        nm0 = name(dsts,i)
        s=set(nm0)
        if len(s)== len(dsts) :
            return nm0
        else:
            i = i+1
            nm0=name(dsts,i)
def isdigit(ss):
    sp = ss.split('.')
    for i in sp:
        if not i.isdigit():
            return False
    return True
def mkdir(s):
    if(not os.path.isdir(s)):
        os.makedirs(s)
def hepsub(files):
    hep.Sub(files);
    return
    if len(files)>0:
        mypath=os.getcwd()
        print ("current path\t",mypath)
        for i in files:
            path=os.path.split(i)[0]
            File=os.path.split(i)[1]
            name=os.path.splitext(i)[0]
            os.chdir(path)
            os.system('chmod +x '+File)
            os.system('/afs/ihep.ac.cn/soft/common/sysgroup/hep_job/bin/hep_sub -g physics '+File)
            os.chdir(mypath)
        os.chdir(mypath)#return to my work path
def getOpt():
    rs = []
    for i in sys.argv:
        if '-' == i[0]:
            continue
        rs.append(i)
    return rs[1:]

def getArv():
    rs = []
    for i in sys.argv:
        if '-' == i[0]:
            rs.append(i)
    return rs
def MaxJobs():
    num =  do("/afs/ihep.ac.cn/soft/common/sysgroup/hep_job/bin/hep_q -u | wc -l")
    if num == "":
        num = 0
    return 10000 - int(num)
