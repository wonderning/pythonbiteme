#encoding: utf-8
#!/usr/bin/env python
# 一个整数，它加上100和加上268后都是一个完全平方数，请问该数是多少？
# Python also has huge precision issues during calculation.
# import match sqrt() can also be used.

i = 1.0
while i >= 0:
    j = int((float(i + 100.0)) ** 0.5)
    k = int((float(i + 268.0)) ** 0.5)
    if (j ** 2 == (i+100) and (k ** 2 == (i + 268))):
        print("The number is %d" % i)
        i += 1
    else:
        i += 1
    if i>100000000000:
        exit()
