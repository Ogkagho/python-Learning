# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 13:22:13 2024

@author: Lenovo
"""

def bubbleSort(L):
    print(L)
    for j in range(len(L)):
        for i in range(len(L)-1):
            if L[i] > L[i+1]:
                temp = L[i]
                L[i] = L[i+1]
                L[i+1] = temp
                print(L)
    print(L)
    
s = [4, 6, 2, 1, 6, 8]

bubbleSort(s)

def bubbleSort(L):
    print(L)
    for j in range(len(L)):
        swapped = False
        for i in range(len(L)-1):
            if L[i] > L[i+1]:
                temp = L[i]
                L[i] = L[i+1]
                L[i+1] = temp
                swapped = True
                print(L)
        if not swapped : return print(L)
    
    
s = [4, 6, 2, 1, 6, 8]

bubbleSort(s)