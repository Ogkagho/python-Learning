#Order check. Compose a program that accepts three floats x, y, and z as 
#command-line arguments and writes True if the values are strictly ascending or 
#descending ( x < y < z or x > y > z ), and False otherwise.

#1.2.26
x = int(input('Enter: '))
y = int(input('Enter: '))
z = int(input('Enter: '))

if x < y < z or x > y > z:
    print(True)
else:
    print(False)

