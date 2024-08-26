# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 14:04:07 2024

@author: Edward kagho
"""

# =============================================================================
# def fibRecursive(n):
#     global numCalls
#     numCalls += 1
#     #print('fib called with ', n)
#     if n <= 1:
#         return 1
#     else:
#         return fibRecursive(n-1) + fibRecursive(n-2)
#     
# numCalls = 0
# n = 30
# res = fibRecursive(n)
# print('fib of ', n, 'is ',res,'The number of calls =', numCalls)
# 
# 
# 
# def fibfast(n, memo):
#     global numCalls
#     numCalls += 1
#     if not n in memo:
#         memo [n] = fibfast(n-1, memo) + fibfast(n-2, memo)
#     return memo[n]
# 
# def fib1(n):
#     memo = {0:1, 1:1}
#     return fibfast(n, memo)
# 
# numCalls = 0
# n = 30
# res = fib1(n)
# print('fib of ',n,'is ', res)
# print('The number of calls =', numCalls)
# =============================================================================


#knapsack problem

def maxVal(w, v, i, aw):
    
    global numCalls
    numCalls += 1
    if i == 0:    #base case
        if w[i] <= aw:
            return v[i]
        else:
            return 0 
    without_i = maxVal(w, v, i-1, aw)
    if w[i] > aw:
        return without_i
    else:
        with_i = v[i] + maxVal(w, v, i-1, aw - w[i])
    return max(with_i, without_i)

weights = [1, 5, 3, 4]
vals = [15, 10, 9, 5]
numCalls = 0
res = maxVal(weights, vals, len(vals) - 1, 8)
print(f'max val {res}, nummber of calls {numCalls}')



def fastmaxVal(w, v, i, aw, m):
    global numCalls
    numCalls += 1
    try:
        return m[(i, aw)]
    except KeyError:
        if i == 0:    #base case
            if w[i] <= aw:
                return v[i]
            else:
                return 0 
        without_i = maxVal(w, v, i-1, aw)
        if w[i] > aw:
            return without_i
        else:
            with_i = v[i] + maxVal(w, v, i-1, aw - w[i])
        return max(with_i, without_i)
        m[(i, aw)] = res 
        return res

def maxVal0(w, v, i, aw):
    m = {}
    return fastmaxVal(w, v, i, aw, m)