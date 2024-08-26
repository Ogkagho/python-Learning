# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 20:56:48 2024

@author: Edward kagho
"""

import math

def isPrime(n):
    #if n is 2 return true 
    if n == 2:
        return True 
    #if n is even returns false
    if n % 2 == 0:
        return False 
    #range stops at the sqrt of n , and iterates odd numbers
    for i in range (3, int(math.sqrt(n))+ 1, 2):
        if n % i == 0:
            return False
    return True 

n = int(input('Enter a large integer: '))

#initalize sumLofPrime to zero
sumLogPrime = 0

#runs until it reachs n and checks whethet i is prime 
for i in range(2, n+1):
    if isPrime(i):
        sumLogPrime += math.log(i)
        
print("The sum of the log of primes from 2 to ", n, "is", int(sumLogPrime))
print("The ratio of the sum and", n, "is", n / sumLogPrime)
    