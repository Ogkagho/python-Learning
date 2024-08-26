# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 16:20:49 2024

@author: Lenovo
"""
     
def constrainedMatchPair(firstMatch, secondMatch, length):
    tu = ()
    for i in firstMatch:
        if i + length + 1 in secondMatch:
            tu += (i,)
    return tu 




