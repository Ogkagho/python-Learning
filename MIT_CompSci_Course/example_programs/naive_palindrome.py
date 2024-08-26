# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 12:55:35 2024

@author: Lenovo
"""

def silly():
    res= []
    done = False;
    while not done:
        elem = input("Enter element. Return when done. ")
        if elem == '':
            done = True
        else:
            res.append(elem)
            
    #print('res should be [1, a, 2]', res)   # error miostl likey not in the first part    
    tmp = res[:] #previous tmp = res, caused an error
    #print('temp', tmp, 'res', res)
    tmp.reverse() #culprit 
    #print('temp', tmp, 'res', res)
    isPal = (res == tmp)
    #print('temp', tmp, 'res', res, 'ispal', isPal)
    if isPal:
        print('is a palaindrome')
    else:
        print('is NOT a palindrome')
        
        
    
silly()
