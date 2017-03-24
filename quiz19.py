#!/usr/bin/env python
# -*- coding: utf-8 -*-
#一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。

import math
import functools


def divisor(i):
    div = []
    for j in range(1, i):
        if i % j == 0:
            div.append(j)
    return div

def wanshu(i):
    div = divisor(i)
    div_sum = functools.reduce(lambda x, y: x + y, div)
    if div_sum == i:
        return True
    else:
        return False

if __name__ == '__main__':
    for i in range(2, 100001):
        if wanshu(i): print(i, end=" ")
    print()



