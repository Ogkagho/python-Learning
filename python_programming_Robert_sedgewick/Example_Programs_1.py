# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 18:52:15 2024

@author: Edward kagho
"""

import random 

# =============================================================================
# import math
# 
# 
# low = 0
# high = 10
# 
# while high - low >0.001:
#     r = (low + high ) / 2
#     areaCircle = 3.14159*(r**2)
#     areaHex = (3*math.sqrt(3))/2 *(r**2)
#     
#     if areaCircle - areaHex > 24:
#         high  = r
#     else:
#         low = r
#     
#     r = (low + high) / 2
# 
# 
# print(r)
# =============================================================================

# =============================================================================
# n = int(input('Enter: '))
# power = 1
# 
# while 2*power <= n:
#     print(power, 'before')
#     power *= 2
#     print(power)
# =============================================================================
    
# =============================================================================
# product = 1
# for i in range(1,6):
#     product *= i
# 
# print(str(product))
# =============================================================================


# =============================================================================
# ruler = '1'
# print(ruler)
# for i in range(2, 4 + 1):
#     ruler = ruler + ' ' + str(i) + ' ' + ruler
#     print(ruler)
# =============================================================================
    
# =============================================================================
# n = int(input('Enter: '))
# 
# for i in range(1, n+1):
#     print(i,end= " ")
# print()
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if (i % j == 0) or (j % i == 0):
#             print('* ', end ='')
#         else:
#             print('  ',end='')
#     print(i)
# 
# =============================================================================

# =============================================================================
# a = []
# for i in range(n):
#     a += [0.0]
# 
# #reverse an array
# a = [1, 2, 3, 4, 5, 6]
# n = len(a)
# 
# for i in range(n // 2):
#     temp = a[i]
#     a[i] = a[n - 1-i]
#     a[n - 1-i] = temp
# 
# print(a)
# 
# total = 0.0
# for v in a:
#     total += v
#     average = total / len(a)
#     
# float(sum(a)) /len(a)
# =============================================================================
# =============================================================================
# a = [1, 2, 3, 4, 5, 6]
# for i in a:
#     print(i, end=" ")
# =============================================================================

# =============================================================================
# a = [1, 2, 3, 4, 5, 6]  
# y = a[2:6]
# 
# 
# for v in y:
#     print(v, end= " ")
#     
# b = [0.0]*n  
# =============================================================================

# =============================================================================
# #playing card representation
# SUITS = ['Clubs', 'Daimonds', 'Hearts', 'Spades']
# RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
#          'Jack', 'Queen', 'King', 'Ace']
# 
# rank = random.randrange(0, len(RANKS))
# suits = random.randrange(0, len(SUITS))
# 
# print(RANKS[rank] + ' of ' + SUITS[suits])
#     
# deck = []
# 
# for rank in RANKS:
#     for suits in SUITS:
#         card = rank + ' of ' + suits
#         deck += [card]
# 
# #shuffle deck
# 
# n = len(deck)
# for i in range(n):
#     r = random.randrange(i, n)
#     temp = deck[r]
#     deck[r] = deck[i]
#     deck[i] = temp
# 
# random.shuffle(deck) #same as code above 
# =============================================================================

# =============================================================================
# m = int(input('Enter sameple size: '))
# n = int(input('Enter range: '))
# 
# perm = [0]*n
# for i in range(n):
#     perm[i] = i 
# 
# # =============================================================================
# # perm = []
# # 
# # for i in range(n):
# #     perm += [i]
# # =============================================================================
# 
# #permutation
# for i in range(m):
#     r = random.randrange(i, n) #each iteration range changes 
#     
#     temp = perm[r]
#     perm[r] = perm[i]
#     perm[i] = temp
#     
# for i in range(m):
#     print(str(perm[i]) + ' ' ) #replcae str(perm[i]), with deck[perm[i]] for a random poker hand
# print()
# 
# 
# #random sample 
# random.sample(a, k) #k sie of randomly sampled array
# =============================================================================


# =============================================================================
# harmonic = [0.0]*n+1
# for i in range(1, n+1):
#     harmonic[i] = harmonic[i-1] + 1.0 /i
# 
# m = 
# MONTHS = ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', ..]
# 
# print(MONTH[m])
# =============================================================================


# =============================================================================
# #coupon collector simulation
# n = int(input('Enter: '))
# 
# count = 0 #total number of collected tracker
# collectedCount = 0
# isCollected = [False]*n #initializes array of size n, sets  all elements to to false
# 
# while collectedCount < n: #loop condition ensures it terminates when we have all possible coupons
#     #generate another coupon
#     value = random.randrange(0, n)
#     count += 1
#     if not isCollected[value]:  #tracks if we have encountered value before
#         collectedCount += 1
#         isCollected[value] = True 
# print(count)
# =============================================================================

# =============================================================================
# #fixed probability gamblers ruin
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
#         if random.random() < fixed_prob:
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
