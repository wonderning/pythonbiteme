#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 按逗号分隔列表。

a = [11, 2, 3]
string = ','.join(str(i) for i in a)
print(string)
str1='_'.join(str(string))
print(str1)
