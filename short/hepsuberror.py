import os
from commands import getoutput as do
import util as mf
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
jobid =open("log/jobid",'a')
for i in jobCol:
    if "jobid" in i:
        continue
    if not i+".bosslog" in logCol:
        print i
        job = os.path.split(i)[1]
        pth = os.path.split(i)[0]
        #print "jobs ", job
        #print "path", pth
        sublog= do("cd "+pth+'&& boss.condor '+job)
        jobid.write(sublog.split()[-1]+'\n')
for i in logList:
    f=open(i,'r')
    s=f.read()
    if 'INFO Application Manager Finalized successfully' in s:
        continue
    else:
        print i[0:len(i)-8]
        job = os.path.split(i[0:len(i)-8])[1]
        pth = os.path.split(i[0:len(i)-8])[0]
        print("rm %s/%s.boss*"%(pth, job))
        do("rm %s/%s.boss*"%(pth, job))
        print "cd "+pth
        print 'boss.condor '+job
        print "cd -"
        sublog = do("cd "+pth+'&& boss.condor '+job)
        jobid.write(sublog.split()[-1]+'\n')
    f.close()

jobid.close()

