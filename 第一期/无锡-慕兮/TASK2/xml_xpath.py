# -*- coding:utf-8 -*-

__author__ = "Lakisha"

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

if __name__ == "__main__":
    print("Element Tree XPath特性支持示例")

    #加载xml文件
    etree = ET.parse("test.xml")

    #获取根节点, 并打印节点文本data
    root = etree.getroot()

    #选择当前节点，返回当前节点对象列表
    print("当前节点")
    data = root.findall(".")
    for d in data:
        print(d.tag)

    #选择所有country节点
    print("选择所有country节点的方法一")
    countrys = root.findall(".//country")
    for country in countrys:
        print(country.tag, "-", country.attrib["name"])

    print("选择所有country节点的方法二")
    countrys = root.findall("country")
    for country in countrys:
        print(country.tag, "-", country.attrib["name"])

    print("选择name属性为Panama的country的节点")
    countrys = root.findall(".//*[@name='Panama']")
    for contry in countrys:
        print(country.tag, "-", country.attrib["name"])

    print("选择name属性为Panama的country的year节点")
    years = root.findall(".//country[@name='Panama']/year")
    for year in years:
        print(year.text)

    #通过索引来选择country节点，选择第一个country节点
    #注意索引从1开始
    country = root.findall(".//country[1]")
    for c in country:
        print(c.tag, "~", c.attrib["name"])

    #通过子节点的文本内容来选择节点
    #选择子节点gdppc且其目录为59900 的country节点
    #庆祝以这返回的是gdppc的父节点
    print("通过子节点的文本内容来选择节点")
    gdppc = root.findall(".//*[gdppc='59900']")
    for gd in gdppc:
        print(gd.tag)