# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 23:10:27 2024

@author: Lenovo
"""
#Ramanujan-Sato series.

import math

def pi():
    a = math.sqrt(2)
    b = 0
    x = 2 + a
    for i in range(0,6):
        t = math.sqrt(a)
        b = t*(1 + b)/(a+b)
        a = (1/2)*(t + 1/t)
        x = x*b*(1 + a)/(1+b)
    return x

pi()

#D. Bailey, P. Borwein, and S. Plouffe (called "BBP") 

def pi2():
    sum = 0
    for n in range(0, 1001):
        term = 1/16**n*((4/(8*n+1)) - (2/(8*n+4)) - (1/(8*n+5)) - (1/(8*n+6)))
        sum += term
    print("sum =", sum)
    
pi2()