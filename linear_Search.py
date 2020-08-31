# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 16:39:54 2020

@author: Lenovo
"""
def linearSearch(arr,item):
    
    for i in arr:
        if item ==i:
            return True
    return False


print(linearSearch([2,1,3,4,6,7,9,88,44,66,51],10))