# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 18:05:31 2024

@author: Edward kagho
"""
import sys
sys.path.append('C:\\Users\\Lenovo\\Downloads\\introcs-1.0')
import stdio
import stdarray
import random
import math

# =============================================================================
# #1.4.20
# #Dice simulation
# 
# throws = int(input())
# 
# sums = stdarray.create1D(13, 0)
# 
# for t in range(throws):
#     dice_1 = random.randrange(1, 7)
#     dice_2 = random.randrange(1, 7)
#     sum1 = dice_2 + dice_1 
#     sums[sum1] += 1 
# 
# for i in range(2, 13):
#     sums[i] /= throws
#     
# probabilities = stdarray.create1D(13, 0.0) 
# for i in range(1, 7): 
#     for j in range(1, 7): 
#         probabilities[i+j] += 1.0 
# for k in range(2, 13): 
#     probabilities[k] /= 36
# 
# compare = stdarray.create1D(13, 0)
# 
# for i in range(13):
#     compare[i] = abs(sums[i] - probabilities[i])
# =============================================================================
    

# =============================================================================
# #1.4.21
# 
# a = [1, 2, 2, 2, 1, 10 ,5, 5, 5, 5, 1]
# 
# i = 1
# length = 1
# maxLength = 0
# 
# #len(a)-(len(a)-1-i)
# while i < len(a)-1:
#     while i != len(a) - 1 and a[i] == a[i+1]:
#         if a[i-1] < a[i]:  
#             position = i
#         length += 1
#         i += 1
#     if a[position+length -1] > a[position+length] and a[position-1] < a[position] and length > maxLength:
#         maxLength = length
#         finalposition = position
#     i += 1
#     length = 1
# 
# if maxLength == 0:
#     print('There is no such sequence')
# else:
#     print(f'The position of the sequence of integers is {finalposition} \
#           and the length is {maxLength}')
# =============================================================================





# =============================================================================
# #1.4.29
# 
# a = [1, 5, 1, 3]
# found = False
# for i in range(len(a)):
#     for j in range(i+1, len(a)):
#         if a[i] == a[j]:
#             found = True 
#             break 
#     if found:
#         break 
# if found:
#     print('There\'s a duplicate.')
# else:
#     print('No duplicate')
# =============================================================================


# =============================================================================
# #1.4.36
# #Birthday problem
# 
# trials = int(input())
# count1= 0
# for t in range(trials):
#     count = 0
#     birthdays = [0]*365
#     while sum(birthdays) < 364:
#         r = random.randrange(1, 365)
#         birthdays[r] += 1 
#         count += 1
#         if birthdays[r] == 2:
#             break 
#     if 2 in birthdays:
#         count1 += count 
# 
# print(count1/trials)
# =============================================================================
        

# =============================================================================
# 
# trials = int(input())
# count1= 0
# for t in range(trials):
#     count = 0
#     birthdays = [0]*365
#     while True:
#         r = random.randrange(1, 365)
#         birthdays[r] += 1 
#         count += 1
#         if birthdays[r] == 2:
#             break 
#     count1 += count 
# 
# print(count1/trials)
# =============================================================================
