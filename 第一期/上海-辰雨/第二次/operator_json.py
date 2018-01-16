#!/usr/bin/env python
# encoding: utf-8
import json
'''
json 常用函数：
json.dumps():将python对象编码成json字符串，返回json串
json.loads():将已经编码的json字符串解码为python对象，返回python对应的数据类型
'''
print ('json转dict')
json_str = '{"name":"开源优测", "url":"www.testingunion.com","id":"DeepTest"}'

#原类型：
print ('原类型：',type(json_str))

#转成dict 对象，会被转换成字典类型
json_dict = json.loads(json_str)

print ('转换后的类型：',type(json_dict))

#遍历字典：
for (k,v) in json_dict.items():
	print (k,":",v)


#dict字典转成json串示例：
print ('字典转json串')

json_dict = {

	'name':'zhangsan',
	'age':'28',
	'sex':'F'
}

print ('原类型：',type(json_dict))

#将字典转换成json串,会被转换成字符串类型：
json_str = json.dumps(json_dict)

print ('转换后的类型：',type(json_str))
print (json_str)



print ('json串解析高级实例')
json_demo = """
        {
            "weixin": [
                {
                    "name": "开源优测",
                    "uid": "DeepTest",
                    "desc": "分享开源测试技术"
                },
                {
                    "name": "开源优测_demo",
                    "uid": "DeepTest_demo",
                    "desc": "分享开源测试技术_demo"
                }
            ],
            "web": [
                {
                    "url": "www.testingunion.com",
                    "name": "开源优测社区",
                    "desc": "分享各类开源测试技巧"
                },
                {
                    "url": "www.testingunion.com_demo",
                    "name": "开源优测社区_demo",
                    "desc": "分享各类开源测试技巧_demo"
                }
            ]
        }
    """

#将json串转换成字典：
json_dict = json.loads(json_demo)

#遍历字典
for (k,v) in json_dict.items():
	#输出第一层级,k veixin veb；v 为其对应的列表即[]中的数据
	print (k,':',v)
	for data in v:
		#遍历字典
		#v 为 []
		for (data_k,data_v) in data.items():
			#每个data为[]中的一个字典
			#遍历列表中的字典
			print (' ',data_k,":",data_v)

