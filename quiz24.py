#!/usr/bin/env python
# -*- coding: utf-8 -*-
#题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和

import functools
a = 1.0
b = 2.0
lst = []
for i in range(20):
    print(b, a)
    lst.append(float(b/a))
    b, a =  a + b, b
sum = functools.reduce(lambda x, y: x+y, lst)
print(sum)


