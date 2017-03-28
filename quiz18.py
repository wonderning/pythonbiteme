#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。

from functools import reduce

try:
    a = int(input("Input a for a+aa+aaaa...:"))
    n = int(input("Iput how many a* in a row: "))
except:
    exit("Wrong input!")
a_list = []
for i in range(1, n + 1):
    a_s = str(a) * i
    print(a_s)
    a_list.append(int(a_s))
print(a_list)
print(sum(a_list))
# Updated with lambda:
a_sum = reduce(lambda x, y: x+y, a_list)
print(a_sum)

