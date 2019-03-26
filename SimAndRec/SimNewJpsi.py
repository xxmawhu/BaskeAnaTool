from SimWithKKMC import SimWithKKMC 
class SimNewJpsi(SimWithKKMC) : 
    def __init__(self):
        SimWithKKMC.__init__(self)
        self.SetOpt('KKMC', 'CMSEnergy',' 3.097')
        self.SetOpt('KKMC', 'BeamEnergySpread','0.0008')
        self.SetOpt('KKMC', 'NumberOfEventPrinted','1')
        self.SetOpt('KKMC', 'GenerateJPsi','true')
        self.SetOpt('EvtDecay', 'userDecayTableName','"IPATH/DECNAME"')
        self.SetOpt('BesRndmGenSvc', 'RndmSeed',' 10001')
        self.SetOpt('RealizationSvc', 'RunIdList',' {-55053,0,-52940}')
        self.SetOpt('RootCnvSvc', 'digiRootOutputFile','"RTRAW/NAME_NUM.rtraw"')
        self.SetOpt('MessageSvc', 'OutputLevel',' 5')
        self.SetOpt('ApplicationMgr', 'EvtMax','  10')
