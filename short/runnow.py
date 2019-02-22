import os
import sys
import util as m
import boss
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
if '-r' in opt:
    s=m.findfiler('.')
else:
    s=m.findfile('.')
#------find all jobs
jobcol = []
name=""
if len(arv) !=0:
    name=arv[0]
else:
    if "-sh" in opt:
        name=".sh"
for i in s:
    if name in i:
        jobcol.append(i)
jobcol.sort()
if "-sh" in opt:
    boss.shrun(jobcol)
else:
    boss.rootrun(jobcol)
