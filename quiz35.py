#/usr/bin/env python
# -*- coding: utf-8 -*-
# 题目：文本颜色设置。

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERlINE = '\033[4m'

print(bcolors.WARNING + "警告" + bcolors.ENDC)

from color import Colors

print(Colors('文本内容','字体颜色','背景颜色','字体样式'))
