# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 17:45:50 2020

@author: Lenovo
"""
def selectionSort(arr):
    
    for i in range(0,len(arr)-1):
        min=i
        
        for j in range(i,len(arr)-1):
            if arr[i]>arr[j+1] and arr[j+1]<=arr[min]:
                min=j+1
                
        arr[i],arr[min]=arr[min],arr[i]
        
    return arr
    

print(selectionSort([9,6,5,7,2,1,8]))