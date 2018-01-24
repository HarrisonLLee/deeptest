# -*- coding:utf-8 -*-
# __author__ = 'PantaQ'

from selenium import webdriver
from time import sleep
import threading

web_list = ['http://www.hao123.com', 'http://www.baidu.com', 'http://www.163.com']

def open_brower(website):
    browser = webdriver.Firefox()
    browser.get(website)
    a = input("input")
    sleep(int(a))
    browser.quit()

brower_threads = []
for i in range(3):
    brower_thread = threading.Thread(target=open_brower, args=(web_list[i],))
    brower_threads.append(brower_thread)
    brower_thread.start()

for brower_thread in brower_threads:
    brower_thread.join()

print('all done')
print('开源优测')