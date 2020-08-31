# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 18:01:10 2020

@author: Lenovo
"""


def insertionSort(arr):
    
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while(j>=0 and arr[j]>key):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr

print(insertionSort([9,6,5,7,2,1,8])) 