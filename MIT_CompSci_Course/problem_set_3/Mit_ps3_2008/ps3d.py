# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 16:26:18 2024

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

def constrainedMatchPair(firstMatch, secondMatch, length):
    tu = ()
    for i in firstMatch:
        if i + length + 1 in secondMatch:
            tu += (i,)
    return tu 

def subStringMatchExactlyOneSub(target,keyString):
    allAnswers = ()
    for i in range(len(keyString)):
        keyString1 = keyString[:i]
        keyString2 = keyString[i+1:]
        start1 = subStringMatchExact(target, keyString1)
        start2 = subStringMatchExact(target, keyString2)
        filtered = constrainedMatchPair(start1, start2, len(keyString1))
        
        allAnswers += filtered
    return allAnswers 

