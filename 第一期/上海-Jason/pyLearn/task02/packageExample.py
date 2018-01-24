# _*_ coding : utf-8 _*_
__author__ = "Jason"

'''
包
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
    
    ...
    
'''
