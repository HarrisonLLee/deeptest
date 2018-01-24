# coding = utf -8

__author__ = 'Aimee'

# INI文件被用来对操作系统或特定程序初始化或进行参数设置。
# 通过 ConfigParser模块来对ini文件进行读写操作

# 读取
# read（filename） 读取nin文件内容
# section（）获取所有的section，并以列表的形式返回
# option（section）获取指定section的所有option
# get（section，option）获取section中opeion的值，返回为string类型

#导入
#set（section，option，value）对section中的option进行更新


import configparser

if __name__ == "__main__":
    #先构建一个对象
    config = configparser.ConfigParser()

    #引入几组数据
    #先新增一个section
    config.add_section("开源优测")
    #在新增的section下加key-value键值对
    config.set("开源优测","love","you")
    config.set("开源优测","love1","her")
    config.set("开源优测","love2","his")

    #再新增一个section但是不加key-value键值对
    config.add_section("我好孤单")
    #写文件
    with open('iniConfig.ini','w') as configfile:
        config.write(configfile)




    #把刚才的ini文件读出来看看
    config.read("iniConfig.ini")
    #获取他的所有section
    sections = config.sections()
    print(sections)

    #获取section下所有的option
    for sec in sections:
        options = config.options(sec)
        print(options)

    #根据section和option获取对应的value值

    for sec in sections:
        for options in  config.options(sec):
            print("[%s] %s %s" % (sec,options,config.get(sec,options)))


