# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 00:46:01 2024

@author: Edward kagho
"""

#used list instead of tuple, change later
packages = []
packages += [int(input('Enter the size of the pack: '))]
packages += [int(input('Enter the size of the pack: '))]
packages += [int(input('Enter the size of the pack: '))]

def diophantine(n):
    for a in range(0,n//packages[0] + 1):
        for b in range(0, n // packages[1] + 1):
            for c in range(0,n // packages[2] + 1):
                if packages[0]*a + packages[1]*b +packages[2]*c == n:
                    return True 
    return False

i = 1
consec = 0

while consec < 6 and i < 200:
    if diophantine(i):
        consec += 1
    else:
        consec = 0
        save = i
    i += 1
        
print('Given packages sizes',packages[0], ',',packages[1], ',',packages[2], 
      'the largest number of McNuggets that cannot be bought in exact quantity is', save)
    
                
