# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 23:40:12 2020

@author: Lenovo
"""

def swap(arr,i,j):
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp


def pivot(arr,start,end):
    pivot=arr[start]
    swapidx=start
    
    for i in range(start+1,len(arr)):
        if pivot>arr[i]:
            swapidx+=1
            swap(arr,swapidx,i)
            
    swap(arr,swapidx,start)
    return swapidx

def quikSort(arr,left,right):
    if len(arr)==1: 
        return arr
    if (left<right):
        pivotIdx=pivot(arr,left,right)
        
        quikSort(arr,left,pivotIdx-1)
        quikSort(arr,pivotIdx+1,right)
        
    return arr
arr=[9,4,8,2,1,5,7,6,3]
print(quikSort(arr,0,len(arr)))