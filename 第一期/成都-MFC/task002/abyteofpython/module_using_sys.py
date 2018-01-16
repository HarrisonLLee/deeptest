# -*- coding:utf-8 -*-


# A Byte of Python -- P68 -- Python3


import sys
import os

print('The command line arguments are:')
for i in sys.argv:
    print(i)

print('\n\nThe  PYTHONPATH is', sys.path, '\n')

# 查看程序目前所处在的目录
print("-------------------")
print("当前目录是:")
print(os.getcwd())