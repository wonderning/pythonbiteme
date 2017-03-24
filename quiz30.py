#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。

def symm(str):
    str_len = len(str)
    str_half = round(str_len/2)
    for i in range(1, str_half+1):
        if str[i] != str[-i-1]:
            return 0
    return 1

print(symm('12344321'))
print(symm('1234321'))
print(symm('1234567'))


