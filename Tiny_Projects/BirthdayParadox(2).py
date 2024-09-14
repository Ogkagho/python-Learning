# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 16:46:06 2024

@author: Edward kagho
"""
import random

def generateRandomBirthday(n):
    """Generate a list of n random birthdays (1-365)."""
    birthday = [random.randrange(1,366) for i in range(n)] 
    return birthday

def getMatch(ls):
    """Check for duplicates using exhaustive search."""
    for i in range(len(ls)-1):  #this is less efficient because it is a nested loop with O(n^2)
        for j in range(i+1, len(ls)):
            if ls[i] == ls[j]:
                return True 
    return False

def getMatch2(ls):
    """Check for duplicates using a set."""
    return len(ls) == len(set(ls))   #creates a set which contains no duplicates and compares length 
                                     #if the lengths are the same there is no duplicate birthday indicating no match
                                     #else if the lengths are different there is at least one matching birthday 

def getMatch3(ls):
    """Check for duplicates using a dictionary."""
    seen = {} #Creates a dict to store seen values 
    for birthday in ls:    #iterats through birthdays 
        if birthday not in seen:   #adds birthdays to seen if not in the dictionary
            seen.update({birthday:0})
        else:
            return True  #returns True if seen twice, indicating a match
    return False    #else it return False if a birthday doesn't occur twice

def simulation(n, trials):
    """Simulates the probability of at least two people sharing a birthday.
    
    Parameters:
    n (int): The number of birthdays to generate.
    trials (int): The number of simulation runs to perform.
    
    Returns:
    float: The probability (as a percentage) that at least two birthdays match, 
           based on the number of trials conducted.
    """
    count = 0 
    for i in range(trials):
        ls  = generateRandomBirthday(n)
        if getMatch2(ls):
            count += 1 
    prob = (count / trials) * 100
    prob = round(prob, 2)
    return prob
            
