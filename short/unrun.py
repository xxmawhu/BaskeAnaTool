import util
import walksearch
import os
from util import jobCandidates
from SubJob import hep
_USAGE = '''Usage:  without any option now
Function:
    1) find all ".txt" and ".sh" file recursively
    2) try to find a log file assocaited with the ".txt" (or ".sh") file
    3) Once miss the log file, then resub this file 
'''
_USAGE = '''
Usage:  [option] [file or path]
Option: 
    -c submit all the c++ file in the path, and execute it with ROOT,
         First a .sh file will be made associated with a .c file
         Then sub this .sh file to the server center

    -sh Add x mod to the bash files, and submit all of them.

    -txt Sub all .txt file with hep_contior

    -r sub all file in this path
    sub="hep_sub" can assign special sub command
    exe="root -l - b -q" can set run command

Path: the default path is ".", and you can special it as a path or a file.
'''
class hepsub(jobCandidates):
    def __init__(self):
        jobCandidates.__init__(self)
        self._Uasge = _USAGE
        self._diy['type'] = '.0, .bosslog'

    def run(self):
        self._prepare()
#find the unruned job
        shlog = []
        txtlog = []
        for i in self._jobList:
            if walksearch.typeMatch(i, '.0') :
                shlog.append(i)
            elif walksearch.typeMatch(i, '.bosslog'):
                txtlog.append(i)
        for i in shlog:
            jobname = os.path.split(i)[1]
            nn = jobname.split('sh')[0]+'sh'
            nn = os.path.abspath(nn)
            #print nn
            if nn in self._jobList:
                self._jobList.remove(nn)
        for i in txtlog:
            jobname = os.path.split(i)[1]
            nn = jobname.split('txt')[0]+'txt'
            nn = os.path.abspath(nn)
            if nn in self._jobList:
                self._jobList.remove(nn)
        nologjob = []
        for i in self._jobList:
            jobname = os.path.split(i)[1]
            if not len(jobname.split('.')) >2:
                nologjob.append(i)
        self._jobList = nologjob

        if 'sub' in self._diy.keys() and  not 'exe' in self._diy.keys():
            hep.Sub(self._jobList, self._diy['sub'])
        if  'exe' in self._diy.keys():
            hep.SubDIY(self._jobList, self._diy['exe'])
        if not 'sub' in self._diy.keys():
            hep.smartSub(self._jobList)


test = hepsub()
test.run()
exit()
