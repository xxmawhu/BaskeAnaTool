from SimAndRec import SimRecAna
from SimAndRec import util
opt = '''//test'''
svc = SimRecAna.process(
    "/besfs/users/maxx/local/BaskeAnaTool/SimAndRec/template/sim4600.txt",
    "/besfs/users/maxx/local/BaskeAnaTool/SimAndRec/template/rec4600.txt")
svc.SetOpt(opt)
if len(util.getArv()) == 0:
    svc.Make()
    svc.Sub()
    exit(0)
elif '-make' in util.getArv():
    svc.Make()
    exit(0)