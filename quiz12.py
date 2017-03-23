#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 判断101-200之间有多少个素数，并输出所有素数。
# 因为一个数n如果在2,到根号n内没有被整除,那么在根号n,到n之间也一定没有被整除.


import math

total = 0
for i in range(101, 201):
    i_sqrt = round(math.sqrt(i))
    i_prime = True
    for j in range(2, i_sqrt + 1):
        if i % j == 0:
            i_prime = False
            break
    if i_prime:
        print(i, end=" ")
        total += 1
print("\nTotal number:", total)


