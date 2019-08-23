import SimAndRec
import os
class process:
    def __init__(self, name, simff, recff):
        self._name = name
        self._simff = simff
        self._recff = recff
    def AnA(self):
        ffName = "ana%s.py"%(self._name)
        pth = os.getcwd() 
        self._simff = os.path.join(pth, self._simff)
        self._recff = os.path.join(pth, self._recff)
        f=open(ffName,'w')
        ss = 'from SimAndRec import SimRecAna\n'
        ss += 'from SimAndRec import util\n'
        ss += "opt='''//test'''\n"
        ss += 'svc = SimRecAna.process("%s","%s")\n'\
                %(self._simff,self._recff)
        ss += 'svc.SetOpt(opt)\n'
        ss += '''if len(util.getArv()) ==0:
    svc.Make()
    svc.Sub()
    exit(0)
elif '-make' in util.getArv() :
    svc.Make()
    exit(0)
        '''
        f.write(ss)
        f.close()
    
    
    def Make(self):
        self.AnA()
        ffName = "init%s.py"%(self._name)
        pth = os.getcwd() 
        self._simff = os.path.join(pth, self._simff)
        self._recff = os.path.join(pth, self._recff)
        f=open(ffName,'w')
        ss = 'import SimAndRec\n'
        ss += 'import util\n'
        ss += 'svc = SimAndRec.process("%s","%s")\n'%(self._simff,self._recff)
        ss += '''if len(util.getArv()) ==0:
    svc.Make()
    svc.Sub()
    exit(0)
elif '-make' in util.getArv() :
    svc.Make()
    exit(0)
        '''
        f.write(ss)
        f.close()
        setup_bash = ''
        for line in open("setup.sh").readlines():
            if "Sim%s"%(self._name) in line:
                continue
            setup_bash += line 
        setup_bash +=  'alias Sim%s="python ${SIMANDRECDIR}/init%s.py"'%(self._name, self._name)
        #print (setup_bash)
        f = open("setup.sh", 'w')
        f.write(setup_bash+'\n')
        f.close()
        
        setup_tcsh = ''
        for line in open("setup.csh").readlines():
            if "Sim%s"%(self._name) in line:
                continue
            setup_tcsh += line 
        setup_tcsh +=  'set Sim%s="python ${SIMANDRECDIR}/init%s.py"'%(self._name, self._name)
        f = open("setup.csh", 'w')
        f.write(setup_tcsh+'\n')
        f.close()
