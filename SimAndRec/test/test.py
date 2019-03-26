#print getOpt()
#a = Rec()
#a.SetRaw("araw")
#a.PrintToFile("rec.txt")
from configRecEasy import configRecEasy
a = configRecEasy("recPsi2S.txt")
a.Make("Rec")
