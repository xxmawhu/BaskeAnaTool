#!/usr/bin/env python
# -*- coding: utf-8 -*-
# <===<===<===<===<===<===<===<===<===~===>===>===>===>===>===>===>===>===>
# File Name:    cmt_lib.py
# Author:       Hao-Kai SUN
# Created:      2019-10-29 Tue 16:19:50 CST
# <<=====================================>>
# Last Updated: 2019-10-30 Wed 13:26:01 CST
#           By: Hao-Kai SUN
#     Update #: 81
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
Generate include paths for compiling flags.
"""
import os
import subprocess as sp
from sys import version_info as verinfo

# python version check!
VERMSG: str = "TOO old python version! 3.7+, please!"
assert verinfo.major == 3 and verinfo.minor >= 7, VERMSG

# check for current working directory simply
ERRMSG: str = "NOT working under package's 'cmt' directory!"
assert os.getcwd().endswith("cmt"), ERRMSG

# extract CMT system info from environment variables
try:
    CMTROOT: str = os.environ['CMTROOT']
    CMTBIN: str = os.environ['CMTBIN']
    CMT: str = os.path.join(CMTROOT, CMTBIN, 'cmt.exe')
except Exception as excep:
    print("Is BOSS environment set correctly?")
    raise excep
else:
    cmd_PKGNAME: list = [CMT, 'show', 'macro_value', 'package']
    cmd_PKGROOT: list = [CMT, 'show', 'macro_value']
    cmd_rawLIB: list = [CMT, 'show', 'macro_value']


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


PKGNAME: str = srun(cmd_PKGNAME).strip()
print('Package Name:', PKGNAME)
cmd_PKGROOT.append(PKGNAME + '_root')
PKGROOT: str = srun(cmd_PKGROOT).strip()
print('Package root:', PKGROOT)
cmd_rawLIB.append(PKGNAME + '_shlibflags')
rawLIB: list = list(dict.fromkeys(
    srun(cmd_rawLIB).strip().replace('..', PKGROOT).split()))

temp: list = []
LIB: list = []
for l in rawLIB:
    if l.startswith('-L'):
        LIB.append(' '.join(temp))
        temp.clear()
    temp.append(l)

for l in LIB:
    print(l)
# ===================================================================<<<
# ======================== cmt_lib.py ends here ========================
