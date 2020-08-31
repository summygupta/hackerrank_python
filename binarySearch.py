# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 16:49:26 2020

@author: Lenovo
"""
import math

def binarySearch(arr,item):
    start=0
    end=len(arr)
    mid=math.floor((start+end)/2)
    
    while (start<=end):
        if item==arr[mid]:
            return True
        if item >arr[mid]:
            start=mid +1
            mid=math.floor((start+end)/2)
        else:
            end =mid-1
            mid=math.floor((start+end)/2)
        if mid==start==end:
            return False
    
    return False


print(binarySearch([2,1,3,4,6,7,9,88,44,66,51],70))
    
    