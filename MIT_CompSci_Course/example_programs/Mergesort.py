# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 02:15:15 2024

@author: Lenovo
"""


def merge(left, right):
     result = []
     i,j = 0,0
     while i < len(left) and j < len(right):
         if left[i] <= right[j]:
             result.append(left[i])
             i += 1
         else:
             result.append(right[j])
             j = j+ 1
             
     while i < len(left):
         result.append(left[i])
         i += 1
     while j < len(right):
         result.append(right[j])
         j += 1
     return result
        
            

def mergeSort(L):
    print(L)
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left = mergeSort(L[:middle])
        right = mergeSort(L[middle:])
        together = merge(left,right)
        print('merged', together)
        return together
        
        
s = [5, 7, 1, 4, 8, 9, 10, 90]

mergeSort(s) 


# =============================================================================
# def merge(left, right, compare):
#     result = []
#     i,j = 0, 0
#     while i < len(left) and j < len(right):
#         if compare(left[i], right[j]):
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     while (i < len(left)):
#         result.append(left[i])
#         i += 1 
#     while j < len(right):
#         result.append(right[j])
#         j += 1 
#     return result
# 
# def merge_sort(L, compare = lambda x, y: x < y):
#     if len(L) < 2:
#         return L[:]
#     else:
#         middle = len(L)//2
#         left = merge_sort(L[:middle], compare)
#         right = merge_sort(L[middle:], compare)
#         return merge(left, right, compare)
# =============================================================================


# =============================================================================
# def merge(sortedls1, sortedls2, ls):
#     if len(sortedls1) == 0:
#         ls += sortedls2
#         return ls
#     if len(sortedls2) == 0:
#         ls += sortedls1
#         return ls
#     
#     if sortedls1[0] < sortedls2[0]:
#         ls.append(sortedls1[0])
#         return merge(sortedls1[1:], sortedls2, ls)
#     else:
#         ls.append(sortedls2[0])
#         return merge(sortedls2[1:], sortedls1, ls)
# 
# def mergesort(ls):
#     mid = len(ls) // 2
#     lsrtls = mergesort(ls[:mid])
#     rsrtls = mergesort(ls[mid:])
#     together = merge(lsrtls, rsrtls)
#     return together 
# =============================================================================
