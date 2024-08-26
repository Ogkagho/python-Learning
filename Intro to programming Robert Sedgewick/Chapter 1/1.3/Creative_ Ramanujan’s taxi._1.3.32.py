# Ramanujan’s taxi. cool problem
#compose a program that takes a command-line argument n and writes all integers less than 
#or equal to n that can be expressed as the sum of two cubes in two different ways. 
#In other words, find distinct positive integers a, b, c, and d such that a3 + b3 = c3 + d3. 
#Use four nested for loops.
#try 1729 as input

#1.3.32
#ramanujan's taxi
n = int(input())

found = False
for a in range(1, n+1):
    for b in range(1, n+1):
        for c in range(1, n+1):
            for d in range(1, n+1):
                cond = a != b and a != c and a != d 
                cond2 = b != c and b != d 
                cond3 = c != d
                if a**3 + b**3 == d**3 + c**3 and cond and cond2 and cond3 :
                    found = True
                    break
                if found:
                    break
            if found:
                break
        if found:
            break
    if found:
        break
if found:
    print(a**3 + b**3,a, b, c, d)
else:
    print('not found')
