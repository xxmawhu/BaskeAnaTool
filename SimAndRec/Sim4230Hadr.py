from SimWithKKMC import SimWithKKMC 
class Sim4230Hadr(SimWithKKMC) : 
    def __init__(self):
        SimWithKKMC.__init__(self)
        self.SetOpt('EvtDecay', 'userDecayTableName',' "hadr.dec"')
        self.SetOpt('EvtDecay', 'ParentParticle',' "vpho"')
        self.SetOpt('ApplicationMgr', 'DLLs',' { "BesServices"}', "+=")
        self.SetOpt('ApplicationMgr', 'EvtMax',' 30')
        self.SetOpt('BesRndmGenSvc', 'RndmSeed','100')
        self.SetOpt('RealizationSvc', 'RunIdList',' {30438,0,30491,32239,0,32849,32850,0,33484}')
        self.SetOpt('RootCnvSvc', 'digiRootOutputFile',' "4415a.rtraw"')
        self.SetOpt('MessageSvc', 'OutputLevel',' 6')
