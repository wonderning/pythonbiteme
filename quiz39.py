#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。

my_list = [1, 3, 5, 7, 9]
item = float(input("Input a number: "))
for i in range(len(my_list)):
    if item < my_list[i]:
        my_list.insert(i, item)
        break
print(my_list)
