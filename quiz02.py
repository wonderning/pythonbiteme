# -*- coding: utf-8 -*-
#! /usr/bin/env python
'''企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
'''
# This is a much better version:
prize = 0
standard = [1000000, 600000, 400000, 200000, 100000, 0]
ratio = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]

try:
    earning = float(input("Enter your earnings:"))
    earning_original = earning
except:
    print('Wrong input type, not a digit!')

for s, r in zip(standard, ratio):
    if earning > s:
        prize += (earning - s) * r
        earning = s
    # print(prize)
print("Total prize is %f for earning %f" % (prize, earning_original))

# This is my first version:
# try:
#     earning = float(input("Enter your earnings:"))
#     earning_original = earning
# except:
#     print('Wrong input type, not a digit!')
# prize = 0
# if earning > 1000000:
#     prize += (earning - 1000000) * 0.01
#     earning = 1000000
# elif earning > 600000:
#     prize += (earning - 600000) * 0.015
#     earning = 600000
# elif earning > 400000:
#     prize += (earning - 400000) * 0.04
#     earning = 400000
# elif earning > 200000:
#     prize += (earning - 200000) * 0.05
#     earning = 200000
# elif earning > 100000:
#     prize += (earning - 100000) * 0.075
#     earning = 100000
# elif earning > 0:
#     prize += earning * 0.1
# print("Total prize is %f for earning %f" % (prize, earning_original))
