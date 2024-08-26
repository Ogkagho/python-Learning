# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 02:38:45 2024

@author: Lenovo
"""
# =============================================================================
# 
# target = "atgacatgcacaagtatgcat"
# key = "atgc"
# index = target.find(key,6)
# 
# print(index)
# =============================================================================

# =============================================================================
# def countSubStringMatch(target, key):
#     #print(target)
#     countInstance = 0
#     while len(target) >= len(key):
#         if target.find(key) >= 0:
#             countInstance += 1
#         target = target[target.find(key)+len(key) :len(target)]
#         #print(target)
#     return countInstance
#     
# #countSubStringMatch("atgacatgcacaagtatgcat", "atgc")
# 
# 
# def countSubStringMatchRecursive(target, key):
#     if target.find(key) >= 0:
#         countInstance = 1
#         return countInstance + countSubStringMatchRecursive(target[target.find(key)+len(key) :len(target)], key)
#     else:
#         countInstance = 0
#         return countInstance
#     
# 
# #countSubStringMatchRecursive("atgacatgcacaagtatgcat", "atgc")
# =============================================================================

# =============================================================================
# def subStringMatchExact(target, key): 
#     exactposition = ()
#     start = 0
#     while len(target) >= len(key):
#         if target.find(key) >= 0: 
#             exactposition += (target.find(key) + start,)
#         target = target[target.find(key)+len(key) :len(target)]
#         start += target.find(key) + len(key) - 1
#         print(target)
#         
#     return exactposition
# 
# target = input('Enter: ')
# key = input('Enter: ')
# 
# print(subStringMatchExact(target,key))
# =============================================================================

# =============================================================================
# def subStringMatchExact(target, key):
#     exactposition = ()
#     start = 0
#     while len(target) - start >= len(key):
#         index = target.find(key, start)
#         if index >= 0:
#             exactposition += (index,)
#             start = index + 1  # Move to the next character after the found key
#         else:
#             break
#         
#     return exactposition
# 
# print(subStringMatchExact("atgacatgcacaagtatgcat", "atgc"))
# =============================================================================


# =============================================================================
# def subStringMatchExactRec(target, key, start, exactposition):
#     if len(target) - start >= len(key):
#         index = target.find(key, start)
#         if index == -1:
#             return exactposition
#         exactposition += (index,)
#         return subStringMatchExactRec(target, key, index + 1, exactposition)
#     else:
#         return exactposition
# 
# exactposition = ()
# print(subStringMatchExactRec("atgacatgcacaagtatgcat", "atgc", 0, exactposition))
# 
# =============================================================================
