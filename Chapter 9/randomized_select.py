# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 16:43:21 2018

@author: Administrator
"""

import random

def Randomized_select(nums, start, end, key):
    if start == end:
        return nums[start]
    divide = Randomized_partition(nums, start, end)
    num = divide - start + 1
    if num == key:
        return nums[num]
    elif key < num:
        return Randomized_select(nums, start, divide-1, key)
    else:
        return Randomized_select(nums, divide+1, end, key)
    
def Randomized_partition(nums, start, end):
    rand = random.randint(start, end)
    nums[rand], nums[end] = nums[end], nums[rand]
    return Partition(nums, start, end)

def Partition(nums, start, end):
    flag = nums[end]
    small = start - 1
    for large in range(start, end):
        if nums[large] < flag:
            small += 1
            nums[small], nums[large] = nums[large], nums[small]
    nums[small+1], nums[end] = nums[end], nums[small+1]
    return small+1

nums = [random.randint(0, 100) for _ in range(10)]
num = Randomized_select(nums, 0, len(nums)-1, 5)
print(nums)
print(num)