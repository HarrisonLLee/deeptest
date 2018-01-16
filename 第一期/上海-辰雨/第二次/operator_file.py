#!/usr/bin/env python
# encoding: utf-8
import os
# 返回完整的路径目录：
print ('获取当前工作目录')
print (os.getcwd())

# 返回的是：
print ('获取当前目录')
print (os.curdir)

# 创建目录，创建目录必须是存在的，否则抛出异常：
os.mkdir('test_mk1')

# 重命名目录：
os.rename('test_mk1', 'test_mk2')


# 将改变至c盘:
print ('改变工作目录到dirname')
os.chdir('c:')
print (os.getcwd())

# path模块常用的方法：

# 先床实话档期那文件全路径变量：
path = __file__
print ('当前文件全路径为：%s' % path)

# 是目录则返回True,否则返回False:
print ('目录判断：%s'%os.path.isfile(path))

# 判断目录或文件是否存在：
print ('目录/文件存在：%s' % os.path.exists(path))

# 获取文件大小,若目标为目录则返回0
print ('文件大小:%s'%os.path.getsize(path))


# 获取文件的绝对路径：
print ('文件绝对路径：%s' %os.path.abspath(path))

# 将目录路径规范化，即更规范路径表达式，跨平台标识：
print ('规范化路径：%s' %os.path.normpath(path))


# 将文件名和目录分隔：
# 若传入的是目录，则将最后的目录名作为文件名分隔：
print ('目录和文件名分隔：')
print (os.path.split(path))

# 分离文件名和扩展名：
print ('文件名和扩展名分离：')
print (os.path.splitext(path))

# 获取文件名
print ('文件名为：%s' % os.path.basename(path))

# 获取文件所在的目录:
print ('文件目录为：%s' % (os.path.dirname(path)))

# os模块所提供的目录遍历方法：walk
# wallk返回值说明：返回值为一个迭代器对象，它的每个部分包含一个元组，

def walk_dir(target_dir):
    # root：	当前根目录；
    # dirs: 	root下的子目录
    # files:	root
    walk_result = os.walk(target_dir)

    for root, dirs, files in walk_result:
        print ('-', root)

        # 遍历当前子目录：
        for name in dirs:
            print ('--', name)

        # 遍历当前目录的子文件：
        for name in files:
            print ('--', name)


if __name__ == "__main__":
    target_dir = os.curdir
    walk_dir(target_dir)


