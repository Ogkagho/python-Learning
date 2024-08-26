#polar cordinates
#Compose a program that converts 
#from Cartesian to polar coordinates. Your program should 
#accept two floats x and y from the command line and write 
#the polar coordinates r and . Use the Python function math.
#atan2(y, x), which computes the arctangent value of y/x that 
#is in the range from -pi to pi

#1.2.23
import math 

x = float(input('Enter x:'))
y = float(input('Enter y: '))

r = math.sqrt(x**2 + y**2)
theta = math.atan2(y, x)

print("The polar cordinates of (",x,",",y,") is (",r,",",theta,")")

