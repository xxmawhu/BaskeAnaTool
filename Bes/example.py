from Bes import ana
from Bes.commands import getoutput as do
head = r'''
#include "$ROOTIOROOT/share/jobOptions_ReadRec.txt"
#include "$JTOSSALGROOT/share/jobOptions.txt"
// Number of events to be processed (default is 10)
ApplicationMgr.EvtMax = -1;

// Set output level threshold (2=DEBUG, 3=INFO, 4=WARNING, 5=ERROR, 6=FATAL)
MessageSvc.OutputLevel = 5;
'''
l = ana.ana()
l.setjobhead(head)
"""
    maxsize: 
    constrain the bulk of input `dst` file in one job, 
    the unit is `GB`. Once the total bulk is larger than `maxsize`, the 
    additional `.dst` will moved to the others or new one. 
    setjobnum():
    the number of jobs intend to make. Of course, the number of jobs will 
    increase once the total `dst` is larger than expectation
"""
l.maxsize(20)
l.setjobnum(30)
# some one use `FILE`, while some prefer `FILE1`
l.setrootname("FILE")
"""
    addst:
    add a directory, which contains the `.dst` files directly.
    Recommend use the following method, if you want to add too many directly

dirList = do("ls /besfs3/offline/data/664p03/psip/12mc/* -d").split()
dirList += do("ls /besfs3/offline/data/664p03/psip/09mc/* -d").split()
for dir in dirList:
    l.addst(dir)
"""
l.addst("/besfs3/offline/data/664p03/psip/12mc/dst")
# addcut(`the input tree name`, `the cut`, `the output tree name`)
# suggest to keep the output tree name same as the `input`
l.addcut('sig', "1==1", 'sig')
l.make()
# open the comment, once you decide to sub all jobs
# l.sub()
