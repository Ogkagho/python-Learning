# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 19:25:21 2024

@author: Lenovo
"""
import sys
sys.path.append('C:\\Users\\Lenovo\\Downloads\\introcs-1.0')

import stdio
import random
import math


# =============================================================================
# #1.3.32
# #ramanujan's taxi
# n = int(input())
# 
# found = False
# for a in range(1, n+1):
#     for b in range(1, n+1):
#         for c in range(1, n+1):
#             for d in range(1, n+1):
#                 cond = a != b and a != c and a != d 
#                 cond2 = b != c and b != d 
#                 cond3 = c != d
#                 if a**3 + b**3 == d**3 + c**3 and cond and cond2 and cond3 :
#                     found = True
#                     break
#                 if found:
#                     break
#             if found:
#                 break
#         if found:
#             break
#     if found:
#         break
# if found:
#     print(a**3 + b**3,a, b, c, d)
# else:
#     print('not found')
# =============================================================================

# =============================================================================
# #1.3.33
# #Checksums
# 
# n = input()
# 
# sum1 = 0
# for i in range(len(n)):
#     sum1 += (10 - i)*int(n[i])
# for i in range(0, 10):
#     sum1 += i
#     if sum1 % 11 == 0:
#         checksum = i
#         break
#     else:
#         sum1 -= i
# print(n + str(i))
# =============================================================================
    
# =============================================================================
# #1.3.34
# #Counting Primes
# # =============================================================================
# # def isPrime(n):
# #     i = 2
# #     while i*i <= n:
# #         if n % i == 0:
# #             return False
# #     if n > 1:
# #         return True 
# # =============================================================================
#         
#     
# n = int(input('Enter:'))
# 
# countPrime = 0
# if n > 2:
#     countPrime = 1  # Counting 2 as a prime number
# 
# for i in range(3, n, 2):
#     isPrime = True
#     for j in range(3, int(math.sqrt(i)) + 1, 2):
#         if i % j == 0:
#             isPrime = False
#             break
#     if isPrime:
#         countPrime += 1
# 
# print(countPrime)
# =============================================================================

# =============================================================================
# #1.3.35
# #2d random walk
# 
# n = int(input())
# 
# positioni = 0
# positionj = 0
# steps  = 0
# 
# while abs(positioni) < n and abs(positionj) < n:
#     decision =random.randrange(1, 5)
#     if decision == 1:
#         positioni += 1 
#     elif decision == 2:
#         positioni -= 1
#     elif decision == 3:
#         positionj += 1 
#     elif decision == 4:
#         positionj -= 1
#     steps += 1
# 
# print(steps)
# =============================================================================

# =============================================================================
# #1.3.36
# #Median-of-5
# 
# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# num4 = int(input())
# num5 = int(input())
# 
# if num1 < num2:
#     min1 = num1
#     max1 = num2
# else:
#     min1 = num2
#     max1 = num1
# 
# if num3 < num4:
#     min2 = num3 
#     max2 = num4
# else:
#     min2 = num4 
#     max2 = num3 
# if min1 < min2:
#     minF = min2
# else:
#     minF = min1 
#
# if max1 < max2:
#     maxF = max1 
# else:
#     maxF = max2 
#     
# if maxF < num5:
#     median = maxF
# else:
#     median = num5
#     
# if median < minF:
#     median = minF
# 
# print(median)
# 
# 
# 
# #or 
# import sys
# 
# num1 = int(sys.argv[1])
# num2 = int(sys.argv[2])
# num3 = int(sys.argv[3])
# num4 = int(sys.argv[4])
# num5 = int(sys.argv[5])
# 
# nums = [num1, num2, num3, num4, num5]
# 
# # Sort the list
# nums.sort()
# 
# # The median is the middle element
# median = nums[2]
# 
# print(median)
# =============================================================================
    


# =============================================================================
# #1.3.38
# #Trigonometric functions
# #sine function
# x = float(input('Enter: '))
# #n = int(input('Enter integer: '))
# sin = x
# fact = 1
# count = 1
# 
# for i in range(3,50,2):
#     fact *= i * (i - 1) 
#     sin += (-1)**count *(x**i / fact)
#     count += 1
#     
# # =============================================================================
# # for i in range(3,50,2):
# #     fact *= i * (i - 1)
# #     if count % 2 == 1:
# #         sin += -(x**i / fact)
# #     elif count % 2 == 0:
# #         sin += (x**i / fact)
# #     
# #     count += 1
# # =============================================================================
#     
# 
# print(sin)
# 
# #cosine function
# 
# x = float(input('Enter: '))
# #n = int(input('Enter integer: '))
# cos = 1
# fact = 1
# count = 1
# 
# # =============================================================================
# # for i in range(2, 50, 2):
# #     fact *= i * (i - 1)
# #     if count % 2 == 1:
# #         cos += -(x**i / fact)
# #     elif count % 2 == 0:
# #         cos += (x**i) / fact
# #     
# #     count += 1
# # =============================================================================
# 
# for i in range(2, 50, 2):
#     fact *= i * (i - 1)
#     cos += (-1)**count*(x**i / fact)
#     count += 1
# 
# print(cos)
# =============================================================================


# =============================================================================
# #1.3.40
# #Pepys's problem
# 
# #How many times to run the simulation
# n = int(input('Enter: '))
# six = 0
# twelve = 0
# for i in range(n+1):
#     ones6 = 0
#     for j in range(6):
#         if random.randrange(1, 7) == 1:
#             ones6 += 1
#             if ones6 == 1:
#                 six += 1
#                 break
#     
#     ones12 = 0
#     for j in range(12):
#         if random.randrange(1, 7) == 1:
#             ones12 += 1 
#             if ones12 == 2:
#                 twelve += 1
#                 break
#     
# prob6 = 100 * (six / n)
# prob12 = 100 * (twelve / n)
# 
# stdio.writeln('Getting 1 at least once when rolling a fair die six times: ' 
#               + str(prob6) + '%')
# stdio.writeln('Getting 1 at least once when rolling a fair die twelve times: ' 
#               + str(prob12) + '%')
# =============================================================================


# =============================================================================
# #1.3.41
# #Game simulation mantyhall
# n = int(input('Enter: '))
# #prize = random.randrange(1,4)
# win = 0
# for i in range(n+1):
#     prize = random.randrange(1,4)
#     choice = random.randrange(1,4)
#     #presenterOpen = random.randrange(1,4)
#     if choice == prize:
#         win += 1
# stdio.writeln(str(100*(win/n)) + ' % wins if no switch')
#  
# win = 0
# for i in range(n+1): 
#     prize = random.randrange(1,4)
#     choice = random.randrange(1,4)
#     presenterOpen = random.randrange(1,4)
#     while presenterOpen == choice or presenterOpen == prize:
#         presenterOpen = random.randrange(1,4)
#     if choice != prize:
#         newchoice = random.randrange(1,4)
#         while choice == newchoice or newchoice == presenterOpen:
#             newchoice = random.randrange(1,4)
#         if newchoice == prize:
#             win += 1
# stdio.writeln(str(100*(win/n)) + ' % wins if switch')
# =============================================================================


# =============================================================================
# #1.3.42
# #Chaos
# 
# x = 0.01#float(input('Enter: '))
# r = float(input('Enter: '))
# t = 0
# stabilize = 1 - 1/r
# #and t < 70
# while x > 0 and x <=1:
#     x = r*x*(1-x)
#     print(x)
#     if abs(x - stabilize) < 1e-8:
#         print(r)
#         break
#     t += 1
# =============================================================================

