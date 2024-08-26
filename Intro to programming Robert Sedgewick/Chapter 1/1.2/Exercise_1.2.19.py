#Compose a program that takes three floats x0, v0, and t from the command 
#line, evaluates x0  v0t − G t 2  2, and writes the result.

#1.2.19
x_0 = float(input('Enter: '))
v_0 = float(input('Enter: '))
t = float(input('Enter: '))

GRAVITATION = 9.80665

print(x_0 + v_0*t - (GRAVITATION*t**2) / 2)
