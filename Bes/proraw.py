#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Bes import boss


class proraw:
    def __init__(self):
        self.rawpth = 'root'
        self.outpth = 'mode'
        self.job = 'cxx'
        self.tree = "sig"
        self.cut = ""
        self.name = 'example'

    def setcut(self, x):
        self.cut = x

    def setree(self, x):
        self.tree = x

    def setcxxpth(self, x):
        if x[-1] == '/':
            self.job = x[0:len(x) - 1]
        else:
            self.job = x

    def setraw(self, x):
        if x[-1] == '/':
            self.rawpth = x[0:len(x) - 1]
        else:
            self.rawpth = x

    def setout(self, x):
        if x[-1] == '/':
            self.outpth = x[0:len(x) - 1]
        else:
            self.outpth = x

    def setname(self, x):
        self.name = x

    def mkdir(self):
        boss.mkdir(self.job)
        boss.mkdir(self.outpth)

    def mkcxx(self):
        self.mkdir()
        f = open(self.job + '/' + self.name + '.cxx', 'w')
        f.write('{ \n')
        f.write('    TChain* ch=new TChain("' + self.tree + '");\n')
        f.write('    ch->Add("' + self.rawpth + '/*.root");\n')
        f.write('    TFile *f=new TFile("' + self.outpth + '/' + self.name +
                '.root","recreate");\n')
        f.write('    TTree *t=ch->CopyTree("' + self.cut + '");\n')
        f.write('    t->Write();\n')
        f.write('    f->Close();\n}\n')
