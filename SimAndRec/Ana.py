#!/usr/bin/env python
# -*- coding: utf-8 -*-
class ana():
    def __init__(self, opt='', dst='', out=''):
        self._opt = opt
        self._dst = dst
        self._out = out

    def Make(self, ff):
        f = open(ff, 'w')
        s = self._opt
        s += '''
ApplicationMgr.EvtMax = -1; 

// Set output level threshold (2=DEBUG, 3=INFO, 4=WARNING, 5=ERROR, 6=FATAL )
MessageSvc.OutputLevel = 5;

ApplicationMgr.HistogramPersistency = "ROOT";

EventCnvSvc.digiRootInputFile = {
    "''' + self._dst + '''"
};
NTupleSvc.output={
    "FILE DATAFILE = ' ''' + self._out + '''' OPT = 'new' TYP = 'ROOT'"
};
'''
        f.write(s)
        f.close()
