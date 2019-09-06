#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import util as m
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

Path: the default path is ".", and you can special it as a path or a file.
'''
opt = []
arv = []
#------get the option----------
for i in range(1, len(sys.argv)):
    if '-' in sys.argv[i]:
        opt.append(sys.argv[i])
    else:
        arv.append(sys.argv[i])
#  m.findfiler(path) :return all files in path
#  m.findfile(parh):  return files in path
#  m.findtype(files,type='.txt'):    return type file in files
#
# --------------------------
# mypath=os.getcwd()
# the jobs list
s = []
if len(arv) > 0:
    if '-r' in opt:
        for i in arv:
            s += m.findfiler(i)
    else:
        for i in arv:
            s += m.findfile(i)
else:
    if '-r' in opt:
        s = m.findfiler('.')
    else:
        s = m.findfile('.')
list.sort(s)
if "-help" in opt or "--help" in opt:
    print _USAGE
    exit(0)
if len(opt) == 0:
    jobcol = m.findtype(s, '.txt')
    hep.Sub(jobcol)
if '-txt' in opt:
    jobcol = m.findtype(s, '.txt')
    hep.Sub(jobcol)

if '-sh' in opt:
    jobcol = m.findtype(s, '.sh')
    hep.Sub(jobcol)

if '-c' in opt:
    cjobcol = m.findtype(s, '.C')
    cjobcol += m.findtype(s, '.cxx')
    cjobcol += m.findtype(s, ".cc")
    cjobcol += m.findtype(s, ".cpp")
    if len(cjobcol) > 0:
        hep.SubCxx(cjobcol)
