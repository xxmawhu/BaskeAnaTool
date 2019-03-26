class configProcessEasy:
    def __init__(self, name="JPsi",simName="SimJPsi", recName="RecJPsi"):
        self._name = name
        self._simName = simName
        self._recName = recName
    def Make(self):
        self.GenProcess(self._name)
    def GenProcess(self, name):
        if name == "process":
            print "Please change the name:\t" ,name 
            return
        f=open("process.py")
        txt = f.read()
        f.close()
        txt= txt.replace("SimPsi2S", self._simName)
        txt= txt.replace("RecJPsi", self._recName)
        #print txt
        f2=open("process"+name+'.py','w')
        f2.write(txt)
        f=open("init"+name+'.py','w')
        f.write("from SimAndRec.process%s import process\n"%name)
        f.write("svc = process()\n")
        f.write("svc.Make()\n")
        f.write("svc.Sub()\n")
        f.close()

test = configProcessEasy("JJJ")
test.Make()

