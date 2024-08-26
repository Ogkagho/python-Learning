# Longest plateau. Given an array of integers, compose a program that finds 
#the length and location of the longest contiguous sequence of equal values where 
#the values of the elements just before and just after this sequence are smaller.

#1.4.21

a = [1, 2, 2, 2, 1, 10 ,5, 5, 5, 5, 1]

i = 1
length = 1
maxLength = 0

while i < len(a)-1:
    while i != len(a) - 1 and a[i] == a[i+1]:
        if a[i-1] < a[i]:  
            position = i
        length += 1
        i += 1
    if a[position+length -1] > a[position+length] and a[position-1] < a[position] and length > maxLength:
        maxLength = length
        finalposition = position
    i += 1
    length = 1

if maxLength == 0:
    print('There is no such sequence')
else:
    print(f'The position of the sequence of integers is {finalposition} \
          and the length is {maxLength}')

