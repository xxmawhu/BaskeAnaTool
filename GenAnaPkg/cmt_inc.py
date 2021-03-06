#!/usr/bin/env python
# -*- coding: utf-8 -*-
# <===<===<===<===<===<===<===<===<===~===>===>===>===>===>===>===>===>===>
# File Name:    cmt_inc.py
# Author:       Hao-Kai SUN
# Created:      2019-10-29 Tue 16:19:50 CST
# <<=====================================>>
# Last Updated: 2019-11-09 Sat 14:06:30 CST
#           By: Hao-Kai SUN
#     Update #: 51
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

ODDTUPLE: tuple = (
    '-I"include_dirs"',
    '-I"apply_pattern"',
    '-I"component_library"',
)

# extract CMT system info from environment variables
try:
    CMTROOT: str = os.environ['CMTROOT']
    CMTBIN: str = os.environ['CMTBIN']
    CMT: str = os.path.join(CMTROOT, CMTBIN, 'cmt.exe')
except Exception as excep:
    print("Is BOSS environment set correctly?")
    raise excep
else:
    cmd_rawINC: list = [CMT, 'show', 'macro_value', 'includes']


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


rlt_rawINC: str = srun(cmd_rawINC)
rawINC: list = rlt_rawINC.strip().split()

# remove unknown(odd) terms
for oddElt in ODDTUPLE:
    rawINC.remove(oddElt)

INC: list = [inc[2:] for inc in rawINC]

# for use in CMakeLists.txt `target_include_directories`
CMAKESTR: str = """
target_include_directories(
    ${{PROJECT_NAME}} PUBLIC
    {INCD}
    )
"""
print(CMAKESTR.format(INCD='\n    '.join(INC)))
# for i in INC:
#     print(' ' * 4 + i)
# ===================================================================<<<
# ======================== cmt_inc.py ends here ========================
