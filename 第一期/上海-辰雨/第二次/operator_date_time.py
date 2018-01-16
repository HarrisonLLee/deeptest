#!/usr/bin/env python
# encoding: utf-8

from datetime import date
from datetime import time
from datetime import datetime
'''
python 关于时间处理的类分为：
date:仅用于日期处理(年，月，日)
time:仅用于时间处理（时，分，秒，毫秒）
datetime:可以处理日期和时间的组合（年，月，日，时，分，秒，毫秒）
timedelta:日期时间处理，可以用于时间运算等
tzinfo:用于时区处理
'''
#获取今天的日期
today = date.today()
print ('今天是 %s'%today)

#把今天的日期年月日分开，重新格式化一下：
print('今天是:%s %s %s'%(today.year,today.month,today.day))

#weekday 会获取到对应的序号，请根据序号对上上述表，来看是星期几
weekday_num = today.weekday()
print ('今天weekday是 %s'%weekday_num)

#输出可读性更好的星期几
weekdays = ('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')
print ('今天是 %s'%weekdays[weekday_num])
print ('*'*30)

#看看现在的时间：
today_now = datetime.now()
print ('现在是%s'%today_now)

#用time来构造个时间
t = time(hour=12,minute=20,second=30,microsecond=200)
print ('我们自己造的时间是%s'%t)

#再造个日期时间出来试试：
d = datetime(year=2008,month=8,day=8,minute=8,second=8)
print ('造的日期时间为：%s'%d)


'''
格式化日期时间：strftime 函数
常用的时间格式如下：
%y	两位数的年份（00-99）
%Y  四位数的年份（000-9999）
%m  月份（01-12）
%d  月内的一天（0-31）
%H  24小时制小时数（0-23）
%I  12小时制的小时数（01-12）
%M  分钟数（00-59）
%S	秒（00-59）
'''
#当前默认格式化时间：
import time
t = time.localtime()
print ('未格式化前的时间：t = %s'%t)
print (u'当前默认日期时间格式：%s'%time.asctime(t))

#格式化为：年-月-日 时：分：秒 星期几
print (u'24小时制全格式：',time.strftime('%Y-%m-%d %H:%M:%S %A'),time.localtime())
print (u'12小时制缩写格式:',time.strftime('%Y-%m-%d %I:%M:%S %a',time.localtime()))

#带a.m 或p.m 24小时制格式：
print ("带a.m或p.m 24小时制全格式：",time.strftime("%Y-%m-%d %H:%M:%S %p %A",time.localtime()))

#格式乱排序:
print ('随意拍格式：',time.strftime("%A %Y-%d-%m %p %H:%M:%S %z",time.localtime()))