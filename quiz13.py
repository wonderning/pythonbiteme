#!/usr/bin/env python
# -*- coding: utf-8 -*-
#打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。

for i in range(100, 1000):
    i_hundred = i // 100
    i_ten = (i - 100 * i_hundred) // 10
    i_one = (i - 100 * i_hundred - 10 * i_ten)
    if i == i_hundred ** 3 + i_ten ** 3 + i_one ** 3:
        print(i)

