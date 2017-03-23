#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 将一个列表的数据复制到另一个列表中。
import copy

a = [1, 2, 3, [1]]
b = copy.deepcopy(a)
c = a
d = a[:]

a[3].append(4)

print(a, b, c, d)
