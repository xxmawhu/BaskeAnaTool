#!/afs/ihep.ac.cn/soft/common/python27_sl65/bin/python
# -*- coding: utf-8 -*-
import boss
import proraw
import name
import hepsub
import os
from commands import getoutput as do
import myfunction as myfun
class ana:
    def __init__(self):
        self.dsts=[]
        self.body=''
        self.wkpth=do('pwd')+'/' 
        self.job=self.wkpth+'jobs/'
        self.log=self.wkpth+'log/'
        self.mode=self.wkpth+'mode/'
        self.rawpth=self.wkpth+'root/'
        self.cxxpth=self.wkpth+'cxx/'
        self.rootnm='FILE'
        self.size=1.0 
        self.cut=[]
        self._num=1
        self.tree=[]
        self.name=[]
        self._drop = []
    def addcut(self,tree,cut='',name='(1+1==2)'):
        self.tree.append(tree)
        self.cut.append(cut)
        if name=='(1+1==2)':
            self.name.append(tree)
        else:
            self.name.append(name)
    def setpath(self,x):
        self.wkpth=x
        if x[-1]=='/':
            self.wkpth=x
        else:
            self.wkpth=x+'/'
        self.job=self.wkpth+'jobs/'
        self.log=self.wkpth+'log/'
        self.mode=self.wkpth+'mode/'
        self.rawpth=self.wkpth+'root/'
    def mkdir(self):
        boss.mkdir(self.job)
        boss.mkdir(self.log)
        boss.mkdir(self.mode)
        boss.mkdir(self.rawpth)
        boss.mkdir(self.cxxpth)
    def maxsize(self,x):
        self.size=x
    def setrootname(self, x):
        self.rootnm=x
    def setjobhead(self,x):
        t1='ApplicationMgr.HistogramPersistency = "ROOT";\n'
        t2='\nEventCnvSvc.digiRootInputFile = {\n'
        self.body=x+t1+t2

    def addst(self,x):
        t=len(x)
        if x[-1]=='/':
            adst=x[0:t-1]
        else:
            adst=x[0:t]
        self.dsts.append(adst)
    def make(self):
        self.mkdir()
        f=open(self.log+'list.txt','w')
        for i in self.dsts:
            for j in myfun.findfile(i):
                f.write(j+'\n')
        f.close()
        self.mkdir()
        dstname=name.getname(self.dsts)
        for i in range(0,len(self.dsts)):
            self.ajob(self.dsts[i],dstname[i])
            for k in range(0,len(self.cut)):
                self.mkadd(self.tree[k],self.cut[k],self.name[k]+'.'+dstname[i],dstname[i])

        f=open(self.mode+"hadd.sh","w")
        f.write("#!/bin/bash\n")
        for i in self.name:
            f.write("hadd -f "+i+"_all.root "+i+".*root && rm  "+ i+".*root\n")
        f.close()
        do("chmod 755 "+self.mode+"hadd.sh")
        print "Total:", do("ls jobs/*/*.txt -1 | wc -l"), "jobs"
    def sub(self):
        boss.mkdir(self.log)
        sub=hepsub.hepsub()
        sub.setlog(self.log)
        sub.setpath(self.job)
        sub.sub()
    def mkadd(self,tree,cut,name,jobnm):
        p=proraw.proraw()
        p.setname(name)
        p.setraw(self.rawpth+jobnm)
        p.setout(self.mode)
        p.setcut(cut);
        p.setree(tree)
        p.mkcxx()
    def setjobnum(self,n):
        self._num = n
    def drop(self,s):
        self._drop=s 
    def ajob(self,dst,name): 
        print '.........................................................'
        print dst
        print 'each job contain about ',self.size,'G dsts'
        dsts = int(do('ls -1 -F '+ dst+r'  | grep -v [/$] | wc -l'))
        print "total dsts: ", dsts
        size = int( int(do('du ' + dst ).split()[0])/1024./1024./self.size )
        job=self.job+name
        root=self.rawpth+name
        boss.mkdir(job)
        boss.mkdir(root)
        j=boss.subjobs()
        j.setbody(self.body)
        jobnum = self._num
        if jobnum < size:
            jobnum = size+1
        if dsts<jobnum: 
            jobnum = dsts
        j.setjobnum(jobnum)
        j.setjobname("jobs_") 
        j.setname(self.rootnm)
        j.setdstpath(dst)
        j.setjobpath(job)
        j.drop(self._drop)
        j.setrootpath(root)
        j.jobs()


class anaJpsi(ana):
    def __init__(self):
        ana.__init__(self)
    def addJpsi(self, date):
        Dict = {2009:'/besfs3/offline/data/703-1/jpsi/round02/dst',
                2012:'/besfs3/offline/data/703-1/jpsi/round05/dst',
                2017:'/bes3fs/offline/data/704-1/jpsi/round11/dst',
                2018:'/bes3fs/offline/data/704-1/jpsi/round12/dst'}
        hintDict = {2009:'add 2009 Jpsi data(0.2 billion)',
                2012:'add 2012 Jpsi data(1.1 billion)',
                2017:'add 2017-2018 Jpsi data(4.6 billion)',
                2018:'add 2018-2019 Jpsi data(4.1 billion)'}
        print(hintDict[date])
        dst = Dict[date]
        ll = do('ls %s/* -d' %dst).split()
        for l in ll:
            ana.addst(self, l)
