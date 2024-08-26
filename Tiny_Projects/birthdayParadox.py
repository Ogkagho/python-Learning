# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 16:32:39 2024

@author: Edward kagho
"""

import random

months = { 1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
          7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}

def generateBirthday(n):
    #print(f'Here are {n} birthdays:')
    birthdays = []
    for i in range(n):
        month = random.randrange(1, 13) 
        day = random.randrange(1, 32)
        if not (month == 2 and day > 29):
            birthdays.append(f'{months[month]} {day}')
    return birthdays

def getMatch(birthdays, show=False):
    for i in range(len(birthdays)):
        for j in range(i+1, len(birthdays)):
            if birthdays[i] == birthdays[j]:
                if show:
                    print(f'In this simulation, multiple people have a birthday on {birthdays[i]}')
                return 1
    return 0

def simulation(n):
    print("Let's run 100,000 simulations.")
    TRIALS = 100000
    count = 0
    for i in range(TRIALS):
        ls = generateBirthday(n)
        count += getMatch(ls)
        if i % 10000 == 0:
            print(f"Simulation Running... {i}'th trial" )
            
    print("Simulation done")
    
    prob = (count / TRIALS) * 100
    print(f'Out of 100,000 simulations of {n} people, there was a ' \
          f'matching birthday in that group {count} times. This means '\
          f'that {n} people have a {prob:.2f} % chance of sharing a birthday')



print('Birthday Paradox, By Ed, adapted from Al sweigwart')
print('How many birthdays shall I generate? )')
ans = int(input())
ls = generateBirthday(ans)

print(", ".join(ls))
getMatch(ls, show=True)

simulation(ans)


