#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。

for a in range(ord('x'), ord('z') + 1):
    for b in range(ord('x'), ord('z') + 1):
        for c in range(ord('x'), ord('z') + 1):
            # a != b and b != c and a != c, a,b,c 必须不等, 必须对不同的人
            # a != ord('x'), a不能对x
            # c != ord('x') and c != ord('z'), c不能对x,z
            if (a != b and b != c and a != c) and (a != ord('x')) and (c != ord('x') and c != ord('z')):
                print("a -- %s, b -- %s, c -- %s" % (chr(a), chr(b), chr(c)))


xyz = ['x', 'y', 'z']  # 0 for x, 1 for y, 2 for z
for a in range(3):
    for b in range(3):
        for c in range(3):
            if a != b and b != c and a != c and a != 0 and c != 0 and c != 2:
                print(xyz[a], xyz[b], xyz[c])
