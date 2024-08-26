# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 22:42:25 2024

@author: Lenovo
"""

#naive impementaion

def isPrime(n):
    if n % 2 == 0 and n != 2:
        return False
    i = 3
    while i * i < n:
        if n % i == 0:
            return False
        i += 2
    
    return True 