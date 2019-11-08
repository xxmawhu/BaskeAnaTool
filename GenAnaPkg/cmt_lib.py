#!/usr/bin/env python

# -*- coding: utf-8 -*-
# <===<===<===<===<===<===<===<===<===~===>===>===>===>===>===>===>===>===>
# File Name:    cmt_lib.py
# Author:       Hao-Kai SUN
# Created:      2019-10-29 Tue 16:19:50 CST
# <<=====================================>>
# Last Updated: 2019-11-08 Fri 17:03:43 CST
#           By: Hao-Kai SUN
#     Update #: 131
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
Generate library link flags from CMT.
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

CMAKESTR: str = """
set(LIBNAMES
    {libn}
)
set(LIBDIRS
    {libd}
)

target_compile_options("${{PROJECT_NAME}}" PUBLIC
    {cppf}
    )

foreach(LIBN "${{LIBNAMES}}")
    find_library(TEMPLIB
        NAMES "${{LIBN}}"
        PATHS "${{LIBDIRS}}"
        NO_DEFAULT_PATH
    )

    target_link_libraries("${{PROJECT_NAME}}"
        PUBLIC "${{TEMPLIB}}")

    # clear temp variable.
    unset(${{TEMPLIB}})
endforeach()
"""


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


def equalsplit(longlist: list, seplength: int = 70, sep: str = " ") -> list:
    """Merge and/or split long list into appx-equal-length-element list.

    e.g.
    longlist: ['a', 'b', 'c', .... 'z']
    result:
    ['a b c d e f g', 'h i j k l m n', ...]
    """
    tem: str = ""
    rlt: list = []
    for ele in longlist:
        if len(ele) >= seplength:
            rlt.append(ele)
            continue
        if len(tem) + len(ele) + len(sep) > seplength:
            rlt.append(tem)
            tem = ""
        else:
            tem += f'{sep}{ele}'

    if len(tem) != 0:
        rlt.append(tem)

    return rlt


cmd_CPPFLAGS: list = cmd_rawLIB + ['cppflags']
CPPFLAGS: list = equalsplit(srun(cmd_CPPFLAGS).strip().split())

PKGNAME: str = srun(cmd_PKGNAME).strip()
# print('Package Name:', PKGNAME)

cmd_PKGROOT.append(PKGNAME + '_root')
PKGROOT: str = srun(cmd_PKGROOT).strip()
# print('Package root:', PKGROOT)

cmd_rawLIB.append(PKGNAME + '_shlibflags')
rawLIB: list = list(
    dict.fromkeys(srun(cmd_rawLIB).strip().replace('..', PKGROOT).split()))


# for CMakeLists.txt compile flags setting (1)
def cmake1():
    """Version 1 for target_link_options"""
    temp: list = []
    libs: list = []
    for lib in rawLIB:
        if lib.startswith('-L'):
            libs.append(' '.join(temp))
            temp.clear()
        temp.append(lib)

    for lib in libs:
        print('"{0}"'.format(lib))


# for CMakeLists.txt compile flags setting (2)
def cmake2():
    """Version 2 for cmake1() + foreach, find_libary, target_link_libraries."""
    oths: list = []
    dirs: list = []
    dirf: bool = False
    libs: list = []
    for lib in rawLIB:
        if lib.startswith('-L'):
            dirf = True
            dirs.append(lib[2:])
        elif lib.startswith('-l') and dirf:
            libs.append(lib[2:])
        elif not (dirf or lib.startswith('.') or lib.startswith('/')):
            oths.append(lib)
        else:
            print(f"Cannot parse this link option: {lib}.")
            raise Exception

    libd: str = '\n    '.join(equalsplit(dirs))
    libn: str = '\n    '.join(equalsplit(libs))
    cppf: str = '\n    '.join(equalsplit(oths))
    print(CMAKESTR.format(libd=libd, libn=libn, cppf=cppf))


cmake2()
# ===================================================================<<<
# ======================== cmt_lib.py ends here ========================
