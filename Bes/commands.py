#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C)2019 All rights reserved.
#
#   Author        : Xin-Xin MA
#   Email         : xxmawhu@163.com
#   File Name     : getoutput.py
#   Create Time   : 2019-12-05 12:12
#   Last Modified : 2019-12-05 12:12
#   Describe      :
#
# ====================================================

import subprocess


def getoutput(command):
    pr = subprocess.Popen(command,
                          shell=True,
                          stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE)
    out, err = pr.communicate()
    output = out.decode()
    if err.decode() != "":
        output += "\n" + err.decode()
    return output


if __name__ == "__main__":
    print(getoutput("ls"))
