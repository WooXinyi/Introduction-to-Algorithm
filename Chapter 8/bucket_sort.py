# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 11:12:51 2018

@author: Administrator
"""
import random

def Bucket_sort(nums):
    B = [[] for _ in range(10)]
    C = []
    for i in range(len(nums)):
        B[int(nums[i]*10)].append(nums[i])
    for i in range(len(B)):
        Insert_sort(B[i])
    for i in range(len(B)):
        C += B[i]
    return C

def Insert_sort(nums):
    if len(nums) < 2:
        return nums
    else:
        for i in range(1, len(nums)):
            j = i - 1
            key = nums[i]
            while j >= 0 and nums[j] > key:
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = key
                
if __name__ == '__main__':
    nums = [random.random() for _ in range(100)]
    result = Bucket_sort(nums)
    print(result)