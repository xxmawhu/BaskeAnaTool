import SimAndRec
svc = SimAndRec.process("/ihepbatch/bes/maxx/local/BaskeAnaTool/SimAndRec/template/simNewJpsi.txt","/ihepbatch/bes/maxx/local/BaskeAnaTool/SimAndRec/template/recNewJpsi.txt")
svc.Make()
svc.Sub()
