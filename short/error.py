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
for i in log:
    f=open(i,'r')
    s=f.read()
    if 'INFO Application Manager Finalized successfully' in s:
        continue
    else:
        print i[0:len(i)-8]
    f.close()
print("process is done.")

