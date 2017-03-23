#encoding: utf-8
#!/usr/bin/env python
# 输入某年某月某日，判断这一天是这一年的第几天？
# The only variation is February. Judge


def leap_year(y):
    if((y % 4 == 0 and y % 100 != 0) or y % 400 == 0):
        return True
    else:
        return False


def judge_day(year, month, day):
    dayth = 0
    if leap_year(year):
        month_list = (0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    else:
        month_list = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    for i in range(1, month):
        dayth += month_list[i]
    dayth += day
    print("%d/%d/%d is the %dth day of the year." % (year, month, day, dayth))


if __name__ == '__main__':
    year = int(input("Enter year: "))
    month = int(input("Enter month: "))
    day = int(input("Enter day: "))
    judge_day(year, month, day)
