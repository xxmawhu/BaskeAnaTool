#!/afs/ihep.ac.cn/soft/common/python27_sl65/bin/python
# -*- coding: utf-8 -*-
import os
import logging
logger = logging.getLogger(__name__)


def mkdir(s):
    if (not os.path.isdir(s)):
        os.makedirs(s)
