# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 21:57:09 2024

@author: Lenovo
"""

annual_salary = float(input("Enter your starting annual"
                            "salary: "))
portion_saved = float(input("Enter the portion of "
                            "salary to be saved: "))
total_cost = float(input("Enter the cost of your dream "
                         "home: " ))

portion_down_payment = 0.25 * total_cost 
currentSavings = 0   #current savinf starting from zero
interestRate = 0.04
portion_saved *= annual_salary/12  #the portion(percent) from the user is multiplied
                                   #is the monthly salary
months = 0    #setting months to zer to be counted

returnInvest = (currentSavings * interestRate) / 12  

while currentSavings < portion_down_payment:
    currentSavings += returnInvest + portion_saved #updates current savings in a loop
    months += 1    #updates months
    returnInvest = (currentSavings * interestRate) / 12   #calculates return with new savings
    
print("It will take", months, "months to have enough money for the down payment")



