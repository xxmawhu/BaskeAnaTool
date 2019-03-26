class configRecEasy:
    def __init__(self, temp = "template/psi2S.txt"):
        self._temp = temp
        self._opt=[]
        self._val={}
        self._com={}
        self._inc={}
    def _Split(self,ll):
        v1 = ll.split(".")[0]
        indx = len(v1)+1
        l2 = ll[indx:]
        v2 = l2.split("=")[0]
        l3 = l2.split("=")[1]
        #l3 = l2[len(v2):]
        v3 = l3.split(";")[0]
        return [v1,v2,v3]
    def _GetOpt(self):
        lineNum=0
        comtmp = ""
        inctmp=""
        for ll in open(self._temp):
            lineNum += 1
            name = "line_%02d"%(lineNum)
            print "line: ", lineNum
            print ll
            if len(ll.split()) == 0:
                continue
            if "//" == ll.split()[0][0:2]:
                comtmp = ll[2:].replace('\n',"")
            if "include" in ll:
                inctmp = ll.split()[1].replace('\n',"")
                self._opt.append(name)
                self._inc[name] = inctmp
                self._com[name] = comtmp
                inctmp = ""
                comtmp = ""
                continue
            if not "." in ll:
                continue
            optAndVal = self._Split(ll)
            opt = optAndVal[0]
            obj = optAndVal[1]
            var = optAndVal[2]
            if not opt in self._opt:
                self._opt.append(opt)
            if opt in self._val.keys():
                self._val[opt].append(obj +'='+ var)
            else:
                self._val[opt] =[ obj + "=" + var]

    def SetConfigTxt(self, ff):
        self._temp = ff
    def Make(self, name="Rec3770", test = False):
        self._GetOpt()
        f = open(name+".py",'w')
        f.write("from Zeus import zeus \n")
        f.write("class "+ name+ "(zeus) : \n")
        body = r'''    def __init__(self):
        zeus.__init__(self)
'''
        inde = 8*' '
        for i in self._opt:
            inctmp = '""'
            comtmp = ''
            if i in self._inc.keys():
                inctmp = self._inc[i]
            if i in self._com.keys():
                comtmp = self._com[i]
            print i, inctmp, comtmp
            body += inde + "zeus.AddOpt(self,\\\n"
            body += inde + '    "%s",\\\n' %(i)
            body += inde + '    %s,\\\n'%(inctmp)
            body += inde + '    "%s"\\\n'%(comtmp.replace('\n',""))
            body += inde + '    )\n'
        for i in self._val.keys():
            for j in self._val[i]:
                body += inde + 'zeus.SetOpt(self,\'%s\', \'%s\',\'%s\')\n' \
                    %(i.strip(), j.split("=")[0].strip(), j.split("=")[1])
        body += '''
    def SetRaw(self, raw):
        self.SetOpt("EventCnvSvc","digiRootInputFile",'"%s"'%raw)
    def SetDst(self, dst):
        self.SetOpt("EventCnvSvc","digiRootOutputFile",'"%s"'%dst)
    def SetSeed(self, seed):
        self.SetOpt("BesRndmGenSvc","RndmSeed",str(seed))
        '''
        f.write(body)
        if test:
            f.write('test = %s()\n'%(name))
            f.write('test.Make("%s.txt")'%(name))
        f.close()
        #self.GenProcess(name)
    def GenProcess(self, name):
        if name == "process":
            print "Please change the name:\t" ,name 
            return
        f=open("process.py")
        txt = f.read()
        f.close()
        txt= txt.replace("SimPsi2S", name)
        print txt
        f2=open("process"+name+'.py','w')
        f2.write(txt)
        f=open("init"+name+'.py','w')
        f.write("from SimAndRec.process%s import process\n"%name)
        f.write("svc = process()\n")
        f.write("svc.Make()\n")
        f.write("svc.Sub()\n")
        f.close()

#test = configSimEasy()
#test.Make()

