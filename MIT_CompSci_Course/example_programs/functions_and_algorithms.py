# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 08:27:26 2024

@author: Lenovo
"""

def isPalindrome(st):
    if len(st) < 2:
        return True
    else:
        if st[0] != st[len(st)-1]:
            return False
        else:
            return isPalindrome(st[1:len(st)-1])
        
isPalindrome('hc')

def isPalindrame2(st):
    if len(st) <= 1: return True 
    else: return st[0] == st[-1] and isPalindrome[1:-1]
    
    
def add(x, y):
    return x + y
add(1, 2)


def exp1(a, b):
    ans = 1
    while (b > 0):
        ans *= a 
        b -= 1 
    return ans 

def exp2(a, b):
    if b == 1:
        return 1 
    else:
        return a*exp2(a, b-1)
    
def Towers(size, fromStack, toStack, spareStack):
    if size == 1:
        print( 'Move disk from', fromStack, 'to', toStack)
    else:
        Towers(size-1, fromStack, spareStack, toStack)
        Towers(1, fromStack, toStack, spareStack)
        Towers(size-1, spareStack, toStack, fromStack)
        
def bsearch(ls, e, first, last):
    print(first, last)
    if (last - first) < 2: 
        return ls[first] == e or ls[last] == e
    mid = (first + last) // 2
    if ls[mid] == e:
        return  True 
    if ls[mid] > e: 
        return bsearch(ls, e, first, mid - 1)
    return bsearch(ls, e, mid+1, last)

def search(s, e):
    return bsearch(s, e, 0, len(s)-1)
    

def selsort(ls):
    print(ls)
    for i in range(len(ls)):
        for j in range(i+1, len(ls)):
            if ls[j] < ls[i]:
                ls[j], ls[i] = ls[i], ls[j]
        print(ls)
        
ls = [3, 4, 10, 8, 2]
#selsort(ls)

def bubbleSort(ls): 
    for i in range(len(ls)):
        #print(ls)
        for j in range(len(ls) - 1):
            if ls[j] > ls[j+1]:
                ls[j+1], ls[j] = ls[j], ls[j+1]
        print(ls)


#bubbleSort(ls)

def bubbleSort2(ls):
    swapped = True
    while swapped:
        swapped = False
        for j in range(len(ls) - 1):
            if ls[j] > ls[j+1]:
                ls[j+1], ls[j] = ls[j], ls[j+1]
                swapped = True
        print(ls)
    #print(ls)

#bubbleSort2(ls)



def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i = i + 1 
        else:
            result.append(right[j])
            j = j + 1 
    while ( i < len(left)):
        result.append(left[i])
        i = i + 1
    while (j < len(right)):
        result.append(right[j])
        j = j + 1
    return result

def mergesort(ls):
    print(ls)
    if len(ls) < 2:
        return ls[:]
    else:
        middle = len(ls) // 2
        left = mergesort(ls[:middle])
        right = mergesort(ls[middle:])
        together = merge(left,right)
        print('merged', together)
        return together

mergesort(ls)