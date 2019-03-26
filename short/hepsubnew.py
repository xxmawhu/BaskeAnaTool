import util
from util import jobCandidates
from SubJob import hep
_USAGE = '''
Usage:  [option] [files or directory]
Option: 
    -help get help
    -c type="c, C, cpp, cc"
        1) make bash job,  into which the follow command will be wrote, 
             `root -l -b -q [the file]`
        2) change the authority: `chmod +x [the file].sh`
        3) submit: `hep_sub -g physics [the file].sh`

    -sh change the authority of those files, then submit all of them to the
        server.

    -txt submit all BOSS job files which end with `.txt`, to the server.
       the submit command is `boss.condor`

    -py type="py" 
        1) make bash job,  into which the follow command will be wrote, 
             `python [the file]`
        2) same as -c mode
    -r recursively

Assign special submit and execute commands or special file type
    ie. sub="hep_sub"
        require all jobs must be submitted by such way
    
    ie. exe="latex"
        make bash file, and write the execute command into the bash file

    ie. type="tex,h"
        separate by ','

    warn: no blank space at both sides of '='

Files or Directory
    1) regular expression:
       "a*txt", "a?", "a."
    2) a file
    3) a directory
    4) the default: current directory "."
'''
class hepsub(jobCandidates):
    def __init__(self):
        jobCandidates.__init__(self)
        self._Uasge = _USAGE
    def run(self):
        self._prepare()
        #print self._jobList
        if 'sub' in self._diy.keys() and  not 'exe' in self._diy.keys():
            hep.Sub(self._jobList, self._diy['sub'])
        if  'exe' in self._diy.keys():
            hep.SubDIY(self._jobList, self._diy['exe'])
        if not 'sub' in self._diy.keys():
            #print "smartSub"
            hep.smartSub(self._jobList)

test = hepsub()
test.run()
