from commands import getoutput
import os
import time
class process():
    def __init__(self):
        self._raw    = "../mode/sig*root"
        self._beamE  = "beamE"
        self._output = "sig.root"
        self._tree   = "sig"
        self._mk = False
        self._cxxfile = []
        self._mass   = {}
        self._input  = []
        self._out    = []
    def SetRawRoot(self, raw, tree = "sig"):
        self._raw = raw
        self._tree = tree
    def OutPut(self, out="sig.root"):
        self._output = out
    def _GetOut(self):
        _input=[]
        for i in self._mass.keys():
            _input.append(i)
        self._out = set(_input)


    def _GetInput(self):
        _input=[]
        for i in self._mass.keys():
            tmp = self._mass[i]
            tmp = tmp.replace('(',' ')
            tmp = tmp.replace(')',' ')
            #tmp = tmp.replace('M',' ')
            tmp = tmp.replace('+',' ')
            tmp = tmp.replace('-',' ')
            tmp = tmp.replace('*',' ')
            tmp = tmp.replace('.',' ')
            tmp = tmp.replace('/',' ')
            tmp = tmp.replace('\\',' ')
            for ll in tmp.split():
                if 'P4' in ll or "p4" in ll:
                    _input.append(ll)
        self._input = set(_input)


    def Add(self,mass, p4):
        self._mass[mass]=p4;


    def SetBeamEStr(self, beamE="beamE"):
        self._beamE = beamE

    def run(self):
        if not self._mk:
            self.mkcxx()
        for i in self._cxxfile:
            print("running ... ", i)
            print getoutput("root -l -b -q "+i)

    def mkcxx(self, name= "addBranch.cxx"):
        self._mk = True
        self._cxxfile.append(name)
        main=name.split('/')[-1].split('.')[0]
        self._GetOut()
        self._GetInput()
        tab ='    '
        f=open(name, 'w')
        s = '// Copyright (C) %d-%d-%d Ma Xinxin\n'%(time.localtime()[0:3])
        s += '''void '''+main+'''() {
    TChain* ch = new TChain("'''+self._tree+'''");
    ch->Add("'''+str(self._raw)+'''");
    TFile *f = new TFile("'''+self._output+'''", "recreate");
    TTree *t = ch->CloneTree(0);
'''
        for i in self._input:
            if 'beam' in i:
                continue
            else:
                s += tab + 'double %s[4];\n'%(i)
        s +='\n'
        for i in self._input:
            if 'beam' in i:
                #s += '\tch->SetBranchAddress("%s", %s);\n'%(self._beamE,i)
                s += '''
    double beamE;
    ch->SetBranchAddress("'''+self._beamE+r'''", &beamE);
'''
                continue
            else:
                s += tab + 'ch->SetBranchAddress("%s", %s);\n'%(i,i)

        for i in self._out:
            s += tab + 'double %s;\n'%(i)
        for i in self._out:
            s += tab + 't->Branch("%s", &%s, "%s/D");\n'%(i,i,i)
        s +='\n'
        for i in self._input:
            if 'beam' in i:
                s += tab + 'TLorentzVector _%s;\n'%(i)
            elif "P4" in i :
                newp4 = i.replace("P4","_P4")
                s += tab + 'TLorentzVector %s;\n'%(newp4)
            elif "p4" in i:
                newp4 = i.replace("p4","_p4")
                s += tab + 'TLorentzVector %s;\n'%(newp4)
            else: 
                newp4 = i.replace("p4","_p4")
                s += tab + 'TLorentzVector %s;\n'%(newp4)

        s +='''
    Int_t n = ch->GetEntries();
    for (Int_t i = 0; i < n; i++) {
        ch->GetEntry(i);
''' 

        for i in self._input:
            if 'beam' in i:
                s += tab + tab + i;
                s += ' = TLorentzVector(2*0.011*beamE,0,0,2*beamE);'
            elif "P4" in i :
                newp4 = i.replace("P4","_P4")
                s += tab + tab + '%s = TLorentzVector(%s);\n'%(newp4, i)
            elif "p4" in i:
                newp4 = i.replace("p4","_p4")
                s += tab + tab + '%s = TLorentzVector(%s);\n'%(newp4, i)
            else: 
                newp4 = i.replace("p4","_p4")
                s += tab + tab + '%s = TLorentzVector(%s);\n'%(newp4, i)
        for i in self._out:
            equl = self._mass[i]
            equl = equl.replace("P4", "_P4")
            equl = equl.replace("p4", "_p4")
            s += tab + tab + '%s = %s;\n'%(i, equl)
        s +='''
        t->Fill();
    }
    t->Write();
    f->Close();
}

'''
        f.write(s)
        f.close()

