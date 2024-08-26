#Compose a program that generates a point that is randomly distributed in 
#the unit disk, but without using a break statement. Compare your solution to the 
#one given at the end of this section

#1.3.30
import random

found = False

while not found:
    x = -1.0 + 2.0*random.random()
    y = -1.0 + 2.0*random.random()
    if x*x + y*y <= 1.0:
        found = True
print(x, y)
