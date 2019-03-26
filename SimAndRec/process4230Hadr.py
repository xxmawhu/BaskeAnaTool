from Sim4230Hadr import Sim4230Hadr as sim
from Rec4230Hadr import Rec4230Hadr as Rec
import Sub
import util,os
class process(sim, Sub.Sub):
    def __init__(self, datpth = '.'):
        Sub.Sub.__init__(self)
        sim.__init__(self)
        self._jobs = 1
        self._decayCard = "test.dec"
        self._totEvts =  10
        self._sedBegin  = 1
        self._datPth = datpth
    def SetDatPath(self, datpth):
        self._datPth = datpth
    def _config(self):
        opts = util.getOpt()
        self._decayCard = opts[0]
        print "The decay card is \t", self._decayCard
        self._totEvts = float(opts[1])
        print "Simulation events\t", int(self._totEvts)
        maxjobs = util.MaxJobs()
        if self._totEvts / 2E4 > maxjobs :
            self._jobs = maxjobs
        elif self._totEvts > 50E4:
            self._jobs = int( self._totEvts / 2E4 )
        else:
            self._jobs = int(self._totEvts / 1E4)
        if self._jobs==0:
            self._jobs = 1
        print "The total jobs is \t", int(self._jobs)
        util.mkdir(self._datPth)
        self._subPth =  os.path.join(self._datPth, "sub")
        self._rawPth =  os.path.join(self._datPth, "raw")
        self._dstPth =  os.path.join(self._datPth, "dst")
        util.mkdir(self._dstPth)
        util.mkdir(self._rawPth)
        util.mkdir(self._subPth)
    def Make(self):
        self._config()
        #sim
        simSvc = sim()
        decaycard = os.path.abspath(self._decayCard)
        self.SetDecayCard(decaycard)
        #rec
        recSvc = Rec()
        #os.chdir(self._subPth)
        evts = self._totEvts / self._jobs
        self.SimEvtMax(evts)
        left = self._totEvts - evts * self._jobs 
        simjobs = []
        recjobs = []
        for i in range(self._jobs):
            if i==0:
                simSvc.SimEvtMax(evts + left)
            self.SimSeed(self._sedBegin + i)
            recSvc.SetSeed(self._sedBegin + i)
            simtxt = os.path.join(self._subPth, "sim_%04d.txt"%(i+1))
            rectxt = os.path.join(self._subPth, "rec_%04d.txt"%(i+1))
            simjobs.append(simtxt)
            recjobs.append(rectxt)
            output = os.path.join(self._rawPth, "raw_%04d.rtraw"%(i+1))
            output = os.path.abspath(output)
            self.SimOutputFile(output)
            self.MakeSimFile(simtxt)
            recSvc.SetRaw(output)
            dstFile = os.path.join(self._dstPth, "dst_%04d.dst"%(i+1))
            dstFile = os.path.abspath(dstFile)
            recSvc.SetDst(dstFile)
            recSvc.PrintToFile(rectxt)
        #sub = Sub.Sub(simjobs, recjobs)
        self.SetSimJobs(simjobs)
        self.SetRecJobs(recjobs)
        self._bashs = self.MakeBashFile()
        #print self._bashs
    def Sub(self):
        util.hepsub(self._bashs)
