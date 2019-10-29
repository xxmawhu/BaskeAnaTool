#!/usr/bin/env python
# <===<===<===<===<===<===<===<===<===~===>===>===>===>===>===>===>===>===>
# File Name:    cmt_inc.py
# Author:       Hao-Kai SUN
# Created:      2019-10-29 Tue 16:19:50 CST
# <<=====================================>>
# Last Updated: 2019-10-29 Tue 16:25:30 CST
#           By: Hao-Kai SUN
#     Update #: 3
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

# extract CMT system info from environment variables
CMTROOT: str = os.environ['CMTROOT']
CMTBIN: str = os.environ['CMTBIN']
CMT: str = os.sep.join([CMTROOT, CMTBIN, 'cmt.exe'])

print(CMT)
# ===================================================================<<<
# ======================== cmt_inc.py ends here ========================
