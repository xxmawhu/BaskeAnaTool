name = "4600"
simff="template/sim4600.txt"
recff="template/rec4600.txt"
import Gen
g = Gen.process(name, simff, recff)
g.Make()

