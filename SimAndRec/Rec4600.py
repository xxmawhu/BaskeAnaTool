from Zeus import zeus 
class Rec4600(zeus) : 
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
            "line_05",\
            "$BESEVENTMIXERROOT/share/jobOptions_EventMixer_rec.txt",\
            " background mixing"\
            )
        zeus.AddOpt(self,\
            "line_06",\
            "$CALIBSVCROOT/share/job-CalibData.txt",\
            ""\
            )
        zeus.AddOpt(self,\
            "line_07",\
            "$MAGNETICFIELDROOT/share/MagneticField.txt",\
            ""\
            )
        zeus.AddOpt(self,\
            "line_08",\
            "$ESTIMEALGROOT/share/job_EsTimeAlg.txt",\
            ""\
            )
        zeus.AddOpt(self,\
            "line_10",\
            "$MDCXRECOROOT/share/jobOptions_MdcPatTsfRec.txt",\
            " PAT+TSF method for MDC reconstruction"\
            )
        zeus.AddOpt(self,\
            "line_11",\
            "$KALFITALGROOT/share/job_kalfit_numf_data.txt",\
            ""\
            )
        zeus.AddOpt(self,\
            "line_12",\
            "$MDCDEDXALGROOT/share/job_dedx_all.txt",\
            ""\
            )
        zeus.AddOpt(self,\
            "line_13",\
            "$TRKEXTALGROOT/share/TrkExtAlgOption.txt",\
            ""\
            )
        zeus.AddOpt(self,\
            "line_14",\
            "$TOFRECROOT/share/jobOptions_TofRec.txt",\
            ""\
            )
        zeus.AddOpt(self,\
            "line_15",\
            "$TOFENERGYRECROOT/share/TofEnergyRecOptions_MC.txt",\
            ""\
            )
        zeus.AddOpt(self,\
            "line_16",\
            "$EMCRECROOT/share/EmcRecOptions.txt",\
            ""\
            )
        zeus.AddOpt(self,\
            "line_17",\
            "$MUCRECALGROOT/share/jobOptions_MucRec.txt",\
            ""\
            )
        zeus.AddOpt(self,\
            "line_18",\
            "$EVENTASSEMBLYROOT/share/EventAssembly.txt",\
            ""\
            )
        zeus.AddOpt(self,\
            "line_19",\
            "$PRIMARYVERTEXALGROOT/share/jobOptions_kalman.txt",\
            ""\
            )
        zeus.AddOpt(self,\
            "line_20",\
            "$VEEVERTEXALGROOT/share/jobOptions_veeVertex.txt",\
            ""\
            )
        zeus.AddOpt(self,\
            "line_21",\
            "$HLTMAKERALGROOT/share/jobOptions_HltMakerAlg.txt",\
            ""\
            )
        zeus.AddOpt(self,\
            "line_22",\
            "$EVENTNAVIGATORROOT/share/EventNavigator.txt",\
            ""\
            )
        zeus.AddOpt(self,\
            "line_25",\
            "$ROOTIOROOT/share/jobOptions_Dst2Root.txt",\
            "output ROOT REC data"\
            )
        zeus.AddOpt(self,\
            "line_28",\
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
        zeus.SetOpt(self,'EventCnvSvc', 'digiRootInputFile',' {"NAMEA.rtraw"}')
        zeus.SetOpt(self,'EventCnvSvc', 'digiRootOutputFile','"NAMEB.dst"')
        zeus.SetOpt(self,'ApplicationMgr', 'EvtMax',' -1')
        zeus.SetOpt(self,'BesRndmGenSvc', 'RndmSeed',' LIPR')
        zeus.SetOpt(self,'MessageSvc', 'OutputLevel',' 5')

    def SetRaw(self, raw):
        self.SetOpt("EventCnvSvc","digiRootInputFile",'{"%s"}'%raw)
    def SetDst(self, dst):
        self.SetOpt("EventCnvSvc","digiRootOutputFile",'"%s"'%dst)
    def SetSeed(self, seed):
        self.SetOpt("BesRndmGenSvc","RndmSeed",str(seed))
        