# _*_ coding:utf-8 _*_
__author__ ="Jason"
import sys,re
from util import *
print('<html><head><title>simpleMarkup</title><body>')

title = True
for block in blocks(sys.stdin):
    block = re.sub(r'\*(.+?)\*',r'<em>\1</em>',block)
    if title:
        print('<h1>')
        print(block)
        print('</h1>')
        title = False
    else:
        print('<p>')
        print(block)
        print('</p>')
print('</body></html>')