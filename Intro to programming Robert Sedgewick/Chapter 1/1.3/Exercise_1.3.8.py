#Generalizing the “uniform random numbers” exercise from section 1.2 
#(exercise 1.2.27), compose a program stats.py that accepts an integer n as a com
#mand-line argument, uses random.random() to write n uniform random numbers 
#between 0 and 1, and then writes their average value, their minimum value, and 
#their maximum value.

#1.3.8
n = int(sys.argv[1])

total = 0
max1 = 0
min1 = 2
for i in range(n):
    a = random.random()
    stdio.write(str(a) + ' ')
    total += a
    if a < min1:
        min1 = a
    
    if a > max1:
        max1 = a
    
stdio.writeln('Average:' + str(total/n) + '  and Max is ' + str(max1) +
              'and the Min is ' + str(min1))
