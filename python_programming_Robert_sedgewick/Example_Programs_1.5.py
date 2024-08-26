# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 05:52:22 2024

@author: Lenovo
"""

import sys
sys.path.append('C:\\Users\\Lenovo\\Downloads\\introcs-1.0')

import stdio
import math 
import random
import stdarray

# =============================================================================
# stdio.write('Hi, ')
# stdio.write(sys.argv[1])
# stdio.writelin('. How are you ?')
# =============================================================================

# =============================================================================
# stdio.write('Hi ')
# stdio.write(sys.argv[1])
# stdio.write(', ')
# stdio.write(sys.argv[2])
# stdio.write(', and ')
# stdio.writeln(sys.argv[3])
# =============================================================================

# =============================================================================
# theta = float(sys.argv[1])
# 
# stdio.writeln(math.sin(theta)**2 + math.cos(theta)**2)
# =============================================================================

# =============================================================================
# a = random.random()
# b = random.random()
# c = random.random()
# d = random.random()
# e = random.random()
# 
# average = (a + b + c + d)/5
# 
# stdio.writeln(str(a) + ', ' + str(b) + ', ' + str(c) + ', ' + str(d) + ','+ str(e))
# stdio.writeln(str(average))
# stdio.write('The largest is ' + str(max(a, b, c, d, e)))
# stdio.write(' and the smallest is ' + str(min(a, b, c, d, e)))
# =============================================================================

# =============================================================================
# r = float(sys.argv[1])
# g = float(sys.argv[2])
# b = float(sys.argv[3])
# 
# w = max(r/225, g/255, b/255)
# c = (w - (r/255)) / w
# m = (w - (g / 255)) / w
# y = (w - (b /255)) / w
# k = 1 - w
# 
# stdio.writeln('RGB to CMYK, R: ' + str(r) + ' G: ' 
#               + str(g) + ' B: ' + str(b) + ' CMYK: '+ str(c)
#               + ' ' + str(m) + ' ' + str(y) + ' ' + str(k))
# =============================================================================

# =============================================================================
# discriminant  = b**2 + 4*a*c
# 
# if discriminant < 0.0: stdio.writeln( 'No real roots')
# else:
#     d = math.sqrt(discriminant)
#     stdio.writeln((-b + d) / 2.0)
#     stdio.writeln(((-b + d))/ 2.0)
# =============================================================================
    
    
# =============================================================================
# if random.randrange(0, 2) == 0:
#     stdio.writeln('tails')
# else: stdio.writeln('Heads')
# =============================================================================


# =============================================================================
# n = int(sys.argv[1])
# power = 1
# i = 0
# while i <= n:
#     stdio.writeln('2^'+str(i) + ' ' + str(power)) 
#     power *= 2
#     i = i + 1
# =============================================================================
    
# =============================================================================
# while 2*power < n:
#     print(power, 'after, change within loop', end =' ')
#     power = 2* power
#     print(power)
# stdio.write(str(power))
# =============================================================================

# =============================================================================
# ruler = '1'
# stdio.writeln(ruler)
# for i in range(2, 5+1):
#     ruler = ruler + ' '+ str(i) + ' ' + ruler
#     stdio.writeln(ruler)
# =============================================================================


# =============================================================================
# n = int(sys.argv[1])
# total = 0.0
# for i in range(1,n+1):
#     total += 1.0 / i
# stdio.write(str(total))
# =============================================================================

# =============================================================================
# EPSILON = 1e-15
# 
# c = float(sys.argv[1])
# t = c
# #abs(t*t - c)
# while abs(t - c/t) > EPSILON:
#     t = (c/t + t) / 2.0
# 
# stdio.writeln(t)
# =============================================================================

# =============================================================================
# #Converting to binary
# n = int(sys.argv[1])
# 
# #Compute v as the largest power less than n 
# v = 1
# while v <= n // 2:
#     v *= 2
# #Cast out powers of 2 in decreasing order   
# while v > 0:
#     if n < v:
#         stdio.write(0)
#     else:
#         stdio.write(1)
#         n -= v
#     v // 2
# =============================================================================
    

#Prime factors

# =============================================================================
# n = int(sys.argv[1])
# 
# factor =  2
# while factor**2 <= n:
#     while (n % factor) == 0:
#         
#         n //= factor 
#         stdio.write(str(factor) + ' ')
#     factor += 1
#     
# if n > 1:
#     stdio.write(n)
# stdio.writeln()
# =============================================================================


# =============================================================================
# #gamblers ruin
# 
# stake = int(sys.argv[1])
# goal = int(sys.argv[2])
# trials = int(sys.argv[3])
# upperLimit = int(sys.argv[3])
# 
# bets = 0
# wins = 0
# for t in range(trials):
#     #Run one experiment 
#     cash = stake
#     while (cash > 0) and (cash < goal) and (bets < upperLimit):
#         #Simulate one bet
#         bets += 1
#         if random.randrange(0,2) == 0:
#             cash += 1
#         else:
#             cash -= 1
#     if cash == goal:
#         wins += 1
# 
# stdio.writeln(str(100 * wins //trials) + '% wins')
# stdio.writeln('Avg # bets: ' + str(bets // trials)) 
# =============================================================================

# =============================================================================
# #Loop and a half
# while True:
#     x = -1.0 + 2.0*random.random() #scales the  points to [-1,1]
#     y = -1.0 + 2.0*random.random()
#     if x*x + y*y <= 1.0:
#         break
# =============================================================================

# =============================================================================
# n = 10
# m = 3
# 
# perm = [0]*n
# for i in range(n):
#     perm[i] = i
# 
# for i in range(m):
#     r = random.randrange(i, m)
#     t = perm[i]
#     perm[i] = perm[r]
#     perm[r] = t
# =============================================================================


# =============================================================================
# n = 16
# 
# count = 0
# collectedCount = 0
# isCollected = stdarray.create1D(n, False)
# 
# while collectedCount < n:
#     value = random.randrange(0, n)
#     count += 1
#     if not isCollected[value]:
#         collectedCount += 1
#         isCollected[value] = True 
# 
# stdio.writeln(count)
# =============================================================================

# =============================================================================
# #sieve eratosthenes
# 
# n = 14
# isPrime = stdarray.create1D(n+1, True)
# 
# #for i in range(2, math.sqrt(n))
# for i in range(2, n):
#     if(isPrime[i]):
#         for j in range(2, n//i + 1):
#             isPrime[i*j] = False 
# 
# count = 0
# for i in range(2, n+1):
#     if (isPrime[i]):
#         count += 1
# =============================================================================
        
# =============================================================================
# #self avoiding random walk 
# n = int(input())
# trials = int(input())
# deadends = 0
# 
# for t in range(trials):
#     a = stdarray.create2D(n, n, False)
#     x = n // 2
#     y = n // 2
#     while (x > 0) and (x < n-1) and (y >0) and (y < n-1):
#         
#         a[x][y] = True
#         if a[x-1][y] and a[x+1][y] and a[x][y-1] and a[x][y+1]:
#             deadends += 1
#             break 
#         r = random.randrange(1, 5)
#         if (r == 1) and (not a[x+1][y]): x += 1 
#         elif (r == 2) and (not a[x-1][y]): x -= 1 
#         elif (r == 3) and (not a[x][y+1]): y += 1 
#         elif (r == 4) and (not a[x][y-1]): y -=1  
#         
# stdio.writeln(str(100*deadends // trials) + '% dead ends')
# =============================================================================
