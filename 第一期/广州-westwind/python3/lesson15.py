#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/16 23:58
# @Author  : caijiangchun
# @Site    : 
# @File    : lesson15.py
# @Software: PyCharm
from  datetime import date
from  datetime import time
from datetime import datetime
if __name__ =="__main__":
    #获取今天的日期
    today = date.today()
    print("Today is %s " % today)

    #把今天的日期年月日分开，重新格式化
    print("Today is %s %s %s " % (today.year, today.month, today.day))

    # 看下今天是星期几
    # 星期几    序号
    # Monday     0
    # Tuesday    1
    # Wednesday  2
    # Thursday   3
    # Friday     4
    # Saturday   5
    # Sunday     6
    # weekday会获取到对应的序号，请根据序号对上上述表，来看是星期几

    # weekday会获取到对应的序号，请根据序号对上上述表，来看是星期几
    weekday_num = today.weekday()
    print("weekdays is %s" % weekday_num)

    weekdays = ('Monday', 'Tuesday', "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    print("Today is %s" %weekdays[weekday_num])

    print("-" * 30)

    #现在的时间
    #time_now = time()
    #print(time_now)
    datetime_now = datetime.now()
    print(datetime_now)

    #用time构造个时间
    time_one = time(hour= 9, minute=8, second=56,microsecond= 30)
    print(time_one)

    #构造日期时间
    time_two = datetime(year=2018, month=8, day=18, hour=8, minute=48, second=58)
    print(time_two)