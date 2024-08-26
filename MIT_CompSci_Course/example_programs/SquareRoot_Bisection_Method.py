# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 23:38:27 2024

@author: Lenovo
"""

def squareRootBi(x, epsilon):
    assert x >=0, 'x must be a non-negative integer'
    assert epsilon > 0, 'epsilon must be greater than zero'
    
    low = 0
    high = x
    guess = (low + high )/2.0
    ctr = 1
    
    while abs(guess**2 - x) > epsilon and ctr <= 100:
        if guess**2 < x:
            low = guess
        else:
            high = guess
        guess = (low + high) /2.0
        ctr += 1
    assert ctr <= 100, 'Iteration count reached'
    print(' Bi method. number of iterations:', ctr, 'Estimate: ', guess)
    return guess

#
#def improve(x, y):
#    return (x + y/x)/2
#
#def squareRoot(x, epsilon):
#    guess = 1
#    ctr = 0
#    while abs(guess**2 - x) > epsilon and ctr <= 100:
#        if abs(guess**2 - x) < epsilon:
#            return guess
#        else:
#           guess = improve(guess, x)
#       ctr += 1
        
 