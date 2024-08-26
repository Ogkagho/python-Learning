# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 10:09:26 2024

@author: Edward kagho
"""

annual_salary = float(input("Enter your starting annual salary: "))
semi_annual_raise = 0.07
interestRate = 0.04
down_payment = 0.25
cost_of_house = 1000000
down_payment_amount = down_payment * cost_of_house
tempSalary = annual_salary
steps = 0
low = 1
high = 10000
rate = (low + high) / 2

while steps < 1000:
    currentSavings = 0
    returnInvest = 0
    annual_salary = tempSalary
    months = 0
    rate_decimal = rate / 10000
    portion_saved_amount = rate_decimal * (annual_salary / 12)

    while months < 36:
        returnInvest = (currentSavings * interestRate) / 12
        currentSavings += returnInvest + portion_saved_amount
        months += 1

        if months % 6 == 0:
            annual_salary += semi_annual_raise * annual_salary
            portion_saved_amount = rate_decimal * (annual_salary / 12)

    if abs(currentSavings - down_payment_amount) <= 100:
        break
    else:
        if currentSavings < down_payment_amount:
            low = int(rate)
            rate = (low + high) // 2 
        elif currentSavings > down_payment_amount:
            high = int(rate)
            rate = (low + high) // 2 
        steps += 1

if abs(currentSavings - down_payment_amount) <= 100:
    print("Best savings rate:", rate_decimal)
    print("Steps in bisection search:", steps)
else:
    print("It is not possible to pay the down payment in three years.")