#Compose a program that writes five uniform 
#random floats between 0.0 and 1.0, their average value, and their minimum and 
#maximum values. Use the built-in min() and max() functions.


#1.2.27
#for loops haven't been introduced yet, so cheating a bit :)
import random

min1 = random.random()
max1 = min1 
print(min1)
average =  min1

for i in range(4):
    r = random.random()
    print(r)
    if r > max1:
        max1 = r 
    if r < min1:
        min1 = r 
    average += r
    
average /= 5 
print('The average is',average) 
print('The minimum is',min1)
print('The maximum is', max1)
