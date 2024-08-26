#Compose a program that takes two integers m and d from the command 
#line and writes True if day d of month m is between March 20 and June 20, and 
#False otherwise. (Interpret m with 1 for January, 2 for February, and so forth.)

#1.2.20

m = int(input('Enter month: '))
d = int(input('Enter day: '))

if (m == 3 and d > 20) or (m == 6 and d < 20) or (m > 3 and m < 6):
    print(True)
else:
    print(False)
