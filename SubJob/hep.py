import os
import progressbar
from commands import getoutput
def Sub(files, Type='.sh', logID=''):
    if len(files) == 0:
        print("Sub All Jobs Successful!!!")
        return
    list.sort(files)
    print("Sub %d jobs......"%(len(files)))
    for i in progressbar.progressbar(range(len(files))):
        JOB = os.path.split(files[i])
        out=''
        if Type==".sh":
            getoutput("chmod +x %s"%(files[i]))
            out=getoutput('cd %s; hep_sub -g physics %s'%(JOB[0], JOB[1]))
        elif Type==".txt":
            out=getoutput('cd %s; boss.condor %s'%(JOB[0], JOB[1]))
            #print out
        if logID!='':
            f=open(logID,  'a')
            f.write(out.split()[-1]+'\n')
            f.close()
    print("Sub All Jobs Successful!!!")

def mkBash(afile):
    #print afile
    Path=os.path.split(afile)[0]
    File=os.path.split(afile)[1]
    name=os.path.splitext(File)[0]
    bashNm = os.path.join(Path, name+ '.sh')
    f=open(bashNm,'w')
    f.write('#!/bin/bash\n')
    f.write('cd '+ Path+'\n')
    f.write('root -l -b -q '+File+'\n')
    f.write('rm -f  '+name+'.sh\n')
    f.close()
    return bashNm

def SubCxx(files, Type = '.cxx', logID=''):
    if len(files) == 0:
        print("No Jobs found!!!")
        return
    list.sort(files)
    # make .bash file
    bashCol = []
    for i in files:
        bashCol.append(mkBash(i))
    print("Sub %d jobs......"%(len(bashCol)))
    for i in progressbar.progressbar(range(len(bashCol))):
        JOB = os.path.split(bashCol[i])
        out=''
        getoutput("chmod +x %s"%(bashCol[i]))
        out=getoutput('cd %s; hep_sub -g physics %s'%(JOB[0], JOB[1]))
        if logID!='':
            f=open(logID,  'a')
            f.write(out.split()[-1]+'\n')
            f.close()
    print("Sub All Jobs Successful!!!")
