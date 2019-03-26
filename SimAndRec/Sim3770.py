from SimWithKKMC import SimWithKKMC 
class Sim3770(SimWithKKMC) : 
    def __init__(self):
        SimWithKKMC.__init__(self)
        self.SetOpt('KKMC', 'CMSEnergy',' 3.773')
        self.SetOpt('KKMC', 'BeamEnergySpread','0.00097')
        self.SetOpt('KKMC', 'NumberOfEventPrinted','1')
        self.SetOpt('KKMC', 'GeneratePsi3770','true')
        self.SetOpt('KKMC', 'ThresholdCut','3.740')
        self.SetOpt('KKMC', 'ReadEcmsFromDB',' 1')
        self.SetOpt('EvtDecay', 'userDecayTableName','"/scratchfs/bes/kangxianwei/maxx/DEC/psi3770/Dp_phiomega.dec"')
        self.SetOpt('EvtDecay', 'statDecays',' true')
        self.SetOpt('BesRndmGenSvc', 'RndmSeed',' 60011')
        self.SetOpt('RealizationSvc', 'RunIdList',' {-11414,0,-13988,-14395,0,-14604,-20448,0,-23454}')
        self.SetOpt('RootCnvSvc', 'digiRootOutputFile','"/scratchfs/bes/kangxianwei/maxx/rtraw/Dp_phiomega/sim_001.rtraw"')
        self.SetOpt('MessageSvc', 'OutputLevel',' 6')
        self.SetOpt('ApplicationMgr', 'EvtMax',' 10000')
