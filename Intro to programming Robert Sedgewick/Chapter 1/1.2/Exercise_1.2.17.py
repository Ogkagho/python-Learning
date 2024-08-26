#Compose a program that writes the sum of two random integers between 
#1 and 6 (such as you might get when rolling dice).

#1.2.17
import random

randNum1 = random.randrange(1, 7)
randNum2 = random.randrange(1, 7)

sum1 = randNum1 + randNum2

print(sum1)
