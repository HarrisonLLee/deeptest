# coding=utf-8

import  sys

# import  os
# import requests
# print(os.getcwd())

# r = requests.get("https://www.baidu.com")
# print (r.url)
# print(r.encoding)
# print(r.text)
# 数据类型 字符串 单引号、双引号、三引号
# print('hello world')
# print('''hello world
# the sencond''')
# # format 的使用
# age = 3
# name = "Tom"
# print("{0} was {1} years old".format(name,age))
# print(name  +  " was "  +  str(age)  +  " years old")
# # 字面常量
# a = 3
# b = 4
# c = 5.66
# d = 8.0
# e = complex(c,d)
# f = complex(float(a),float(b))
#
# print("a is type:",type(a))
# print("c is type",type(c))
# print("e is type",type(e))
#
# print(sys.float_info)
#
# print("黄\n多个")
#
# list = [1,3,5,7]
# print(list)
# print('list:'+  str(list))
# 函数
# def say_hi():
#     print("hi!")
#
# def print_sum_two(a,b):
#     c = a + b
#     print(c)
#
# def hello_some(str):
#     print("hello"+ str + "!")
#
# def repeat_str(str,times = 1):
#     repeated_strs = str*times
#     return repeated_strs



# print_sum_two(3,6)
# hello_some(" China ")
# c = repeat_str(" happy birthday ! ",2)
# print(c)

# def func(a,b=4,c=8):
#     print('a is',a,'and b is',b,'and c is',c)
# func(13,17)
# func(125,c=10)

# number = 59
# guess = int(input('enter an integer:'))
# if guess == number:
#     print("Bingo!,you guessed it right.")
# elif guess < number:
#     print("no,the number is highter than that")
# else:
#     print("no,the number is a lower than that5")
#
# # for i in range(1,10):
#     print(i)
# else:
#     print('The for Loop is over')

# a_list = [1,3,5,7,9]
# for i in a_list:
#     print(i)
#
# a_tuple = (1,3,5,7,9)
# for i in a_tuple:
#     print(i)
#
# a_dict = {"Tom":"123",'Jerry':"222","Cathy":"333"}
# for ele in a_dict:
#     print(ele)
#     # print(a_dict[ele])
#
# for key ,elem in a_dict.items():
#     print(key,elem)

# while 循环 比大小

# number = 59
# guess_flag = False
#
# while guess_flag == False:
#     guess = int(input('enter an integer:'))
#     if guess == number:
#         guess_flag = True
#
#     elif guess > number:
#      print("no,the number is highter than that")
#
#     else:
#       print("no,the number is a lower than that!")
#
# print("Bingo!,you guessed it right.")
# print('Done')


# while range 3次输入的机会
# number = 59
# num_chances = 3
# print("you have only 3 chances to guess")
#
# for i in range(1,num_chances + 1):
#     print("chance " + str(i))
#     guess = int(input('enter an integer:'))
#     if guess == number:
#         print("Bingo!,you guessed it right.")
#         break
#
#     elif guess < number:
#      print("no,the number is highter than that,keep guessing, you have "+ str(num_chances - i) + ' chances left')
#
#     else:
#       print("no,the number is a lower than that!you have "+ str(num_chances - i) + ' chances left')




# break ,continue,Pass使用
# 读文件 写文件
sentences = '''i love python
besatskglasjg
skdlasdk
'''
# 写文件
# f = open("sentences.txt",'w')
# f.write(sentences)
# 读文件
# f = open('sentences.txt')
# while True:
#     line = f.readline()
#     if len(line) == 0:
#         break
#     print(line)
# 错误与异常1、语法错误 syntax errors2、异常 exceptions


