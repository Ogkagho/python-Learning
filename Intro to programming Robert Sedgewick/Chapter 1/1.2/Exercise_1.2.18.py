#Compose a program that takes a float t from the command line and writes 
#the value of sin(2t)  sin(3t).

#1.2.18
t = float(input('Enter: '))
print(math.sin(2*t) + math.sin(3*t))
