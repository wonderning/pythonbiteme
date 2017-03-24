#!/usr/bin/env python
# -*- coding: utf-8 -*-
#题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。 程序分析：学会分解出每一位数。

# a = input("Input an integer: ")
# print(len(a))
# a = a[::-1]
# print(a)

# Another way:
x = int(input("Input an integer: "))

a = x / 10000
b = x % 10000 / 1000
c = x % 1000 / 100
d = x % 100 / 10
e = x % 10


