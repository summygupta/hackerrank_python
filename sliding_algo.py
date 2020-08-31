# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 16:07:24 2020

@author: Lenovo
"""

# max sum of the cosecutive numbers in a list

n=3
arr=[2,6,9,2,1,8,5,6,3]
temp=0
maxsum=0;
for i in range(0,n):
    maxsum=arr[i]+maxsum

temp=maxsum

for i in range(n,len(arr)):
    temp=temp-arr[i-n]+arr[i]
    maxsum=max(maxsum,temp)

print(maxsum)
    