#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/16 23:47
# @Author  : caijiangchun
# @Site    : 
# @File    : lesson14.py
# @Software: PyCharm
import os

def walk_dir(target_dir):

    walk_result = os.walk(target_dir)
    # root 当前根目录
    # dirs ：root下的子目录
    # files：root下的子文件
    print(walk_result)
    print(type(walk_result))

    for root,dirs,files in walk_result:
        print("-", root)

        # 遍历当前子目录
        for name in dirs:
            print("--", name)

        # 遍历当前目录的子文件
        for name in files:
            print("--", name)

if __name__ == "__main__":
    target_dir = os.curdir
    walk_dir(target_dir)