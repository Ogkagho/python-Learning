# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 21:19:15 2024

@author: Edward kagho
"""

#guess and check method, computing primes

import math 

def isPrime(n):
    if n % 2 == 0:
        return False 
    for i in range (3, int(math.sqrt(n))+ 1, 2):
        if n % i == 0:
            return False
    return True 

count = 1
i = 3

while i > 1 and count < 1000:
    if isPrime(i):
        count += 1
        if count == 1000:
            print('The 1000th prime is', i)
    i += 2
    
