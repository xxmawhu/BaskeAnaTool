#!/bin/env python
import sys
import os
from Bes.commands import getoutput

user = os.environ['USER']
content = getoutput("hep_q -u %s" % user).strip().split('\n')


def skey(x):
    if len(x) != 0 and x.strip()[0] in "123456789":
        if sys.version_info[0] == 3:
            return float("{0}{1:0>4s}".format(*x.strip().split(" ")[0].split(".")))
        else:
            tmpl = x.strip().split(" ")[0].split(".")
            tmpt = (int(tmpl[0]), int(tmpl[1]))
            return float("%s%04d" % tmpt)
    else:
        return -1


sortc = sorted(content[:-1], key=skey)

for s in sortc:
    sys.stdout.write(s)
    sys.stdout.write('\n')

sys.stdout.write(content[0])
sys.stdout.write('\n')
sys.stdout.write('\n')
sys.stdout.write(content[-1])
