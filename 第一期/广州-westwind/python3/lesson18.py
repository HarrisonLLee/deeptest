#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/19 16:08
# @Author  : caijiangchun
# @Site    : 
# @File    : lesson18.py
# @Software: PyCharm
try:
    # 若想加快速度，可以使用C语言编译的API xml.etree.cElementTree。
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

def demo_xml():
    #加载xml文件
    tree = ET.parse("data_demo.xml")

    #获取根节点，并打印节点文本：data
    root = tree.getroot()
    print(root.tag)

    # 遍历输出country及其name属性
    for child in root:
        print(child.tag, "name:", child.attrib["name"])

    # 遍历rank节点
    # 我们借助iter迭代器来进行全迭代查找感兴趣的节点
    # 输出节点tag及其文本
    print(u"使用iter迭代器查找目标节点")
    for rank in root.iter("rank"):
        print(rank.tag, "-", rank.text)

    # 换一种方式来遍历rank节点
    # 我们借助findall和find方法来查找感兴趣的节点
    # 输出节点tag及其文本
    # 注意：findall只能查找从当前节点的子节点查找目标节点
    print(u"使用findall查找目标节点")
    for country in root.findall("country"):
        rank = country.find("rank")
        print(rank.tag, "-", rank.text)

    # 把所有的rank的文本都修改为： 开源优测
    for rank in root.iter("rank"):
        rank.text = "开源优测"
        rank.set("updated","yes")
    # 把修改后的rank的文本重新遍历打印出来，这时应该打印出： 开源优测
    for rank in root.iter("rank"):
        print(rank.text)

    #给所有的country新增一个<url>www.testengineer.com<url>节点
    for country in root.iter("country"):
        url = ET.Element("url")
        url.text = "www.testengineer.com"

        country.append(url)

    # 打印下整个xml出来看看是不是所有country节点都新增了一个url节点
    for country in root.iter("country"):
        url = country.find("url")

        print(url.text)


    for country in root.iter("country"):
        year = country.find("year")

        if year is not None:
            print("删除了个year节点")
            country.remove(year)


if __name__ == "__main__":
    demo_xml()