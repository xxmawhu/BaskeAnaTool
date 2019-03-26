from SimWithKKMC import SimWithKKMC 
class SimJPsi(SimWithKKMC) : 
    def __init__(self):
        SimWithKKMC.__init__(self)
        self.SetOpt('KKMC', 'CMSEnergy',' 3.097')
        self.SetOpt('KKMC', 'BeamEnergySpread','0.0008')
        self.SetOpt('KKMC', 'NumberOfEventPrinted','1')
        self.SetOpt('KKMC', 'GenerateJPsi','true')
        self.SetOpt('EvtDecay', 'userDecayTableName','"/scratchfs/bes/kangxianwei/maxx/DEC/Jpsi/J_etamumu.dec"')
        self.SetOpt('BesRndmGenSvc', 'RndmSeed',' 60001')
        self.SetOpt('RealizationSvc', 'RunIdList',' {-9947,0,-10878, -27255, 0, -28236 }')
        self.SetOpt('RootCnvSvc', 'digiRootOutputFile','"/scratchfs/bes/kangxianwei/maxx/rtraw/J_etamumu/sim_000.rtraw"')
        self.SetOpt('MessageSvc', 'OutputLevel',' 6')
        self.SetOpt('ApplicationMgr', 'EvtMax',' 10000')
