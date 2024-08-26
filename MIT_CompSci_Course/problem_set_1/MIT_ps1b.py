# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 01:10:36 2024

@author: Lenovo
"""

annual_salary = float(input("Enter your starting annual"
                            "salary: "))
semi_annual_raise = float(input("Enter your semi-annual raise: "))
                          
portion_saved = float(input("Enter the portion of "
                            "salary to be saved: "))

total_cost = float(input("Enter the cost of your dream "
                         "home: " ))

portion_down_payment = 0.25 * total_cost 
currentSavings = 0   #current savinf starting from zero
interestRate = 0.04
portion_saved_amount = portion_saved * (annual_salary/12) 
months = 0    #setting months to zero to be counted
returnInvest = (currentSavings * interestRate) / 12  

while currentSavings < portion_down_payment:
    currentSavings += returnInvest + portion_saved_amount #updates current savings in a loop
    returnInvest = (currentSavings * interestRate) / 12 
    months += 1
    
    if months % 6 == 0:
        annual_salary += semi_annual_raise * annual_salary
        portion_saved_amount = portion_saved * (annual_salary/12)
    
print("It will take", months, "months to have enough money for the down payment")