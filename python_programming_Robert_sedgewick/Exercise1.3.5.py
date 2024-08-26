# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 16:06:15 2024

@author: Lenovo
"""

import sys
sys.path.append('C:\\Users\\Lenovo\\Downloads\\introcs-1.0')

import stdio
import random
import math


# =============================================================================
# #1.3.21 and #1.3.22
# #gamblers ruin
# 
# stake = int(sys.argv[1])
# goal = int(sys.argv[2])
# trials = int(sys.argv[3])
# #upperLimit = int(sys.argv[3])
# 
# bets = 0
# wins = 0
# indec = 1
# for t in range(trials):
# #t = 1
# #while t <= trials:
#     #Run one experiment 
#     cash = stake
#     while (cash > 0) and (cash < goal): #and (bets < upperLimit):
#     #for c in range(i):
#         #Simulate one bet
#         bets += 1
#         if random.randrange(0,2) == 0:
#             cash += 1
#         else:
#             cash -= 1
#         stdio.writeln('*'*cash) 
#         
#     if cash == goal:
#         wins += 1
#     #t += 1
# 
# stdio.writeln(str(100 * wins //trials) + '% wins')
# stdio.writeln('Avg # bets: ' + str(bets // trials))
# =============================================================================

# =============================================================================
# #1.3.21
# #inner loop 
# for c in range(1e45):
#     if cash <= 0 or cash >= goal:
#         break 
# =============================================================================
    

# =============================================================================
# #1.3.23
# 
# stake = int(input())
# goal = int(input())
# trials = int(input())
# fixed_prob = float(input()) 
# #upperlimit = int(input())
# 
# bets = 0
# wins = 0
# total_cash = 0
# 
# for t in range(trials):
#     cash = stake 
#     while (cash > 0) and (cash < goal):
#         bets += 1
#         if random.randrange(0, 2) < fixed_prob:
#             cash += 1
#         else:
#             cash -= 1
#         #print('*'*cash)
#     if cash == goal:
#         wins += 1
#     total_cash += cash
#     #print()
# 
# print(str(100 * wins // trials) + '% wins')
# print('Avg # bets: ' + str(bets//trials))
# =============================================================================

# =============================================================================
# #1.3.24
# 
# stake = int(input())
# goal = int(input())
# trials = int(input())
# fixed_prob = float(input()) 
# upperlimit = int(input())
# 
# bets = 0
# wins = 0
# total_cash = 0
# 
# for t in range(trials):
#     cash = stake 
#     while (cash > 0) and (cash < goal) and (bets < upperlimit):
#         bets += 1
#         if random.randrange(0, 2) == 0:
#             cash += 1
#         else:
#             cash -= 1
#         print('*'*cash)
#     if cash == goal:
#         wins += 1
#     total_cash += cash
#     print()
# 
# print(str(100 * wins // trials) + '% wins')
# print('Avg # bets: ' + str(bets//trials))
# print('How much money gambler takes home,', total_cash/trials)
# =============================================================================

# =============================================================================
# #1.3.27
# n = int(sys.argv[1])
# 
# for i in range(1,n+1):
#     for j in range(1,(n*2)):
#         if (i % 2 == 1 and j % 2 == 1) or(i % 2 == 0 and j % 2== 0):
#             stdio.write('*')
#         else:
#             stdio.write(' ')
#     stdio.writeln()
# =============================================================================


# =============================================================================
# #1.3.25
# 
# n = #int(sys.argv[1])
# 
# factor =  2
# while factor**2 <= n:
#     while (n % factor) == 0:
#         
#         n //= factor 
#         if not (n % factor) == 0: 
#             stdio.write(str(factor) + ' ')
#     factor += 1
#     
# if n > 1:
#     stdio.write(n)
# stdio.writeln()
# =============================================================================


 
        

  
      
# =============================================================================
# #1.3.30
# 
# found = False
# 
# while not found:
#     x = -1.0 + 2.0*random.random()
#     y = -1.0 + 2.0*random.random()
#     if x*x + y*y <= 1.0:
#         found = True
# print(x, y)
# =============================================================================

# =============================================================================
# def gcd(x, y):
#     while y != 0:
#         x, y = y, x % y
#     return x
# 
# #1.3.28
# x = int(input("Enter the first number: "))
# y = int(input("Enter the second number: "))
# 
# while y != 0:
#     if x > y:
#         if x % y == 0:
#             print("The GCD is:", y)
#             break
#         else:
#             x, y = y, x % y
#     else:
#         x, y = y, x % y
# 
# if y == 0:
#     print("The GCD is:", x)
# =============================================================================

# =============================================================================
# #1.3.29
# #relative prime
# for x in range(1, 4):  # set values for rows
#     for y in range(1, 4): #set values for columns 
#         i = x   #variables to check for gcd
#         j = y   
#         while j != 0:   #gcd starts checking 
#             if i > j == 0:
#                 if i % j == 0 and j == 1:
#                     print('* ', end ='')
#                     break
#                 elif i % j == 0:
#                     print('  ', end = '')
#                 else:
#                     i, j = j, i % j 
#             else:
#                 i, j = j, i % j 
#         if j == 0 and i == 1:
#             print('* ', end ='')
#         elif j == 0:
#             print('  ', end = '')
#     print()
# =============================================================================

