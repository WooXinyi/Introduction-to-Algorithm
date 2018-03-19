# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 17:17:52 2018

@author: wuxin
"""

#Method one
def Find_max_crossing_subarray(nums, low, middle, high):
    left_sum = float('-inf')
    sum = 0
    for i in range(middle, low-1, -1):
        sum += nums[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    right_sum = float('-inf')
    sum = 0
    for j in range(middle+1, high+1):
        sum += nums[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
    return max_left, max_right, left_sum+right_sum


def Find_maximum_subarray(nums, low, high):
    if low == high:
        return low, high, nums[low]
    else:
        mid = int((low+high)/2)
        left_low, left_high, left_sum = \
        Find_maximum_subarray(nums, low, mid)
        right_low, right_high, right_sum = \
        Find_maximum_subarray(nums, mid+1, high)
        cross_low, cross_high, cross_sum = \
        Find_max_crossing_subarray(nums, low, mid, high)
    if left_sum > right_sum and left_sum > cross_sum:
        return left_low, left_high, left_sum
    if right_sum > left_sum and right_sum > cross_sum:
        return right_low, right_high, right_sum
    if cross_sum > left_sum and cross_sum > right_sum:
        return cross_low, cross_high, cross_sum
    
#Method two
def Find_maximum_subarray_II(nums):
    max_sum = cur_sum = 0
    for num in nums:
        cur_sum = max(cur_sum+num, num)
        max_sum = max(cur_sum, max_sum)
    return max_sum
    
nums = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
max_sum = Find_maximum_subarray_II(nums)
print(max_sum)