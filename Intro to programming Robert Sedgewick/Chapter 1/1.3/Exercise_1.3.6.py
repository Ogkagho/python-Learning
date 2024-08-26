#Redesign tenhellos.py to compose a program hellos.py that takes the 
#number of lines to write as a command-line argument. You may assume that the 
#argument is less than 1000. Hint: Use i % 10 and i % 100 to determine when to use 
#st, nd, rd, or th for writing the ith Hello

#1.3.6
import sys


n = int(sys.argv[1])
for i in range(1,n+1):
    if (i % 10 == 1 or i % 100 == 1) and not i == 11:
        stdio.writeln(str(i) + 'st Hello' )
    elif (i % 10 == 2 or i % 100 == 2) and not i == 12:
        stdio.writeln(str(i) + 'nd Hello')
    elif (i % 10 == 3 or i % 100 == 3) and not i ==13:
        stdio.writeln(str(i) + 'rd Hello')
    else:
        stdio.writeln(str(i) + 'th Hello')
