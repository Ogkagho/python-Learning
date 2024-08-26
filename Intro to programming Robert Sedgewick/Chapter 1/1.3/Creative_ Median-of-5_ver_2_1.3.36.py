#Median-of-5
#Compose a program that takes five distinct integers from the 
#command line and writes the median value (the value such that two of the other 
#integers are smaller and two are larger). Extra credit : Solve the problem with a pro
#gram that compares values fewer than seven times for any given input.

#1.3.36 Ver 2.

import sys

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
num3 = int(sys.argv[3])
num4 = int(sys.argv[4])
num5 = int(sys.argv[5])

nums = [num1, num2, num3, num4, num5]

# Sort the list
nums.sort()

# The median is the middle element
median = nums[2]

print(median)
