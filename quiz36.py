#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 题目：求100之内的素数。

def is_prime(i):
    i_sqrt = round(i ** 0.5)
    for j in range(2, i_sqrt + 1):
        if i % j == 0:
            return False
            break
    return True

for i in range(2, 101):
    if is_prime(i):
        print(i)
