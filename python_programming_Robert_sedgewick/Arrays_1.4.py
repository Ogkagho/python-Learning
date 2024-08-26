# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 16:32:48 2024

@author: Lenovo
"""

import sys
sys.path.append('C:\\Users\\Lenovo\\Downloads\\introcs-1.0')
import stdio
import stdarray
import random

# =============================================================================
# m = int(sys.argv[1]) #choose this many elements 
# n = int(sys.argv[2]) #from 0, 1, ...., n-1
# 
# #initialize array perm = [0, 1, ...., n-1]
# perm = stdarray.create1D(n, 0)
# for i in range(n):
#     perm[i] = i
#     
# for i in range(m):
#     r = random.randrange(i, n) #ensures no duplicates 
#     
#     temp = perm[r]
#     perm[r] = perm[i]
#     perm[i] = temp
#     
# for i in range(m):
#     stdio.write(str(perm[i]) + ' ')
# stdio.writeln()
# =============================================================================

# =============================================================================
# n = int(sys.argv[1])
# harmonic = stdarray.create1D(n+1, 0.0)
# for i in range(1, n+1):
#     harmonic[i] = harmonic[i-1] + 1.0/i
# =============================================================================

# =============================================================================
# #coupon collecter
# n = int(sys.argv[1])
# 
# count = 0
# collectedCount = 0
# isCollected = stdarray.create1D(n, False)
# 
# while collectedCount < n:
#     #Generate another coupon 
#     value = random.randrange(0, n)
#     count += 1
#     if not isCollected[value]:
#         collectedCount += 1
#         isCollected[value] = True 
#         
#         
# stdio.writeln(count)
# =============================================================================

# =============================================================================
# #prime checker
# n = int(sys.argv[1])
# 
# count = 0 #change count = 1
# for i in range(2,n+1):  # range(3, n+1, 2)
#     factor = 2 
#     isPrime = True
#     while factor*factor <= i: #for i in range(2, math.sqrt(n)+1):
#         if (i % factor) == 0:
#             isPrime = False
#             break
#         factor += 1 
#     
#     if isPrime:
#         count += 1
# 
# print(count)
# =============================================================================

# =============================================================================
# #prive sieve
# n = int(sys.argv[1])
# 
# isPrime = stdarray.create1D(n+1, True)
# 
# for i in range(2, n):
#     if(isPrime[i]):
#         for j in range(2, n//i + 1):
#             isPrime[i*j] = False
# 
# count = 0
# for i in range(2, n+1):
#     if(isPrime[i]):
#         count += 1 
# stdio.writeln(count)
# =============================================================================

a = []
for i in range(m):
    row = [0.0] * n
    a += [row]

for i in range(m):
    for j in range(n):
        std