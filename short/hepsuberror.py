import sys
import os
from commands import getoutput as do
import util as mf
_USAGE = '''Usage:  without any option now
Function:
    1)find all .txt file and the log files producted by the boss.exe
    recursively, and read one by one, if any one jobs is not procedured
    successful, then print them. the followings faile job that:
       i) Without one associated .bosslog file generated
       ii) Can't find any line contains `Manager Finalized successful` 
       
    2) Sub them to the servior one by one
'''
if "-help" in sys.argv or "--help" in sys.argv:
    print _USAGE
    exit(0)
#jobs=os.listdir('.')
jobs=mf.findfiler('.')
logList=[]
for i in jobs:
    if '.bosslog'==os.path.splitext(i)[1]:
        logList.append(i)
list.sort(logList)
logCol=[]
jobCol=[]
for i in jobs:
    if '.bosslog'==os.path.splitext(i)[1]:
        logCol.append(i)
    if '.txt'==os.path.splitext(i)[1]:
        jobCol.append(i)

IDList = []

for i in jobCol:
    if "jobid" in i:
        continue
    if not i + ".bosslog" in logCol:
        job = os.path.split(i)[1]
        pth = os.path.split(i)[0]
        #print "jobs ", job
        #print "path", pth
        sublog= do("cd "+pth+'&& boss.condor '+job)
        IDList.append(sublog.split()[-1]+'\n')
errorList=[]
for i in logList:
    f=open(i,'r')
    lines =f.readlines()
    AMFS = False
    for l in lines[-5:]:
        if 'Finalized successfully' in l:
            AMFS = True
            break
    f.close()
    if not AMFS:
        errorList.append(i[:-8])

from SubJob import hep
print "Inf:: total", len(errorList), "jobs fail"
for j in errorList:
    do("rm %s.*"%(j))
hep.Sub(errorList)
