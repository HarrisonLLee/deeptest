#coding = utf-8

__author__ = 'Aimee'

import os

if __name__=="__main__":
    #返回完整的路径目录
    print("获取当前工作目录")
    print(os.getcwd())

    #返回的是:.
    print("获取当前目录")
    print(os.curdir)

    #创建目录
    # os.mkdir("test_mkl")
    # os.rename("test_mkl","test_mk2")
    # os.removedirs("test_mk2")

    os.chdir("c:")
    print(os.getcwd())
























#
# if __name__== "__main__":
#
#     #先初始化当前文件全路径变量
#
#     path = __file__
#     print("当前文件全路径为： %s" %path)
#
#
#     #是目录则返回True，否则返回False
#     print("文件判断：%s" % os.path.isfile(path))
#
#     #判断目录或文件是否存在
#
#     print("目录/文件存在：%s" % os.path.exists(path))
#
#     #获取文件大小，若目标为目录则返回0
#     print("文件大小：%s" % os.path.getmtime(path))
#
#     #获取文件的绝对路径
#     print("文件绝对路径：%s" % os.path.abspath(path))
#
#     #将目标路径规范化，即更规范的路径表达方式，跨平台标识
#     print("规范路径：%s" % os.path.normpath(path))
#
#     #将文件名和目录分割
#     print("目录和文件名分割：",end="" )
#     print(os.path.splitext(path))
#
#     #获取文件名
#     print("文件名：%s" % os.path.basename(path))
#
#     #获取文件所在目录
#     print("文件目录为：%s" % os.path.dirname(path))



    #目录遍历  walk

# import os
#
# def walk_dir(target_dir):
#     #root 当前根目录
#     #dirs ：root下的子目录
#     #files：root下的子文件
#     walk_result = os.walk(target_dir)
#     print(type(walk_result))
#
#     for root,dirs,files in walk_result:
#         print("_",root)
#
#         for name in dirs:
#             print("--",name)
#
#         for name in files:
#             print("---",name)
#
#
# if __name__ == "__main__":
#
#     target_dir = os.curdir
#     walk_dir(target_dir)
