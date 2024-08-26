#Median-of-5
#Compose a program that takes five distinct integers from the 
#command line and writes the median value (the value such that two of the other 
#integers are smaller and two are larger). Extra credit : Solve the problem with a pro
#gram that compares values fewer than seven times for any given input.

#1.3.36

num1 = int(input('Enter number: '))
num2 = int(input('Enter number: '))
num3 = int(input('Enter number: '))
num4 = int(input('Enter number: '))
num5 = int(input('Enter number: '))

if num1 < num2:
    min1 = num1
    max1 = num2
else:
    min1 = num2
    max1 = num1

if num3 < num4:
    min2 = num3 
    max2 = num4
else:
    min2 = num4 
    max2 = num3 
if min1 < min2:
    minF = min2
else:
    minF = min1 

if max1 < max2:
    maxF = max1 
else:
    maxF = max2 
    
if maxF < num5:
    median = maxF
else:
    median = num5
    
if median < minF:
    median = minF

print(median)

#i guess i got the extra point :))
#This problem took a while wheewww
