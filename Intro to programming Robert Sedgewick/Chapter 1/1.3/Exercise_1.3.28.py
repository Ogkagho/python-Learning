#Compose a program gcd.py that finds the greatest common divisor (gcd) 
#of two integers using Euclid’s algorithm, which is an iterative computation based on 
#the following observation: if x is greater than y, then if y divides x, the gcd of x and 
#y is y; otherwise, the gcd of x and y is the same as the gcd of x % y and y


#1.3.28
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

while y != 0:
    if x > y:
        if x % y == 0:
            print("The GCD is:", y)
            break
        else:
            x, y = y, x % y
    else:
        x, y = y, x % y

if y == 0:
    print("The GCD is:", x)

#yes yes i know i could use recursrion gcd(x, y) is the same as gcd(y , x%y)
#but rcursion hasn't been introduced :)
def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x
