import myfunction as m
from commands import getoutput as do
import os, SubJob
from SubJob import hep
class hepsub:
    def __init__(self):
        self.jobcol=[]
        self.pth=''
        self.log='log'
    def setlog(self,x):
        self.log=x
    def setpath(self,x):
        self.pth=x
    def findjob(self):
        s=m.findfiler(self.pth)
        list.sort(s)
        self.jobcol= m.findtype(s,'.txt')
    def sub(self):
        self.findjob()
        hep.Sub(self.jobcol, '.txt', self.log+'/jobid')
        s='''# delete jobs
from commands import getoutput as do
f=open('jobid','r')
for i in f.readlines():
    id=str( i[0:-2])
    print do( 'hep_rm '+id )
'''
        f=open(self.log+'deletejob.py','w')
        f.write(s)
        f.close()
        ss=r'''# qtate jobs
from time import sleep
from commands import getoutput as do
def run(): # 1 finish
    f=open('jobid','r')
    jobs = do('hep_q -u')
    for i in f.readlines():
        if i[0:-2] in jobs:
            return 0
    return 1
if run()==1:
    print "#################################"
    print "# all of your jobs are done !!! #"
    print "#################################"
else:
    print "Some jobs is still running, please wait for some times..."
'''
        f=open(self.log+'qstate.py','w')
        f.write(ss)
        f.close()




