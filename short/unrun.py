import os
from commands import getoutput as do
import util as mf
from SubJob import hep
import sys

_USAGE = '''Usage:  without any option now
Function:
    1) find all ".txt" and ".sh" file recursively
    2) try to find a log file assocaited with the ".txt" (or ".sh") file
    3) Once miss the log file, then resub this file 
'''

if "-help" in sys.argv or "--help" in sys.argv:
    print _USAGE
    exit(0)
#jobs=os.listdir('.')
jobs=mf.findfiler('.')
##########################
#  BOSS job, type = .txt #
##########################
logCol=[]
jobCol=[]
for i in jobs:
    if '.bosslog'==os.path.splitext(i)[1]:
        logCol.append(i)
    if '.txt'==os.path.splitext(i)[1]:
        jobCol.append(i)
list.sort(logCol)
list.sort(jobCol)
unrunTxtlist = []
for i in jobCol:
    if not i+".bosslog" in logCol:
        unrunTxtlist.append(i)
log = ""
if os.path.exists("log"):
    log="log/jobid"
hep.Sub(unrunTxtlist, '.txt', log)
###################
# sim and rec job #
###################
simJobList=[]
simJoblogs=[]
for i in jobs:
    if '.out.' in os.path.splitext(i)[0]:
        fname = os.path.split(i)[1]  
        logname = fname.split("sh")
        simJoblogs.append(logname[0]+".sh.out")
    if '.sh'==os.path.splitext(i)[1]:
        simJobList.append(i)
list.sort(simJobList)
unrunShList=[]
for i in simJobList:
    jobname = os.path.split(i)[1]
    nn = jobname.split('sh')[0]+'.sh'
    if not nn+'.out' in simJoblogs:
        unrunShList.append(i)

hep.Sub(unrunShList, '.sh')

