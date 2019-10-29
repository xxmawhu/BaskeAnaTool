#!/usr/bin/env python
# -*- coding: utf-8 -*-
# <===<===<===<===<===<===<===<===<===~===>===>===>===>===>===>===>===>===>
# File Name:    cmt_inc.py
# Author:       Hao-Kai SUN
# Created:      2019-10-29 Tue 16:19:50 CST
# <<=====================================>>
# Last Updated: 2019-10-29 Tue 20:25:35 CST
#           By: Hao-Kai SUN
#     Update #: 33
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

ODDTUPLE: tuple = (
    '-I"include_dirs"',
    '-I"apply_pattern"',
    '-I"component_library"',
)
# extract CMT system info from environment variables
try:
    CMTROOT: str = os.environ['CMTROOT']
    CMTBIN: str = os.environ['CMTBIN']
    CMT: str = os.sep.join([CMTROOT, CMTBIN, 'cmt.exe'])
except Exception as excep:
    print("Is BOSS environment set correctly?")
    raise excep
else:
    cmd_rawINC: list = [CMT, 'show', 'macro_value', 'includes']


def srun(cmd: list, timeout: int = 10) -> str:
    """Wrapper for subprocess."""
    try:
        proc = sp.Popen(cmd, stdout=sp.PIPE, encoding="utf-8")
        tmp: tuple = proc.communicate(timeout=timeout)
    except Exception as excep:
        print("during run cmt show: ")
        raise excep
    else:
        return tmp[0] if tmp[1] is None else tmp[1]


rlt_rawINC: str = srun(cmd_rawINC)
rawINC: list = rlt_rawINC.strip().split()

# remove unknown(odd) terms
for oddElt in ODDTUPLE:
    rawINC.remove(oddElt)

INC: list = [inc[2:] for inc in rawINC]

print(INC)
# ===================================================================<<<
# ======================== cmt_inc.py ends here ========================
