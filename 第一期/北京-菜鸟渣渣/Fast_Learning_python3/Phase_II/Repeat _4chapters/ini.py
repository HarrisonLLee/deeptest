# coding=utf -8

import configparser

'''

ConfigParser

读取

read(filename) 读取ini文件内容
sections() 获取所有的section，并以列表的形式返回
options(sections) 获取指定section的所有option
get(section,option) 获取section中option的值，返回为string类型

写入

set( section, option, value) 对section中的option进行更新
'''

config = configparser.ConfigParser()

config.add_section("OPEN_TEST")

config.set("OPEN_TEST", "username", "root")
config.set("OPEN_TEST", "password", "123456")
config.set("OPEN_TEST", "ps", "note")

config.add_section("STACK_FLOW")

with open("iniConfig.ini", "w") as  configfile:
    config.write(configfile)

read_ok = config.read("iniConfig.ini")
print(read_ok)

sections = config.sections()
print(sections)
options = config.options(sections[0])
print(options)

username = config.get("OPEN_TEST", "username")
print(username)
