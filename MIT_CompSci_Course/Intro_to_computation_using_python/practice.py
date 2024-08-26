# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 17:18:51 2024

@author: Lenovo
"""

# =============================================================================
# def sum_digits(s):
#     sum1 = 0
#     for c in s:
#         if c in '1234567890':
#             sum1 += int(c)
#     return sum1 
# sum_digits('a2b3c')
# =============================================================================

# =============================================================================
# def sum_digits(s):
#     sum1 = 0
#     try:
#         for c in s:
#             sum1 += c 
#     except TypeError:
#         print('unsupportd operator for int and str')
#     return sum1 
# 
# sum_digits('a2b3c')
# =============================================================================

# =============================================================================
# def sum_digits(s):
#     sum1 = 0
#     for c in s:
#         try:
#             sum1 += int(c)
#         except TypeError:
#             print('unsupported')
#     return sum1 
# sum_digits('a2b3c')
# =============================================================================


class Toy(object):
    def __init__(self):
        self._elems = []
    def add(self, new_elems):
        self.elems += new_elems
    def size(self):
        return len(self._elems)