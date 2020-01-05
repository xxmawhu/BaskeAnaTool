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


// main properties
OmegaXiKAlg.UseMatch = false;
OmegaXiKAlg.Mother = 100443;
OmegaXiKAlg.MothersNumber = 1;
OmegaXiKAlg.Ecm = 3.686;
OmegaXiKAlg.ReadBeamE = false;
OmegaXiKAlg.FillMCInfo = true;
OmegaXiKAlg.FillMCParAll = true;
OmegaXiKAlg.MinChargedTracks = 4;
OmegaXiKAlg.MaxChargedTracks = 13;
OmegaXiKAlg.MinShowers = 0;
OmegaXiKAlg.MaxShowers = 50;
OmegaXiKAlg.UseKinematicFit = false;
OmegaXiKAlg.Debug = false;
OmegaXiKAlg.InfoLevel = 0;

OmegaXiKAlg.TagCCID = 3334;
OmegaXiKAlg.IncludeCC = true;
OmegaXiKAlg.FID = {3334, 310};

// Xi0: 1.31486    Xi-: 1.32171
/// Xi0: 1.2995 1.3247 Hong-Fei Shen
OmegaXiKSelectorSignal.MinRecMass = 1.271;
OmegaXiKSelectorSignal.MaxRecMass = 1.371;
// OmegaXiKSelectorSignal.MinRecMass = 1.264;
// OmegaXiKSelectorSignal.MaxRecMass = 1.364;

// Omega
OmegaXiKSelectorOmega.MinMass = 1.550;
OmegaXiKSelectorOmega.MaxMass = 1.850;
OmegaXiKSelectorOmega.MaxChisq = 1000;
OmegaXiKSelectorOmega.Use2ndVFit = false;
OmegaXiKSelectorOmega.MaxVFitChisq = 3000;
OmegaXiKSelectorOmega.UseFlightSig = false;
OmegaXiKSelectorOmega.MinFlightSig= 0.0;

// Lambda
OmegaXiKSelectorLambda.MinMass = 1.095;
OmegaXiKSelectorLambda.MaxMass = 1.135;
OmegaXiKSelectorLambda.MaxChisq = 300; // 200
OmegaXiKSelectorLambda.Use2ndVFit = false;
OmegaXiKSelectorLambda.MaxVFitChisq = 1000;
OmegaXiKSelectorLambda.UseFlightSig = false;
OmegaXiKSelectorLambda.MinFlightSig = 2.0;

// Ks
OmegaXiKSelectorKs.MinMass = 0.469; // 0.487;
OmegaXiKSelectorKs.MaxMass = 0.529; // 0.511;
OmegaXiKSelectorKs.MaxChisq = 200; // 50; // 20
OmegaXiKSelectorKs.Use2ndVFit = false; // true;
OmegaXiKSelectorKs.MaxVFitChisq = 200; // 50; // 20
OmegaXiKSelectorKs.MinFlightSig= 2.0;

// primary kaons from IP
OmegaXiKSelectorKaonPrimary.UseP3MagCut = true;
OmegaXiKSelectorKaonPrimary.MinP3Mag = 0.0;
OmegaXiKSelectorKaonPrimary.RxyCut = 1.0;
OmegaXiKSelectorKaonPrimary.Vz0Cut = 10.0;
OmegaXiKSelectorKaonPrimary.UsePID = true;
OmegaXiKSelectorKaonPrimary.RejectProton = true;

// all the kaons
OmegaXiKSelectorKaonAll.UseP3MagCut = true;
OmegaXiKSelectorKaonAll.MinP3Mag = 0.0;
OmegaXiKSelectorKaonAll.RxyCut = 20.0;
OmegaXiKSelectorKaonAll.Vz0Cut = 30.0;
OmegaXiKSelectorKaonAll.UsePID = true;
OmegaXiKSelectorKaonAll.RejectProton = true;

// primary pions from IP
OmegaXiKSelectorPionPrimary.UseP3MagCut = true;
OmegaXiKSelectorPionPrimary.MinP3Mag = 0.0;
OmegaXiKSelectorPionPrimary.RxyCut = 1.0;
OmegaXiKSelectorPionPrimary.Vz0Cut = 10.0;
OmegaXiKSelectorPionPrimary.UsePID = true;
OmegaXiKSelectorPionPrimary.RejectProton = true;

// all the pions
OmegaXiKSelectorPionAll.UseP3MagCut = true;
OmegaXiKSelectorPionAll.MinP3Mag = 0.0;
OmegaXiKSelectorPionAll.RxyCut = 20.0;
OmegaXiKSelectorPionAll.Vz0Cut = 30.0;
OmegaXiKSelectorPionAll.UsePID = true;
OmegaXiKSelectorPionAll.RejectProton = true;

//  protons from primary
OmegaXiKSelectorProtonPrimary.UseP3MagCut = true;
OmegaXiKSelectorProtonPrimary.MinP3Mag = 0.0;
OmegaXiKSelectorProtonPrimary.RxyCut = 1.0;
OmegaXiKSelectorProtonPrimary.Vz0Cut = 10.0;
OmegaXiKSelectorProtonPrimary.UsePID = true;
OmegaXiKSelectorProtonPrimary.UsePIDProbability = true;
OmegaXiKSelectorProtonPrimary.MinPIDProb = 0.0001;
OmegaXiKSelectorProtonPrimary.RejectPionKaon = true;
OmegaXiKSelectorProtonPrimary.RejectElectron = false;

// all the protons
OmegaXiKSelectorProtonAll.UseP3MagCut = true;
OmegaXiKSelectorProtonAll.MinP3Mag = 0.0;
OmegaXiKSelectorProtonAll.RxyCut = 20.0;
OmegaXiKSelectorProtonAll.Vz0Cut = 30.0;
OmegaXiKSelectorProtonAll.UsePID = true;
OmegaXiKSelectorProtonAll.UsePIDProbability = true;
OmegaXiKSelectorProtonAll.MinPIDProb = 0.0001;
OmegaXiKSelectorProtonAll.RejectPionKaon = true;
OmegaXiKSelectorProtonAll.RejectElectron = false;

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
