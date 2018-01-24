#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/15 22:32
# @Author  : caijiangchun
# @Site    : 
# @File    : lesson12.py
# @Software: PyCharm
import configparser
if __name__ == "__main__":
    #先创建一个对象
    config = configparser.ConfigParser()
    config.add_section(u"中国")

    #在新增的section下，增加key-value值
    config.set(u"中国", u"广东", u"广州")
    config.set(u"中国", u"广西", u"南宁")

    config.add_section(u"美国")

    #写入文件
    with open("iniconfig.ini",'w',encoding="utf-8") as configfile:
        config.write(configfile)

    print("*********************************************************")

    #把刚才创建的ini文件读出来
    with open("iniconfig.ini", "r", encoding="utf-8") as configtext:
        config.read(configtext)

    #获取所有的sections
    sections = config.sections()
    print(sections)

    #获取所有sections下的option
    for sec in sections:
        option = config.options(sec)
        print(option)

    #根据sections和options获取对应的value值
    for sec in sections:
        for option in config.options(sec):
            print("[%s] %s=%s " % (sec, option, config.get(sec, option)))

