# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 17:33:26 2020

@author: Lenovo
"""

def bubbleSort(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
            

print(bubbleSort([8,7,9,6,4,5,2,1]))