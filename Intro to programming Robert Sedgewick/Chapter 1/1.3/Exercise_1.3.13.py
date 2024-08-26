#Compose a program that takes a command-line argument n and writes all 
#the positive powers of 2 less than or equal to n. Make sure that your program works 
#properly for all values of n. (Your program should write nothing if n is negative.)

#1.3.13
n  = int(input())

power = 1

while power <= n and n > 0:
    stdio.write(str(power) + ' ')
    power *= 2
