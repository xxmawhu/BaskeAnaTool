class zeus:
    def __init__(self):
        self._class    = []
        self._member   = []
        self._operator = []
        self._value    = []
        self._type     = []
    def _processLine(self, line):
        #the line is a comment
        index = len(self._class)+1
        ll = line.split()
        if len(ll) ==0:
            return
        if ll[0][0:2] == "//":
            _class = "comment"+str(index)
            self._class.append(_class)
            self._member.append("")
            self._operator.append("")
            self._value.append(line)
            self._type.append("comment")
            return
        #the line is include head
        if ll[0].strip()=="#include":
            _class = "include"+str(index)
            self._class.append(_class.strip())
            self._member.append("")
            self._operator.append("")
            self._value.append(line)
            self._type.append("include")
            return
        #line is a class
        _class = line.split(".")[0].strip()
        _operator = ""
        if "=" in line:
            _operator = "="
        elif "+=" in line:
            _operator = "+="
        _member = line.split(".")[1].split(_operator)[0]
        _value = line.split(_operator)[1]
        
        self._class.append(_class.strip())
        self._member.append(_member.strip())
        self._operator.append(_operator.strip())
        self._value.append(_value.strip())
        self._type.append("class")
        return
    def ProcessFile(self, ff):
        for line in open(ff):
            self._processLine(line)
    def SetOpt(self, _class, _member, _value, _operator = "="):
        n = len(self._class)
        _member = _member.strip()
        _class = _class.strip()
        _value = _value.strip()
        _operator = _operator.strip()
        for i in range(n):
            if _class == self._class[i] and _member == self._member[i]:
                self._operator[i] = _operator
                self._value[i] = _value
    def PrintToFile(self, ff):
        f = open(ff, "w")
        n = len(self._class)
        for i in range(n):
            _type = self._type[i]
            if _type == "comment":
                f.write(self._value[i])
                continue
            if _type == "include":
                f.write(self._value[i])
                continue
            if _type== "class":
                _line = self._class[i]+"."+self._member[i]
                _line += self._operator[i]+self._value[i]+'\n'
                f.write(_line)
                continue
        f.close()
    def SetDecayCard(self, card):
        self.SetOpt('EvtDecay', 'userDecayTableName','"%s";'%card, "=")
    def SetEvtMax(self,num):
        self.SetOpt("ApplicationMgr", "EvtMax",\
                str(int(num))+';',"=")
    def SetRunIdList(self, runList):
        self.SetOpt('RealizationSvc', 'RunIdList ',str(runList),"=")
    def SetSeed(self, seed):
        self.SetOpt('BesRndmGenSvc', 'RndmSeed',str(seed)+';',"=")
    def SimOutputFile(self,output):
        self.SetOpt('RootCnvSvc', 'digiRootOutputFile',\
                '"%s";'%(output) ,"=")
    def RecOutputFile(self,output):
        self.SetOpt('EventCnvSvc', 'digiRootOutputFile',\
                '"%s";'%(output) ,"=")

