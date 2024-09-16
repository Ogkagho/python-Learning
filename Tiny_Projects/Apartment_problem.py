# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 11:33:13 2024

@author: Lenovo
"""

# =============================================================================
# def maximizeProfit(rentOccupy, increaserent, maintain):
#     """
#     Function to calculate the number of units to be rented 
#     to maximize profits.
#     Assumes initial number of units is 50.
#     prarameters: The rent to occupy all the units.
#                  The increase in rent that results in a vacant unit.
#                  Amount to maintain a rented unit.
#     return a tuple, of the maximum profit and the number of units 
#     """
#     maxProfit = 0
#     for i in range(49):
#         n = 50 - i  #decreases the number of units each iteration, based on the rent 
#         profit = n * (rentOccupy - maintain) #calcullates profit, each iteration accounting for changes in rent and units
#         
#         if profit > maxProfit:
#             maxProfit = profit 
#             optimalUnits = n
#         rentOccupy += increaserent #approriately increases the rent each iteration 
#          
#     return maxProfit, optimalUnits
# 
# maximizeProfit(600, 40, 27)
# =============================================================================

    
# =============================================================================
# rentOccupy = float(input('Enter the amount of rent to occupy all the units: '))
# increaseRent = float(input('Enter the increase in rent that results in a vacant unit: '))
# maintain = float(input('Enter the amount to maintain a rented unit: '))
# maxProfit = 0
# optimalUnits = 0
#     
# for i in range(50):
#     n = (50 - i)
#     profit = n*(rentOccupy - maintain)
#     if profit > maxProfit:
#         maxProfit = profit
#         optimalUnits = n
#     rentOccupy += increaseRent
#     
# print(f'The number of units to be rented to maximize profit is {optimalUnits} units.')
# =============================================================================

