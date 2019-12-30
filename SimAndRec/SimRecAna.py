from Zeus import zeus
import Ana
import util, os, inspect
import SimAndRec
from Bes.commands import getoutput as do


class process(SimAndRec.process):
    def __init__(self, _simTemp, _recTemp):
        SimAndRec.process.__init__(self, _simTemp, _recTemp)
        self._opt = ''
        self._simOuts = []
        self._recOuts = []
        self._anaJobs = []

    def SetOpt(self, opt):
        self._opt = opt

    def Make(self):
        SimAndRec.process.Make(self)
        # config
        self._anaPth = os.path.join(self._datPth, "ana")
        util.mkdir(self._anaPth)

        for i in range(self._numOfJob):
            rawFile = os.path.join(self._rawPth, "raw_%04d.rtraw" % (i + 1))
            rawFile = os.path.abspath(rawFile)
            self._simOuts.append(rawFile)
            dstFile = os.path.join(self._dstPth, "dst_%04d.dst" % (i + 1))
            dstFile = os.path.abspath(dstFile)
            self._recOuts.append(dstFile)

            anaout = os.path.join(self._anaPth, "%04d.root" % (i + 1))
            anaout = os.path.abspath(anaout)
            anaFile = os.path.join(self._subPth, "ana_%04d.txt" % (i + 1))
            anaFile = os.path.abspath(anaFile)
            self._anaJobs.append("ana_%04d.txt" % (i + 1))
            ana = Ana.ana(self._opt, dstFile, anaout)
            ana.Make(anaFile)

    def Sub(self):
        jobList = []
        curFF = inspect.stack()[1][1]
        curPth = os.path.split(curFF)[0]
        for i in range(self._numOfJob):
            fnm = "jobs_%d.sh" % (i)
            ffnm = os.path.join(self._subPth, fnm)
            f = open(ffnm, 'w')
            f.write("boss.exe " + self._simJobs[i] + '\n')
            f.write("sleep 10\n")
            f.write("boss.exe " + self._recJobs[i] + '\n')
            f.write("sleep 10\n")
            f.write("boss.exe " + self._anaJobs[i] + '\n')
            f.write("rm -rf " + self._simOuts[i] + '\n')
            f.write("rm -rf " + self._recOuts[i] + '\n')
            f.close()
            jobList.append(os.path.abspath(ffnm))
        util.hepsub(jobList)
