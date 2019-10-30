#!/usr/bin/env python
# -*- coding: utf-8 -*-
# <===<===<===<===<===<===<===<===<===~===>===>===>===>===>===>===>===>===>
# File Name:    env_lib.py
# Author:       Hao-Kai SUN
# Created:      2019-10-29 Tue 16:19:50 CST
# <<=====================================>>
# Last Updated: 2019-10-30 Wed 16:56:56 CST
#           By: Hao-Kai SUN
#     Update #: 95
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
import os
import subprocess as sp
from sys import exit as sys_exit
from sys import version_info as verinfo


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
finally:
    sys_exit(0)

ENVL: list = srun(['env']).strip().split('\n')

LIBP: list = [e for e in ENVL if 'ROOT=' in e]

# ===================================================================<<<
# ======================== env_lib.py ends here ========================
