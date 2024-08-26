# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 03:32:21 2024

@author: Lenovo
"""

# =============================================================================
# x = int(input())
# y = int(input())
# z = int(input())
# 
# if x % 2 == 1 or y % 2 == 1 or z % 2 == 1:
#     if x > y and x > z and x % 2 == 1:
#         print(x)
#     elif y > z and y % 2 == 1:
#         print(y)
#     else:
#         print(z)
# else:
#     if x < y and x < z:
#         print(x)
#     elif y < z:
#         print(y)
#     else:
#         print(z)
# 
# 
# answer = min(x, y, z) #assumming they are all even, and finding th minimum
# #checks if odd and larger than previous valus, updates accordingly 
# if x % 2 != 0:  
#     answer = x
# if y % 2 != 0 and y > answer:
#     answer = y
# if z % 2 != 0 and z > answer:
#     answer = y 
# print(answer)
# 
# 
# print((x if x > z else z) if  x > y else (y if y > z else z))
# 
# #finger exercise 
# birthDay = input('Enter birthday(mm/dd/yyyy):')
# 
# print(f'You were born in the year {birthDay[6:]}') 
# =============================================================================

# =============================================================================
# num_x = int(input('How many times should i print the letter X ?'))
# to_print = ''
# track = 0
# while track < num_x:
#     to_print += 'X'
#     track += 1 
# print(to_print)
# =============================================================================

# =============================================================================
# x = 0
# while x < 10:
#     num = int(input())
#     large = 0
#     odd = 0
#     if num % 2 != 0 and num > large:
#         large = num 
#         odd += 1
#     x += 1
#     
# if odd > 0:
#     print(large)
# else:
#     print('No odd numbers entered')
# =============================================================================

# =============================================================================
# sum1 = 0
# for i in range(3, 1000, 2):
#     isPrime = True 
#     for j in range(2, i):
#         if i % j == 0:
#             isPrime = False
#             break 
#     if isPrime:
#         sum1 += i
# print(sum1)
# =============================================================================

# =============================================================================
# import math
# sum1 = 0 
# for i in range(3, 1000,2):
#     isPrime = True
#     for j in range(2, int(math.sqrt(i)) + 1):
#         if i % j == 0:
#             isPrime = False
#             break
#     if isPrime : 
#         sum1 += i
# =============================================================================
    
    
# =============================================================================
# n = int(input())
# fact = 2
# found = False
# while fact*fact <= n:
#     if n % fact == 0:
#         print(fact, 'is the smallest divisor of', n)
#         found = True
#         break
#     fact += 1
# if not found:
#     print(n, 'is a prime number')
# =============================================================================

# =============================================================================
# n = int(input())
# smallest_div = None
# for i in range(2, n):
#     if n % i == 0:
#         smallest_div = i 
#         break 
# if smallest_div != None:
#     #print('Smallest divisor of', n, 'is', smallest_div)
#     print('The largest divisor of', n, 'is', n//smallest_div)
# else:
#     print(n, 'is  a prime number')
# =============================================================================

# =============================================================================
# n = int(input())
# smallest_div = None
# 
# if n % 2 == 0 and n!= 2:
#     smallest_div = 2
# else:
#     for i in range(3, n, 2):
#         if n % i == 0:
#             smallest_div = i 
#             break 
# if smallest_div != None:
#     #print('Smallest divisor of', n, 'is', smallest_div)
#     print('The largest divisor of', n, 'is', n//smallest_div)
# else:
#     print(n, 'is  a prime number')
# =============================================================================


# =============================================================================
# #finger exercise
# n = int(input())
# found = False
# for root in range(1, n//2+1):
#     for pwr in range(2, 6):
#         if root**pwr == n:
#             found = True 
#             break
#     if found:
#         break 
# if found:
#     print(root, pwr)
# else:
#     print('not found')
# =============================================================================

# =============================================================================
# #bisection search, sqrt 
# x = int(input()) 
# epsilon = 0.001
# if x < 0:
#     print('Does not exist')
# else:
#     low = 0
#     high = max(1, x)
#     ans = (high + low) / 2
#     while abs(ans**2 - x) >= epsilon:
#         if ans**2 < x:
#             low = ans 
#         else:
#             high = ans 
#         ans = (high + low) / 2
#     print(ans, 'is an approx. to the square root of', x)
# =============================================================================

# =============================================================================
# def find_root(x, power, epsilon):
#     if x < 0 and power%2 == 0:
#         return None 
#     low = min(-1, x)
#     high = max(1, x) 
#     #nisection search 
#     ans = (high + low) / 2
#     while abs(ans**power - x) >= epsilon:
#         if ans**power < x:
#             low = ans 
#         else:
#             high = ans 
#         ans = (high + low) /2 
#     return ans 
# 
# def test_find_root(x_vals, powers, epsilons):
#     for x in x_vals:
#         for p in powers:
#             for e in epsilons:
#                 result = find_root(x, p, e)
#                 if result == None:
#                     val = 'No root exists'
#                 else:
#                     val = 'Okay'
#                     if abs(result**p - x)> e:
#                         val = 'Bad'
#                 print(f'x = {x}, power = {p}, epsilon = {e} : {val}') 
# x_vals = (0.25, 8, -8)
# powers = (1, 2, 3)
# epsilons = (0.1, 0.001, 1)
# test_find_root(x_vals, powers, epsilons)
# =============================================================================


# =============================================================================
# def mult(x = 1, y = 1):
#     '''returns multiple of arguments, if one ag=rgument is specified returns that argument'''
#     return x*y 
# 
# def harmonic(n):
#     if n == 1:
#         return 1 
#     return harmonic(n-1) + 1/n
# =============================================================================

# =============================================================================
# def log(x, base, epsilon):
#     '''Assumes x and epsilon int or float, base and int,
#             x > 1, epsilon & power >= 1
#         Returns float y such that base**y is within epsilon
#     of x'''
#     low = 0
#     high = x
#     guess = (low + high) / 2 
#     
#     while abs(base**guess - x) > epsilon:
#         if base**guess < x:
#             low = guess 
#         else:
#             high = guess 
#         guess = (low + high) / 2
#     return guess
# =============================================================================

# =============================================================================
# 
# def find_root_bounds(x, power):
#     low = min(-1, x)
#     high = max(1, x)
#     return low, high    
# 
# def square(x):
#     return x*x 
# 
# def bisection_solve(x, eval_ans, epsilon, low, high):
#     
#     ans = (high + low) /2.0
#     while abs(eval_ans(ans) - x) >= epsilon:
#         if eval_ans(ans) < x:
#             low = ans 
#         else:
#             high = ans 
#         ans = (high + low) / 2
#     return ans 
# 
# low, high = find_root_bounds(99, 2)
# #print(bisection_solve(99, square, 0.01, low, high))
# 
# 
# #lambda x, y: x*y  #anonymous naming of functions
# print(bisection_solve(4, lambda ans: ans**2, 0.01, low, high))
# =============================================================================

# =============================================================================
# divide = lambda x, y: None if y == 0 else x/y
# result = divide(10, 9)
# print(result)
# =============================================================================

# =============================================================================
# result = (lambda x, y: None if y == 0 else x/y)(10, 2)
# print(result)
# 
# def create_eval_ans():
#     power = input('Enter a positive integer: ')
#     return lambda ans: ans**int(power)
# eval_ans = 
# =============================================================================


# =============================================================================
# def find_last1(s, sub):
#     new_string = s[::-1]
#     new_sub = sub[::-1]
#     reversed_index = new_string.find(new_sub)
#     
#     if reversed_index != -1:
#         return len(s) - reversed_index - len(sub)
#     else:
#         return None
# =============================================================================

#finger exercise 
def find_last(s, sub):
    last_index = -1
    current_index = s.find(sub)
    
    while current_index != -1:
        last_index = current_index
        current_index = s.find(sub, last_index + 1)
    
    return last_index if last_index != -1 else None

# Example usage
print(find_last('aabbaabbaac', 'aa'))  

        

