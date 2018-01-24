#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/17 21:28
# @Author  : caijiangchun
# @Site    : 
# @File    : lesson16.py
# @Software: PyCharm
import json
def json_dictionary():
    #json转成dict
    json_str = '{"name": "westwind","url": "https://github.com//caijc00","id": "caijc00"}'
    print(type(json_str))
    json_dict = json.loads(json_str)
    print(json_dict)
    print(type(json_dict))

    #遍历字典
    for (k, v) in json_dict.items():
        print(k ,":" ,v)
def dict_json():
    dict_jsonone = {
        "name": "westwind",
        "url": "https://github.com//caijc00",
        "id": "caijc00",
    }
    print(type(dict_jsonone))
    dict_json_two = json.dumps(dict_jsonone)
    print(dict_json_two)
    print(type(dict_json_two))

if __name__ == "__main__":
    json_dictionary()
    dict_json()
