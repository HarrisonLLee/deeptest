#!/usr/bin/env python
# encoding: utf-8
import configparser
'''
通过Python的ConfigParser模块来对ini 文件进行读写操作：
ConfigParser：
读取：
read(filename):读取ini文件的内容；
sections():获取所有的section,并以列表的形式返回；
options(sections):获取指定section的所有option；
get(section,option)获取section中的option的值，返回为string类型：
'''
#写入：
#set(section,option,value)对section中的option进行更新

#先创建一个对象：
config = configparser.ConfigParser()

#先写入机组数据增加一个section:
config.add_section(u'Person')

#在新增加的section下增加key-value键值对：
config.set(u'Person',u'name',u'zhangsan')
config.set(u'Person',u'age',u'28')
config.set(u'Person',u'sex',u'F')

#在新增一个section,但不加key-value键值对
config.add_section(u'python')

#写入文件：
with open(r'iniConfig.ini','w') as configfile:
	config.write(configfile)

#下面开始我们来把刚才的ini文件读出来看看
config.read('iniConfig.ini')
#获取它的section
sections = config.sections()
print sections

#获取section下所有的options:
for sec in sections:
	options = config.options(sec)
	print (options)


#根据section和options获取对应的value值：
for sec in sections:
	for option in config.options(sec):
		print ('[%s] %s=%s'%(sec,option,config.get(sec,option)))

