#Compose a program that takes three positive integers as command-line 
#arguments and writes False if any one of them is greater than or equal to the sum 
#of the other two and True otherwise.


#1.2.12
a = int(input("enter:"))
b = int(input('enter:'))
c = int(input('enter:'))

if c >= a + b or b >= a + c or a >= b + c:
    print(False)
else:
    print(True)
