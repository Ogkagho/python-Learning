#Dragon curves

#recursive implementation
#LtoR - left to right, reversing the steps

def LtoR(st):
    return st[::-1].replace('L', 'X').replace('R', 'L').replace('X', 'R') #replaces 'R' with 'L'
            
def dragonCurve(n):
    if n == 0:
        return 'F'
    return dragonCurve(n-1) + 'L' + LtoR(dragonCurve(n-1))

print(dragonCurve(5))


#for-loop implementation
dragon = 'F'
for i in range(5):
    dragonR = dragon[::-1].replace('L', 'X').replace('R', 'L').replace('X', 'R')
    dragon = dragon + 'L' + dragonR
     

print(dragon)
