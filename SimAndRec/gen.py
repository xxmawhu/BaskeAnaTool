name = "NewJpsi"
simff="template/simNewJpsi.txt"
recff="template/recNewJpsi.txt"
import Gen
g = Gen.process(name, simff, recff)
g.Make()

