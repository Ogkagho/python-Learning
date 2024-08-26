# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 16:46:06 2024

@author: Edward kagho
"""
import random

def generateRandomBirthday(n):
    birthday = [random.randrange(1,366) for i in range(n)]
    return birthday

def getMatch(ls):
    for i in range(len(ls)-1):
        for j in range(i+1, len(ls)):
            if ls[i] == ls[j]:
                return True 

def getMatch2(ls):
    return len(ls) == len(set(ls))

def simulation(n, trials):
    Trials = trials #1000000
    count = 0 
    for i in range(Trials):
        ls  = generateRandomBirthday(n)
        if getMatch2(ls):
            count += 1 
    prob = (count / Trials) * 100
    return prob
            