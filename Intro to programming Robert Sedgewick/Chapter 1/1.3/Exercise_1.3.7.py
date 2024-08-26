#Compose a program fiveperline.py that, using one for loop and one if 
#statement, writes the integers from 1,000 (inclusive) to 2,000 (exclusive) with five 
#integers per line

#1.3.7

for i in range(1000, 2000):
    if i % 10 == 4 or i % 10 == 9:
        stdio.writeln(str(i))
    else:
        stdio.write(str(i) + ' ')
