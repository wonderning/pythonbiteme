#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 题目：打印出如下图案（菱形）:

max = 41
half = round(max/2)
for i in range(1, half+1):
    print(' '*(half-i+1), end="")
    print('*' * (i*2-1))
for i in range(half-1, 0, -1):
    print(' '*(half-i+1), end="")
    print('*' * (i*2-1))


