#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Bes import myfunction as m
from Bes.commands import getoutput as do
from Bes import hepsub
import os
from Bes.commands import getoutput
import glob
import time
from multiprocessing.pool import ThreadPool
import logging
logger = logging.getLogger(__name__)
# from SubJob import hep


class SubWithProcId(hepsub.hepsub):
    """
    path: hepsub.getPath()
       sub all jobs_%{ProcId}.txt in the fildor
    """
    def __init__(self):
        super(SubWithProcId, self).__init__()

    def getSubJobDir(self):
        dirList = os.listdir(self.getPath())
        logging.debug(dirList)
        logging.debug("self.getPath() = {}".format(self.getPath()))
        for i in range(len(dirList)):
            dirList[i] = os.path.join(self.getPath().strip(), dirList[i])
        logging.debug(dirList)
        return dirList

    def _subJobInOneDir(self, aDir):
        logging.debug("cd {dir} ; boss.condor -n {Njobs} {JOB}".format(
            dir=aDir,
            Njobs=len(glob.glob(aDir + "/jobs_*.txt")),
            JOB=r"jobs_%{ProcId}.txt"))
        out = getoutput("cd {dir} ; boss.condor -n {Njobs} {JOB}".format(
            dir=aDir,
            Njobs=len(glob.glob(aDir + "/jobs_*.txt")),
            JOB=r"jobs_%{ProcId}.txt"))
        num = out.split()[-1]
        logging.debug(out)
        logger.debug("num = {}".format(num))
        return num

    def subAllJobs(self, jobsList):
        if not jobsList:
            logger.warning("no jobs")
            return
        logger.debug("Please wait for some seconds!")
        t0 = time.time()
        if len(jobsList) == 1:
            logger.info("Sub all Jobs in {}".format(jobsList[0]))
            jobId = self._subJobInOneDir(jobsList[0])
            logger.info("job ID: {}".format(jobId))
            f = open(self.getLog() + "/.id", 'w')
            f.write("{} {}\n".format(" jobID ", "jobdir"))
            f.write("{} {}\n".format(jobdir, jobsList[0]))
            f.close()
            return
        t = ThreadPool(processes=5)
        numList = t.map(self._subJobInOneDir, jobsList)
        t.close()
        t1 = time.time()
        logger.info("sub all jobs successful!")
        logger.info("Sub jobs consumes {0:.3f} s".format(t1 - t0))
        with open(self.getLog() + "/.id", 'w') as f:
            f.write("{} {}\n".format(" jobID ", "jobdir"))
            for i, jobdir in zip(numList, jobsList):
                try:
                    float(i)
                    logger.info("job ID: {}".format(i))
                    f.write("{} {}\n".format(i, jobdir))
                except Expection as e:
                    logger.error(e)

    def sub(self):
        """
        overload the base function `sub`
        """
        self.subAllJobs(self.getSubJobDir())


if __name__ == "__main__":
    logger.debug("test the command")
    command = "cd {dir} ; boss.condor -n {Njobs} {JOB}".format(
        dir="~", Njobs=len(os.listdir('.')), JOB=r"jobs_%{ProcId}.txt")
    logger.debug("the command is {}".format(command))
