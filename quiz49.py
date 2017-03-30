#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 使用lambda来创建匿名函数。


my_max = lambda x, y: (x > y) * x + (x < y) * y
my_min = lambda x, y: (x < y) * x + (x > y) * y

print(my_max(2, 1))
print(my_min(2, 1))
