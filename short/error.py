# Copyright (C) 2019 Ma Xinxin
import os
import util as mf
import sys
_USAGE = '''Usage:  without any option now
Function:
    find all .txt file and the log files producted by the boss.exe recursively, 
    and read one by one, if any one jobs is not procedured successful, then
    print them.
'''
if "-help" in sys.argv or "--help" in sys.argv:
    print _USAGE
    exit(0)
#jobs=os.listdir('.')
jobs=mf.findfiler('.')
log=[]
for i in jobs:
    if '.bosslog'==os.path.splitext(i)[1]:
        log.append(i)
list.sort(log)
errsize=0
for i in log:
    f=open(i,'r')
    lines =f.readlines()
    AMFS = False
    for l in lines[-5:]:
        if 'Finalized successfully' in l:
            AMFS = True
            break
    f.close()
    if not AMFS:
        errsize += 1
        print i[0:-8]
print "Done: ", errsize, "jobs fail"
