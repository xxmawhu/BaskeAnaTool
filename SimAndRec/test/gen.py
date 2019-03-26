#print getOpt()
#a = Rec()
#a.SetRaw("araw")
#a.PrintToFile("rec.txt")
from configRecEasy import configRecEasy
a = configRecEasy("recJpsi.txt")
a.Make("RecJPsi")
