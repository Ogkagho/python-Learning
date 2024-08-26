#Suppose that x and y are two floats that represent the Cartesian coordinates 
#of a point (x, y) in the plane. Give an expression that evaluates to the distance of 
#the point from the origin.

#1.2.15
import math 

x = int(input("Input: "))
y = int(input("Input: "))

distance = math.sqrt(x**2 + y**2)
print(distance)

print(random.randrange(x, y))
