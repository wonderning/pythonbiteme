#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 题目：求1+2!+3!+...+20!的和。

# i_sum = 0
# for i in range(1, 21):
#     j_ladder = 1
#     for j in range(1, i + 1):
#         j_ladder *= j
#     i_sum += j_ladder
# print(i_sum)

#A better version:
i_sum = 0
j_ladder = 1
for i in range(1, 21):
    j_ladder *= i
    i_sum += j_ladder
print(i_sum)
