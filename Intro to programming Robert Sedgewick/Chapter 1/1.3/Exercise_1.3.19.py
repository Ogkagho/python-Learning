#create a program kary.py that takes i and k as com
#mand-line arguments and converts i to base k. Assume that k is an integer between 
#2 and 16. For bases greater than 10, use the letters A through F to represent the 11th 
#through 16th digits, respectively.


#1.3.19
#kary
i = int(input("Enter the number to convert: "))
k = int(input("Enter the base (2-16): "))

v = 1
while v <= i // k:
    v *= k

while v > 0:
    digit = i // v
    if digit < 10:
        print(digit, end='')
    else:
        print(chr(ord('A') + digit - 10), end='')
    i %= v
    v //= k
print()
