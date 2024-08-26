# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 12:35:31 2024

@author: Lenovo
"""
import sys
sys.path.append('C:\\Users\\Lenovo\\Downloads\\introcs-1.0')
import stdio

def harmonic(n):
    if n == 1:
        return n
    return harmonic(n-1) + 1.0/n 


# =============================================================================
# #Eucilds algorithm,
# def gcd(p, q):
#     if q == 0: return p
#     return gcd(q, p % q)
# 
# def main():
#     p = int(sys.argv[1])
#     q = int(sys.argv[2])
#     stdio.writeln(gcd(p, q))
# 
# if __name__ == '__main__': main()
# =============================================================================

def moves(n, left):
    if n == 0: return
    moves(n-1, not left)
    if left:
        stdio.writeln(str(n) + ' left')
    else:
        stdio.writeln(str(n) + ' right')
    moves(n-1, not left)
    
n = int(input())
moves(n, True)