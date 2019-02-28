import os
import commands
import sys
#------the function to select the files whose type is txt
def findtype(files,type='.txt'):
    txt=[]
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
def findfiler(p):
    file=[]
    if os.path.isfile(p):
        file.append(os.path.abspath(p))
    else:
        path=[]
        for i in os.listdir(p):
            path.append(p+'/'+i)
        for i in path:
            file.extend(findfiler(i))
        file.sort()
    return file
#-----end-------#
#-----find only file in current dir:p
def findfile(p):
    file=[]
    if os.path.isfile(p):
        file.append(os.getcwd()+'/'+p)
    else:
        for i in os.listdir(p):
            if '/' in p :
                file.append(os.getcwd()+'/'+p+i)
            elif p=='.':
                file.append(os.getcwd()+'/'+i)
            else:
                file.append(os.getcwd()+'/'+p+'/'+i)
        file.sort()
    return file
#-------end-----------#

class heprm:
    def __init__(self):
        self._opt=[]
        self._arv=[]
        self._stat=''
        self._ids=[]
        self._keyword='maxx'
    def _getopt(self):
        for i in range(1,len(sys.argv)):
            if '-' in sys.argv[i]:
                self._opt.append(sys.argv[i])
            else:
                self._arv.append(sys.argv[i])
    def _getkey(self):
        self._getopt()
        if len(self._arv)>0:
            self._keyword=self._arv[0]
    def _qstat(self):
        self._getkey()
        self._stat=commands.getoutput('hep_q -u | grep '+self._keyword)
    def _getids(self):
        self._qstat()
        lines=self._stat.splitlines()
        for i in lines:
            if not 'JOBID' in i:
                self._ids.append(int(float(i.split()[0]))) 
    def run(self):
        self._getids()
        for i in self._ids:
            os.system('hep_rm '+str(i))

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
    print( mypath)
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

