import os
import sys
import util
from util import jobCandidates
from multiprocessing.pool import ThreadPool
import logging
logger = logging.getLogger(__name__)

_USAGE = '''Usage:  Running [option] [keyword]
Function:
    1.find all files (recursively)
    2.exe it with "root" or "sh"
Option:
    -r recursively
    -sh exe the file with "sh"
'''

class Runnow(jobCandidates):
    def __init__(self):
        jobCandidates.__init__(self)
        self._Uasge = _USAGE
    def _Process(self, aJob):
        logging.info("process {}".format(aJob))
        dn = os.path.split(aJob)
        Dir, name = dn[0], dn[1]
        if aJob[-3:] == ".sh":
            logging.info("cd {} ;bash {}".format(Dir, name))
            os.system("cd {} ;bash {}".format(Dir, name))
        else:
            logging.info("cd {} ;root -l -b -q {}".format(Dir, name))
            os.system("cd {} ; root -l -b -q {}".format(Dir, name))
    def run(self):
        self._prepare()
        # print self._jobList
        #sub="...", define the sub commands
        # exe="...", define the way to execute the file
        # if exe in the diy, then the bash file will be made
        t = ThreadPool(processes=25)
        t.map(self._Process, self._jobList)

if __name__ == "__main__":
    r = Runnow();
    r.run()
