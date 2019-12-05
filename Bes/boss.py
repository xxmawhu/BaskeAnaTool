#!/afs/ihep.ac.cn/soft/common/python27_sl65/bin/python
# -*- coding: utf-8 -*-
import os


# from Bes.commands import getoutput as do
#-----small functions-----
def mkdir(s):
    if (not os.path.isdir(s)):
        os.makedirs(s)


#-----sub jobs with a given abs path
def hepsub(files):
    if len(files) > 0:
        mypath = os.getcwd()
        for i in files:
            path = os.path.split(i)[0]
            file = os.path.split(i)[1]
            name = os.path.splitext(i)[0]
            os.chdir(path)
            #f=open(name+'.sh','w')
            #f.write('#!/bin/bash\n')
            #f.write('cd '+ path+'\n')
            #f.write("source /afs/ihep.ac.cn/users/m/maxx/head/.b702p1\n")
            #f.write('boss.exe  '+file+'\n')
            #f.close()
            #os.system('chmod +x '+name+'.sh')
            #if '.sh' in file:
            #   os.system('chmod +x '+file)
            os.system('boss.condor   ' + file)
            #os.system('hep_sub  -g  physics '+name+'.sh')
        os.chdir(mypath)  #return to my work path


def shsub(files):
    if len(files) > 0:
        mypath = os.getcwd()
        for i in files:
            path = os.path.split(i)[0]
            file = os.path.split(i)[1]
            name = os.path.splitext(i)[0]
            os.chdir(path)
            os.system('chmod +x ' + file)
            os.system('hep_sub -g physics   ' + file)
        os.chdir(mypath)  #return to my work path


#---sub .C ---first mkdir a .sh
def csub(files):
    mypath = os.getcwd()
    for i in files:
        path = os.path.split(i)[0]
        file = os.path.split(i)[1]
        name = os.path.splitext(i)[0]
        os.chdir(path)
        f = open(name + '.sh', 'w')
        f.write('#!/bin/bash\n')
        f.write('cd ' + path + '\n')
        f.write('root -l -b -q ' + file + '\n')
        f.write('rm -f  ' + name + '.sh\n')
        f.close()
        os.system('chmod +x ' + name + '.sh')
        os.system('hep_sub -g physics ' + name + '.sh')
    os.chdir(mypath)


def shortsub(files):
    mypath = os.getcwd()
    for i in files:
        path = os.path.split(i)[0]
        file = os.path.split(i)[1]
        name = os.path.splitext(i)[0]
        os.chdir(path)
        f = open(name + '.sh', 'w')
        f.write('#!/bin/bash\n')
        f.write('cd ' + path + '\n')
        f.write('root -l -b -q ' + file + '\n')
        f.write('rm -f  ' + name + '.sh\n')
        f.close()
        os.system('chmod +x ' + name + '.sh')
        os.system('qsub -q shortq ' + name + '.sh')
    os.chdir(mypath)


def rootrun(files):
    mypath = os.getcwd()
    f = open('rootrun.sh', 'w')
    f.write('#!/bin/bash\n')
    for i in files:
        path = os.path.split(i)[0]
        file = os.path.split(i)[1]
        name = os.path.splitext(i)[0]
        f.write('cd ' + path + '\n')
        f.write("root -l -b -q " + file + '\n')
    f.write('rm -f rootrun.sh\n')
    f.close()
    os.chdir(mypath)
    print(mypath)
    os.system("chmod +x rootrun.sh")
    os.system('source ' + mypath + '/' + 'rootrun.sh')
    os.system('rm -f rootrun.sh')


def shrun(files):
    mypath = os.getcwd()
    f = open('runSH.sh', 'w')
    f.write('#!/bin/bash\n')
    for i in files:
        path = os.path.split(i)[0]
        file = os.path.split(i)[1]
        name = os.path.splitext(i)[0]
        f.write('cd ' + path + '\n')
        f.write("sh " + file + '\n')
    f.write('rm -f runSH.sh\n')
    f.close()
    os.chdir(mypath)
    print(mypath)
    os.system("chmod +x runSH.sh")
    os.system('source ' + mypath + '/' + 'runSH.sh')


#-----hep sub--
###################the class to make jobs
class subjobs(object):
    def setdstpath(self, dst, key=''):
        self._dst = dst
        files = os.listdir(self._dst)
        list.sort(files)
        self._s = []
        for i in files:
            if (('dst' in i) and (key in i)):
                self._s.append(i)

    def drop(self, dsts):
        self._bad = dsts

    def _drop(self):
        for i in self._bad:
            self._rm(i)

    def _rm(self, badst):
        for i in self._s:
            if badst in i:
                self._s.remove(i)

    def setjobpath(self, job):
        self._job = job
        if (not os.path.isdir(self._job)):
            os.makedirs(self._job)

    def setrootname(self, name):
        self.root = name

    def setrootpath(self, root):
        self._root = root
        if (not os.path.isdir(self._root)):
            os.makedirs(self._root)

    def setjobnum(self, n):
        self._n = n

    def __init__(self):
        self._dst = os.getcwd()
        self._job = os.getcwd()
        self._n = 1
        self._name = 'default'
        self.root = 'root'
        self._bad = []
        self._jobname = 'job'

    def _process(self, i, j):
        list.sort(self._s)
        dst = ''
        for k in range(i, j):
            dst += '\t"' + self._dst + '/' + self._s[k - 1] + '",\n'
        dst += '\t"' + self._dst + '/' + self._s[j - 1] + '"' + '\n'
        return dst

    def setbody(self, s):
        self._body = s

    def setname(self, name):
        self._name = name

    def setjobname(self, name):
        self._jobname = name

    def _creatjob(self, i, j, k):
        self._drop()
        _num = '%d' % k
        name = self._job + '/' + self._jobname + _num + '.txt'
        f = open(name, 'w')
        f.write(self._body)
        f.write(self._process(i, j))
        f.write('};\n')
        root = 'NTupleSvc.output={\n'
        root += '\t"' + self._name
        root += " DATAFILE = '" + self._root + '/' + self.root + _num + ".root'"
        root += " OPT = 'new'"
        root += " TYP = 'ROOT'\"\n"
        root += "};\n"
        f.write(root)
        f.close()

    def jobs(self):
        n = self._n
        self._tot = len(self._s)
        each = int(self._tot / n)
        print("[Info] Total .dst files is {}".format(self._tot))
        print("[Info] Each job contains {} .dst file".format(each))
        over = self._tot - each * n
        for i in range(0, over):
            m = each + 1
            self._creatjob(i * m + 1, (i + 1) * m, i)
        for i in range(over, n):
            m = each
            self._creatjob(i * m + 1 + over, (i + 1) * m + over, i)


class mcevt:
    def __init__(self):
        self.seed = 110
        self_boss = 'b702p1'
        self.run = 34480
        self.rawpath = '.'
        self.dec = ''
        self.events = 1000
        self.name = 'sim'

    def setseed(self, n):
        self.seed = n

    def setevents(self, n):
        self.events = n

    def setdec(self, s):
        self.dec = s

    def setrawpath(self, p):
        self.rawpath = p
        mkdir(self.rawpath)

    def setjobpath(self, s):
        self.job = s
        mkdir(self.job)

    def setdstpath(self, s):
        self.dstpath = s
        mkdir(self.dstpath)

    def simjob(self, name='sim'):
        self.name = self.job + '/' + name + '.txt'
        f = open(self.name, 'w')
        self.raw = self.rawpath + '/' + name + '.rtraw'
        self.dst = self.dstpath + '/' + name + '.dst'
        s = joboption.simevt(self.dec, self.raw, self.seed, self.run,
                             self.events)
        f.write(s)
        f.close()

    def recjob(self, name='rec'):
        rec = self.job + '/' + name + '.txt'
        f = open(rec, 'w')
        s = joboption.evtrec(self.seed, self.raw, self.dst)
        f.write(s)
        f.close()

    def setboss(self, boss):
        self._boss = boss

    def subjob(self, k=1):
        name1 = 'sim_' + '%0.3d' % k
        self.simjob(name1)
        name2 = 'rec_' + '%0.3d' % k
        self.recjob(name2)
        sub = self.job + '/simandrec_' + str(k) + '.sh'
        f = open(sub, 'w')
        l0 = '#!/bin/bash\n'
        l01 = 'source /afs/ihep.ac.cn/users/m/maxx/.' + self._boss + '\n'
        l1 = 'cd ' + self.job + '\n'
        l2 = 'boss.exe ' + name1 + '.txt&&\n'
        l3 = 'sleep 10\n'
        l4 = 'boss.exe ' + name2 + '.txt\n'
        l5 = 'rm -f sub_' + sub + '\n'
        f.write(l0 + l01 + l1 + l2 + l3 + l4)
        os.system('chmod +x ' + sub)
        os.system('hep_sub -g physics ' + sub)

    def subjobs(self, n):
        for i in range(0, n):
            self.seed += i * 10
            self.subjob(i)
