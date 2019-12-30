#!/usr/bin/env python
import Gen
name = ["Jpsi", "NewJpsi", "Psi2S"]
simff = ["template/simJpsi.txt", 
        "template/simNewJpsi.txt",
        "template/simPsi2S.txt"]
recff = ["template/recJpsi.txt",
        "template/recNewJpsi.txt",
        "template/recPsi2S.txt"]

for n, s, r in zip(name, simff, recff):
    g = Gen.process(n, s, r)
    g.Make()
