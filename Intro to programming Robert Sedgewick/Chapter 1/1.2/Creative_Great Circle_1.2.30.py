#Great circle. 
#Compose a program that accepts four floats as command-line 
#arguments—x1, y1, x2, and y2—(the latitude and longitude, in degrees, of two 
#points on the earth) and writes the great-circle distance between them


#1.2.30
import math

x_1 = math.radians(float(input()))
y_1 = math.radians(float(input()))
x_2 = math.radians(float(input()))
y_2 = math.radians(float(input()))

d = 60*math.acos(math.sin(x_1)*math.sin(x_2) + math.cos(x_2)*math.cos(x_2)*math.cos(y_1 - y_2))

print(f'great circle distance: {d:.4f}')
