import SimAndRec
svc = SimAndRec.process("/ihepbatch/bes/maxx/local/BaskeAnaTool/SimAndRec/template/sim3770.txt","/ihepbatch/bes/maxx/local/BaskeAnaTool/SimAndRec/template/rec3770.txt")
svc.Make()
svc.Sub()
