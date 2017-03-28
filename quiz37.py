#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 题目：对10个数进行排序。

my_list=[4,3,2,6,8,11,3,1]
# for i in range(10):
#     my_list.append(int(input("Input ith number:")))
# for i in sorted(my_list): print(i)

def insert_sort(lists):
    for j in range(len(lists)-1):
        i = j
        for i in range(i, -1, -1):
            if lists[i] > lists[i+1]:
                lists[i], lists[i+1] = lists[i+1], lists[i]
            print(j, i, lists)
    return lists
print(insert_sort(my_list))



