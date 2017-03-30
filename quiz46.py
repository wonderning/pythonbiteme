#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 求输入数字的平方，如果平方运算后小于 50 则退出.

while True:
    num = float(input("Input a number: ")) ** 2
    print(num)
    if num < 50: exit()
