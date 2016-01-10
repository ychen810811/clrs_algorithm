# -*- coding:utf-8 -*-
import math


# INSERTION SORT algorithm implementation
def insertion_sort(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            i -= 1
        a[i + 1] = key


# Merge function for MERGE SORT algorithm implementation
def merge(A, p, q, r):
    L = A[p:q + 1]
    R = A[q + 1:r + 1]
    L.append(None)
    R.append(None)
    j = k = 0
    for i in range(p, r + 1):
        try:
            if L[j] <= R[k]:
                A[i] = L[j]
                j += 1
            else:
                A[i] = R[k]
                k += 1
        except TypeError as e:
            if L[j] is None:
                A[i:r + 1] = R[k:-1]
                break
            elif R[k] is None:
                A[i:r + 1] = L[j:-1]
                break
            else:
                raise e


# MERGE SORT algorithm implementation
def merge_sort(A, p, r):
    if p < r:
        q = math.floor((r + p) / 2)
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)


# BUBBLE SORT algorithm implementation
def bubble_sort(A):
    loop_flag = True
    while loop_flag:
        loop_flag = False
        for i in range(len(A) - 1):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                loop_flag = True
