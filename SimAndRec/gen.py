name = "Psi2S"
simff="template/simPsi2S.txt"
recff="template/recJpsi.txt"
import Gen
g = Gen.process(name, simff, recff)
g.Make()

