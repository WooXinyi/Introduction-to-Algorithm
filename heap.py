# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 15:38:52 2018

@author: Administrator
"""

def Parent(i):
    return int((i+1)/2)-1

def Left(i):
    return 2 * i + 1

def Right(i):
    return 2 * i + 2

#维护以i节点为根节点的最大堆,length用来调节需要建堆的元素个数
def Max_heapify(A, i, length):
    left = Left(i)
    right = Right(i)
    largest = i
    if left < length and A[left] > A[i]:
        largest = left
    if right < length and A[right] > A[largest]:
        largest = right
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        Max_heapify(A, largest, length)

#维护以i节点为根节点的最小堆        
def Min_heapify(A, i, length):
    left = Left(i)
    right = Right(i)
    least = i
    if left < length and A[left] < A[i]:
        least = left
    if right < length and A[right] < A[least]:
        least = right
    if least != i:
        A[i], A[least] = A[least], A[i]
        Min_heapify(A, least, length)

#生成最大堆        
def Build_max_heap(A):
    for i in range(int(len(A)/2), -1, -1):
        Max_heapify(A, i, len(A))
#生成最小堆        
def Build_min_heap(A):
    for i in range(int(len(A)/2), -1, -1):
        Min_heapify(A, i, len(A))

#最大堆排序        
def Max_heap_sort(A):
    Build_max_heap(A)
    heap_size = len(A) - 1
    while heap_size > 0:
        A[0], A[heap_size] = A[heap_size], A[0]
        Max_heapify(A, 0, heap_size)
        heap_size -= 1

#最小堆排序
def Min_heap_sort(A):
    Build_min_heap(A)
    heap_size = len(A) - 1
    while heap_size > 0:
        A[0], A[heap_size] = A[heap_size], A[0]
        Min_heapify(A, 0, heap_size)
        heap_size -= 1

def Heap_max(A):
    Build_max_heap(A)
    return(A[0])

def Heap_min(A):
    Build_min_heap(A)
    return(A[0])    
        
def Heap_extract_max(A):
    if len(A) < 1:
        print('Heap underflow')
        return
    Build_max_heap(A)
    maximum = A[0]
    A[0] = A[len(A)-1]
    Max_heapify(A, 0, len(A)-1)
    return maximum

def Heap_extract_min(A):
    if len(A) < 1:
        print('Heap underflow')
        return
    Build_min_heap(A)
    minimum = A[0]
    A[0] = A[len(A)-1]
    Min_heapify(A, 0, len(A)-1)
    return minimum

def Heap_increase_key(A, i, key):
    if A[i] > key:
        print('New key is smaller than current key')
        return
    if i >= len(A):
        print('Index overflow')
        return
    Build_max_heap(A)
    A[i] = key
    while i > 0 and A[Parent(i)] < A[i]:
        A[Parent(i)], A[i] = A[i], A[Parent(i)]
        i = Parent(i)
        
def Heap_decrease_key(A, i, key):
    if A[i] < key:
        print('New key is larger than current key')
        return
    if i>= len(A):
        print('Index overflow')
        return
    Build_min_heap(A)
    A[i] = key
    while i > 0 and A[Parent(i)] > A[i]:
        A[Parent(i)], A[i] = A[i], A[Parent(i)]
        i = Parent(i)

def Max_heap_insert(A, key):
    if len(A) < 1:
        A.append(key)
        return
    Build_max_heap(A)
    A.append(float('-inf'))
    Heap_increase_key(A, len(A)-1, key)
    
def Min_heap_insert(A, key):
    if len(A) < 1:
        A.append(key)
        return
    Build_min_heap(A)
    A.append(float('inf'))
    Heap_decrease_key(A, len(A)-1, key)

def Heap_delete(A, i):
    if i >= len(A):
        print('Error occured')
        return
    Build_max_heap(A)
    A.pop(i)
    Build_max_heap(A)
    
A = [4, 1, 3, 2, 9, 5]
Min_heap_insert(A, 4)
print(A)