# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 17:19:02 2024

@author: Lenovo
"""

#binary search 

#def binarySearch(list1, n):
#    lowerBound = 0
#    upperBound = len(list1) - 1
#    mid = (lowerBound + upperBound) // 2 
#    guess = list1[mid]
    
#    while upperBound - lowerBound > 0:
#        if guess == n:
#            return True 
#        elif guess < n:
#            lowerBound = mid + 1
#        else:
#            upperBound = mid - 1 
#        mid = (lowerBound + upperBound) // 2
#        guess = list1[mid]
       
#    return False

s = range(1000)

#binarySearch(s, -1)


def bsearch(s, e, first, last, calls):
    print (first, last, calls)
    if (last - first) < 2 : return s[first] == e or s[last] == e
    mid = first + (last - first) // 2
    if s[mid] == e: return True 
    if s[mid] > e: return bsearch(s, e, first, mid-1, calls + 1)
    return bsearch(s, e, mid + 1, last, calls + 1) 

def search(s, e):
    print (bsearch(s, e, 0, len(s) - 1, 1))
    
    
search(s, 50)