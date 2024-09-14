# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 14:23:48 2024

@author: Lenovo
"""
import random

def intgenerator(c):
    num1 = random.randrange(10**(c-1),10**c)
    num2 = random.randrange(10**(c-1),10**c)
    
    return num1, num2

valid = input('Start game (1): ')

while valid != '0':
    while valid != "1":
        print("Please enter 1 to start game: ")
        valid = input('Start game (1): ')
        
    difficulty = int(input('Select difficulty level, 1 or 2: '))
    while difficulty != 1 and difficulty != 2:
        print("Invalid input.\n Enter a valid input")
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
        entry = 1
        while ans != n1*n2 or entry != 0:
            choice = random.randrange(1,4)
            if choice == 1:
                print('No. Please try again.')
            elif choice == 2:
                print("Wrong, you can do it try again")
            else:
                print("Incorrect")
            entry = input("Enter (0) to quit, any other integer to continue: ")
            if entry != "0":
                ans = int(input(f'How much is {n1} times {n2}? '))
            else:
                print("Sorry to see you go")
            
        choice = random.randrange(1,4)
        if choice == 1:
            print('Very good')
        elif choice == 2:
            print('Nice Work')
        else:
            print('Keep up the good Work')
    valid = input('End (0) or conitnue(1): ')

    
