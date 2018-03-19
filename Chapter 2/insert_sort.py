# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 21:56:29 2018

@author: wuxin
"""

def insert_sort(nums):
    if len(nums) < 2:
        return nums
    else:
        for i in range(1, len(nums)):
            key = nums[i] #初始化。在运行时会发生变化
            j = i - 1 # 初始化。在运行时会发生变化
            while j >= 0 and nums[j] > key:
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = key                
        return nums
    
nums = [5, 2, 4, 6, 1, 3]
result = insert_sort(nums)
print(result)