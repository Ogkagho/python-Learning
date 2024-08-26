# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 22:41:50 2024

@author: Edward kagho
"""
#exhaustive search

def diophantine(n):
    for i in range(0, n // 6 + 1):
        for j in range(0, n // 9 + 1):
            for k in range(0, n // 20 + 1):
                if 6*i + 9*j + 20*k == n:
                    return True
    return False

# Initialize variables
i = 1
max_non_representable = 0
consecutive_count = 0

# Loop until we find a sequence of 20 consecutive numbers that can be bought exactly
while consecutive_count < 6:
    if not diophantine(i):
        max_non_representable = i
        consecutive_count = 0
    else:
        consecutive_count += 1
    i += 1

print("Largest number of McNuggets that cannot be bought in exact quantity is", max_non_representable)

# =============================================================================
# def diophantine(n):
#     for a in range(0,n//6 + 1):
#         for b in range(0, n // 9 + 1):
#             for c in range(0,n // 20 + 1):
#                 if 6*a + 9*b +20*c == n:
#                     return True 
#     return False
# 
# i = 1
# consec = 0
# 
# while consec < 6:
#     if diophantine(i):
#         consec += 1
#     else:
#         consec = 0
#         save = i
#     i += 1
#         
# print(save)
# =============================================================================

# =============================================================================
# #without functions
# 
# n = 1
# consecutive_successes = 0
# 
# while consecutive_successes < 6:
#     found = False
#     for a in range(n // 6 + 1):
#         for b in range(n // 9 + 1):
#             for c in range(n // 20 + 1):
#                 if 6 * a + 9 * b + 20 * c == n:
#                     found = True
#                     break
#             if found:
#                 break
#         if found:
#             break
#     
#     if found:
#         consecutive_successes += 1
#     else:
#         save = n
#         consecutive_successes = 0
#     
#     n += 1
# 
# print(save)
# =============================================================================
