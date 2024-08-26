# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 17:47:56 2024

@author: Lenovo
"""

def linearSearch(list1, n):
    for i in range(0, len(list1)):
        if n == list1[i]:
            return True 
        
    return False

s = range(100)

linearSearch(s, 7)