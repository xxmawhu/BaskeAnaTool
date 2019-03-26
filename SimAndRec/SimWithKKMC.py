from Sim import sim
class SimWithKKMC(sim):
    def __init__(self):
        sim.__init__(self)
        #Loop
        Loop_base = "$OFFLINEEVENTLOOPMGRROOT/share/OfflineEventLoopMgr_Option.txt"
        sim.AddOpt(self,"Loop",Loop_base, "")
        #KKMC
        KKMC_desc = "***** job options for generator (KKMC) *****"
        KKMC_base = "$KKMCROOT/share/jobOptions_KKMC.txt"
        #sim.AddOpt(self,"KKMC",KKMC_base, KKMC_desc)
        #EvtGen
        EvtGen_base = "$BESEVTGENROOT/share/BesEvtGen.txt"
        EvtGen_desc = "******* job options for EvtGen *****"
        sim.AddOpt(self,"EvtDecay",EvtGen_base, EvtGen_desc)
        seed_desc = "*********job options for random number***"
        seed_base = ""
        sim.AddOpt(self,"BesRndmGenSvc",seed_base, seed_desc)
        sim.AddOpt(self, "G4Svc_BesSim",\
                "$BESSIMROOT/share/G4Svc_BesSim.txt",\
                "*** job options for detector simulation ***"\
                )
        cal_desc = "configure for calibration constants"
        cal_base = "$CALIBSVCROOT/share/calibConfig_sim.txt"
        sim.AddOpt(self,"calibSvc",cal_base, cal_desc)
        run_base = ""
        run_desc = " run ID used for this simulation"
        sim.AddOpt(self,"RealizationSvc",run_base, run_desc)
        #root
        root_base =  "$ROOTIOROOT/share/jobOptions_Digi2Root.txt"
        root_desc = ""
        sim.AddOpt(self,"RootCnvSvc",root_base, root_desc)
        #message
        message_base = ""
        message_desc = "OUTPUT PRINTOUT LEVEL: (2=DEBUG, 3=INFO,"+\
                       "4=WARNING, 5=ERROR, 6=FATAL )"
        sim.AddOpt(self,"MessageSvc",message_base, message_desc)
        #events 
        evts_desc = " Number of events to be processed (default is 10)"
        sim.AddOpt(self,"ApplicationMgr","", evts_desc)
