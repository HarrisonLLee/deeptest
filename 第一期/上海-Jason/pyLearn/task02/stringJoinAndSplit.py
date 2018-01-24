# _*_ coding : utf-8 _*_
__author__ = 'Jason_copy'

if __name__ == "__main__":
    t = ('1','2','3','4','5','a','b','c','efg')

    #用“-”将t中的元素合并成一个字符串
    str_demo = '-'.join(t)
    print(str_demo)#结果为1-2-3-4-5-a-b-c-efg

    #将str_demo用“-”分割
    str_set = str_demo.split('-')
    print(str_set)#结果为['1', '2', '3', '4', '5', 'a', 'b', 'c', 'efg']

    #将t中的元素合并成一个新的字符串
    str_demo = ''.join(t)
    print(str_demo)#结果为12345abcefg