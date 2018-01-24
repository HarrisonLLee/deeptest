#-*- coding:utf-8 -*-

#模块导入基本格式

#直接导入整个模块
import 模块名

import sys


#方法二
#从模块中导入指定的类、方法等资源
from 模块名 import 模块/类/方法/变量

#从sys中导入path
from sys import path


#方法三
#将模块中所有资源都导入
#少用
from 模块 import *



#包
autoTest/           #顶层包
    __init__.py     #初始化autoTest包
    log/            #日志管理子包
        __init__.py
        htmlLogger.py
        xmlLogger.py
        ...
    fromats/        #文件解析子包
        __init__.py
        excelParser.py
        xmlParser.py
        htmlParser.py
        ...
    driver/         #自动化测试驱动子包
        __init__.py
        wbDriver.py
        httpDriver.py
        ...

    ...
auto.py     #mian入口

#以下演示如何在auto.py中导入autoTest中的模块

#导入wbDriver
from autoTest.driver import wbDriver

#如果wbDriver.py中有wbDriver类
#那么可以这样导入wbDriver类
from autoTest.driver.wbDriver import wbDriver


