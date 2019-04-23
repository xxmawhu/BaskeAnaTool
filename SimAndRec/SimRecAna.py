from Zeus import zeus
import Ana
import util,os, inspect
import SimAndRec
from commands import getoutput as do
class process(SimAndRec.process):
    def __init__(self, _simTemp, _recTemp):
        SimAndRec.process.__init__(self, _simTemp, _recTemp)
        self._simOuts=[]
        self._recOuts=[]
        self._anaJobs=[]
    def Make(self):
        SimAndRec.process.Make(self)
        # config
        self._anaPth = os.path.join(self._datPth, "ana")
        util.mkdir(self._anaPth)

        for i in range(self._numOfJob):
            rawFile = os.path.join(self._rawPth, "raw_%04d.rtraw"%(i+1))
            rawFile = os.path.abspath(rawFile)
            self._recOuts.append(rawFile)
            dstFile = os.path.join(self._dstPth, "dst_%04d.dst"%(i+1))
            dstFile = os.path.abspath(dstFile)
            self._dstOuts.append(dstFile)
            
            anaFile = os.path.join(self._anaPth, "%04d.root"%(i+1))
            anaFile = os.path.abspath(anaFile)

            self._recSvc.RecOutputFile(dstFile)
            self._recSvc.PrintToFile(rectxt)
    def Sub(self):
        jobList=[]
        curFF = inspect.stack()[1][1]
        curPth = os.path.split(curFF)[0]
        for i in range(self._numOfJob):
            _NUMFILE = os.path.join(curPth,".NUM")
            _NUM = int(do('cat %s'%(_NUMFILE)))+1
            do('echo "%d" > %s '%(_NUM, _NUMFILE))
            fnm = "jobs_%06d.sh"%(_NUM)
            ffnm = os.path.join(self._subPth, fnm)
            f=open(ffnm,'w')
            f.write("boss.exe " +self._simJobs[i]+'\n')
            f.write("sleep 100\n")
            f.write("boss.exe " +self._recJobs[i]+'\n')
            f.close()
            jobList.append(os.path.abspath(ffnm))
        util.hepsub(jobList)
