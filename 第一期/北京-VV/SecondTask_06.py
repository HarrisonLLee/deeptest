# -*- coding:utf-8 -*-

__author__ = 'VV'

# import date and time

from datetime import date, time, datetime

if __name__ == '__main__':
    # get date of today
    today = date.today()
    print(f"Today is {today}")

    # split year, moth and day
    print(f"Today is {today.day} {today.month} {today.year}")

    # what day is today
    # day       number
    # Monday    0
    # Tuesday   1
    # Wednesday 2
    # Thursday  3
    # Friday    4
    # Saturday  5
    # Sunday    6
    # weekday will get the number
    weekday_num = today.weekday()
    print(f"Today is {weekday_num}")

    # print specific weekday
    weekdays = ("Moday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    print(f"Today is {weekdays[weekday_num]}")
    print("-" * 30)

    # what's time now
    today_now = datetime.now()
    print(f"Now is {today_now}")

    # create a time
    t = time(hour=12, minute=20, second=30, microsecond=200)
    print(f"We create the time is {t}")

    # create a date
    d = datetime(year=2008, month=8, day=8, hour=8, minute=8, second=8)
    print(f"We create the date is {d}")
    print("-" * 30)

import time

if __name__ == '__main__':
    # time.strftime(format[, t])

    # default format time
    localtime = time.asctime(time.localtime())
    print(f"The default time format of current time is: {localtime}")

    # format it to year-month-day hour:minute:second weekday
    print("24hrs full format: ", time.strftime("%Y-%m-%d %H:%M:%S %A", time.localtime()))
    print("12hrs full format: ", time.strftime("%Y-%m-%d %I:%M:%S %a", time.localtime()))

    # time with a.m. or p.m.
    print("24 hrs full time with a.m. or p.m.: ",time.strftime("%Y-%m-%d %H:%M:%S %p %A", time.localtime()))

    # time with timezone
    print("Time with timezone: ", time.strftime("%Y-%m-%d %H:%M:%S %p %A %z", time.localtime()))

    # random format
    print("Random format: ", time.strftime("%A %Y-%d-%m %p %H:%M:%S %z", time.localtime()))
    print("-" * 30)


import json

if __name__ == '__main__':
    print("json turn to dict")

    json_str = '{"name": "KYYC", "url": "www.testingunion.com", "id": "DeepTest"}'

    # origin type
    print("Origin type: ", type(json_str))

    # turn to dict
    # will be turn to dict type
    json_dict = json.loads(json_str)
    print("The type after turn to dict: ", type(json_dict))

    # traverse dict
    for (k, v) in json_dict.items():
        print(k, ":", v)
    print("-" * 30)


if __name__ == '__main__':
    print("Dict turn to json")

    json_dict = {
        "name": "KYYC",
        "url": "www.testingunion.com",
        "id": "DeepTest"
    }

    print("Origin type: ", type(json_dict))

    # dict turn to json
    # will be turn to string type
    json_str = json.dumps(json_dict)

    print("The type after turn to json: ", type(json_str))
    print(json_str)
    print("-" * 30)


if __name__ == '__main__':
    print("Senior instance of json")
    json_demo = """
        {
            "weixin": [
                {
                    "name": "KYYC",
                    "uid": "DeepTest",
                    "desc": "Share with testing tech"
                },
                {
                    "name": "KYYC_demo",
                    "uid": "DeepTest_demo",
                    "desc": "Share with testing tech_demo"
                }
            ],
            "web": [
                {
                    "url1": "www.testingunion.com",
                    "name": "KYYCSQ",
                    "desc": "Share with testing tech"
                },
                {
                    "url1": "www.testingunion.com_demo",
                    "name": "KYYCSQ_demo",
                    "desc": "Share with testing tech_demo"
                }
            ]
        }
    """

    # turn json to dict
    json_dict = json.loads(json_demo)

    # traverse dict
    for (k, v) in json_dict.items():
        # print first layer, k is weixin web; v is their values, the datas in []
        print(k, ":", v)
        for data in v:
            # traverse table
            # v is []
            for (data_k, data_v) in data.items():
                # every data is the [] in the dict
                # traverse dict of table
                print ("    ", data_k, ":", data_v)
    print("-" * 30)


try:
    # you can use API (xml.etree.cElementTree) of C language if you want to make speed up
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

if __name__ == '__main__':
    print("parse local data_demo.xml file")
    # load xml file
    tree = ET.parse("data_demo.xml")

    # get root and print
    root = tree.getroot()
    print(root.tag)

    # traverse country name's attribute
    for child in root:
        print(child.tag, "name: ", child.attrib["name"])

    # traverse rank node
    # search node by iter
    # print node tag and text
    print("Search target node by iter")
    for rank in root.iter("rank"):
        print(rank.tag, " - ", rank.text)

    # traverse rank node by another way
    # search node by findall and find
    # print node tag and text
    # NOTE: findall only can search from the child node of current node
    print("Search target node by findall")
    # find all country node by findall to traverse
    for country in root.findall("country"):
        # print(country)
        # find rank from country node by find function
        rank = country.find("rank")
        print(rank.tag, " - ", rank.text)

    # update all rank text to "KYYC"
    for rank in root.iter("rank"):
        rank.text = "KYYC"
        rank.set('updated', 'yes')

    # traverse and print updated rank
    for rank in root.iter("rank"):
        print(rank.text)

    # add <url>www.testingunion.com</url> node to all countrys
    for country in root.iter("country"):
        # create a node
        url = ET.Element("url")
        # print(url)

        # assign value to url node
        url.text = "www.testingunion.com"

        # append url node to country
        country.append(url)

    # print and check if all the url nodes already added to countrys' node
    for country in root.iter("country"):
        # search url node
        url = country.find("url")

        # print url text
        print(url.text)

    # delete year node
    for country in root.iter("country"):
        year = country.find("year")

        # delete year node if it's exist
        if year is not None:
            print("Deleted a year node")
            country.remove(year)

    # save above update to a new xml data_demo_new.xml
    # open and check the new xml see if all update are updated
    tree.write("data_demo_new.xml", encoding="utf-8")
