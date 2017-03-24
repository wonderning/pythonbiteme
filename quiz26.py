#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 题目：利用递归方法求5!。

def fact(i):
    sum = 1
    if i != 0:
        sum = i * fact(i - 1)
    return sum

for i in range(5):
    print(fact(i))


