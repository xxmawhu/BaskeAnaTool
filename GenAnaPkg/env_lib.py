#!/usr/bin/env python
# -*- coding: utf-8 -*-
# <===<===<===<===<===<===<===<===<===~===>===>===>===>===>===>===>===>===>
# File Name:    env_lib.py
# Author:       Hao-Kai SUN
# Created:      2019-10-29 Tue 16:19:50 CST
# <<=====================================>>
# Last Updated: 2019-10-30 Wed 19:19:38 CST
#           By: Hao-Kai SUN
#     Update #: 138
# <<======== COPYRIGHT && LICENSE =======>>
#
# Copyright © 2019 SUN Hao-Kai <spin.hk@outlook.com>. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GNU Emacs.  If not, see <https://www.gnu.org/licenses/>.
#
# ============================== CODES ==============================>>>
"""
Generate library link flags from BOSS environment variables..
"""
import pathlib as pl
import subprocess as sp
from sys import version_info as verinfo

# BOSS 6.6.4.p03 architecture
ARCH: str = 'x86_64-slc5-gcc43-opt'
LDHEAD: str = '-shared -fPIC -ldl -Wl,--no-undefined -Wl,--as-needed'
WCLHEP: str = '1.9.4.2'
WGAUDI: str = 'v27r6'
WGAUDIAUD: str = 'v9r1'

ODDTUPLE: tuple = (
    'ZPLUG_',
    # 'CMTROO',
    'SITERO',
    'TESTRE',
)


def srun(cmd: list, timeout: int = 10):
    """Wrapper for subprocess."""
    try:
        proc = sp.Popen(cmd, stdout=sp.PIPE, encoding="utf-8")
        tmp: tuple = proc.communicate(timeout=timeout)
    except Exception as excep:
        print("during run cmt show: ")
        raise excep
    else:
        return tmp[0] if tmp[1] is None else tmp[1]


# python version check!
VERMSG: str = "TOO old python version! 3.7+, please!"
assert verinfo.major == 3 and verinfo.minor >= 7, VERMSG

# check for current working environment
try:
    srun(['boss', '-h'])
except Exception as excep:
    print("It seems that the BOSS environment is not set correctly!")
    raise excep

ENVL: list = srun(['env']).strip().split('\n')

LIBP: list = [e for e in ENVL if 'ROOT=' in e and e[:6] not in ODDTUPLE]

# remove odd libs and adapt for CMakeLists.txt
fullLIBP: list = []
temp: list = []
for l in LIBP:
    hasso: bool = False
    lp: str = ''.join(l.split('=')[1:])
    for fp in list(pl.Path(lp).rglob('lib*.so')):
        fpr = fp.resolve(strict=True)
        if (ARCH in fpr.as_posix() and WCLHEP not in fpr.as_posix()
                and WGAUDI not in fpr.as_posix()
                and WGAUDIAUD not in fpr.as_posix()):
            hasso = True
            libn: str = fpr.name[3:-3]
            temp.append('-L' + fpr.parent.as_posix())
            temp.append('-l' + libn)
    if hasso:
        fullLIBP.append(' '.join(list(dict.fromkeys(temp))))
    temp.clear()

print(f'"{LDHEAD}"')
for l in fullLIBP:
    print(f'"{l}"')
# ===================================================================<<<
# ======================== env_lib.py ends here ========================
