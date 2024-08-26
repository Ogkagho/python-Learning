# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 23:41:15 2024

@author: Lenovo
"""

#import math

# =============================================================================
# for a in range(10):
#     b = a+1
#     c = a*b
#     d = a**2 + b**2 + c**2
#     d1 = math.sqrt(d)
#     
#     print(d1 % 2)
# =============================================================================

# =============================================================================
# def gcd(a,b):
#     g = 1
#     for i in range(1,a+1):
#         if a % i == 0 and b % i == 0:
#             g = i
#     return g
# 
# 
# gcd(4, 6)
# 
# def get_gcd(a,b):
#     if a < b:
#         return gcd(a, b)
#     else:
#         return gcd(b, a)
# =============================================================================
    
# =============================================================================
# numerator = int(input("Enter the numerator: "))
# denominator = int(input("enter the denominator: "))
# 
# print("The reduced fraction of", numerator, "/", denominator, "is ", end="")
# print(numerator/gcd(numerator, denominator),"/", denominator/gcd(numerator, denominator))
# 
# 
# =============================================================================

def gcd2(a, b):
    if b == 0:
        return a
    else:
        while b != 0:
            remainder = a % b
            a = b
            b = remainder
        return a
    
def gcd2_1(a, b):
    if b == 0:
        return a
    else:
        return gcd2_1(b, a % b)

    
gcd2(66, 29)

# =============================================================================
# def gcd3(a, b, c):
#     return gcd2(a,gcd2(b, c))
# =============================================================================
