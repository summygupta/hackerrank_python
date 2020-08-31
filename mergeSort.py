# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 23:02:18 2020

@author: Lenovo
"""
import math
def merge(arr1,arr2):
    result=[]
    i=0
    j=0
    
    while (i<len(arr1) and j<len(arr2)):
        if arr1[i]>arr2[j]:
            result.append(arr2[j])
            j+=1
        else:
            result.append(arr1[i])
            i+=1
    while i<len(arr1):
        result.append(arr1[i])
        i+=1
    while j<len(arr2):
        result.append(arr2[j])
        j+=1 
    
    return result


def mergeSort(arr):
    if len(arr)<2:
        return arr
    
    mid=math.floor(len(arr)/2)
    
    left=mergeSort(arr[0:mid])
    
    right=mergeSort(arr[mid:len(arr)])
    
    return merge(left,right)

    
print(mergeSort([9,7,5,8,1,9]))

