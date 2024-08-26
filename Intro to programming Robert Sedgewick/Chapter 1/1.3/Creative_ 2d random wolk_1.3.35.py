#2d random walk
#A two-dimensional random walk simulates the behavior 
#of a particle moving in a grid of points. At each step, the random walker moves 
#north, south, east, or west with probability equal to 1/4, independent of previous 
#moves. Compose a program randomwalker.py that takes a command-line argu
#ment n and estimates how long it will take a random walker to hit the boundary of 
#a 2n-by-2n square centered at the starting point.


#1.3.35
import random

n = int(input())

positioni = 0
positionj = 0
steps  = 0

while abs(positioni) < n and abs(positionj) < n:
    decision =random.randrange(1, 5)
    if decision == 1:
        positioni += 1 #moves right
    elif decision == 2:
        positioni -= 1 #moves left
    elif decision == 3:
        positionj += 1 #moves up
    elif decision == 4:
        positionj -= 1  #moves down
    steps += 1

print(steps)

