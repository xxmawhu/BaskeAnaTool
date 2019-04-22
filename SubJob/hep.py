import os
import progressbar
from commands import getoutput
def Sub(files, subcommand='hep_sub -g physics', Type='.sh', logID=''):
    if len(files) == 0:
        print("No Job found!!!")
        return
    list.sort(files)
    print("Sub %d jobs......"%(len(files)))
    for i in progressbar.progressbar(range(len(files))):
        JOB = os.path.split(files[i])
        out = getoutput('cd %s; %s %s'%(JOB[0], subcommand, JOB[1]))
        #print('cd %s; %s %s'%(JOB[0], subcommand, JOB[1]))
        #print out
        if logID!='':
            f=open(logID,  'a')
            f.write(out.split()[-1]+'\n')
            f.close()
    print("Sub All Jobs Successful!!!")

# sub one job
def smartSubOneJob(File, logID='.log'):
    JOB = os.path.split(File)
    #sub the job
    if JOB[1].split('.')[-1] == 'txt':
        subcommand = 'boss.condor'
        out = getoutput('cd %s; %s %s'%(JOB[0], subcommand, JOB[1]))
    elif JOB[1].split('.')[-1] == 'sh':
        subcommand = 'hep_sub -g physics'
        out = getoutput('cd %s; %s %s'%(JOB[0], subcommand, JOB[1]))
        print('cd %s; %s %s'%(JOB[0], subcommand, JOB[1]))
    elif JOB[1].split('.')[-1] in ['C', 'cxx', 'cc', 'cpp']:
        shName = mkBash(File, 'root -l -b -q')
        JOB = os.path.split(shName)
        subcommand = 'hep_sub -g physics'
        out = getoutput('cd %s; %s %s'%(JOB[0], subcommand, JOB[1]))
    elif JOB[1].split('.')[-1] == 'py':
        shName = mkBash(files[i], 'python')
        JOB = os.path.split(shName)
        subcommand = 'hep_sub -g physics'
        out = getoutput('cd %s; %s %s'%(JOB[0], subcommand, JOB[1]))
        #print out
    if logID!='':
        f=open(logID,  'a')
        f.write(out.split()[-1]+'\n')
        f.close()

#sub job list
def smartSub(files, logID='.log'):
    if len(files) == 0:
        print("No Job found!!!")
        return
    list.sort(files)
    print("Sub %d jobs......"%(len(files)))
    for i in progressbar.progressbar(range(len(files))):
        # path / file
        JOB = os.path.split(files[i])
        #print JOB
        #sub the job
        if JOB[1].split('.')[-1] == 'txt':
            subcommand = 'boss.condor'
            out = getoutput('cd %s; %s %s'%(JOB[0], subcommand, JOB[1]))
        elif JOB[1].split('.')[-1] == 'sh':
            subcommand = 'hep_sub -g physics'
            getoutput("chmod +x " + JOB[1])
            out = getoutput('cd %s; %s %s'%(JOB[0], subcommand, JOB[1]))
        elif JOB[1].split('.')[-1] in ['C', 'cxx', 'cc', 'cpp']:
            shName = mkBash(files[i], 'root -l -b -q')
            JOB = os.path.split(shName)
            subcommand = 'hep_sub -g physics'
            out = getoutput('cd %s; %s %s'%(JOB[0], subcommand, JOB[1]))
        elif JOB[1].split('.')[-1] == 'py':
            shName = mkBash(files[i], 'python')
            JOB = os.path.split(shName)
            subcommand = 'hep_sub -g physics'
            out = getoutput('cd %s; %s %s'%(JOB[0], subcommand, JOB[1]))
        #print out
        if logID!='':
            f=open(logID,  'a')
            f.write(out.split()[-1]+'\n')
            f.close()


def mkBash(afile, command="root -l -b -q"):
    #print afile
    Path=os.path.split(afile)[0]
    File=os.path.split(afile)[1]
    name=os.path.splitext(File)[0]
    bashNm = os.path.join(Path, File+ '.sh')
    f=open(bashNm,'w')
    f.write('#!/bin/bash\n')
    f.write('cd '+ Path+'\n')
    f.write(command + " " + File +'\n')
    #f.write('rm -f  '+name+'.sh\n')
    f.close()
    getoutput('chmod +x ' + bashNm)
    return bashNm

#generate Bash file
def genBashList(files, command='root -l -b -q'):
    jobs = []
    for i in files:
        jobs.append(mkBash(i, command))
    jobs.sort()
    return jobs

def SubBash(jobs, logID='.log'):
    Sub(jobs, 'hep_sub -g physics', logID)

def SubBOSS(jobs, logID='.log'):
    Sub(jobs, 'boss.condor', logID)


def SubCxx(files, logID=''):
    jobs = genBashList(files, 'root -l -b -q')
    SubBash(jobs)

def SubPy(files, logID=''):
    jobs = genBashList(files, 'python')
    SubBash(jobs)

def SubDIY(files, command, logID=''):
    jobs = genBashList(files, command)
    SubBash(jobs)
