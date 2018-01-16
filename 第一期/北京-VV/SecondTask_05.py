# -*- coding:utf-8 -*-

__author__ = 'VV'
'''
# def a class
class DemoClass():
    """docstring for DemoClass."""
    def __init__(self):
        print("init")

    def output(self, text):
        # output text to console
        print(text)

    def output_none(self):
        # function without parameter
        print("I cannot income parameter")

# inheritance a closs
class ChildDemoClass(DemoClass):
    """docstring for ChildDemoClass."""
    def __init__(self):
        print("I'm a chila class")

    # re-write output_none
    def output_none(self):
        print("I'm the function of child class that cannot income parameter")

if __name__ == '__main__':
    # create a object
    demo_obj = DemoClass()

    # call output
    demo_obj.output("I'm parameter")

    # call output_none
    demo_obj.output_none()

    print("------------------------------")
    # create object of child class
    child_demo_obj = ChildDemoClass()

    # call output of parent class
    child_demo_obj.output("I'm a parameter")

    # call output_none of child class
    child_demo_obj.output_none()

import sys

if __name__ == '__main__':
    seq_tuple = (1, 2, 3, 4, 5)

    # create a iterator
    seq_it = iter(seq_tuple)

    # locate and print first element
    print(f"First element: {next(seq_it)}")

    # locate and print second element
    print(f"Second element: {next(seq_it)}")

    # locate and print third element
    print(f"Third element: {next(seq_it)}")

    # traverse iter by for loop
    print("\nfor loop traverse iter: ")
    for_it = iter(seq_tuple)
    for x in for_it:
        print(x, end=' ')

    # traverse iter by while and next
    print("\n\nwhile & next traverse iter: ")
    while_it = iter(seq_tuple)
    while True:
        try:
            print(next(while_it))
        except StopAsyncIteration:
            sys.exit()

# function of generator
# Fibonacci numbers
def fibonacci(n):
    # init var
    a, b, count = 0, 1, 0

    while True:
        if count > n:
            return

        yield a

        a, b = b, a + b
        count = count + 1

if __name__ == '__main__':
    # init generator, create a generator function
    f = fibonacci(20)

    while True:
        try:
            print(next(f), end=' ')
        except StopAsyncIteration:
            sys.exit(0)
print("\n\n")

import configparser

if __name__ == '__main__':
    # create a object
    config = configparser.ConfigParser()

    # write some groups of datas
    # create a section firstly
    config.add_section("ukulele")

    # add key-value under section
    config.set("ukulele", "u", "uku")
    config.set("ukulele", "d", "dance")
    config.set("ukulele", "o", "oilpainting")

    # create another section, but dont add key-value for it
    config.add_section("I'm so lonly")
    # write file
    with open('iniConfig.ini', 'w') as configfile:
        config.write(configfile)

    #######################################

    # read the above ini file
    config.read("iniConfig.ini")
    # get all section
    sections = config.sections()
    print(sections)

    # get all options under section
    for sec in sections:
        options = config.options(sec)
        print(options)

    # get value from sections and options
    for sec in sections:
        for option in config.options(sec):
            print(f"[{sec}] {options}={config.get(sec, option)}")

import os

if __name__ == '__main__':
    # return full path
    print("Get current work path")
    print(os.getcwd())

    # return '.'
    print("Get current path")
    print(os.curdir)

    # create folder
    # target should not exist or raise a exception
    os.mkdir("test_mk1")

    # rename folder
    os.rename("test_mk1", "test_mk2")

    # delete specific folder
    # notice that the delete folder can not include sub-folder and files
    # target folder should be existed or raise a exception
    os.removedirs("test_mk2")

    # jump to C root
    print("Jump to dirname")
    os.chdir("c:")
    print(os.getcwd())
'''
import os

if __name__ == '__main__':

    # ini full path for current file
    path = __file__
    print(f"Current full path: {path}")

    # return True if it's a folder, or return False
    print(f"Is it a folder: {os.path.isdir(path)}")

    # return True if it's a file, or return False
    print(f"Is it a file: {os.path.isfile(path)}")

    # if folder or file exist
    print(f"Is it folder or file exist: {os.path.exists(path)}")

    # get file size, return 0 if it's a folder
    print(f"File size: {os.path.getsize(path)}")

    # get absolute path
    print(f"File absolute path: {os.path.abspath(path)}")

    # normal path
    print("Normal path: {os.path.normpath(path)}")

    # split file name and path
    print("Split file name and path: ", end="")
    print(os.path.split(path))

    # split file name and extension name
    print("Split file name and extension name: ", end="")
    print(os.path.splitext(path))

    # get file name
    print(f"File name is: {os.path.basename(path)}")

    # get path of file
    print(f"File path is: {os.path.dirname(path)}")
