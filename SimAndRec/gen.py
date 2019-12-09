name = "DIYPsi2S"
simff = "template/simdiyPsi2S.txt"
recff = "template/recJpsi.txt"
import Gen
g = Gen.process(name, simff, recff)
g.Make()
