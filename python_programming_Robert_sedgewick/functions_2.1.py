# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 20:31:15 2024

@author: Lenovo
"""

import sys
sys.path.append('C:\\Users\\Lenovo\\Downloads\\introcs-1.0')

import stdio
#import random
#import math
#import stddraw 
#import stdarray

# =============================================================================
# def harmonic(n):
#     total =0.0
#     for i in range(1, n+1):
#         total +=  1.0/i
#     return total 
# 
# for i in range(1, len(sys.argv)):
#     arg = int(sys.argv[i])
#     
#     value = harmonic(arg)
#     stdio.writeln(value)
# =============================================================================

#primality test

def isPrime(n):
    if n < 2: return False
    i = 2
    while i*i <=n:
        if n % i == 0: return False 
        i += 1 
    return True 

def harmonic(n, r=1):
    total = 0.0
    for i in range(1, n+1):
        total += 1.0/(i**r)
    return total
