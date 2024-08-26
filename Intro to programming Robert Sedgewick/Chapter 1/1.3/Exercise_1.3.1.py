#Compose a program that takes three integer command-line arguments and 
#writes 'equal' if all three are equal, and 'not equal' otherwise

#1.3.1
import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

if a == b and b == c:
    stdio.writeln('Equal')
else:
    stdio.writeln('Not equal')


