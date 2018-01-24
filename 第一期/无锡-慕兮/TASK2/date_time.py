# -*- coding:utf-8 -*-
__author__ = 'Lakisha'

'''
from datetime import date
from datetime import datetime
from datetime import time

if __name__ == "__main__":
    #获取今天的日期
    today = date.today()
    print("今天是： %s"%today)

    #把今天的日期年月日分开，重新格式化
    print("今天是 %s %s %s"%(today.day, today.month, today.year))

    # 看下今天是星期几
    # 星期几    序号
    # Monday     0
    # Tuesday    1
    # Wednesday  2
    # Thursday   3
    # Friday     4
    # Saturday   5
    # Sunday     6
    #weekday 会获取到对应的序号，请根据序号对上上述表，来看是星期几
    week_day = today.weekday()
    print("几天是星期 %s"%(week_day+1))

    # 输出可读性更好的星期几
    weekdays = ("Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday")
    print("今天是 %s"%weekdays[week_day])
    print("-"*30)

    # 看看现在的时间
    today_now = datetime.now()
    print("现在是 %s"%today_now)

    # 用time来构造个时间出来
    t = time(hour=12, minute=20, second=30, microsecond=200)
    print("我们自己造的时间： %s"%t)

    # 再造个日期时间出来试试
    d = datetime(year=2017, month=12, day=12, hour=12, minute=30, second=30, microsecond=200)
    print("我们自己造的日期： %s"%d)
'''
import time

if __name__ == "__main__":
    # 先看下当前默认格式化的时间
    localtime = time.asctime(time.localtime())
    print("当前默认时间格式： %s"%localtime)

    # 格式化为： 年-月-日 时:分:秒 星期几
    print("24小时制全格式：", time.strftime("%Y-%m-%d %H:%M:%S %A", time.localtime()))
    print("12小时全格式：", time.strftime("%Y-%m-%d %I:%M:%S %a", time.localtime()))

    # 带a.m. 或 p.m. 标识时间格式  %p
    print("带a.m或p.m 24小时制全格式：",
          time.strftime("%Y-%m-%d %H:%M:%S %p %A", time.localtime()))

    # 把时区也带上看看 %z
    print("带时区的全格式：",
          time.strftime("%Y-%m-%d %H:%M:%S %p %A %z", time.localtime()))

    # 格式乱排下试试
    print("随意排格式：",
          time.strftime("%A %Y-%d-%m %p %H:%M:%S %z", time.localtime()))