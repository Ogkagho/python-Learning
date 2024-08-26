# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 20:47:32 2024

@author: Lenovo
"""
import math 

# =============================================================================
# #Word count problem
# line = input('Enter: ')
# total_count = line.count(' ')  + 1
# print(total_count)
# 
# 
# #Cone volume problem
# 
# radius = int(input())
# height  =int(input())
# 
# volume = (math.pi*radius**2 * height) / 3.0
# 
# print(volume)
# 
# #DMOJ problem wc16c1j1, A Spooky Season
# 
# incantation = int(input('Enter incantation S(2 < S <= 20): '))
# print('sp' + 'o'*incantation + 'ky')
# 
# #DMOJ problem wc15c2j1, A New Hope
# 
# n = int(input('Enter N( 1 <= N <= 5): '))
# n = n - 1
# 
# line = 'A long time ago in a galaxy ' + 'far, '*n + 'far away...' 
# print(line)
# 
# =============================================================================
# =============================================================================
# #Debug of someones code (A new hope)
# N = int(input('Enter: '))
# line = 'A long time ago in a galaxy'
# words = ' '
# for i in range(1, N):
#     words +=  'far, '
# 
# print(line + words + "far away...")
# 
# N = int(input('Enter: '))
# words = " far, "
# line = 'A long time ago in a galaxy'
# newwords = ''
# for i in range(1, N):
#     newwords += words
# 
# print(line + newwords + "far away...")
# =============================================================================

# =============================================================================
# # DMOJ problem ccc13j1, Next in Line
# 
# y = int(input('Enter age of youngest child: '))
# m = int(input('Enter age of middle child: '))
# diff = m - y
# #olderAge=2*m - y
# #olderAge = 2*diff + y
# #olderAge = m + diff
# print(str(y+2*diff))
# =============================================================================

p = int(input('Enter: '))
b = int(input('Enter: '))
d = int(input('Enter: '))

numcaps = p // b
numremain = p % b
sell = d*numcaps
total = sell + numremain
print(total)

