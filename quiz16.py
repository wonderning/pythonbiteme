#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 使用 datetime 模块。

import datetime
if __name__ == '__main__':
    print(datetime.date.today().strftime('%d/%m/%Y'))
    print(datetime.date(2016, 1, 5))
    BirthDate = datetime.date(1941, 1, 5)
    print(BirthDate.strftime('%d/%m/%Y'))
    BirthNextDay = BirthDate + datetime.timedelta(days = 1)
    print(BirthNextDay.strftime('%d/%m/%Y'))
    FirstBirthday = BirthDate.replace(year = BirthDate.year + 1)
    print(FirstBirthday.strftime('%d/%m/%Y'))
