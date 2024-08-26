
#1.3.11
#reverses a number
n = 123456789
m = 0
stdio.writeln(str(m) + ' ' + str(n))
while n != 0:
    m = (10 * m) + (n % 10)
    n //= 10
    #print(m,n)

stdio.writeln(str(m) + ' ' + str(n))
