import os
from nom import NUM
from commands import getoutput as do
class Sub:
    def __init__(self, sim=[], rec=[]):
        self._sim = sim
        self._rec = rec
    def SetSimJobs(self, sim):
        self._sim = sim
    def SetRecJobs(self, rec):
        self._rec = rec
    def MakeBashFile(self):
        if len(self._sim) != len(self._rec):
            print "Please cheack !!! The number of simulation jobs"+\
            " is not equal to the number of reconstruct jobs"
            return
        pth = os.getcwd()
        jobs = []
        for i in range(len(self._sim)):
            simpth = os.path.split(self._sim[i])[0]
            NUM +=1 
            do('echo "NUM=%d" > %s'%(NUM,\
                "/besfs/users/maxx/home/head/num.py"))
            name = 'simJob_%04d.sh'%(NUM)
            ff = os.path.join(simpth,name)
            jobs.append(ff)
            f = open(ff,'w')
            f.write("#!/bin/bash\n")
            f.write("cd %s\n"%os.path.abspath(simpth))
            f.write("boss.exe %s\n"%(os.path.split(self._sim[i])[1]))
            f.write("sleep 100\n")
            f.write("boss.exe %s\n"%(os.path.split(self._rec[i])[1]))
        return jobs
