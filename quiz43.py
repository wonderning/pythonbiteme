#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 演示一个python作用域使用方法


class Num:
    nNum = 1

    def inc(self):
        self.nNum += 1
        print('nNum = %d' % self.nNum)

if __name__ == '__main__':
    nNum = 2
    inst = Num()
    ins1 = Num()
    for i in range(3):
        inst.inc()
        inst.inc()
        ins1.inc()
