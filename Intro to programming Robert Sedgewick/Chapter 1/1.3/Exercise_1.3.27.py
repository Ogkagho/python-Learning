#Compose a program checkerboard.py that takes one command-line ar
#gument n and uses a loop within a loop to write a two-dimensional n-by-n check
#erboard pattern with alternating spaces and asterisks, like the following 5-by-5 pattern
#* * * * * 
# * * * * 
#* * * * * 
# * * * * 
#* * * * *


#1.3.27

import sys

n = int(sys.argv[1])

for i in range(1,n+1):
    for j in range(1,(n*2)):
        if (i % 2 == 1 and j % 2 == 1) or(i % 2 == 0 and j % 2== 0):
            print('*')
        else:
            print(' ')
    print()
