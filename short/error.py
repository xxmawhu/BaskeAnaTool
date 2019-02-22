import os
import util as mf
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

