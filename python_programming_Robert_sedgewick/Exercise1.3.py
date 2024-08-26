# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 01:07:30 2024

@author: Lenovo
"""

import sys
sys.path.append('C:\\Users\\Lenovo\\Downloads\\introcs-1.0')

import stdio
import random
import math

# =============================================================================
# #1.31
# a = int(sys.argv[1])
# b = int(sys.argv[2])
# c = int(sys.argv[3])
# 
# if a == b and b == c:
#     stdio.writeln('Equal')
# else:
#     stdio.writeln('Not equal')
# =============================================================================

# =============================================================================
# #1.3.2
# #Quadratic
# 
# a = float(sys.argv[1])
# b = float(sys.argv[2])
# c = float(sys.argv[3])
# 
# if a == 0:
#     stdio.writeln('This is not a quadratic equation.')
# else:
#     d = b*b - 4*a*c
#     if d < 0:
#         stdio.writeln('The equation has no real roots')
#     elif d == 0:
#         stdio.write('The equation has a repeated root')
#         stdio.writeln(str((-b+d)/2.0))
#     else:
#         stdio.write('The equation has two distinct roots')
#         stdio.writeln(str((-b+d)/2.0) + ' and ' + str((-b-d)/2.0))
# =============================================================================

# =============================================================================
# #1.3.3
# 
# a = float(sys.argv[1])
# b = float(sys.argv[2])
# 
# if (0.0 < a and a < 1.0) and (0.0 < b and b < 1.0):
#     stdio.writeln('True')
# else: stdio.writeln('False')
# =============================================================================

# =============================================================================
# j = 0
# for i in range(j,10):
#     stdio.write(j)
#     j += i
#     stdio.writeln(' ' + str(j))
#     
# stdio.write(j)
# =============================================================================


# =============================================================================
# #1.3.6
# n = int(sys.argv[1])
# for i in range(1,n+1):
#     if (i % 10 == 1 or i % 100 == 1) and not i == 11:
#         stdio.writeln(str(i) + 'st Hello' )
#     elif (i % 10 == 2 or i % 100 == 2) and not i == 12:
#         stdio.writeln(str(i) + 'nd Hello')
#     elif (i % 10 == 3 or i % 100 == 3) and not i ==13:
#         stdio.writeln(str(i) + 'rd Hello')
#     else:
#         stdio.writeln(str(i) + 'th Hello')
# =============================================================================

# =============================================================================
# #1.3.7
# for i in range(1000, 2000):
#     if i % 10 == 4 or i % 10 == 9:
#         stdio.writeln(str(i))
#     else:
#         stdio.write(str(i) + ' ')
# =============================================================================

# =============================================================================
# #1.3.8
# n = int(sys.argv[1])
# 
# total = 0
# max1 = 0
# min1 = 2
# for i in range(n):
#     a = random.random()
#     stdio.write(str(a) + ' ')
#     total += a
#     if a < min1:
#         min1 = a
#     
#     if a > max1:
#         max1 = a
#     
# stdio.writeln('Average:' + str(total/n) + '  and Max is ' + str(max1) +
#               'and the Min is ' + str(min1))
# =============================================================================

# =============================================================================
# #1.3.9
# n = int(sys.argv[1])
# ruler = '1'
# stdio.writeln(ruler)
# for i in range(2, n+1):
#     ruler = ruler + ' ' + ruler
#     stdio.writeln(ruler)
# =============================================================================


# =============================================================================
# #1.3.10
# 
# n = int(sys.argv[1])
# stdio.writeln('log_2N\t\t n\t\t nlog_en\t\t n^2\t\t n^3\t\t 2^n')
# i = 2
# while i <= n:
#     stdio.writeln(str(math.log(i, 2)) + '\t\t' + str(i) + '\t\t' + str(i*math.log(i, math.e)) + '\t\t'
#                   + str(i**2) + '\t\t' + str(i**3) + '\t\t' + str(2**i))
#     i *= 2
# =============================================================================

# =============================================================================
# #1.3.11
# #reverses a number
# n = 123456789
# m = 0
# stdio.writeln(str(m) + ' ' + str(n))
# while n != 0:
#     m = (10 * m) + (n % 10)
#     n //= 10
#     #print(m,n)
# 
# stdio.writeln(str(m) + ' ' + str(n))
# =============================================================================

# =============================================================================
# #1.3.12
# #Fibonacci numbers 
# 
# f = 0
# g = 1
# for i in range(16):
#     stdio.writeln(f)
#     f = f + g
#     g = f - g
# #stdio.writeln(f)
# #stdio.writeln(g)
# =============================================================================

# =============================================================================
# #1.3.13
# n  = int(input())
# 
# power = 1
# 
# while power <= n and n > 0:
#     stdio.write(str(power) + ' ')
#     power *= 2
# =============================================================================

# =============================================================================
# #1.3.14
# 
# principal = float(input('Enter the pricipal amount: '))
# rate = float(input('Enter the interest rate: '))
# number_years = int(input('Enter the number of years: '))
# 
# monthly_rate = rate/12
# number_months = number_years * 12
# 
# for i in range(1, number_months+1):
#     amount = principal*math.e**(i*monthly_rate)
#     principal -= amount 
#     print(f"{i:<10}{amount:<20.2f}{principal:<20.2f}")
# =============================================================================
    

# =============================================================================
# #1.3.15 
# #divisor pattern
# n = int(sys.argv[1])
# 
# i = 1
# while i <= n:
#     j = 1
#     while j <= n:
#         if (i %  j == 0) or (j % i == 0):
#             stdio.write('* ')
#         else:
#             stdio.write('  ')
#         j += 1
#     stdio.writeln(i)
#     i += 1
# =============================================================================

# =============================================================================
# total = 0.0
# for i in range(1, 10000):
#     total += 1.0 /(i*i)
# print(total)
# =============================================================================

# =============================================================================
# #1.3.18
# #k-th root using newtons method
# c = int(sys.argv[1])
# k = int(sys.argv[2])
# EPSILON = 1e-10
# t = c
# r = k - 1
# 
# while abs((t**k) - c) > (EPSILON):
#     t = 1/k * (r*t + c/(t**r))
#     
# stdio.write('The ' + str(k) + ' root of ' + str(c) + ' is '
#             + str(t))
# =============================================================================

# =============================================================================
# #1.3.19
# #kary
# i = int(input("Enter the number to convert: "))
# k = int(input("Enter the base (2-16): "))
# 
# v = 1
# while v <= i // k:
#     v *= k
# 
# while v > 0:
#     digit = i // v
#     if digit < 10:
#         print(digit, end='')
#     else:
#         print(chr(ord('A') + digit - 10), end='')
#     i %= v
#     v //= k
# print()
# =============================================================================




    