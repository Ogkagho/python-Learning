#Compose a code fragment that takes two float command-line arguments 
#and writes True if both are strictly between 0.0 and 1.0, and False otherwise

#1.3.3
import sys

a = float(sys.argv[1])
b = float(sys.argv[2])

if (0.0 < a and a < 1.0) and (0.0 < b and b < 1.0):
    print('True')
else: print('False')


