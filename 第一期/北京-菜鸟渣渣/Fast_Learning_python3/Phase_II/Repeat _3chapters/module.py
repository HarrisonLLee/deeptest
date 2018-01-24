# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   Description :
   Author :       Young
   Change Activity: 2018/1/17:
-------------------------------------------------
"""
__author__ = 'Young'

'''
在Python中模块可以理解为颗粒度更大的组织方式，其中可以包含类、函数、变量等等资源。

而为了更好的把一些基础服务提供给大家应用，Python提供了大量的标准模块，以及大量开源的第三方模块。

我们先看一下模块导入的基本格式：

# 方式一

# 直接导入整个模块
import 模块名

# 例如导入sys模块
import sys


# 方式二

# 从模块中导入指定的类、方法等资源
from 模块名 import 模块/类/方法/变量

# 例如从sys中导入path
from sys import path


# 方式三

# 将模块中所有资源都导入
# 少用
from 模块 import *
'''

'''
包是一种管理Python模块命名空间的形式，采用".模块名称"。

例如一个模块的名称为X.Y，那么表示一个包X中的子模块Y。

下面我们给出一个可能的包结构组织方式：

autoTest/           # 顶层包
    __init__.py     # 初始化autoTest包    
    log/            # 日志管理子包
        __init__.py
        htmlLogger.py
        xmlLogger.py
        ...
    formats/        # 文件解析器子包
        __init__.py
        excelParser.py
        xmlParser.py
        htmlParser.py
        ...
    driver/         # 自动化测试驱动子包
        __init__.py
        wbDriver.py
        httpDriver.py
        ...
'''

# 下面我们演示在auto.py导入autoTest中的模块，请看下述代码示例：
from .autoTest.driver import wbDriver
import sys

sys.path.append("E:\Fast_Learning_python3\Phase_II\Repeat _3chapters")

if __name__ == "__main__":
    wd = wbDriver()
    print(wd)
