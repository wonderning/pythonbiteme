#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。

week_list = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
choice = []
letter_first = (input("Input first letter: ")).upper()
for i in week_list:
    if letter_first == i[0]:
        # print(i)
        choice.append(i)
if len(choice) > 1:
    letter_second = (input("Input second letter: ")).lower()
    for i in choice:
        if letter_second == i[1]:
            print("Your input is %s." % i)
else:
    print("Your input is %s." % choice[0] )1


