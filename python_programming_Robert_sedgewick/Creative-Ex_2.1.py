# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 23:33:35 2024

@author: Lenovo
"""

# =============================================================================
# #Horner's mwthod
# 
# def getElements(n):
#     a = [0.0]*n
#     for i in range(n):
#         a[i] = int(input())
#     return a
# 
# def evaluate2(x,n):
#     ls = getElements(n)
#     value = 0
#     for i in range(1, n+1):
#         value = x*value + ls[n-i]
#     return value
# =============================================================================
# =============================================================================
# #2.1.29
# #horner's method
# 
# def evaluate(x, a):
#     # Horner's method
#     n = len(a)
#     value =  0
#     for i in range(1, n+1):
#         value *= x
#         value += a[n-i]
#     return value
# 
# def exp(x, n):
#     ls = [0.0]*n #number of coefficients, increase for precision
#     ls[0] = 1 
#     fact = 1 #start factorial
#     for i in range(1,n):
#         fact *= i  #update factorial
#         ls[i] = 1/fact
#         
#     return evaluate(x, ls) #call with x, and list 
# 
# print(exp(3, 10))
# print(math.exp(3))
# =============================================================================
