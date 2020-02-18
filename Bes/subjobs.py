#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from multiprocessing.pool import ThreadPool as ProcessPoolExecutor
# from concurrent.futures import ProcessPoolExecutor
import time
import glob
import logging
logger = logging.getLogger(__name__)


class subjobs(object):
    def __init__(self):
        self._inputDstDir = ""
        self._jobsDir = "."
        self._n = 1
        self._NTupleFile = 'FILE'
        self._outFilePrefix = 'root'
        self._bad = []
        self._jobname = 'job'
        self._dstFileList = []
        self._nprocesser = 20

    def setInputDstDir(self, dstdir, key=''):
        self._inputDstDir = dstdir
        dstfileList = glob.glob(self._inputDstDir+"/*.dst")
        list.sort(dstfileList)
        if key == "":
            self._dstFileList = sorted(dstfileList)
        else:
            self._dstFileList = list(filter(lambda x: key in x, sorted(
                dstfileList)))
        # no dst
        if not self._dstFileList:
            logger.error("No dst file in this directory: {}".format(
               dstdir
                ))
            return False
        else:
            return True

    def setdstpath(self, dstdir, key=""):
        self.setInputDstDir(dstdir, key)

    def drop(self, dsts):
        self._bad = dsts

    def _drop(self):
        for i in self._bad:
            self._rm(i)

    def _rm(self, badst):
        for i in self._dstFileList:
            if badst in i:
                self._dstFileList.remove(i)

    def setjobpath(self, job):
        self._jobsDir = job
        if (not os.path.isdir(self._jobsDir)):
            os.makedirs(self._jobsDir)

    def setrootname(self, outFilePrefix):
        self._outFilePrefix = outFilePrefix

    def setrootpath(self, root):
        self._root = root
        if (not os.path.isdir(self._root)):
            os.makedirs(self._root)

    def setjobnum(self, n):
        self._n = n

    def _process(self, i, j):
        """
        process self._dstFileList[i:j] then return a string
        "dst_1",
        "dst_2",
        ...
        "dst_last"
        """
        dst = ''
        for k in range(i, j):
            dst += '    "{}",\n'.format(self._dstFileList[k-1])
        # add the last file without `,`
        dst += '    "{}"\n'.format(self._dstFileList[j-1])
        return dst

    def setbody(self, s):
        self._body = s

    def setname(self, name):
        self._NTupleFile = name

    def setjobname(self, name):
        self._jobname = name

    def _creatjob(self, i, j, jobindex):
        """
        i: the begin index the dstList
        j: the end index of the dstList
        k: the file name index in the tail, such as `job_1.txt`
        """
        if self._bad:
            self._drop()
        # name = self._job + '/' + self._jobname + _num + '.txt'
        name = "{}/{}{}.txt".format(self._jobsDir, self._jobname, jobindex)
        f = open(name, 'w')
        f.write(self._body)
        f.write(self._process(i, j))
        f.write('};\n')
        root = 'NTupleSvc.output={\n'
        root += '    "' + self._NTupleFile
        root += " DATAFILE = '{}/{}.root' OPT= 'new' type='ROOT'".format(
                self._root,
                self._outFilePrefix+str(jobindex))
        root += '"\n};'
        f.write(root)
        f.close()

    def _MakeOneJob(self, args):
        self._creatjob(*args)

    def setProcesser(self, nprocessor):
        self._nprocesser = nprocessor

    def jobs(self):
        n = self._n
        if n == 0 :
            logger.error("the number of jobs is zero: {} ".format(
                self._inputDstDir))
        self._tot = len(self._dstFileList)
        each = int(self._tot / n)
        logger.info("Total `.dst` files is {}".format(self._tot))
        logger.info("Each job contains {} `.dst` file \n".format(each))
        over = self._tot - each * n
        argsList = []
        t0 = time.time()
        for i in range(0, over):
            m = each + 1
            # self._creatjob(i * m + 1, (i + 1) * m, i)
            argsList.append((i * m + 1, (i + 1) * m, i))
        for i in range(over, n):
            m = each
            # self._creatjob(i * m + 1 + over, (i + 1) * m + over, i)
            argsList.append((i * m + 1 + over, (i + 1) * m + over, i))
        pool = ProcessPoolExecutor(processes=self._nprocesser)
        pool.map(self._MakeOneJob, argsList)
        pool.close()
        t1 = time.time()
        logger.debug("Time: {0:.03f}".format(t1-t0))


if __name__ == "__main__":
    pass
