  
import sys
import time

import progressbar
import sys,time
def shortcut_example():
    for i in progressbar.progressbar(range(100)):
        print i
        time.sleep(0.01)
#shortcut_example()
import hep,os
files =[]
for i in range(100):
    #os.system("touch %d.sh"%i)
    files.append("%d.sh"%(i))
hep.Sub(files, '.sh', 'log')

    
