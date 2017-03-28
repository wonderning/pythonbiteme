#/usr/bin/env python
# -*- coding: utf-8 -*-
# 题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。

def reverse(str):
    str_len = len(str)
    str_reverse = str
    if str_len > 0:
        str_reverse = str[-1] + reverse(str[:-1])
    return str_reverse
print(reverse('sadfasf'))

