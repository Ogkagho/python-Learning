# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 14:23:48 2024

@author: Lenovo
"""
import random

def product(*args):
    prod = 1
    for v in args:
        prod *= v
    return prod

product(1, 2, 4, 5)

def intgenerator(c):
    num1 = random.randrange(1,10**c)
    num2 = random.randrange(1,10**c)
    
    return num1, num2

valid = input('Start game (1): ')
while valid != '0':
    difficulty = int(input('Select difficulty level, 1 or 2: '))
    n1, n2 = intgenerator(difficulty)
    ans = int(input(f'How much is {n1} times {n2} ? '))
    
    if ans == n1*n2:
        choice = random.randrange(1,4)
        if choice == 1:
            print('Very good')
        elif choice == 2:
            print('Nice Work')
        else:
            print('Keep up the good Work')
    else:
        while ans != n1*n2:
            print('No. Please try again.')
            ans = int(input(f'How much is {n1} times {n2}? '))
        choice = random.randrange(1,4)
        if choice == 1:
            print('Very good')
        elif choice == 2:
            print('Nice Work')
        else:
            print('Keep up the good Work')
    valid = input('End (0) or conitnue(1): ')

    