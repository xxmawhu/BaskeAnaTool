#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
import myfunction as m
import hep
opt=[]
arv=[]
#------get the option----------
for i in range(1,len(sys.argv)):
    if('-' in sys.argv[i]):
        opt.append(sys.argv[i])
    else:
        arv.append(sys.argv[i])
#---------end ------------
#  m.findfiler(path) :return all files in path
#  m.findfile(parh):  return files in path
#  m.findtype(files,type='.txt'):    return type file in files
#
##--------------------------
mypath=os.getcwd()
if len(arv)>0:
    if '-r' in opt:
        s=m.findfiler(arv[0])
    else:
        s=m.findfile(arv[0])
else:
    if '-r' in opt:
        s=m.findfiler('.')
    else:
        s=m.findfile('.')
list.sort(s)
#------find all jobs
if len(opt)==0:
    jobcol=(m.findtype(s,'.txt'))
    hep.Sub(jobcol)
if '-txt' in opt:
    jobcol=(m.findtype(s,'.txt'))
    hep.Sub(jobcol)
if '-sh' in opt:
    jobcol=(m.findtype(s,'.sh'))
    hep.Sub(jobcol)
if '-c' in opt:
    cjobcol=m.findtype(s,'.C')+m.findtype(s,'.cxx') \
            + m.findtype(s, ".cc")
    if len(cjobcol)>0:
        hep.SubCxx(cjobcol)
