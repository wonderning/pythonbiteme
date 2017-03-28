#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# 将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

import math


def is_prime(i):
    i_sqrt = round(math.sqrt(i))
    for j in range(2, i_sqrt + 1):
        if i % j == 0:
            return False
            break
    return True


def break_to_prime(j):
    if j == 1:
        return [1]
    item = []
    i = 1
    while i in range(1, int(j // 2 + 1)):
        if j % i == 0:
            if i != 1:
                item.append(int(i))
            j = j / i
            if is_prime(j):
                item.append(int(j))
                return item
            i = 2
        else:
            i += 1


num = int(input("Input an integer: "))
a = break_to_prime(num)
print("%d=" % num, end="")
for index, value in enumerate(a):
    if index < (len(a) - 1):
        print("%d*" % value, end="")
    else:
        print("%d" % value)
