#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 题目：学习使用auto定义变量的用法。


num = 2
def autofunc():
    num = 1
    print("Internal block num = %d" % num)
    num += 1
for i in range(3):
    print("THe num = %d" % num)
    num += 1
    autofunc()
