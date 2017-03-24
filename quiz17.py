#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

str = input("Input a string: ")
str_len = len(str)
(str_alpha, str_space, str_digit, str_others) = (0, 0, 0, 0)
for i in str:
    if i.isalpha():
        str_alpha += 1
    elif i.isspace():
        str_space += 1
    elif i.isnumeric():
        str_digit += 1
    else:
        str_others += 1
print("Total length: %d, Alpha: %d, Space: %d, Digit: %d, Others: %d" % (str_len, str_alpha, str_space, str_digit, str_others))
