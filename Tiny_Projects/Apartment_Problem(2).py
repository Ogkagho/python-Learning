# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 12:12:22 2024

@author: Lenovo
"""

def profit(units, rentOccupy, increaserent, maintain, total_units):
    rent = rentOccupy + (total_units - units) * increaserent
    return (rent * units) - (maintain * units)

def maximizeProfit():
    # Prompt the user for inputs
    rentOccupy = float(input("Enter the rent to occupy all the units: "))
    increaserent = float(input("Enter the increase in rent that results in a vacant unit: "))
    maintain = float(input("Enter the amount to maintain a rented unit: "))
    total_units = int(input("Enter the total number of units: "))
    
    low = 0
    high = total_units
    epsilon = 1e-5  # Small tolerance value for convergence
    
    while high - low > epsilon:
        mid1 = low + (high - low) / 3
        mid2 = high - (high - low) / 3
        
        profit1 = profit(mid1, rentOccupy, increaserent, maintain, total_units)
        profit2 = profit(mid2, rentOccupy, increaserent, maintain, total_units)
        
        if profit1 < profit2:
            low = mid1
        else:
            high = mid2
    
    optimal_units = (low + high) / 2
    max_profit = profit(optimal_units, rentOccupy, increaserent, maintain, total_units)
    
    print(f"The number of units to be rented to maximize the profit is: {int(optimal_units)}")
    print(f"The maximum profit is: ${max_profit:.2f}")

# Call the function
maximizeProfit()
