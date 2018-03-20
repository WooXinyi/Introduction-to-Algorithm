# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 16:03:05 2018

@author: Administrator
"""
import random

def Minimum_and_maximum(nums):
    minimum = maximum = 0 #初始化
    i = 0 #初始化
    if len(nums) % 2 == 0:
        minimum = min(nums[0], nums[1])
        maximum = max(nums[0], nums[1])
        i = 2
    if len(nums) % 2 == 1:
        minimum = maximum = nums[0]
        i = 1
    while i+1<len(nums):
            minimum = min(minimum, min(nums[i], nums[i+1]))
            maximum = max(maximum, max(nums[i], nums[i+1]))
            i += 2
    return minimum, maximum

nums = [random.randint(0, 100) for _ in range(10)]
minimum, maximum = Minimum_and_maximum(nums)
print(nums)
print(minimum, maximum)