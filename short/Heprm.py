import os
import sys
import commands
sys.path.append("/afs/ihep.ac.cn/users/m/maxx/head/")
class heprm:
    def __init__(self):
        self._opt=[]
        self._arv=[]
        self._stat=''
        self._ids=[]
        self._keyword='maxx'
    def _getopt(self):
        for i in range(1,len(sys.argv)):
            if '-' in sys.argv[i]:
                self._opt.append(sys.argv[i])
            else:
                self._arv.append(sys.argv[i])
    def _getkey(self):
        self._getopt()
        if len(self._arv)>0:
            self._keyword=self._arv[0]
    def _qstat(self):
        self._getkey()
        self._stat=commands.getoutput('hep_q -u maxx | grep '+self._keyword)
    def _getids(self):
        self._qstat()
        lines=self._stat.splitlines()
        for i in lines:
            if not 'JOBID' in i:
                self._ids.append(int(float(i.split()[0]))) 
    def run(self):
        self._getids()
        for i in self._ids:
            os.system('hep_rm '+str(i))
h=heprm()
h.run()
