import util
from util import jobCandidates
from SubJob import hep
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
    def run(self):
        self._prepare()
        print self._jobList
        if 'sub' in self._diy.keys() and  not 'exe' in self._diy.keys():
            hep.Sub(self._jobList, self._diy['sub'])
        if  'exe' in self._diy.keys():
            hep.SubDIY(self._jobList, self._diy['exe'])
        if not 'sub' in self._diy.keys():
            hep.smartSub(self._jobList)


test = hepsub()
test.run()
