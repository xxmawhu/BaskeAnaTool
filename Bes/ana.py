#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from Bes import subjobs
from Bes import proraw
from Bes import name
# from Bes import hepsub
from Bes import SubWithProcId
from Bes.commands import getoutput as do
from Bes import myfunction as myfun
import util
import logging
logger = logging.getLogger(__name__)


class ana:
    def __init__(self):
        self.dsts = []
        self.body = ''
        self.wkpth = do('pwd').split()[0] + '/'
        self.job = self.wkpth + 'jobs/'
        self.log = self.wkpth + 'log/'
        self.mode = self.wkpth + 'merged/'
        self.rawpth = self.wkpth + 'rawFile/'
        self.cxxpth = self.wkpth + 'hadd/'
        self.rootnm = 'FILE'
        self.size = 1.0
        self.cut = []
        self._num = 1
        self.tree = []
        self.name = []
        self._drop = []

    def addcut(self, tree, cut='', name='(1+1==2)'):
        self.tree.append(tree)
        self.cut.append(cut)
        if name == '(1+1==2)':
            self.name.append(tree)
        else:
            self.name.append(name)

    def setCutForTree(self, tree, cut, name):
        self.addcut(tree, cut, name)

    def setpath(self, x):
        self.wkpth = x
        if x[-1] == '/':
            self.wkpth = x
        else:
            self.wkpth = x + '/'
        self.job = self.wkpth + 'jobs/'
        self.log = self.wkpth + 'log/'
        self.mode = self.wkpth + 'mode/'
        self.rawpth = self.wkpth + 'root/'

    def mkdir(self):
        util.mkdir(self.job)
        util.mkdir(self.log)
        util.mkdir(self.mode)
        util.mkdir(self.rawpth)
        util.mkdir(self.cxxpth)

    def maxsize(self, x):
        self.size = x

    def setrootname(self, x):
        self.rootnm = x

    def setjobhead(self, x):
        t1 = 'ApplicationMgr.HistogramPersistency = "ROOT";\n'
        t2 = '\nEventCnvSvc.digiRootInputFile = {\n'
        self.body = x + t1 + t2

    def setJobOption(self, joboptions):
        self.setjobhead(joboptions)

    def addst(self, x):
        t = len(x)
        if x[-1] == '/':
            adst = x[0:t - 1]
        else:
            adst = x[0:t]
        self.dsts.append(adst)

    def addDataSet(self, dateSet):
        self.addst(dateSet)

    def make(self):
        self.mkdir()
        f = open(self.log + 'list.txt', 'w')
        for i in self.dsts:
            fileList = myfun.findfile(i)
            if len(fileList) == 0:
                logger.warning("no dst in this file, " + i)
                continue
            for j in fileList:
                f.write(j + '\n')
        f.close()
        self.mkdir()
        dstname = name.getname(self.dsts)
        for i in range(0, len(self.dsts)):
            self.ajob(self.dsts[i], dstname[i])
            for k in range(0, len(self.cut)):
                self.mkadd(self.tree[k], self.cut[k],
                           self.name[k] + '.' + dstname[i], dstname[i])

        f = open(self.mode + "hadd.sh", "w")
        f.write("#!/bin/bash\n")
        for i in self.name:
            f.write("hadd -f " + i + "_all.root " + i + ".*root && rm  " + i +
                    ".*root\n")
        f.close()
        do("chmod 755 " + self.mode + "hadd.sh")
        logger.info("Total: {} {}".format(
            do("ls jobs/*/*.txt -1 | wc -l").split()[0], "jobs"))

    def sub(self):
        util.mkdir(self.log)
        sub = SubWithProcId.SubWithProcId()
        sub.setlog(self.log)
        logger.debug("self.job = {}".format(self.job))
        sub.setpath(os.path.abspath(self.job))
        sub.sub()

    def mkadd(self, tree, cut, name, jobnm):
        p = proraw.proraw()
        p.setname(name)
        p.setraw(self.rawpth + jobnm)
        p.setout(self.mode)
        p.setcut(cut)
        p.setree(tree)
        p.mkcxx()

    def setjobnum(self, n):
        self._num = n

    def drop(self, s):
        self._drop = s

    def ajob(self, dst, name):
        logger.info("Process " + dst)
        logger.info('each job contain about {} {}'.format(
            self.size, 'G dsts'))
        dsts = int(do('ls -1 -F ' + dst + r'  | grep -v [/$] | wc -l'))
        logger.debug("total dsts: {}".format(dsts))
        size = int(int(do('du ' + dst).split()[0]) / 1024. / 1024. / self.size)
        job = self.job + name
        root = self.rawpth + name
        util.mkdir(job)
        util.mkdir(root)
        j = subjobs.subjobs()
        j.setbody(self.body)
        jobnum = self._num
        if jobnum < size:
            jobnum = size + 1
        if dsts < jobnum:
            jobnum = dsts
        j.setjobnum(jobnum)
        j.setjobname("jobs_")
        j.setname(self.rootnm)
        j.setdstpath(dst)
        j.setjobpath(job)
        j.drop(self._drop)
        j.setrootpath(root)
        j.jobs()

