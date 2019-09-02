import os
import commands
import sys
import re
import walksearch 
#-----find only file in current dir:p
def findfile(p):
    File = []
    # if p is a file
    if os.path.isfile(p):
        File.append(os.path.abspath(p))
        File.sort()
        return File
    # p is a director
    if os.path.isdir(p):
        for i in os.listdir(p):
            if os.path.isfile(i):
                File.append(os.path.join(os.path.abspath(p), i))
        File.sort()
        return File
    # p is a string, such as *.cxx
    s = p.replace("*", "[a-zA-Z0-9._]*")
    pattern = re.compile(s)
    for i in os.listdir("."):
        if pattern.match(i):
            File.append(os.path.abspath(i))
    File.sort()
    return File


def findtype(files, type = '.txt'):
    # the function to select the files whose type is txt
    txt = []
    for i in files:
        tp=os.path.splitext(i)[1]
        if(tp==type):
            txt.append(i)
    return txt
#-----find .c .cxx in files list
#--------end of function-------------------------------#
mypath=os.getcwd()
path=os.listdir('.')
#-----find all file in path 'p'
def findfiler(p, Type = ".", r="r"):
    if r != "r" :
        return findfile(p)
    File = []
    if os.path.isfile(p) and Type in p:
        File.append(os.path.abspath(p))
    else:
        path=[]
        for i in os.listdir(p):
            path.append(p+'/'+i)
        for i in path:
            File.extend(findfiler(i, Type, r))
    File.sort()
    return File
#-----end-------#
#-------end-----------#

class heprm:
    def __init__(self):
        self._opt=[]
        self._arv=[]
        self._stat=''
        self._ids=[]
        self._keyword='XXXX'
    def _getopt(self):
        for i in range(1, len(sys.argv)):
            if '-' == sys.argv[i][0]:
                self._opt.append(sys.argv[i])
            else:
                self._arv.append(sys.argv[i])
        if len(self._arv) == 0:
            self._arv.append(".")
    def _getkey(self):
        self._getopt()
        if len(self._arv)>0:
            self._keyword=self._arv[0]
    def _qstat(self):
        self._getkey()
        self._stat = commands.getoutput('hep_q -u ')
    def _getids(self):
        self._qstat()
        lines = self._stat.splitlines()
        key = self._keyword
        if key[0] == "*":
            key = "[a-zA-Z0-9_]" + self._keyword
        key = self._keyword.replace("*", "[a-zA-Z0-9._]*")
        print("Inf::Delete jobs ==> "+self._keyword)
        pattern = re.compile(key)
        for i in lines:
            if "JOBID" in i or len(i.split()) < 1:
                continue
            if pattern.findall(i):
                ID = float(i.split()[0])
                #print key, pattern, i
                self._ids.append(int(ID)) 
    def run(self):
        self._getids()
        for i in self._ids:
            os.system('hep_rm '+str(i))

class hep_q(heprm):
    """get the state information with key word"""
    def __init__(self):
        heprm.__init__(self)
    def run(self):
        self._getids()
        total = 0
        idl = 0
        R = 0
        for l in self._stat.split('\n')[:-2]:
            ll = l.split()
            if len(ll) <1 or ll[0] == "JOBID":
                continue
            aid = int(float(ll[0]))
            if aid in self._ids:
                total += 1
                if "I" in ll:
                    idl += 1
                if "R" in ll:
                    R += 1
                print l
        print total,"jobs;", idl, "idle,", R, "running"

        
def shrun(files):
    """ 
    Running all bash and cpp files 
    """
    mypath=os.getcwd()
    f=open('runSH.sh','w')
    f.write('#!/bin/bash\n')
    for i in files:
        path=os.path.split(i)[0]
        file=os.path.split(i)[1]
        name=os.path.splitext(i)[0]
        f.write('cd '+path+'\n')
        f.write("sh "+file+'\n')
    f.write('rm -f runSH.sh\n')
    f.close()
    os.chdir(mypath)
    print(mypath)
    os.system("chmod +x runSH.sh")
    os.system('source '+mypath+'/'+'runSH.sh')


def rootrun(files):
    """
    ls all cpp file recursively, and process one by one with "root -l -b -q"
    """
    mypath=os.getcwd()
    f=open('rootrun.sh', 'w')
    f.write('#!/bin/bash\n')
    for i in files:
        path=os.path.split(i)[0]
        file=os.path.split(i)[1]
        name=os.path.splitext(i)[0]
        f.write('cd '+path+'\n')
        f.write("root -l -b -q "+file+'\n')
    f.write('rm -f rootrun.sh\n')
    f.close()
    os.system("chmod +x rootrun.sh")
    os.system('source '+mypath+'/'+'rootrun.sh')
    os.system('rm -f rootrun.sh')

class jobCandidates:
    def __init__(self):
        self._jobList = []
        self._opt = []
        self._arv = []
        self._diy = {}
        self._Uasge = ""
    def _prepare(self):
        if '-help' in sys.argv or "--help" in sys.argv:
            print(self._Uasge)
            exit()
        # devide the input into option and var
        for i in range(1, len(sys.argv)):
            if '=' in sys.argv[i]:
                #print sys.argv[i]
                ss = sys.argv[i].split('=')
                #print ss
                self._diy[ss[0]] = ss[1]
                continue
            elif '-' == sys.argv[i][0]:
                self._opt.append(sys.argv[i])
            else:
                self._arv.append(sys.argv[i])
        if len(self._arv) == 0:
            self._arv.append(".")
        
        r = ""
        self._jobList = []
        if "-r" in self._opt:
            r = "-r"
        Type = []
        # get the default type: .txt, .c, .cxx, .cpp, .C, .py .sh
        if '-txt' in self._opt:
            Type.append('.txt')
        if '-c' in self._opt:
            Type += ['.C', '.cc', '.cxx', '.cpp']
        if '-sh' in self._opt:
            Type += ['.sh', '.csh']
        if '-py' in self._opt:
            Type.append('.py')
        #diy type
        #print self._diy.keys()
        if 'type' in self._diy.keys():
            #print self._diy["type"].split(',')
            Type += self._diy['type'].split(',')
            #if not 'sub' in self._diy.keys():
            #    self._diy['sub'] = 'hep_sub -g physics'
            #if not 'exe' in self._diy.keys():
            #    self._diy['exe'] = 'root -l -b -q '

        #print self._diy
        #print  "all Type", Type
        for p in self._arv:
            for t in Type:
                #print "path is:  ", p
                #print "type: ", t
                #print "r: ", r
                self._jobList += walksearch.findfiler(p, t, r)
                #print walksearch.findfiler(p, t, r)

    def run(self):
        self._prepare()
        return


