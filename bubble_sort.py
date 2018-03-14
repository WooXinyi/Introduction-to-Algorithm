# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 22:16:24 2018

@author: wuxin
"""

#Method1，最小的沉下去
def bubble_sort(nums):
    for i in range(len(nums)): 
        for j in range(i+1, len(nums)): 
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            print(nums)


#Method 2
'''
def bubble_sort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-1, 0, -1):
            if nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
            print(nums)
'''
                

nums = [5, 2, 4, 7, 1, 3, 2, 6]
bubble_sort(nums)
print(nums)