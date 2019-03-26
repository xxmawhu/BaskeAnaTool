import SimAndRec
import os
class process:
    def __init__(self, name, simff, recff):
        self._name = name
        self._simff = simff
        self._recff = recff
    def Make(self):
        ffName = "init%s.py"%(self._name)
        pth = os.getcwd() 
        self._simff = os.path.join(pth, self._simff)
        self._recff = os.path.join(pth, self._recff)
        f=open(ffName,'w')
        ss = 'import SimAndRec\n'
        ss += 'svc = SimAndRec.process("%s","%s")\n'\
                %(self._simff,self._recff)
        ss += 'svc.Make()\n'
        ss += 'svc.Sub()\n'
        f.write(ss)
        f.close()
        f=open("setup.sh","a+")
        alias = 'alias Sim%s="python ${SIMANDRECDIR}/init%s.py"'%(self._name, self._name)
        f.write(alias+'\n')
        f.close()
