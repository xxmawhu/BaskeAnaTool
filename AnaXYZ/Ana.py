import Bes, JobOption, os
from commands import getoutput as do
import DataSet


class XYZData:
    def __init__(self):
        self._cwd = os.getcwd()
        self._BaseJobOpt = JobOption.Default
        self._sub = False
        self._opt = ''
        self._bossVersion = "7.0.3"
        self.BeamE = 4.2
        self._dataSet = {}
        self._beamE = {}
        self._tail = JobOption.tail
        self._alg = "Phi2PiAlg"

    def setJobOpt(self, s):
        self._opt = s

    def setBeamE(self, s):
        self.BeamE = s

    def setBossVersion(self, s="7.0.3"):
        self._bossVersion = s
        CMTPATH = do('echo $CMTPATH')
        if len(CMTPATH.split()) == 0:
            print("warning: please set the BOSS first!!!")
        if "7.0.3" in CMTPATH:
            print("The current BOSS version is 7.0.3")
        if "6.6.4" in CMTPATH:
            print("The current BOSS version is 6.6.4")
        if not s in CMTPATH:
            print("warning: what the BOSS version you set is: ", s, "!!!")

    def _getDataSet(self, bossVersion):
        if "7.0.3" in bossVersion:
            self._dataSet = DataSet.dstlocation
            self._beamE = DataSet.beamE

    def SetMainAlg(self, alg):
        self._alg = alg

    def _ana(self, ID, dsts):
        if not os.path.isdir(ID):
            os.mkdir(ID)
        os.chdir(ID)
        if len(dsts) == 0:
            print("warning: The data Set are empty!!!")
            return
        datAna = Bes.ana.ana()
        datAna.setjobnum(1)
        jobOpt = self._BaseJobOpt + "\n"
        jobOpt += self._opt + "\n"
        jobOpt += "%s.BeamE = %f;\n" % (self._alg, self.BeamE)
        jobOpt += self._tail
        datAna.setjobhead(jobOpt)
        datAna.maxsize(15)
        datAna.setjobnum(1)
        for i in dsts:
            datAna.addst(i)
        datAna.setrootname("FILE")
        datAna.addcut('sig', "", 'sig')
        datAna.make()
        if self._sub:
            datAna.sub()
        os.chdir(self._cwd)

    def make(self):
        self._getDataSet(self._bossVersion)
        self._sub = False
        for ID in self._dataSet.keys():
            #print ID, self._dataSet[ID]
            self.BeamE = self._beamE[ID]
            dsts = []
            for ff in os.listdir(self._dataSet[ID]):
                print("read " + ff)
                tmp = os.path.join(self._dataSet[ID], ff)

                if not os.path.isdir(tmp):
                    continue
                if len(os.listdir(tmp)) == 0:
                    continue
                dsts.append(tmp)
            self._ana(ID, dsts)

    def sub(self):
        self._getDataSet(self._bossVersion)
        self._sub = True
        for ID in self._dataSet.keys():
            print("process %s!!!" % (ID))
            self.BeamE = self._beamE[ID]
            dsts = []
            for ff in os.listdir(self._dataSet[ID]):
                print("read " + ff)
                tmp = os.path.join(self._dataSet[ID], ff)
                if not os.path.isdir(tmp):
                    continue
                if len(os.listdir(tmp)) == 0:
                    continue
                dsts.append(tmp)
            self._ana(ID, dsts)
