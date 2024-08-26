# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 13:11:11 2024

@author: Lenovo
"""

# =============================================================================
# def newtonSqrt(n, e):
#     assert n >= 0, 'The number must be non-negative'
#     assert e >0, 'epsilon must be greater than zero'
#     
#     guess = 1
#     
#     while abs(guess**2 - n) > e:
#         guess = guess - (guess**2 - n) / (2*guess)
#     
#     return guess
#     
# newtonSqrt(100, 0.0001)
# =============================================================================

def improve(g, n):
    return g - (g**2 - n )/ (2*g)

def newtonSqrt1(n, e):
    guess = 1
    
    while abs(guess**2 - n) > e*guess:
        guess = improve(guess, n)
    return guess


newtonSqrt1(100)


# =============================================================================
# #newtons method different implemntation
# EPSILON = 1e-15
# 
# c = float(input('Enter number to find sqrt of : '))
# t = c
# 
# while abs(t - c/t) > (EPSILON * t):
#     t = (c/t + t) / 2.0
#     
# print(t)
# =============================================================================
