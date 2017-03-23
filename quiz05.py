#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 输入三个整数x,y,z，请把这三个数由小到大输出。


# This version works, but not flexible enough.
# try:
#     i = int(input("Enter a number: "))
#     j = int(input("Enter a number: "))
#     k = int(input("Enter a number: "))
#     a = [i, j, k]
#     a.sort()
#     print(i) for i in a
# except:
#     print("Wrong input!")

# This is a better version:
num = []
while True:
    try:
        num.append(int(input("Input an integer, or input something else to stop: ")))
    except:
        print("stop")
        break
num.sort()
for i in num:
    print(i, end=" ")
