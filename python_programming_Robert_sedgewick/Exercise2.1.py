# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 21:29:42 2024

@author: Lenovo
"""

import math 

# =============================================================================
# #2.1.1
# def max3(a,b,c):
#     if a > b and a > c:
#         return a
#     elif b > c : return b
#     else:
#         return c 
# 
# 
# #2.12
# def odd(x, y, z):
#     if (x + y + z) % 2 == 1:
#         return True 
#     else:
#         return False 
# 
# #2.1.3
# def majority(x, y, z):
#     return x + y + z >= 2
# =============================================================================

# =============================================================================
# #2.14
# def pythagoreanTriple(a, b, c):
#     if a > b and a > c:
#         return a**2 == b**2 +c**2
#     elif b > c:
#         return b**2 == a**2 + c**2
#     else:
#         return c**2 == a**2 + b**2 
# 
# def areTriangular(a, b, c):
#     return a + b > c and a + c > b and b + c > a 
# =============================================================================


#2.1.5
def sigmoid(n):
    return 1/(1+ math.exp(-n))
