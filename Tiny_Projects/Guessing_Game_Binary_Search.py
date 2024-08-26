# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 11:33:28 2024

@author: Edward kagho
"""

# =============================================================================
# import random
# 
# def hint(mid):
#     ans = input('Would you like a hint? (yes or no): ')
#     if ans.lower() == 'yes':
#         print('Try', mid)
# 
# secretnum = random.randrange(1, 21)
# lowerbound = 1
# upperbound = 20
# 
# print(f'Guess my number between {lowerbound} and {upperbound} with the fewest guesses: ')
# 
# guess = int(input())
# 
# while guess != secretnum: 
#     if guess < secretnum:
#         print('Too low, guess again')
#         lowerbound = guess + 1
#     else:
#         print('Too high, guess again')
#         upperbound = guess - 1
#     
#     mid = (lowerbound + upperbound) // 2
#     hint(mid)
#     
#     guess = int(input('Enter another guess: '))
# 
# print('Congratulations. You guessed it!')
# =============================================================================


import random

def hint(mid):
    ans = input('Would you like a hint? (yes or no): ')
    if ans.lower() == 'yes':
        print('Try', mid)

secretnum = random.randrange(1, 21)
lowerbound = 1
upperbound = 20

print(f'Guess my number between {lowerbound} and {upperbound} with the fewest guesses: ')

guess = int(input())
guess_count = 1

while guess != secretnum and guess_count <= 10: 
    if guess < secretnum:
        print('Too low, guess again')
        lowerbound = guess + 1
    else:
        print('Too high, guess again')
        upperbound = guess - 1
    
    mid = (lowerbound + upperbound) // 2
    hint(mid)
    
    guess = int(input('Enter another guess: '))
    guess_count += 1
    
if guess_count > 10:
    print("You should be able to do better!")
else:
    print('Either you know it or got lucky')
    
#print('Congratulations. You guessed it!')

