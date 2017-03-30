#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
 两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵：
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]
'''
X = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]
Y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]

new = []
for i, j in zip(X, Y):
    new.append([])
    for i_i, j_j in zip(i, j):
        new[-1].append(i_i + j_j)
print(new)
