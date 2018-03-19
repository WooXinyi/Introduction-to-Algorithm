# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 11:38:53 2018

@author: Administrator
"""
import random

def Quick_sort(A, start, end):
    if start < end:
        #divide = Partition(A, start, end)
        divide = Random_Partition(A, start, end)
        Quick_sort(A, start, divide-1)
        Quick_sort(A, divide+1, end)
        
def Partition(A, start, end):
    flag = A[end]
    small = start - 1
    for large in range(start, end):
        if A[large] <= flag:
            small += 1
            A[small], A[large] = A[large], A[small]
    A[small+1], A[end] = A[end], A[small+1]
    return small+1

def Random_Partition(A, start, end):
    i = random.randint(start, end)
    A[end], A[i] = A[i], A[end]
    return Partition(A, start, end)

#Nice method
def Quick_sort_II(A):
    if len(A) < 1:
        return A
    return Quick_sort_II([small for small in A[1:] if small<=A[0]]) + \
                        A[0: 1] + Quick_sort_II([large for large in A[1:] if large>A[-1]])

A = [5, 4, 3, 2, 1]
Quick_sort(A, 0, len(A)-1)
print(A)        