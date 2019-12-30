#!/usr/bin/env python
import Gen
import os


def addSimor():
    name = ["Jpsi", "NewJpsi", "Psi2S"]
    simff = [
        "template/simJpsi.txt", "template/simNewJpsi.txt",
        "template/simPsi2S.txt"
    ]
    recff = [
        "template/recJpsi.txt", "template/recNewJpsi.txt",
        "template/recPsi2S.txt"
    ]

    for n, s, r in zip(name, simff, recff):
        g = Gen.process(n, s, r)
        g.Make()


if __name__ == "__main__":
    if os.path.exists('.addDone'):
        exit(0)
    else:
        addSimor()
        os.system('touch .addDone')
