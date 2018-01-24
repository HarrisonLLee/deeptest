# -*- coding:utf-8 -*-
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return print(sum)
calc(1,2)
calc()

#已有list/tuple
nums = [1,2,3]
calc(nums[0],nums[1],nums[2])
