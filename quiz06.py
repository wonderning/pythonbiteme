#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  斐波那契数列。

# Method 1:
# phib=[0, 1]
# for i in range(100):
#     phib.append(phib[-1] + phib[-2])
# for i in phib:
#     print(i, end=" ")


# Method 2:
def fib1(n):
    if 0 <= n < 2:
        return n
    elif n >= 2:
        return fib1(n - 1) + fib1(n - 2)
    else:
        return "Error!"


print(fib1(10))
