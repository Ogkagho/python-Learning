#Three-sort. Compose a program that takes three integers from the com
#mand line and writes them in ascending order. Use the built-in min() and max() 
#functions
#i don't use the command line for this question.

#1.2.31
x = int(input('Enter: '))
y = int(input('Enter: '))
z = int(input('Enter: '))

maximum = max(x, y, z)
minimum = min(x, y, z)

middle = x + y + z - maximum - minimum #total, subtract maximum , then minimum 

print(minimum, middle, maximum) 
