from Bes import ana
from Bes.commands import getoutput as do
head = r'''
#include "$ROOTIOROOT/share/jobOptions_ReadRec.txt"
#include "$JTOSSALGROOT/share/jobOptions.txt"
// Number of events to be processed (default is 10)
ApplicationMgr.EvtMax = -1;

// Set output level threshold (2=DEBUG, 3=INFO, 4=WARNING, 5=ERROR, 6=FATAL )
MessageSvc.OutputLevel = 5;
'''
l = ana.ana()
l.setjobhead(head)
l.maxsize(20)
l.setjobnum(30)
l.addst("/besfs3/offline/data/664p03/psip/12mc/dst")
l.addcut('sig', "chisq>0 && chisq<200", 'sig')
l.make()
#l.sub()
