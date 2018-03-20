# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 21:20:33 2018

@author: Administrator
"""
import random

def radix_sort(nums, radix):
    for i in range(radix):
        #S是有10个bucket的数组
        S = [[] for _ in range(10)]
        for num in nums:
            S[int(num/(10**i))%10].append(num)
        nums = [num for bucket in S for num in bucket]
    return nums

if __name__ == '__main__':
    nums = [random.randint(0, 999999) for _ in range(10)]
    nums = radix_sort(nums, 10)
    print(nums)