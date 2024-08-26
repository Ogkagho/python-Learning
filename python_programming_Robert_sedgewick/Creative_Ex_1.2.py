# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 14:41:00 2024

@author: Lenovo
"""

import sys
import math
import random

#creative exercises

# =============================================================================
# #continuosly compounded interest 1.2.21
# principal = float(input('Enter the pricipal amount: '))
# rate = float(input('Enter the interest rate: '))
# number_years = int(input('Enter the number of years: '))
# 
# amount = principal*math.e**(rate*number_years)
# 
# print("The amount after ", number_years, "is", amount)
# 
# =============================================================================


# =============================================================================
# #Wind chill 1.2.22
# 
# temp = float(input('Enter the temperature: '))
# speed = float(input('Enter the speed: '))
# 
# while abs(temp) > 50 or (speed > 120 or speed < 3):
#     if abs(temp) > 50:
#         print('The program only works for absolute values of temperature ', end="")
#         print(' greater than 50')
#     else:
#         print("The program only works for absolute values of speed ", end=" ")
#         print("less than 120 and greater then 3")
#     
#     print("Re-enter the values")
#     temp = float(input('Enter the temperature: '))
#     speed = float(input('Enter the speed: '))
# 
# w = 35.74 + 0.6215 * temp + (0.4275*temp - 35.75)*(speed**0.16)
# 
# print("The wind chill is ", w)
# =============================================================================

        
# =============================================================================
# #polar cordinates 1.2.23
# 
# x = float(input('Enter x:'))
# y = float(input('Enter y: '))
# 
# r = math.sqrt(x**2 + y**2)
# theta = math.atan2(y, x)
# 
# print("The polar cordinates of (",x,",",y,") is (",r,",",theta,")")
# =============================================================================

# =============================================================================
# #box-muller formula #1.2.24
# v = random.random()
# u = random.random()
# 
# guassianNumber = math.sin(2*math.pi*v)*((-2*math.log(u))**0.5)
# print(guassianNumber)
# =============================================================================

# =============================================================================
# #1.225
# x = int(input('Enter: '))
# y = int(input('Enter: '))
# z = int(input('Enter: '))
# 
# if x < y < z or x > y > z:
#     print(True)
# else:
#     print(False)
# =============================================================================

# =============================================================================
# #1.2.26
# m = int(sys.argv[1])
# d = int(sys.argv[2])
# y = int(sys.argv[3])
# 
# y_0 = y - (14 - m)/12
# x = y_0 + y_0 - y_0/100 + y_0/400
# m_0 = m + 12 *((14 - m)/12) - 2 
# d_0 = (d + x + (31*m_0) /12) % 7
# 
# if d_0 == 1:
#     print('Monday')
# elif d_0 == 2:
#     print('Tuesday')
# elif d_0 == 3:
#     print('Wednesday')
# elif d_0 == 4:
#     print('Thursday')
# elif d_0 == 5:
#     print('Friday')
# elif d_0 == 6:
#     print('Saturday')
# elif d_0 == 0:
#     print('Sunday')
# 
# =============================================================================

# =============================================================================
# #1.2.27
# #for loops haven't been introduced yet, so cheating
# max1 = random.random()
# 
# for i in range(4):
#     r = random.random()
#     if r > max1:
#         max1 = r 
# 
# print(r)
# =============================================================================

# =============================================================================
# #1.2.28
# 
# lambda_0 = int(input())
# longitude = int(input())
# latitude = int(input())
# 
# x = longitude - lambda_0
# y = math.log((1 + math.sin(latitude)) / (1 - math.sin(latitude))) * 0.5
# 
# print(f'projection: (x, y) = ({x}, {y})')
# =============================================================================

# =============================================================================
# #1.2.30
# x_1 = math.radians(float(input()))
# y_1 = math.radians(float(input()))
# x_2 = math.radians(float(input()))
# y_2 = math.radians(float(input()))
# 
# d = 60*math.acos(math.sin(x_1)*math.sin(x_2) + math.cos(x_2)*math.cos(x_2)*math.cos(y_1 - y_2))
# 
# print(f'great circle distance: {d:.4f}')
# =============================================================================


# =============================================================================
# #1.2.31
# x = int(input('Enter: '))
# y = int(input('Enter: '))
# z = int(input('Enter: '))
# 
# maximum = max(x, y, z)
# minimum = min(x, y, z)
# 
# middle = x + y + z - maximum - minimum #total, subtract maximum , then minimum 
# 
# print(minimum, middle, maximum) 
# =============================================================================

# =============================================================================
# #dragon cruves
# #1.2.32
# 
# left = 'L'
# right ='R'
# dragon0 = 'F'
# 
# dragon1 = dragon0 + left + dragon0
# dragon1R = dragon0 + right + dragon0
# dragon2 = dragon1 + left + dragon1R
# dragon2R = dragon1 + right + dragon1R
# dragon3 = dragon2 + left + dragon2R
# dragon3R = dragon2 + right + dragon2R
# dragon4 = dragon3 + left + dragon3R
# dragon4R = dragon3 + right + dragon3R
# dragon5 = dragon4  + left + dragon4R
# 
# print(dragon5)
# 
# #recursive implementation
# def LtoR(st):
#     return st[::-1].replace('L', 'X').replace('R', 'L').replace('X', 'R') #replaces 'R' with 'L'
#             
# def dragonCurve(n):
#     if n == 0:
#         return 'F'
#     return dragonCurve(n-1) + 'L' + LtoR(dragonCurve(n-1))
# 
# print(dragonCurve(5))
# =============================================================================

# =============================================================================
# #for-loop implementation
# dragon = 'F'
# for i in range(5):
#     dragonR = dragon[::-1].replace('L', 'X').replace('R', 'L').replace('X', 'R')
#     dragon = dragon + 'L' + dragonR
#      
# 
# print(dragon)
# =============================================================================
    
    
    
    