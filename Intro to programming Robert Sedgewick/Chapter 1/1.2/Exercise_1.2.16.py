#Compose a program that takes two integers a and b from the command 
#line and writes a random integer between a and b

#1.2.16
import sys

a = int(sys.argv[1])
b = int(sys.argv[2])

randomnum = random.randrange(a, b+1)
print(randomnum)
