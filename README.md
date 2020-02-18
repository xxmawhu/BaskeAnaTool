# BaskeAnaTool
The package based on Python works independent of BOSS.
"BaskeAnaTool" means a basket of ana useful tools. You can use it to submit jobs
to the computer servers, also generate simulation jobs, check the jobs status,
check the whether the jobs is successful according to the job log files. 

Before using the package, I suggest you to read the "Readme.md" carefully. The
Chinese version of "Readme.md" is also available now.

## How to install
First, you need to clone the repository from "github.com"
```sh
git clone https://github.com/xxmawhu/BaskeAnaTool.git
```
The environment configuration is set well in the "setup.sh", you need to source
it.
```bash
   source BaskeAnaTool/setup.sh
```
For the shell with tcsh users, there is one "setup.csh" file achieving same
effect.
```bash
   source BaskeAnaTool/setup.csh
```


## What does the basket contain?  

* submit jobs flexible

> For example, assuming you are now at directory "jobs", after "ls", you find many jobs
> need to be submitted.
```bash
jobs_ana_001.txt jobs_ana_004.txt jobs_ana_007.txt jobs_ana_010.txt 
jobs_ana_002.txt jobs_ana_005.txt jobs_ana_008.txt jobs_ana_011.txt 
jobs_ana_003.txt jobs_ana_006.txt jobs_ana_009.txt jobs_ana_012.txt 
```
> Now, you only need one command
```bash
Hepsub -txt *.txt
```
> If you find many jobs allocated in different directories at the "jobs". Also
> one command is enough
```bash
Hepsub -txt -r .
```
> Don't forget to ".", which denotes the current directory.
> You also can specify the file type, execute method, and submit way. 
```bash
Hepsub type="C, Cpp, cxx" exe="root -l -b -q" sub="hep_sub -g physics"
```
> Look into [https://github.com/xxmawhu/BaskeAnaTool](https://github.com/xxmawhu/BaskeAnaTool)
> for more details.

* Do MC simulation flexible
> The following command is typically usage.
```bash
SimJpsi [decay.card] [number of events] <-make>
```
> The additional option "-make" will tell the simulator only generate the job
> scrscripts without any submitting action.
> You can enjoy the physics and forget all dirty bash script! 
What job does the script exactly do?
> Make three directories, `sub`, `raw`, `dst`, you can get the content from the
> name. In the fildor `sub`, two text files begined with "rec" and "sim",
> respectively, are generated for each simulation task. Later, an associated
> bash file with name, "job_xxx.sh***" are create. The content is 
```bash
boss.exe sim_xxx.txt
sleep 10
boss.exe rec_xxx.txt
```
> The default events number for each simulation task is 20,000. When then number
> of total events is too large, the event number for each task will be
> increased. 
How to DIY one?
> Write the following into one file, for example "doSim.py"
```python
#!/usr/env python
import SimAndRec
from SimAndRec import util
svc = SimAndRec.process("sim.txt","rec.txt")
if len(util.getArv()) == 0:
    svc.Make()
    svc.Sub()
elif '-make' in util.getArv():
    svc.Make()
```
> The you can use "doSim.py" now
```
python doSim.py [decay.card] [number of events] <-make>
```
> I also suggest you push "alias SimDIY='python /path/to/doSim.py'", into your
> configuration file, once you use "doSim.py frequently.

> A more convenient way is execute the gen.py in "SimAndRec".
> The content of "gen.py" is 
```python
name = "DIYPsi2S"
simff = "template/simdiyPsi2S.txt"
recff = "template/recJpsi.txt"
import Gen
g = Gen.process(name, simff, recff)
g.Make()
```
> This script accompanied two things, first generate one `python` script named
> "initDIYPsi2S.py", then add "alias SimDIYPsi2S ='path/to/initDIYPsi2S.py'" to
> the "setup.(c)sh", so you need soure the setup.sh again.
> You may get it, the special class "Gen" is designed to generate a script for MC
> simulation. You only need to prepare the scripts for simulation and
> reconstruction, then give it a name. Please remember the line break is not
> alloallowed, `line break is not alloallowed`, `line break is not alloallowed`.

>If you want to change some options, just use the member method
``` python
svc.SetOpt(class, member, value)
```
> For example, you have to change the CMSEnergy of KKMC. It's easy to change it
```python
svc.SetOpt("KKMC", "energy",3.097)
```
* generate and submit typically BOSS event selection jobs
> There is one class "ana" in module "Bes". Main features:
```python
setJobOption()
addDataSet()
addcut()
make()
sub()
```
> You can find some examples in the dirdirectory "BaskeAnaTool/tutorials"
> The comments say for itself.
```python
from Bes import ana
from Bes.commands import getoutput as do
head = r"""
#include "$ROOTIOROOT/share/jobOptions_ReadRec.txt"
#include "$MAGNETICFIELDROOT/share/MagneticField.txt"
#include "$RUNEVENTNUMBERALGROOT/share/jobOptions_RunEventNumber.txt"
#include "$ABSCORROOT/share/jobOptions_AbsCor.txt"
#include "$VERTEXFITROOT/share/jobOptions_VertexDbSvc.txt"
#include "$VEEVERTEXALGROOT/share/jobOptions_veeVertex.txt"
#include "$OMEGAXIKALGROOT/share/jobOptions.txt"

// pi0 and eta
#include "$PI0ETATOGGRECALGROOT/share/jobOptions_Pi0EtaToGGRec.txt"
Pi0EtaToGGRecAlg.PhotonInBarrelOrEndcap = true;
Pi0EtaToGGRecAlg.PhotonApplyTimeCut = true;
Pi0EtaToGGRecAlg.RejectBothInEndcap = true;

OmegaXiKAlg.UseMatch = false;
OmegaXiKAlg.ReadBeamE = false;

OmegaXiKAlg.TagCCID = 3334;
OmegaXiKAlg.IncludeCC = true;
OmegaXiKAlg.FID = {3334, 310};

// Ks
OmegaXiKSelectorKs.MinMass = 0.469; // 0.487;
OmegaXiKSelectorKs.MaxMass = 0.529; // 0.511;
OmegaXiKSelectorKs.MaxChisq = 200; // 50; // 20
OmegaXiKSelectorKs.Use2ndVFit = false; // true;
OmegaXiKSelectorKs.MaxVFitChisq = 200; // 50; // 20
OmegaXiKSelectorKs.MinFlightSig= 2.0;

// Number of events to be processed (default is 10)
ApplicationMgr.EvtMax = -1;

// Set output level threshold (2=DEBUG, 3=INFO, 4=WARNING, 5=ERROR, 6=FATAL )
MessageSvc.OutputLevel = 5;

"""
phys_ana = ana.ana()
phys_ana.setjobhead(head)

################################################################
# maxsize: 
# constrain the bulk of input `dst` file in one job, 
# the unit is `GB`. Once the total bulk is larger than `maxsize`, the 
# additional `.dst` will moved to the others or new one. 
# setjobnum():
# the number of jobs intend to make. Of course, the number of jobs will 
# increase once the total `dst` is larger than expectation
################################################################
phys_ana.maxsize(15)
phys_ana.setjobnum(30)

# some one use `FILE`, while some prefer `FILE1`
phys_ana.setrootname("FILE")

################################################################
# addst:
# add a directory, which contains the `.dst` files directly.
# Recommend use the following method, if you want to add too many directly
# 
# dirList = do("ls /besfs3/offline/data/664p03/psip/12mc/* -d").split()
# dirList += do("ls /besfs3/offline/data/664p03/psip/09mc/* -d").split()
# for dir in dirList:
#     phys_ana.addst(dir)
################################################################
# phys_ana.addst("/besfs3/offline/data/664p03/psip/12mc/dst")
# phys_ana.addst("/scratchfs/bes/sunhk/psip/dst")
dirList = ["/bes3fs/offline/data/664p03/psip/09mc/dst",
           "/bes3fs/offline/data/664p03/psip/12mc/dst"]
for dir in dirList:
    phys_ana.addst(dir)

# addcut(`the input tree name`, `the cut`, `the output tree name`)
# suggest to keep the output tree name same as the `input`
phys_ana.addcut('sig', "1==1", 'sig')
phys_ana.addcut('mc', "1==1", 'mc')

phys_ana.make()
# open the comment, once you decide to sub all jobs
#phys_ana.sub()
```
> Running "ana_Psi2S_inc.py", feeling it more directly.
If you meet any problems when using this package, please contact me with email,
"maxx@ihep.ac.cn"
