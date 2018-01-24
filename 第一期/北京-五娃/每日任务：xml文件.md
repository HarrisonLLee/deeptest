
```
# __author__ ='wuwa'
# -*- coding: utf-8 -*-

'''
通过ElementTree解析XML
官方手册：https://docs.python.org/3/library/xml.etree.elementtree.html
通过对一个xml文件进行 增、删、改、查操作
<tag> 标签
<country name="attribute"> 在Tag中可能存在的name/value对
<data> 数据
set 设置某个element的key的值为xxx
remove 删除某节点
write 更新xml文件
'''

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

# 通过字符串方式获取xml文件内容,通过该方式获取的内容无根节点
#root = ET.fromstring(open('country_data.xml').read())

#通过加载指定文件的方式获取xml内容,该方式存在根节点
tree = ET.parse('country_data.xml')

# 获取根节点
root = tree.getroot()
print(root.tag)

# 遍历根节点下的子节点
for child in root:
    print(child.tag, 'name:', child.attrib['name'])

# 通过迭代器查找目标节点“neighbor”
for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)
# 通过findall只能查找从当前节点的子节点查找目标节点，find只要找到一个元素就返回
for country in root.findall('country'):
    # 在country节点下找到rank，并打印其文本内容
    rank = country.find("rank")
    # 打印rank的文本内容
    print(rank.tag, rank.text)

# 修改所有rank的文本的值,通过set的updated
for rank in root.iter("rank"):
    rank.text = "python3"
    rank.set('updated', 'yes')

# 打印修改后的rank的值
for rank in root.iter("rank"):
    print(rank.text)

# 删除节点rank的文本值大约50的country节点
for country in root.findall('country'):
    if int(country.find('year').text) > 2011:
        root.remove(country)

# 将改变内容写到xml文件中
tree.write("data_demo_new.xml", encoding="utf-8")

```




```
<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>
```
