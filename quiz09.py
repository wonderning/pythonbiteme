#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 题目：输出 9*9 乘法口诀表。 每行暂停一秒输出。
# 程序分析：分行与列考虑，共9行9列，i控制行，j控制列。

from time import sleep

for i in range(1, 10):
    for j in range(1, i + 1):
        print("%2d*%2d=%2d" % (i, j, i * j), end="  ")
        j += 1
    print()
    sleep(1)