from AddBranch import addMass
'''Usage:
SetRawRoot(.root file, the name of tree)

OutPut(name): set the name of the out file after add some mass tuples

Add(name of tuple, some expresion): the expresion is some operate on the p4
momentum, such as p4.M(), p4.Angel(p4_1.Vect()), p4.CosTheta()

the momentum of (e+e-) is P4beam

'''
pr = addMass.process()
pr.SetRawRoot("../mode/sig_all.root")
pr.OutPut("sig.root")
pr.Add("ma0", "(P4FitPi0 + P4FitEta).M()")
pr.Add("mX", "(P4FitPi0 + P4FitKaonm + P4FitKaonp).M()")
pr.Add("mF", "(P4FitEta + P4FitKaonm + P4FitKaonp).M()")
pr.Add("mphi", "(P4Kaonp + P4Kaonm).M()")
pr.run()

