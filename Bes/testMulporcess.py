#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C)2019 All rights reserved.
#
#   Author        : Xin-Xin MA
#   Email         : xxmawhu@163.com
#   File Name     : C.py
#   Create Time   : 2019-12-05 13:55
#   Last Modified : 2019-12-05 13:55
#   Describe      :
#
# ====================================================
from multiprocessing.pool import ThreadPool
import time
class C:
    def f(self, name):
        print("hello {}".format(name))
        time.sleep(1)
    def run(self, n):
        nameList = list(map(str, range(n)))
        print(nameList)
        t = ThreadPool(processes=20)
        t.map(self.f, nameList)
        t.close()

if __name__ == "__main__":
    c = C()
    c.run(20)
