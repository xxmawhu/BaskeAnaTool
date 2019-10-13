#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ====================================================
#   Copyright (C)2019 All rights reserved.
#
#   Author        : Xin-Xin MA
#   Email         : xxmawhu@163.com
#   File Name     : hep.py
#   Created Time  : 2019-10-08 11:07
#   Last Modified : 2019-10-08 11:07
# ====================================================
import os
import progressbar
from commands import getoutput
import subprocess
from multiprocessing import Pool
import util
#hep_sub = "/afs/ihep.ac.cn/soft/common/sysgroup/hep_job/bin/hep_sub -g physics"
def SubOneJob(file_sub):
    """
    Args:
        fil_sub -> list, 
        file name: [0]
        sub command: [1]
    return
        job id
    """
    file_name = file_sub[0]
    sub_command = file_sub[1]
    JOB = os.path.split(file_name)
    getoutput('cd %s; %s %s'%(JOB[0], "chmod +x", JOB[1]))
    out = getoutput('cd %s; %s %s'%(JOB[0], sub_command, JOB[1]))
    return out.split()[-1]


def mkBash(afile, command="root -l -b -q"):
    """
       make a bash file, write:
        command afile
    """
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


def smartSubOneJob(file_name):
    """
    determine the sub command by the file type
    return
        string: the id
    """
    sub_command = "/afs/ihep.ac.cn/soft/common/sysgroup/hep_job/bin/hep_sub -g physics"

    #sub the BOSS job
    file_type = file_name.split('.')[-1]
    if file_type == "":
        print "NameError: can't determine the type of this file from name"
        print "\t >>{}".format(file_name)
        return ''
    if file_type == 'txt':
        sub_command="/afs/ihep.ac.cn/soft/common/sysgroup/hep_job/bin/boss.condor"
        file_sub = [file_name, sub_command]
        return SubOneJob(file_sub)

    if file_type in ['sh', 'csh']:
        file_sub = [file_name, sub_command]
        return SubOneJob(file_sub)

    # make the Bash File, then sub
    try:
        exe_command = util.exe[file_type]
        sh_name = mkBash(file_name, exe_command)
        file_sub = [sh_name, sub_command]
        return SubOneJob(file_sub)
    except KeyError as e:
        print "KeyError: no such type in util.exe"
        raise e
    return SubOneJob(file_sub)


def SubJobList(files, sub_command):
    """
    Args:
        files->list, the abspath of each job
        sub_command->list, the type of each job
    return -> list
        job id list
    """
    if not files:
        print("Warning::No Job found!!!")
        return

    #list.sort(files)
    print("Sub %d jobs......"%(len(files)))
    file_sub_list = [[i, sub_command] for i in files]
    idList = []
    pool = Pool(20)
    for i in progressbar.progressbar(range(len(files)/20)):
        # 20 processers perform best!
        ids = pool.map(SubOneJob, file_sub_list[i*20:(i+1)*20])
        for ID in ids:
            idList.append(ID)
    
    print("Sub All Jobs Successful!!!")
    return idList


def Sub(files, Types = [],
        sub_command = "hep_sub"):
    """
    Args:
        files: list, the abspath of each job
        Types: list, the type of each job
    """
    if not files:
        print("Warning::No Job found!!!")
        return

    print("Sub %d jobs......"%(len(files)))
    # list.sort(files)
    file_sub_list = [[i, sub_command] for i in files]
    idList = []
    pool = Pool(20)
    if len(files) % 20 == 0 :
        n_group = len(files)/20
    else:
        n_group = len(files)/20 + 1

    for i in progressbar.progressbar(range(n_group)):
        ids = pool.map(SubOneJob, file_sub_list[i*20:(i+1)*20])
        for ID in ids:
            idList.append(ID)
    
    print("Sub All Jobs Successful!!!")
    return idList


def Sub(files,
        subcommand = "/afs/ihep.ac.cn/soft/common/sysgroup/hep_job/bin/hep_sub",
        Type='.sh', logID=''):
    if not files:
        print("No Job found!!!")
        return
    # list.sort(files)
    print("Sub %d jobs......"%(len(files)))
    for i in progressbar.progressbar(range(len(files)/20)):
        JOB = os.path.split(files[i])
        pool = Pool(20)
        getoutput('cd %s; %s %s'%(JOB[0], "chmod +x", JOB[1]))
        out = getoutput('cd %s; %s %s'%(JOB[0], subcommand, JOB[1]))
        #print('cd %s; %s %s'%(JOB[0], subcommand, JOB[1]))
        if logID!='':
            f=open(logID,  'a')
            f.write(out.split()[-1]+'\n')
            f.close()
    print("Sub All Jobs Successful!!!")


def smartSub(files):
    """
    Args:
        files->list, the abspath of each job
    return -> list
        job id list
    """
    if not files:
        print("Warning::No Job found!!!")
        return
    #list.sort(files)
    print("Sub %d jobs......"%(len(files)))
    idList = []
    pool = Pool(20)
    if len(files) % 20 == 0 :
        n_group = len(files)/20
    else:
        n_group = len(files)/20 + 1
    for i in progressbar.progressbar(range(n_group)):
        # 20 processers perform best!
        ids = pool.map(smartSubOneJob, files[i*20:(i+1)*20])
        for ID in ids:
            idList.append(ID)
    pool.close()
    
    print("Sub All Jobs Successful!!!")
    return idList


def genBashList(files, command='root -l -b -q'):
    """
    Args:
        files->list, 
        command->string, how to execute one job
    return->list
        one list filled with the name of bash file associated 
        with each input file
    """
    jobs = []
    for i in files:
        jobs.append(mkBash(i, command))
    #jobs.sort()
    return jobs

def SubBash(jobs, logID='.log'):
    """
    Args:
        jobs->list, the bash jobs
    return->list
        the job ID list
    """
    hep_sub = "/afs/ihep.ac.cn/soft/common/sysgroup/hep_job/bin/hep_sub -g physics"
    sub_command = [hep_sub for i in jobs]
    return SubJobList(jobs, sub_command)

def SubBOSS(jobs, logID='.log'):
    Sub(jobs, 'boss.condor', logID)


def SubCxx(files, logID=''):
    jobs = genBashList(files, 'root -l -b -q')
    SubBash(jobs)

def SubPy(files, logID=''):
    jobs = genBashList(files, 'python')
    SubBash(jobs)

def SubDIY(files, execommand, subcommand, logID=''):
    jobs = genBashList(files, execommand)
    Sub(jobs, subcommand)
