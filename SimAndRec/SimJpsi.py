from Zeus import zeus 
class SimJpsi(zeus) : 
    def __init__(self):
        zeus.__init__(self)
        zeus.AddOpt(self,\
            "line_02",\
            "$OFFLINEEVENTLOOPMGRROOT/share/OfflineEventLoopMgr_Option.txt",\
            ""\
            )
        zeus.AddOpt(self,\
            "line_05",\
            "$KKMCROOT/share/jobOptions_KKMC.txt",\
            " ****** job options for generator (KKMC) ******"\
            )
        zeus.AddOpt(self,\
            "KKMC",\
            "",\
            ""\
            )
        zeus.AddOpt(self,\
            "line_11",\
            "$BESEVTGENROOT/share/BesEvtGen.txt",\
            ""\
            )
        zeus.AddOpt(self,\
            "EvtDecay",\
            "",\
            ""\
            )
        zeus.AddOpt(self,\
            "line_16",\
            "$BESSIMROOT/share/G4Svc_BesSim.txt",\
            " ****** job options for detector simulation ******"\
            )
        zeus.AddOpt(self,\
            "line_19",\
            "$CALIBSVCROOT/share/calibConfig_sim.txt",\
            " ****** job options of configure for calibration constants ******"\
            )
        zeus.AddOpt(self,\
            "BesRndmGenSvc",\
            "",\
            ""\
            )
        zeus.AddOpt(self,\
            "RealizationSvc",\
            "",\
            ""\
            )
        zeus.AddOpt(self,\
            "line_29",\
            "$ROOTIOROOT/share/jobOptions_Digi2Root.txt",\
            "**************job options for random number************************"\
            )
        zeus.AddOpt(self,\
            "RootCnvSvc",\
            "",\
            ""\
            )
        zeus.AddOpt(self,\
            "MessageSvc",\
            "",\
            ""\
            )
        zeus.AddOpt(self,\
            "ApplicationMgr",\
            "",\
            ""\
            )
        zeus.SetOpt(self, 'RealizationSvc','RunIdList','{-9947,0,-10878, -27255, 0, -28236 }','=')
        zeus.SetOpt(self, 'ApplicationMgr','EvtMax','10000','=')
        zeus.SetOpt(self, 'MessageSvc','OutputLevel','6','=')
        zeus.SetOpt(self, 'BesRndmGenSvc','RndmSeed','60001','=')
        zeus.SetOpt(self, 'RootCnvSvc','digiRootOutputFile','"/scratchfs/bes/kangxianwei/maxx/rtraw/J_etamumu/sim_000.rtraw"','=')
        zeus.SetOpt(self, 'KKMC','CMSEnergy','3.097','=')
        zeus.SetOpt(self, 'KKMC','BeamEnergySpread','0.0008','=')
        zeus.SetOpt(self, 'KKMC','NumberOfEventPrinted','1','=')
        zeus.SetOpt(self, 'KKMC','GenerateJPsi','true','=')
        zeus.SetOpt(self, 'EvtDecay','userDecayTableName','"/scratchfs/bes/kangxianwei/maxx/DEC/Jpsi/J_etamumu.dec"','=')

 #  def SetRaw(self, raw):
 #      self.SetOpt("EventCnvSvc","digiRootInputFile",'{"%s"}'%raw)
 #  def SetDst(self, dst):
 #      self.SetOpt("EventCnvSvc","digiRootOutputFile",'"%s"'%dst)
 #  def SetSeed(self, seed):
 #      self.SetOpt("BesRndmGenSvc","RndmSeed",str(seed))
        
