# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 16:46:08 2018

@author: wuxin
"""

def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    else:
        middle = int(len(nums)/2)
        left = merge_sort(nums[0: middle])
        right = merge_sort(nums[middle:])
        return merge(left, right)
        
def merge(left, right):
    nums = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            nums.append(left[i])
            i += 1
        else:
            nums.append(right[j])
            j += 1
    if i == len(left):
        for num in right[j:]:
            nums.append(num)
    else:
        for num in left[i:]:
            nums.append(num)
    return nums
            
nums = [5, 2, 4, 7, 1, 3, 2, 6]
result = merge_sort(nums)
print(result)
