class configSimEasy:
    def __init__(self, temp = "template/psi2S.txt"):
        self._temp = temp
        self._opt=[]
        self._val={}
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
        for ll in open(self._temp):
            if "include"  in ll or "//" in ll or ll == "":
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
    def Make(self, name="Sim3770", test = False):
        self._GetOpt()
        f = open(name+".py",'w')
        f.write("from SimWithKKMC import SimWithKKMC \n")
        f.write("class "+ name+ "(SimWithKKMC) : \n")
        body = r'''    def __init__(self):
        SimWithKKMC.__init__(self)
'''
        inde = 8*' '
        for i in self._opt:
            for j in self._val[i]:
                if "+=" in j:
                    body += inde + 'self.SetOpt(\'%s\', \'%s\',\'%s\')\n' \
                    %(i.strip(), j.split("+=")[0].strip(), j.split("+=")[1])
                else:
                    body += inde + 'self.SetOpt(\'%s\', \'%s\',\'%s\')\n' \
                    %(i.strip(), j.split("=")[0].strip(), j.split("=")[1])
        f.write(body)
        if test:
            f.write('test = %s()\n'%(name))
            f.write('test.Make("%s.txt")'%(name))
        self.GenProcess(name)
    def GenProcess(self, name):
        if name == "process":
            print "Please change the name:\t" ,name 
            return
        f=open("process.py")
        txt = f.read()
        f.close()
        txt= txt.replace("SimPsi2S", name)
        #print txt
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

