#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Bes.commands import getoutput as do
from Bes.ana import ana


class anaJpsi(ana):
    def __init__(self):
        super()
        # ana.__init__(self)

    def addJpsi(self, date):
        Dict = {
            2009: '/besfs3/offline/data/703-1/jpsi/round02/dst',
            2012: '/besfs3/offline/data/703-1/jpsi/round05/dst',
            2017: '/bes3fs/offline/data/704-1/jpsi/round11/dst',
            2018: '/bes3fs/offline/data/704-1/jpsi/round12/dst'
        }
        hintDict = {
            2009: 'add 2009 Jpsi data(0.2 billion)',
            2012: 'add 2012 Jpsi data(1.1 billion)',
            2017: 'add 2017-2018 Jpsi data(4.6 billion)',
            2018: 'add 2018-2019 Jpsi data(4.1 billion)'
        }
        print(hintDict[date])
        dst = Dict[date]
        ll = do('ls %s/* -d' % dst).split()
        for l in ll:
            ana.addst(self, l)
