#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 题目：求一个3*3矩阵对角线元素之和。


def matrix(dimension):
    matrix = []
    for i in range(dimension):
        matrix.append([])
        for j in range(dimension):
            matrix[i].append(int(input("Input a number for matrxi[%d, %d]: " % (i, j))))
    return(matrix)
if __name__ == '__main__':
    matrix_array = matrix(int(input("Input dimension: ")))
    matrix_sum = 0
    for i in range(len(matrix_array)):
        matrix_sum += matrix_array[i][i]
    print(matrix_sum)
