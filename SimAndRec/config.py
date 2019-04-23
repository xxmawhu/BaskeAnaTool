import os
f = open("NUM.py", 'w')
cdir = os.path.join(os.path.abspath(os.curdir),".NUM")
f.write('NUMFILE="%s"'%(cdir))
f.close()
