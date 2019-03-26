from SimWithKKMC import SimWithKKMC 
class SimPsi2S(SimWithKKMC) : 
    def __init__(self):
        SimWithKKMC.__init__(self)
        self.SetOpt('KKMC', 'CMSEnergy','  3.686')
        self.SetOpt('KKMC', 'BeamEnergySpread','  0.00092')
        self.SetOpt('KKMC', 'NumberOfEventPrinted','  1')
        self.SetOpt('KKMC', 'GeneratePsiPrime','  true')
        self.SetOpt('KKMC', 'RadiationCorrection','  1')
        self.SetOpt('KKMC', 'ThresholdCut','   3.9')
        self.SetOpt('EvtDecay', 'userDecayTableName',' "/scratchfs/bes/maxx/Psi2S/LLPhi/PsiptoLambdaLambdabarPhi.dec"')
        self.SetOpt('BesRndmGenSvc', 'RndmSeed',' 1')
        self.SetOpt('RealizationSvc', 'RunIdList',' {-25338,0,-27090}')
        self.SetOpt('RootCnvSvc', 'digiRootOutputFile',' "/scratchfs/bes/maxx/Psi2S/LLPhi/12/raw/raw_0001.rtraw"')
        self.SetOpt('MessageSvc', 'OutputLevel','  5')
        self.SetOpt('ApplicationMgr', 'EvtMax',' 44')
