name = "PPLL"
simff="template/simPPLL.txt"
recff="template/recJpsi.txt"
import Gen
g = Gen.process(name, simff, recff)
g.Make()

