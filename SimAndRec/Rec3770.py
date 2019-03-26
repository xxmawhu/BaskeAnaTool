from Zeus import zeus 
class Rec3770(zeus) : 
    def __init__(self):
        zeus.__init__(self)
        zeus.AddOpt(self,\
            "line_02",\
            "$ROOTIOROOT/share/jobOptions_ReadRoot.txt",\
            "input ROOT MC data"\
            )
        zeus.AddOpt(self,\
            "line_03",\
            "$OFFLINEEVENTLOOPMGRROOT/share/OfflineEventLoopMgr_Option.txt",\
            ""\
            )
        zeus.AddOpt(self,\
            "line_06",\
            "$BESEVENTMIXERROOT/share/jobOptions_EventMixer_rec.txt",\
            " background mixing"\
            )
        zeus.AddOpt(self,\
            "line_08",\
            "$CALIBSVCROOT/share/job-CalibData.txt",\
            ""\
            )
        zeus.AddOpt(self,\
            "line_09",\
            "$MAGNETICFIELDROOT/share/MagneticField.txt",\
            ""\
            )
        zeus.AddOpt(self,\
            "line_10",\
            "$ESTIMEALGROOT/share/job_EsTimeAlg.txt",\
            ""\
            )
        zeus.AddOpt(self,\
            "line_13",\
            "$MDCXRECOROOT/share/jobOptions_MdcPatTsfRec.txt",\
            " PAT+TSF method for MDC reconstruction"\
            )
        zeus.AddOpt(self,\
            "line_15",\
            "$KALFITALGROOT/share/job_kalfit_numf_data.txt",\
            ""\
            )
        zeus.AddOpt(self,\
            "line_16",\
            "$MDCDEDXALGROOT/share/job_dedx_all.txt",\
            ""\
            )
        zeus.AddOpt(self,\
            "line_17",\
            "$TRKEXTALGROOT/share/TrkExtAlgOption.txt",\
            ""\
            )
        zeus.AddOpt(self,\
            "line_18",\
            "$TOFRECROOT/share/jobOptions_TofRec.txt",\
            ""\
            )
        zeus.AddOpt(self,\
            "line_19",\
            "$TOFENERGYRECROOT/share/TofEnergyRecOptions_MC.txt",\
            ""\
            )
        zeus.AddOpt(self,\
            "line_20",\
            "$EMCRECROOT/share/EmcRecOptions.txt",\
            ""\
            )
        zeus.AddOpt(self,\
            "line_21",\
            "$MUCRECALGROOT/share/jobOptions_MucRec.txt",\
            ""\
            )
        zeus.AddOpt(self,\
            "line_23",\
            "$EVENTASSEMBLYROOT/share/EventAssembly.txt",\
            ""\
            )
        zeus.AddOpt(self,\
            "line_24",\
            "$PRIMARYVERTEXALGROOT/share/jobOptions_kalman.txt",\
            ""\
            )
        zeus.AddOpt(self,\
            "line_25",\
            "$VEEVERTEXALGROOT/share/jobOptions_veeVertex.txt",\
            ""\
            )
        zeus.AddOpt(self,\
            "line_27",\
            "$HLTMAKERALGROOT/share/jobOptions_HltMakerAlg.txt",\
            ""\
            )
        zeus.AddOpt(self,\
            "line_30",\
            "$EVENTNAVIGATORROOT/share/EventNavigator.txt",\
            " EventNavigator"\
            )
        zeus.AddOpt(self,\
            "line_33",\
            "$ROOTIOROOT/share/jobOptions_Dst2Root.txt",\
            "output ROOT REC data"\
            )
        zeus.AddOpt(self,\
            "line_36",\
            "$CALIBSVCROOT/share/calibConfig_rec_mc.txt",\
            "configure of calibration constants for MC"\
            )
        zeus.AddOpt(self,\
            "BesRndmGenSvc",\
            "",\
            ""\
            )
        zeus.AddOpt(self,\
            "MessageSvc",\
            "",\
            ""\
            )
        zeus.AddOpt(self,\
            "EventCnvSvc",\
            "",\
            ""\
            )
        zeus.AddOpt(self,\
            "ApplicationMgr",\
            "",\
            ""\
            )
        zeus.SetOpt(self,'EventCnvSvc', 'digiRootInputFile','{"sim_001.rtraw"}')
        zeus.SetOpt(self,'EventCnvSvc', 'digiRootOutputFile','"/scratchfs/bes/kangxianwei/maxx/dst/Dp_phiomega/sim_001.dst"')
        zeus.SetOpt(self,'ApplicationMgr', 'EvtMax','-1')
        zeus.SetOpt(self,'BesRndmGenSvc', 'RndmSeed',' 60011')
        zeus.SetOpt(self,'MessageSvc', 'OutputLevel',' 5')

    def SetRaw(self, raw):
        self.SetOpt("EventCnvSvc","digiRootInputFile",'{"%s"}'%raw)
    def SetDst(self, dst):
        self.SetOpt("EventCnvSvc","digiRootOutputFile",'"%s"'%dst)
    def SetSeed(self, seed):
        self.SetOpt("BesRndmGenSvc","RndmSeed",str(seed))
        