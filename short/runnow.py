import os
import sys
import util

_USAGE = '''Usage:  Running [option] [keyword]
Function:
    1.find all files (recursively)
    2.exe it with "root" or "sh"
Option:
    -r recursively
    -sh exe the file with "sh"
'''
if "-help" in sys.argv or "--help" in sys.argv:
    print(_USAGE)
    exit(0)

opt = []
arv = []
#------get the option----------
for i in range(1, len(sys.argv)):
    if ('-' in sys.argv[i]):
        opt.append(sys.argv[i])
    else:
        arv.append(sys.argv[i])
#---------end ------------
#
##--------------------------
mypath = os.getcwd()
if '-r' in opt:
    s = util.findfiler('.')
else:
    s = util.findfile('.')
#------find all jobs
jobcol = []
name = ""
if len(arv) != 0:
    name = arv[0]
else:
    if "-sh" in opt:
        name = ".sh"
for i in s:
    if name in i:
        jobcol.append(i)
jobcol.sort()
if "-sh" in opt:
    util.shrun(jobcol)
else:
    util.rootrun(jobcol)
