from Zeus import zeus
import NUM
import util,os, inspect
from commands import getoutput as do
class process():
    def __init__(self, _simTemp, _recTemp):
        self._simSvc = zeus()
        self._simSvc.ProcessFile(_simTemp)
        self._recSvc = zeus()
        self._recSvc.ProcessFile(_recTemp)
        self._numOfJob = 1
        self._decayCard = "test.dec"
        self._totEvts =  10
        self._seedBegin  = 0
        self._datPth = "."
        self._simJobs=[]
        self._recJobs=[]
    def SetDatPath(self, datpth):
        self._datPth = datpth
    def SetSeedBegin(self, seed):
        self._seedBegin = seed
    def SetOpt(self, _class, _member, _value, _operator="="):
        self._simSvc.SetOpt(_class, _member, _value, _operator)
        self._recSvc.SetOpt(_class, _member, _value, _operator)
    def _config(self):
        opts = util.getOpt()
        self._decayCard = opts[0]
        print ("The decay card is \t" + self._decayCard)
        self._totEvts = float(opts[1])
        print ("Simulation events\t" + str(int(self._totEvts)))
        maxjobs = util.MaxJobs()
        if self._totEvts / 2E4 > maxjobs :
            self._numOfJob = maxjobs
        elif self._totEvts > 50E4:
            self._numOfJob = int(self._totEvts / 2E4 )
        else:
            self._numOfJob = int(self._totEvts / 1E4)
        if self._numOfJob==0:
            self._numOfJob = 1
        print ("The total jobs is \t" + str(int(self._numOfJob)))
        util.mkdir(self._datPth)
        self._subPth = os.path.join(self._datPth, "sub")
        self._rawPth = os.path.join(self._datPth, "raw")
        self._dstPth = os.path.join(self._datPth, "dst")
        util.mkdir(self._dstPth)
        util.mkdir(self._rawPth)
        util.mkdir(self._subPth)
    def Make(self):
        self._config()
        curFF = inspect.stack()[1][1]
        curPth = os.path.split(curFF)[0]
        decaycard = os.path.abspath(self._decayCard)
        self._simSvc.SetDecayCard(decaycard)
        evts = self._totEvts / self._numOfJob
        print ("Each job will simulate "+  str(int(evts)) + " evts")
        left = self._totEvts - evts * self._numOfJob 
        if left!= 0:
            print ("The first jobs will simulate extro " + str(evts) + "evts")
        for i in range(self._numOfJob):
            if i==0:
                self._simSvc.SetEvtMax(evts + left)
                self._recSvc.SetEvtMax(evts + left)
            else:
                self._simSvc.SetEvtMax(evts)
                self._recSvc.SetEvtMax(evts)
            _NUMFILE = NUM.NUMFILE
            _NUM = int(do('cat %s'%(_NUMFILE)))+1
            self._simSvc.SetSeed(self._seedBegin + _NUM + i)
            self._recSvc.SetSeed(self._seedBegin + _NUM + i)
            simtxt = os.path.join(self._subPth, "sim_%04d.txt"%(i+1))
            self._simJobs.append("sim_%04d.txt"%(i+1))
            rectxt = os.path.join(self._subPth, "rec_%04d.txt"%(i+1))
            self._recJobs.append("rec_%04d.txt"%(i+1))
            output = os.path.join(self._rawPth, "raw_%04d.rtraw"%(i+1))
            output = os.path.abspath(output)
            self._simSvc.SimOutputFile(output)
            self._simSvc.PrintToFile(simtxt)

            self._recSvc.SetOpt("EventCnvSvc", "digiRootInputFile",\
                   '{"%s"};'% output,"=")
            dstFile = os.path.join(self._dstPth, "dst_%04d.dst"%(i+1))
            dstFile = os.path.abspath(dstFile)
            self._recSvc.RecOutputFile(dstFile)
            self._recSvc.PrintToFile(rectxt)
    def Sub(self):
        jobList=[]
        curFF = inspect.stack()[1][1]
        curPth = os.path.split(curFF)[0]
        for i in range(self._numOfJob):
            _NUMFILE = NUM.NUMFILE
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
