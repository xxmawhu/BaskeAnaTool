#!/bin/env python
import sys
import os
from Bes.commands import getoutput


def makeDT(sortedjobs):
    tmpdt = {}
    for sjl in sortedjobs[2:]:
        sj = str(sjl).strip('\n').split()
        if len(sj) < 1:
            continue

        jobID = sj[0].split('.')[0] + '.'
        jobIDsub = sj[0].split('.')[1]

        if jobID in tmpdt.keys():
            subdt = tmpdt[jobID]
        else:
            subdt = {"I": (), "R": (), "H": (), "X": ()}

        subdt[str(sj[5])] = tuple(list(subdt[str(sj[5])]) + [jobIDsub])
        tmpdt[str(jobID)] = subdt

    return tmpdt


def padstr(strlist):
    maxlen = max([len(str) for str in strlist])
    return [str + (maxlen - len(str)) * " " for str in strlist]


def printlist(li, end="\n"):
    if len(li) == 0:
        pass
    elif len(li) == 1:
        sys.stdout.write(li[-1])
    else:
        for h in li[:-1]:
            sys.stdout.write(str(h))
            sys.stdout.write(" ")
        sys.stdout.write(str(li[-1]))

    sys.stdout.write(end)


def query(idfile, jobsDT):
    ff = open(idfile, 'r')
    fc = ff.readlines()
    ff.close()

    if len(fc) < 2:
        return None

    heads = ['jobID', 'jobDir', 'I     ', 'R     ', 'H     ', 'X     ',
             'T     ', 'R/T   ', '(I+R)/T']
    jobIDs = [jd.strip('\n').split()[0] for jd in fc[1:]]
    jobDirs = [jd.strip('\n').split()[1] for jd in fc[1:]]
    padIDs = padstr([heads[0]] + jobIDs)
    padDirs = padstr([heads[1]] + jobDirs)
    heads[0] = padIDs[0]
    jobIDs = padIDs[1:]
    heads[1] = padDirs[0]
    jobDirs = padDirs[1:]

    printlist(heads)

    jobIN = []
    jobNO = []
    for i, line in enumerate(fc[1:]):
        jobID, jobDir = line.strip('\n').split(' ')
        if jobID in jobsDT.keys():
            jobC = jobsDT[jobID]
            num = [len(jobC[key]) for key in ("I", "R", "H", "X")]
            numT = float(sum(num))
            jobIN.append([jobIDs[i], jobDirs[i],
                          "%s" % str(num[0]).ljust(6),
                          "%s" % str(num[1]).ljust(6),
                          "%s" % str(num[2]).ljust(6),
                          "%s" % str(num[3]).ljust(6),
                          "%s" % str(int(numT)).ljust(6),
                          "%.2f  " % (num[1] / numT),
                          "%.2f" % ((num[0] + num[1]) / numT)])
        else:
            tmp = "-1    "
            jobNO.append([jobIDs[i], jobDirs[i]] + 7 * [tmp])

    for ji in jobIN:
        printlist(ji)

    if len(jobNO) > 0:
        sys.stdout.write("\nThere is NO such jobID on computing farms: \n")
        for jn in jobNO:
            printlist(jn)


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


user = os.environ['USER']
content = getoutput("hep_q -u %s" % user).strip().split('\n')
sortc = sorted(content[:-1], key=skey)


def main():
    arg = sys.argv
    if len(arg) < 2:
        for s in sortc:
            sys.stdout.write(s)
            sys.stdout.write('\n')

        sys.stdout.write(content[0])
        sys.stdout.write('\n')
        sys.stdout.write('\n')
        sys.stdout.write(content[-1])
        sys.stdout.write('\n')
    elif len(arg) == 2:
        sdtc = makeDT(sortc)
        query(arg[1], sdtc)
    else:
        return None


if __name__ == '__main__':
    main()
