# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 14:53:03 2024

@author: Edward kagho
"""
import random

def intgenerator(c):
    num1 = random.randrange(1, 10**c)
    num2 = random.randrange(1, 10**c)
    return num1, num2

def operatorGenerator(n, n1, n2):
    global ans
    if n == 1:
        print(f'How much is {n1} + {n2}? ')
        ans = int(input())
        return n1 + n2 
    elif n == 2:
        print(f'How much is {n1} - {n2}? ')
        ans = int(input())
        return n1 - n2
    elif n == 3:
        print(f'How much is {n1} * {n2}? ')
        ans = int(input())
        return n1 * n2 
    elif n == 4:
        print(f'How much is {n1} // {n2}? ')  # Integer division
        ans = int(input())
        return n1 // n2

difficulty = int(input('Select difficulty level, 1 or 2: '))
operator = int(input('Select the arithmetic operation you want to practice: '
                     '1 for addition, 2 for subtraction, 3 for multiplication, '
                     '4 for division, 5 for random.'))

if operator == 5:
    operator = random.randint(1, 4)

n1, n2 = intgenerator(difficulty)
ans1 = operatorGenerator(operator, n1, n2)

if abs(ans1 - ans) < 0.001:
    choice = random.randrange(1, 4)
    if choice == 1:
        print('Very good')
    elif choice == 2:
        print('Nice Work')
    else:
        print('Keep up the good Work')
else:
    while ans != ans1:
        print('No. Please try again.')
        ans1 = operatorGenerator(operator, n1, n2)
    choice = random.randrange(1, 4)
    if choice == 1:
        print('Very good')
    elif choice == 2:
        print('Nice Work')
    else:
        print('Keep up the good Work')

