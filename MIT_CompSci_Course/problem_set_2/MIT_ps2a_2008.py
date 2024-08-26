# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 22:41:50 2024

@author: Edward kagho
"""

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
while consecutive_count < 20:
    if not diophantine(i):
        max_non_representable = i
        consecutive_count = 0
    else:
        consecutive_count += 1
    i += 1

print("Largest number of McNuggets that cannot be bought in exact quantity is", max_non_representable)

