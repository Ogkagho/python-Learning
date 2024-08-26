# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 11:45:28 2024

@author: Lenovo
"""

def selSort(L):
    for i in range(len(L)-1):
        minIndex = i
        minVal = L[i]
        j = i + 1
        while j < len(L):
            if minVal > L[j]:
                minIndex = j
                minVal = L[j]
            j = j + 1
        temp = L[i]
        L[i] = L[minIndex]
        L[minIndex] = temp
        print(L)


s = [1, 4, 6, 8, 0, 6, 8]

selSort(s)

        