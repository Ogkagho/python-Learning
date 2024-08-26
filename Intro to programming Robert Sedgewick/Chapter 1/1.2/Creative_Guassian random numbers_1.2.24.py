#Gaussian random numbers. 

#box-muller formula
#1.2.24
# u and v are real numbers between 0 and 1

import random

v = random.random()
u = random.random()

guassianNumber = math.sin(2*math.pi*v)*((-2*math.log(u))**0.5)
print(guassianNumber)

