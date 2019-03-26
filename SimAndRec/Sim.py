class sim:
    def __init__(self):
        self._part = []
        self._baseOpt = {}
        self._Descripton = {}
        self._setOpt = {}
        self._Oper = {}
        self._run = ""
        self._events = 10
    def AddOpt(self, name, baseOpt='', description = "", oper = "="):
        self._part.append(name)
        self._baseOpt[name] = baseOpt
        self._Descripton[name] = description
        self._setOpt[name] = []
        self._Oper[name] = []
    def SetOpt(self,name, opt, val ):
        if not name in self._baseOpt: 
            return 
        isNewOpt = True
        for kk in self._setOpt[name]:
            if opt.strip() == kk[0].strip():
                kk[1] = str(val) 
                isNewOpt = False
        if isNewOpt:
            self._setOpt[name].append([opt.strip(), str(val)])
    def SetDecayCard(self, card):
        self.SetOpt('EvtDecay', 'userDecayTableName','"%s"'%card)
    def SimEvtMax(self,num):
        self.SetOpt("ApplicationMgr", "EvtMax", str(int(num)))
    def SetRunIdList(self, runList):
        self.SetOpt('RealizationSvc', 'RunIdList ',str(runList))
    def SimOutputFile(self, ouput):
        self.SetOpt('RootCnvSvc', 'digiRootOutputFile','"%s"'%ouput)
    def SimSeed(self, seed):
        self.SetOpt('BesRndmGenSvc', 'RndmSeed ',str(seed))
    def MakeSimFile(self, ff):
        f = open(ff,"w")
        for i in self._part:
            if self._Descripton[i] != "":
                f.write(r"//"+self._Descripton[i]+'\n')
            if self._baseOpt[i] != "":
                f.write(r'#include "'+self._baseOpt[i]+'"\n')
            for opt in self._setOpt[i]:
                f.write(i+"."+opt[0]+" = "+opt[1]+';\n')
            f.write("\n")
        f.close()
