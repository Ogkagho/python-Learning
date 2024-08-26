# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 16:07:43 2024

@author: Lenovo
"""

def subStringMatchExact(targString, keyString):
    points = ()
    s = 0   #initial start 0 
    while s != -1:  #ensures loop terminates if s is larger than targetstring
        s = targString.find(keyString, s) #finds index of substring occurrence 
        points += (s,)
        if s == -1:
            points = points[0:-1]
            return points 
        s += 1   #moves start to the next index, based on previous found index

subStringMatchExact('atgacatgcacaagtatgcat', 'atgc')