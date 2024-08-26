# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 15:02:37 2024

@author: Lenovo
"""


#substring match iterative
def countSubStringMatch(targString, keyString):
    count = 0
    s = 0   #initial start 0 
    while s < len(targString):  #ensures loop terminates if s is larger than targetstring
        s = targString.find(keyString, s) #finds index of substring occurrence 
        if s == -1:
            return count
        s += 1   #moves start to the next index, based on previous found index
        count += 1
    
print(countSubStringMatch('abcababc','ab'))
print(countSubStringMatch('aaaaaa','aa'))
print(countSubStringMatch('abcababc','ab'))
# =============================================================================
# def countSubStringMatch(targString, keyString):
#     count = 0
#     s = 0
#     for v in range(len(targString)):
#         s = targString.find(keyString, s)
#         if s == - 1:
#             return count
#         s += 1
#         count += 1
# =============================================================================

#recursive
def countSubStringMatchRec(targetString, keyString, start, count=0):
    if len(targetString) < 2:
        if targetString.find(keyString, start) != 1:
            return count + 1
        else:
            return count
    if targetString.find(keyString, start) != -1:
        start = targetString.find(keyString, start) + 1
        return 1 + count + countSubStringMatchRec(targetString, keyString, start, count=0)
    return  count

print(countSubStringMatchRec('aaaaaa','aa', 0))
print(countSubStringMatchRec('abcababc','ab', 0))
print(countSubStringMatchRec('this string does not contain the key', 'notfound', 0))
