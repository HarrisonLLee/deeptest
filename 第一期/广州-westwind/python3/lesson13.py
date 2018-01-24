#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/15 23:54
# @Author  : caijiangchun
# @Site    : 
# @File    : lesson13.py
# @Software: PyCharm
import os
#path模块的常用用法
if __name__ == "__main__":

    print("获取当前的路径：")
    print(os.getcwd())

    #返回的是 .
    print("获取当前目录")
    print(os.curdir)

    #创建目标目录必须是不存在的，存在的会报错
    #os.mkdir("work")

    #重命名
    #os.rename("work","python")

    """
    path模块， 常用的方法

    """
    path = __file__
    print(u"当前文件的全路径：%s" % path)
    #是目录则返回true,否则返回False
    print(u"目录判断：%s" % os.path.isdir(path))
    print(u"是否是文件： %s" % os.path.isfile(path))
    print(u"目录\文件是否存在: %s" % os.path.exists(path))
    #获取文件大小
    print(u"获取文件的大小：%s " % os.path.getsize(path))
    #文件的绝对路径
    print(u"绝对路径：%s" % os.path.abspath(path))

    print(u"规范化路径： %s " % os.path.normpath(path))

    #将文件名和目录分割
    print(u"目录和文件名分割: ", end="")
    print(os.path.split(path))

    #分割文件名和扩展名
    print(u"文件名扩展名： ",end="")
    print(os.path.splitext(path))

    #获取文件名
    print(u"获取文件名：", end="")
    print(os.path.basename(path))

    #获取文件所在目录
    print(u"文件所在目录：%s" % os.path.dirname(path))


