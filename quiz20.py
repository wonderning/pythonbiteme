#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

height_init, height_total = 100.0, -100.0
height = height_init
for i in range(1, 11):
    height_total += height * 2.0
    height /= 2.0
print(height, height_total)
