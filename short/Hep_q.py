import os
import sys
import commands
from util import hep_q
_USAGE='''Heprm [keyword]
keyword: 1) jobId, or part of the jobId, for example
            Heprm 34222, will cancle all jobs with 34222 in the jobId,
            such as 8883422, 3422888, 88342288, etc.
         2) jobname, or part of jobname
            for example '.txt', '.sh', are very useful
         3) status, "H"--hold, "R"--running
'''
if "-help" in sys.argv or "--help" in sys.argv:
    print(_USAGE)
    exit()

h = hep_q()
h.run()
