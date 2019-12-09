import SimAndRec
import util
svc = SimAndRec.process(
    "/besfs/users/maxx/local/BaskeAnaTool/SimAndRec/template/simPsi2S.txt",
    "/besfs/users/maxx/local/BaskeAnaTool/SimAndRec/template/recJpsi.txt")
if len(util.getArv()) == 0:
    svc.Make()
    svc.Sub()
    exit(0)
elif '-make' in util.getArv():
    svc.Make()
    exit(0)
